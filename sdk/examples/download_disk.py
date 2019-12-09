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

from __future__ import print_function

import argparse
import logging
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import ssl
import sys
import time

from six.moves.http_client import HTTPSConnection, HTTPException
from six.moves.urllib.parse import urlparse

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and download the data
# of the disk to a local file.

def parse_args():
    parser = argparse.ArgumentParser(description="Download disk")

    parser.add_argument(
        "disk_uuid",
        help="disk UUID to download")

    parser.add_argument(
        "filename",
        help="path to downloaded disk")

    parser.add_argument(
        "--engine-url",
        required=True,
        help="oVirt engine URL (e.g. https://my-engine:port)")

    parser.add_argument(
        "--username",
        required=True,
        help="username of engine API")

    parser.add_argument(
        "-c", "--cafile",
        required=True,
        help="path to oVirt engine certificate for verifying server.")

    parser.add_argument(
        "--password-file",
        help="file containing password of the specified by user (if file is "
             "not specified, read from standard input)")

    parser.add_argument(
        "-b", "--buffer-size",
        type=lambda v: int(v) * 1024,
        default=128 * 1024,
        help=("buffer size in KiB for upload. The default (128 KiB) provides "
              "best results in our tests, but you may like to tune this"))

    parser.add_argument(
        "--use-proxy",
        dest="use_proxy",
        default=False,
        action="store_true",
        help="download via proxy on the engine host (less efficient)")

    return parser.parse_args()


def read_password(args):
    if args.password_file:
        with open(args.password_file) as f:
            return f.readline().rstrip('\n')
    else:
        return getpass.getpass()


args = parse_args()

# Create the connection to the server:
print("Connecting...")

connection = sdk.Connection(
    url=args.engine_url + '/ovirt-engine/api',
    username=args.username,
    password=read_password(args),
    ca_file=args.cafile,
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the root service:
system_service = connection.system_service()

# Get the reference to the disks service:
disks_service = connection.system_service().disks_service()

# Find the disk we want to download by the id:
disk_service = disks_service.disk_service(args.disk_uuid)
disk = disk_service.get()

print("Creating a transfer session...")

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

if args.use_proxy:
    download_url = urlparse(transfer.proxy_url)
else:
    download_url = urlparse(transfer.transfer_url)

# At this stage, the SDK granted the permission to start transferring the disk, and the
# user should choose its preferred tool for doing it - regardless of the SDK.
# In this example, we will use Python's httplib.HTTPSConnection for transferring the data.

context = ssl.create_default_context()

# Note that ovirt-imageio by default checks the certificates, so if you don't have
# your CA certificate of the engine in the system, you need to pass it to HTTPSConnection.
context.load_verify_locations(cafile=args.cafile)

download_connection = HTTPSConnection(
    download_url.hostname,
    download_url.port,
    context=context,
)

print("Downloading image...")

try:
    # Send the request
    download_connection.request('GET', download_url.path)
    # Get response
    r = download_connection.getresponse()

    # Check the response status
    if r.status not in (200, 204):
        print("Error downloding (%s)" % (r.reason,))
        try:
            data = r.read(512)
        except (EnvironmentError, HTTPException):
            pass
        else:
            print("Response:")
            print(data)
        sys.exit(1)

    start = last_progress = time.time()
    image_size = int(r.getheader('Content-Length'))
    with open(args.filename, "wb") as mydisk:
        pos = 0
        while pos < image_size:
            # Calculate next chunk to read
            to_read = min(image_size - pos, args.buffer_size)

            # Read next chunk
            chunk = r.read(to_read)
            if not chunk:
                raise RuntimeError("Socket disconnected")

            # Write the content to file
            mydisk.write(chunk)
            pos += len(chunk)
            now = time.time()

            # Report progress every 10 seconds
            if now - last_progress > 10:
                print("Downloaded %.2f%%" % (pos / float(image_size) * 100))
                last_progress = now

    elapsed = time.time() - start
    print("Downloaded %.2fg in %.2f seconds (%.2fm/s)" % (
        image_size / float(1024**3), elapsed, image_size / 1024**2 / elapsed))

finally:
    # Finalize the session.
    print("Finalizing transfer session...")
    transfer_service.finalize()

# Close the connection to the server:
connection.close()
