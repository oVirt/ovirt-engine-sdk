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

"""
Download disk example code.

Requires the ovirt-imageio-client package.
"""

import inspect
import time

from ovirt_imageio import client

import ovirtsdk4.types as types

from helpers import common
from helpers import imagetransfer
from helpers import units
from helpers.common import progress

# This example will connect to the server and download the data
# of the disk to a local file.

def parse_args():
    parser = common.ArgumentParser(description="Download disk")

    parser.add_argument(
        "disk_uuid",
        help="Disk UUID to download.")

    parser.add_argument(
        "filename",
        help="Path to write downloaded image.")

    parser.add_argument(
        "-f", "--format",
        choices=("raw", "qcow2"),
        default="qcow2",
        help=("Downloaded file format. For best compatibility, use qcow2 "
              "(default qcow2)."))

    parser.add_argument(
        "--use-proxy",
        dest="use_proxy",
        default=False,
        action="store_true",
        help="Download via proxy on the engine host (less efficient).")

    parser.add_argument(
        "--max-workers",
        type=int,
        default=4,
        help="Maximum number of workers to use for download. The default "
             "(4) improves performance when downloading a single disk. "
             "You may want to use lower number if you download many disks "
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


args = parse_args()
common.configure_logging(args)

progress("Connecting...")
connection = common.create_connection(args)

# Get the reference to the disks service:
disks_service = connection.system_service().disks_service()

# Find the disk we want to download by the id:
disk_service = disks_service.disk_service(args.disk_uuid)
disk = disk_service.get()

# Find a host for this transfer. This is an optional step allowing optimizing
# the transfer using unix socket when running this code on a oVirt hypervisor
# in the same data center.
sd_id = disk.storage_domains[0].id
sds_service = connection.system_service().storage_domains_service()
storage_domain = sds_service.storage_domain_service(sd_id).get()
host = imagetransfer.find_host(connection, storage_domain.name)

progress("Creating image transfer...")

transfer = imagetransfer.create_transfer(
    connection, disk, types.ImageTransferDirection.DOWNLOAD, host=host,
    timeout_policy=types.ImageTransferTimeoutPolicy(args.timeout_policy))

progress("Transfer ID: %s" % transfer.id)
progress("Transfer host name: %s" % transfer.host.name)

# At this stage, the SDK granted the permission to start transferring the disk, and the
# user should choose its preferred tool for doing it. We use the recommended
# way, ovirt-imageio client library.

extra_args = {}

parameters = inspect.signature(client.download).parameters

# Use multiple workers to speed up the download.
if "max_workers" in parameters:
        extra_args["max_workers"] = args.max_workers

if args.use_proxy:
    download_url = transfer.proxy_url
else:
    download_url = transfer.transfer_url

    # Use fallback to proxy_url if feature is available. Download will use the
    # proxy_url if transfer_url is not accessible.
    if "proxy_url" in parameters:
        extra_args["proxy_url"] = transfer.proxy_url

progress("Downloading image...")

try:
    with client.ProgressBar() as pb:
        client.download(
            download_url,
            args.filename,
            args.cafile,
            fmt=args.format,
            secure=args.secure,
            buffer_size=args.buffer_size,
            progress=pb,
            **extra_args)
finally:
    progress("Finalizing image transfer...")
    imagetransfer.finalize_transfer(connection, transfer, disk)

# Close the connection to the server:
connection.close()
