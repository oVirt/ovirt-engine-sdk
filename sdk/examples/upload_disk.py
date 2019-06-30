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

Requires the qemu-img package for checking file type and virtual size.
Requires the ovirt-imageio-common package > 1.5.0.

Usage:

    upload_disk.py FILE
"""

from __future__ import print_function

import argparse
import getpass
import json
import logging
import os
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import subprocess
import sys
import time

from ovirt_imageio_common import client
from ovirt_imageio_common import ui

logging.basicConfig(level=logging.DEBUG, filename='example.log')

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
        help="format of the created disk. Note: cannot convert qcow2 format to raw.")

    parser.add_argument(
        "--sd-name",
        required=True,
        help="name of the storage domain.")

    # Note: unix socket works only when running this tool on the same host serving
    # the image.
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
        "-b", "--buffer-size",
        type=lambda v: int(v) * 1024,
        default=128 * 1024,
        help=("buffer size in KiB for upload. The default (128 KiB) provides best "
              "results in our tests, but you may like to tune this."))

    parser.add_argument(
        "-d", "--direct",
        dest="direct",
        default=False,
        action="store_true",
        help="upload directly to the daemon (if not set, upload to proxy on the engine host. "
             "Uploading directly to the daemon is more efficient.")

    return parser.parse_args()

def get_image_info(filename):
    print("Checking image...")

    out = subprocess.check_output(
        ["qemu-img", "info", "--output", "json", filename])
    image_info = json.loads(out)

    if image_info["format"] not in ("qcow2", "raw"):
        raise RuntimeError("Unsupported image format %(format)s" % filename)

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
        with open(args.filename, "rb") as f:
            f.seek(0x8000)
            primary_volume_descriptor = f.read(8)
        if primary_volume_descriptor == b"\x01CD001\x01\x00":
            content_type = types.DiskContentType.ISO

    image_info["content_type"] = content_type

    if image_info["format"] == "raw":
        image_info["transfer_format"] = types.DiskFormat.RAW
    else:
        image_info["transfer_format"] = types.DiskFormat.COW

    return image_info

def get_disk_format(image_info, args):
    if image_info["format"] == "qcow2":
        if args.disk_format == "raw":
            raise RuntimeError("Cannot convert qcow2 format to raw")
        disk_format = types.DiskFormat.COW
    else:
        if args.disk_format in ("raw", None):
            disk_format = types.DiskFormat.RAW
        elif args.disk_format == "cow":
            disk_format = types.DiskFormat.COW
        else:
            raise RuntimeError("Invalid disk format: %s" % image_info["format"])

    return disk_format


args = parse_args()

# Get image info using qemu-img
image_info = get_image_info(args.filename)
new_disk_format = get_disk_format(image_info, args)

print("Uploaded image format: %s" % image_info["format"])
print("Disk content type: %s" % image_info["content_type"])
print("Disk format: %s" % new_disk_format)
print("Transfer format: %s" % image_info["transfer_format"])

# This example will connect to the server and create a new `floating`
# disk, one that isn't attached to any virtual machine.
# Then using transfer service it will transfer disk data from local
# qcow2 disk to the newly created disk in server.

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
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the root service:
system_service = connection.system_service()

print("Creating disk...")

image_size = os.path.getsize(args.filename)
disks_service = connection.system_service().disks_service()
disk = disks_service.add(
    disk=types.Disk(
        name=os.path.basename(args.filename),
        content_type=image_info["content_type"],
        description='Uploaded disk',
        format=new_disk_format,
        initial_size=image_size,
        provisioned_size=image_info["virtual-size"],
        sparse=new_disk_format == types.DiskFormat.COW,
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
    time.sleep(5)
    disk = disk_service.get()
    if disk.status == types.DiskStatus.OK:
        break

print("Creating transfer session...")

# Get a reference to the service that manages the image
# transfer that was added in the previous step:
transfers_service = system_service.image_transfers_service()

# Add a new image transfer:
transfer = transfers_service.add(
    types.ImageTransfer(
        image=types.Image(
            id=disk.id
        ),
        # 'format' can be used only for ovirt-engine 4.3 or above
        format=image_info["transfer_format"],
     )
)

# Get reference to the created transfer service:
transfer_service = transfers_service.image_transfer_service(transfer.id)

# After adding a new transfer for the disk, the transfer's status will be INITIALIZING.
# Wait until the init phase is over. The actual transfer can start when its status is "Transferring".
while transfer.phase == types.ImageTransferPhase.INITIALIZING:
    time.sleep(1)
    transfer = transfer_service.get()

print("Uploading image...")

# At this stage, the SDK granted the permission to start transferring the disk, and the
# user should choose its preferred tool for doing it - regardless of the SDK.
# In this example, we will use Python's httplib.HTTPSConnection for transferring the data.
if args.direct:
    if transfer.transfer_url is not None:
        destination_url = transfer.transfer_url
    else:
        print("Direct upload to host not supported (requires ovirt-engine 4.2 or above).")
        sys.exit(1)
else:
    destination_url = transfer.proxy_url

image_size = os.path.getsize(args.filename)

with ui.ProgressBar(image_size) as pb:
    client.upload(
        args.filename,
        destination_url,
        args.cafile,
        secure=args.secure,
        progress=pb.update)

print("Finalizing transfer session...")
# Successful cleanup
transfer_service.finalize()
connection.close()

print("Upload completed successfully")
