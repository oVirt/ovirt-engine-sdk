#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2016-2017 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Upload disk example code.

Requires the ovirt-imageio-client package.
"""

import inspect
import json
import os
import subprocess
import time

from ovirt_imageio import client

from ovirtsdk4 import types

from helpers import common
from helpers import imagetransfer
from helpers import units
from helpers.common import progress


def parse_args():
    parser = common.ArgumentParser(description="Upload images")

    parser.add_argument(
        "filename",
        help="Path to image (e.g. /path/to/image.raw). "
             "Supported formats: raw, qcow2, iso.")

    parser.add_argument(
        "--disk-format",
        choices=("raw", "qcow2"),
        help="Format of the created disk (default image format).")

    parser.add_argument(
        "--disk-sparse",
        action="store_true",
        help="Create sparse disk. Cannot be used with raw format on "
             "block storage.")

    parser.add_argument(
        "--enable-backup",
        action="store_true",
        help="Creates a disk that can be used for incremental backup. "
             "Allowed for disk with qcow2 format only.")

    parser.add_argument(
        "--sd-name",
        required=True,
        help="Name of the storage domain.")

    parser.add_argument(
        "--use-proxy",
        dest="use_proxy",
        default=False,
        action="store_true",
        help="Upload via proxy on the engine host (less efficient).")

    parser.add_argument(
        "--max-workers",
        type=int,
        default=4,
        help="Maximum number of workers to use for upload. The default "
             "(4) improves performance when uploading a single disk. "
             "You may want to use lower number if you upload many disks "
             "in the same time.")

    parser.add_argument(
        "--buffer-size",
        type=units.humansize,
        default=client.BUFFER_SIZE,
        help="Buffer size per worker. The default ({}) gives good "
             "performance with the default number of workers. If you use "
             "smaller number of workers you may want use larger value."
             .format(client.BUFFER_SIZE))

    parser.add_argument(
        "--timeout-policy",
        choices=('legacy', 'pause', 'cancel'),
        default='cancel',
        help="The action to be made for a timed out transfer")

    return parser.parse_args()


def get_image_info(filename):
    progress("Checking image...")

    out = subprocess.check_output(
        ["qemu-img", "info", "--output", "json", filename])
    image_info = json.loads(out)

    if image_info["format"] not in ("qcow2", "raw"):
        raise RuntimeError("Unsupported image format %(format)s" % image_info)

    return image_info


def get_disk_info(args, image_info):
    disk_info = {}

    disk_format = args.disk_format or image_info["format"]

    # Convert qemu format names to oVirt constants ("raw", "cow").
    if disk_format == "raw":
        disk_info["format"] = types.DiskFormat.RAW
    elif disk_format == "qcow2":
        disk_info["format"] = types.DiskFormat.COW

    disk_info["provisioned_size"] = image_info["virtual-size"]

    # The initial size is needed only for block storage (iSCSI, FC). We cannot
    # use the actual image size because the image may be compressed.
    out = subprocess.check_output([
        "qemu-img",
         "measure",
         "-f", image_info["format"],
         "-O", disk_format,
         "--output", "json",
         image_info["filename"]
    ])
    measure = json.loads(out)

    disk_info["initial_size"] = measure["required"]

    # Detect disk content type
    #
    # ISO format structure
    # ---------------------------------------------------------------------------
    # offset    type    value       comment
    # ---------------------------------------------------------------------------
    # 0x0000                        system area (e.g. DOS/MBR boot sector)
    # 0x8000    int8    0x01        primary volume descriptor type code
    # 0x8001    strA    "CD001"     primary volume descriptor indentifier
    # 0x8006    int8    0x01        primary volume desctptor version
    # 0x8007            0x00        unused field
    #
    # See https://wiki.osdev.org/ISO_9660#Overview_and_caveats for more info.

    content_type = types.DiskContentType.DATA

    if image_info["format"] == "raw":
        with open(image_info["filename"], "rb") as f:
            f.seek(0x8000)
            primary_volume_descriptor = f.read(8)
        if primary_volume_descriptor == b"\x01CD001\x01\x00":
            content_type = types.DiskContentType.ISO

    # Name the disk based on image file name, format and content type.
    basename = os.path.splitext(os.path.basename(image_info["filename"]))[0]
    ext = "iso" if content_type == types.DiskContentType.ISO else disk_format
    disk_info["name"] = "{}.{}".format(basename, ext)

    disk_info["content_type"] = content_type

    return disk_info


args = parse_args()
common.configure_logging(args)

# Get image and disk info using qemu-img
image_info = get_image_info(args.filename)
disk_info = get_disk_info(args, image_info)

progress("Image format: %s" % image_info["format"])
progress("Disk format: %s" % disk_info["format"])
progress("Disk content type: %s" % disk_info["content_type"])
progress("Disk provisioned size: %s" % disk_info["provisioned_size"])
progress("Disk initial size: %s" % disk_info["initial_size"])
progress("Disk name: %s" % disk_info["name"])
progress("Disk backup: %s" % args.enable_backup)

# This example will connect to the server and create a new `floating`
# disk, one that isn't attached to any virtual machine.
# Then using transfer service it will transfer disk data from local
# image to the newly created disk in server.

progress("Connecting...")
connection = common.create_connection(args)

progress("Creating disk...")

disks_service = connection.system_service().disks_service()
disk = disks_service.add(
    disk=types.Disk(
        name=disk_info["name"],
        content_type=disk_info["content_type"],
        description='Uploaded disk',
        format=disk_info["format"],
        initial_size=disk_info["initial_size"],
        provisioned_size=disk_info["provisioned_size"],
        sparse=args.disk_sparse,
        backup=types.DiskBackup.INCREMENTAL if args.enable_backup else None,
        storage_domains=[
            types.StorageDomain(
                name=args.sd_name
            )
        ]
    )
)

# Wait till the disk is up, as the transfer can't start if the
# disk is locked:
disk_service = disks_service.disk_service(disk.id)
while True:
    time.sleep(1)
    disk = disk_service.get()
    if disk.status == types.DiskStatus.OK:
        break

progress("Disk ID: %s" % disk.id)

progress("Creating image transfer...")

# Find a host for this transfer. This is an optional step allowing optimizing
# the transfer using unix socket when running this code on a oVirt hypervisor
# in the same data center.
host = imagetransfer.find_host(connection, args.sd_name)

transfer = imagetransfer.create_transfer(connection, disk,
    types.ImageTransferDirection.UPLOAD, host=host,
    timeout_policy=types.ImageTransferTimeoutPolicy(args.timeout_policy))

progress("Transfer ID: %s" % transfer.id)
progress("Transfer host name: %s" % transfer.host.name)

# At this stage, the SDK granted the permission to start transferring the disk, and the
# user should choose its preferred tool for doing it. We use the recommended
# way, ovirt-imageio client library.

extra_args = {}

parameters = inspect.signature(client.download).parameters

# Use multiple workers to speed up the upload.
if "max_workers" in parameters:
        extra_args["max_workers"] = args.max_workers

if args.use_proxy:
    upload_url = transfer.proxy_url
else:
    upload_url = transfer.transfer_url

    # Use fallback to proxy_url if feature is available. Upload will use the
    # proxy_url if transfer_url is not accessible.
    if "proxy_url" in parameters:
        extra_args["proxy_url"] = transfer.proxy_url

progress("Uploading image...")

with client.ProgressBar() as pb:
    client.upload(
        args.filename,
        upload_url,
        args.cafile,
        secure=args.secure,
        buffer_size=args.buffer_size,
        progress=pb,
        **extra_args)

progress("Finalizing image transfer...")
imagetransfer.finalize_transfer(connection, transfer, disk)
connection.close()

progress("Upload completed successfully")
