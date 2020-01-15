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
import getpass
import logging
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import time

from ovirt_imageio_common import client
from ovirt_imageio_common import ui

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
        "--insecure",
        dest="secure",
        action="store_false",
        default=False,
        help=("do not verify server certificates and host name (not "
              "recommended)."))

    parser.add_argument(
        "--password-file",
        help="file containing password of the specified by user (if file is "
             "not specified, read from standard input)")

    parser.add_argument(
        "-f", "--format",
        choices=("raw", "qcow2"),
        default="qcow2",
        help=("Downloaded file format. For best compatibility, use qcow2 "
              "(default qcow2)"))

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

        # format=raw enables the NBD backend, enbaling:
        # - Download raw guest data, regardless of the disk format.
        # - Collapsed qcow2 chains to single raw file.
        # - Extents reporting for qcow2 images and raw images on file storage,
        #   speeding up the transfer.
        format=types.DiskFormat.RAW,
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
    download_url = transfer.proxy_url
else:
    download_url = transfer.transfer_url

# At this stage, the SDK granted the permission to start transferring the disk, and the
# user should choose its preferred tool for doing it. We use the recommended
# way, ovirt-imageio client library.

print("Downloading image...")

try:
    with ui.ProgressBar() as pb:
        client.download(
            download_url,
            args.filename,
            args.cafile,
            fmt=args.format,
            secure=args.secure,
            progress=pb)
finally:
    # Finalize the session.
    print("Finalizing transfer session...")
    transfer_service.finalize()

# Close the connection to the server:
connection.close()
