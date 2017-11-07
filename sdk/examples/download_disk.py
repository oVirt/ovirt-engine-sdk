#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2017 Red Hat, Inc.
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
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import ssl
import sys
import time

from httplib import HTTPSConnection

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

# This is the size of each downloaded chunck.
# May be tuned according to setup needs.
BUF_SIZE = 128 * 1024

logging.basicConfig(level=logging.DEBUG, filename='example.log')


# This example will connect to the server and download the data
# of the disk, to the local qcow2 file.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine/ovirt-engine/api',
    username='admin@internal',
    password='123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the root service:
system_service = connection.system_service()

# Get the reference to the disks service:
disks_service = connection.system_service().disks_service()

# Find the disk we want to download by the id:
disk_service = disks_service.disk_service('f2a0da15-2b7e-4ded-be3c-59ff968a6894')
disk = disk_service.get()

# Get a reference to the service that manages the image
# transfer that was added in the previous step:
transfers_service = system_service.image_transfers_service()

# Add a new image transfer:
transfer = transfers_service.add(
    types.ImageTransfer(
        image=types.Image(
            id=disk.id
        ),
        direction=types.ImageTransferDirection.DOWNLOAD,
    )
)

# Get reference to the created transfer service:
transfer_service = transfers_service.image_transfer_service(transfer.id)

# After adding a new transfer for the disk, the transfer's status will be INITIALIZING.
# Wait until the init phase is over. The actual transfer can start when its status is "Transferring".
while transfer.phase == types.ImageTransferPhase.INITIALIZING:
    time.sleep(1)
    transfer = transfer_service.get()

# Set needed headers for downloading:
transfer_headers = {
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

try:
    # Send the request
    proxy_connection.request(
        'GET',
        proxy_url.path,
        headers=transfer_headers,
    )
    # Get response
    r = proxy_connection.getresponse()

    # Check the response status
    if r.status not in (200, 204):
        print "Error downloding (%s)" % (r.reason,)
        try:
            data = r.read(512)
        except (EnvironmentError, HttpException):
            pass
        else:
            print "Response:"
            print data
        sys.exit(1)

    last_extend = time.time()
    bytes_to_read = int(r.getheader('Content-Length'))

    path = "/path/to/disk.qcow2"
    with open(path, "wb") as mydisk:
        while bytes_to_read > 0:
            # Calculate next chunk to read
            to_read = min(bytes_to_read, BUF_SIZE)

            # Read next chunk
            chunk = r.read(to_read)
            if not chunk:
                raise RuntimeError("Socket disconnected")

            # Write the content to file
            mydisk.write(chunk)
            bytes_to_read -= len(chunk)

            # Extend the transfer session once per minute
            now = time.time()
            if now - last_extend > 60:
                transfer_service.extend()
                last_extend = now
finally:
    # Finalize the session.
    transfer_service.finalize()

# Close the connection to the server:
connection.close()
