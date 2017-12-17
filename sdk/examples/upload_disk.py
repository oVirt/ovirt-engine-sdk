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

Usage:

    upload_disk.py FILE
"""

from __future__ import print_function

import json
import logging
import os
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import ssl
import subprocess
import sys
import time

from httplib import HTTPSConnection

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


# This seems to give the best throughput when uploading from my laptop
# SSD to a server that drop the data. You may need to tune this on your
# setup.
BUF_SIZE = 128 * 1024

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
        )
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
destination_url = urlparse(transfer.transfer_url) if direct_upload else urlparse(transfer.proxy_url)
context = ssl.create_default_context()

# Note that ovirt-imageio-proxy by default checks the certificates, so if you don't have
# your CA certificate of the engine in the system, you need to pass it to HTTPSConnection.
context.load_verify_locations(cafile='ca.pem')

proxy_connection = HTTPSConnection(
    destination_url.hostname,
    destination_url.port,
    context=context,
)

# Send the request head. Note the following:
#
# - We must send the Authorzation header with the signed ticket received
#   from the transfer service.
#
# - the server requires Content-Range header even when sending the
#   entire file.
#
# - the server requires also Content-Length.
#

proxy_connection.putrequest("PUT", destination_url.path)
proxy_connection.putheader('Authorization', transfer.signed_ticket)
proxy_connection.putheader('Content-Range',
                           "bytes %d-%d/%d" % (0, image_size - 1, image_size))
proxy_connection.putheader('Content-Length', "%d" % (image_size,))
proxy_connection.endheaders()

# Send the request body.

# Note that we must send the number of bytes we promised in the
# Content-Range header.

start = last_progress = time.time()

with open(image_path, "rb") as disk:
    pos = 0
    while pos < image_size:
        # Send the next chunk to the proxy.
        to_read = min(image_size - pos, BUF_SIZE)
        chunk = disk.read(to_read)
        if not chunk:
            transfer_service.pause()
            raise RuntimeError("Unexpected end of file at pos=%d" % pos)

        proxy_connection.send(chunk)
        pos += len(chunk)
        now = time.time()

        # Report progress every 10 seconds.
        if now - last_progress > 10:
            print("Uploaded %.2f%%" % (float(pos) / image_size * 100))
            last_progress = now

# Get the response
response = proxy_connection.getresponse()
if response.status != 200:
    transfer_service.pause()
    print("Upload failed: %s %s" % (response.status, response.reason))
    sys.exit(1)

elapsed = time.time() - start

print("Uploaded %.2fg in %.2f seconds (%.2fm/s)" % (
      image_size / float(1024**3), elapsed, image_size / 1024**2 / elapsed))

print("Finalizing transfer session...")
# Successful cleanup
transfer_service.finalize()
connection.close()
proxy_connection.close()

print("Upload completed successfully")
