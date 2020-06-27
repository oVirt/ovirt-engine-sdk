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

Usage:

    upload_disk.py FILE
"""

from __future__ import print_function

import argparse
import getpass
import inspect
import json
import logging
import os
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import subprocess
import sys
import time

from ovirt_imageio import client

from helpers import imagetransfer


def parse_args():
    parser = argparse.ArgumentParser(description="Upload images")

    parser.add_argument(
        "filename",
        help="path to image (e.g. /path/to/image.raw) "
             "Supported formats: raw, qcow2, iso")

    parser.add_argument(
        "--engine-url",
        required=True,
        help="transfer URL (e.g. https://engine_fqdn:port)")

    parser.add_argument(
        "--username",
        required=True,
        help="username of engine API")

    parser.add_argument(
        "--password-file",
        help="file containing password of the specified by user (if file is "
             "not specified, read from standard input)")

    parser.add_argument(
        "--disk-format",
        choices=("raw", "qcow2"),
        help="format of the created disk (default image format)")

    parser.add_argument(
        "--disk-sparse",
        action="store_true",
        help="create sparse disk. Cannot be used with raw format on block storage.")

    parser.add_argument(
        "--enable-backup",
        action="store_true",
        help="creates a disk that can be used for incremental backup. "
             "Allowed for disk with qcow2 format only")

    parser.add_argument(
        "--sd-name",
        required=True,
        help="name of the storage domain.")

    parser.add_argument(
        "-c", "--cafile",
        help="path to oVirt engine certificate for verifying server.")

    parser.add_argument(
        "--insecure",
        dest="secure",
        action="store_false",
        default=False,
        help=("do not verify server certificates and host name (not "
              "recommended)."))

    parser.add_argument(
        "--use-proxy",
        dest="use_proxy",
        default=False,
        action="store_true",
        help="upload via proxy on the engine host (less efficient)")

    parser.add_argument(
        "--max-workers",
        type=int,
        default=4,
        help="Maximum number of workers to use for upload. The default "
             "(4) improves performance when uploading a single disk. "
             "You may want to use lower number if you upload many disks "
             "in the same time.")

    parser.add_argument(
        "--debug",
        action="store_true",
        help="log debug level messages to example.log")

    return parser.parse_args()


def get_image_info(filename):
    print("Checking image...")

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

    # If we upload "fedora-30.img" to qcow2 disk, the disk name wil be
    # "fedora-30.qcow2".
    basename = os.path.splitext(os.path.basename(image_info["filename"]))[0]
    disk_info["name"] = "{}.{}".format(basename, disk_format)

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

    disk_info["content_type"] = content_type

    return disk_info


args = parse_args()

logging.basicConfig(
    level=logging.DEBUG if args.debug else logging.INFO,
    filename="example.log",
    format="%(asctime)s %(levelname)-7s (%(threadName)s) [%(name)s] %(message)s"
)

# Get image and disk info using qemu-img
image_info = get_image_info(args.filename)
disk_info = get_disk_info(args, image_info)

print("Image format: %s" % image_info["format"])
print("Disk format: %s" % disk_info["format"])
print("Disk content type: %s" % disk_info["content_type"])
print("Disk provisioned size: %s" % disk_info["provisioned_size"])
print("Disk initial size: %s" % disk_info["initial_size"])
print("Disk name: %s" % disk_info["name"])
print("Disk backup: %s" % args.enable_backup)

# This example will connect to the server and create a new `floating`
# disk, one that isn't attached to any virtual machine.
# Then using transfer service it will transfer disk data from local
# image to the newly created disk in server.

# Create the connection to the server:
print("Connecting...")

if args.password_file:
    with open(args.password_file) as f:
        password = f.read().rstrip('\n') # ovirt doesn't support empty lines in password
else:
    password = getpass.getpass()

connection = sdk.Connection(
    url=args.engine_url + '/ovirt-engine/api',
    username=args.username,
    password=password,
    ca_file=args.cafile,
    debug=args.debug,
    log=logging.getLogger(),
)

# Get the reference to the root service:
system_service = connection.system_service()

print("Creating disk...")

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

print("Disk ID: %s" % disk.id)

print("Creating image transfer...")

# Find a host for this transfer. This is an optional step allowing optimizing
# the transfer using unix socket when running this code on a oVirt hypervisor
# in the same data center.
host = imagetransfer.find_host(connection, args.sd_name)

transfer = imagetransfer.create_transfer(connection, disk,
    types.ImageTransferDirection.UPLOAD, host=host)

print("Transfer ID: %s" % transfer.id)
print("Transfer host name: %s" % transfer.host.name)

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

print("Uploading image...")

with client.ProgressBar() as pb:
    client.upload(
        args.filename,
        upload_url,
        args.cafile,
        secure=args.secure,
        progress=pb,
        **extra_args)

print("Finalizing image transfer...")
imagetransfer.finalize_transfer(connection, transfer, disk)
connection.close()

print("Upload completed successfully")
