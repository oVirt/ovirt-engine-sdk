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

import logging
import os
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import ssl
import time

from httplib import HTTPSConnection

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


logging.basicConfig(level=logging.DEBUG, filename='example.log')


# This example will connect to the server and create a new `floating`
# disk, one that isn't attached to any virtual machine.
# Then using transfer service it will transfer disk data from local
# qcow2 disk to the newly created disk in server.

# Create the connection to the server:
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
initial_size = 1 * 2**30
provisioned_size = 10 * 2**30
disks_service = connection.system_service().disks_service()
disk = disks_service.add(
    disk=types.Disk(
        name='mydisk',
        description='My disk',
        format=types.DiskFormat.COW,
        provisioned_size=provisioned_size,
        initial_size=initial_size,
        storage_domains=[
            types.StorageDomain(
                name='data'
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

# Set needed headers for uploading:
upload_headers = {
    'Authorization': transfer.signed_ticket,
}

# At this stage, the SDK granted the permission to start transferring the disk, and the
# user should choose its preferred tool for doing it - regardless of the SDK.
# In this example, we will use Python's httplib.HTTPSConnection for transferring the data.
proxy_url = urlparse(transfer.proxy_url)
context = ssl.create_default_context()

# Note that ovirt-imageio-proxy by default checks the certificates, so if you don't have
# your CA certificate of the engine in the system, you need to pass it to HTTPSConnection.
context.load_verify_locations(cafile='ca.pem')

proxy_connection = HTTPSConnection(
    proxy_url.hostname,
    proxy_url.port,
    context=context,
)

path = "/path/to/disk.qcow2"
MiB_per_request = 8
with open(path, "rb") as disk:
    size = os.path.getsize(path)
    chunk_size = 1024 * 1024 * MiB_per_request
    pos = 0
    while pos < size:
        # Extend the transfer session.
        transfer_service.extend()
        # Set the content range, according to the chunk being sent.
        upload_headers['Content-Range'] = "bytes %d-%d/%d" % (pos, min(pos + chunk_size, size) - 1, size)
        # Perform the request.
        proxy_connection.request(
            'PUT',
            proxy_url.path,
            disk.read(chunk_size),
            headers=upload_headers,
        )
        # Print response
        r = proxy_connection.getresponse()
        print r.status, r.reason, "Completed", "{:.0%}".format(pos / float(size))
        # Continue to next chunk.
        pos += chunk_size


print "Completed", "{:.0%}".format(pos / float(size))
# Finalize the session.
transfer_service.finalize()

# Close the connection to the server:
connection.close()
