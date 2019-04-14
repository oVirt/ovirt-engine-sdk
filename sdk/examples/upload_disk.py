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

direct_upload = False
if sys.argv[1] == "-d" or sys.argv[1] == "--direct":
    direct_upload = True
    image_path = sys.argv[2]
else:
    image_path = sys.argv[1]
image_size = os.path.getsize(image_path)

# Get image info using qemu-img

print("Checking image...")

out = subprocess.check_output(
    ["qemu-img", "info", "--output", "json", image_path])
image_info = json.loads(out)

if image_info["format"] not in ("qcow2", "raw"):
    raise RuntimeError("Unsupported image format %(format)s" % image_info)

print("Disk format: %s" % image_info["format"])

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
    with open(image_path, "rb") as f:
        f.seek(0x8000)
        primary_volume_descriptor = f.read(8)
    if primary_volume_descriptor == b"\x01CD001\x01\x00":
        content_type = types.DiskContentType.ISO

print("Disk content type: %s" % content_type)

# This example will connect to the server and create a new `floating`
# disk, one that isn't attached to any virtual machine.
# Then using transfer service it will transfer disk data from local
# qcow2 disk to the newly created disk in server.

# Create the connection to the server:
print("Connecting...")

connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the root service:
system_service = connection.system_service()

# Add the disk. Note the following:
#
# 1. The size of the disk is specified in bytes, so to create a disk
#    of 10 GiB the value should be 10 * 2^30.
#
# 2. The disk size is indicated using the 'provisioned_size' attribute,
#    but due to current limitations in the engine, the 'initial_size'
#    attribute also needs to be explicitly provided for _copy on write_
#    disks created on block storage domains, so that all the required
#    space is allocated upfront, otherwise the upload will eventually
#    fail.
#
# 3. The disk initial size must be bigger or the same as the size of the data
#    you will upload.

print("Creating disk...")

if image_info["format"] == "qcow2":
    disk_format = types.DiskFormat.COW
else:
    disk_format = types.DiskFormat.RAW

disks_service = connection.system_service().disks_service()
disk = disks_service.add(
    disk=types.Disk(
        name=os.path.basename(image_path),
        content_type=content_type,
        description='Uploaded disk',
        format=disk_format,
        initial_size=image_size,
        provisioned_size=image_info["virtual-size"],
        sparse=disk_format == types.DiskFormat.COW,
        storage_domains=[
            types.StorageDomain(
                name='mydata'
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
        format=disk_format, # Can be used only for ovirt-engine 4.3 or above
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
if direct_upload:
    if transfer.transfer_url is not None:
        destination_url = transfer.transfer_url
    else:
        print("Direct upload to host not supported (requires ovirt-engine 4.2 or above).")
        sys.exit(1)
else:
    destination_url = transfer.proxy_url

image_size = os.path.getsize(image_path)

with ui.ProgressBar(image_size) as pb:
    client.upload(
        image_path,
        destination_url,
        'ca.pem',
        progress=pb.update)

print("Finalizing transfer session...")
# Successful cleanup
transfer_service.finalize()
connection.close()

print("Upload completed successfully")
