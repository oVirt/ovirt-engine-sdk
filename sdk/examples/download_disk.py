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

from __future__ import print_function

import argparse
import getpass
import inspect
import logging
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import time

from ovirt_imageio import client

from helpers import imagetransfer

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

    parser.add_argument(
        "--max-workers",
        type=int,
        default=4,
        help="maximum number of workers to use for download. The default "
             "(4) improves performance when downloading a single disk. "
             "You may want to use lower number if you download many disks "
             "in the same time.")

    parser.add_argument(
        "--debug",
        action="store_true",
        help="log debug level messages to example.log")

    return parser.parse_args()


def read_password(args):
    if args.password_file:
        with open(args.password_file) as f:
            return f.readline().rstrip('\n')
    else:
        return getpass.getpass()


args = parse_args()

logging.basicConfig(
    level=logging.DEBUG if args.debug else logging.INFO,
    filename="example.log",
    format="%(asctime)s %(levelname)-7s (%(threadName)s) [%(name)s] %(message)s"
)

# Create the connection to the server:
print("Connecting...")

connection = sdk.Connection(
    url=args.engine_url + '/ovirt-engine/api',
    username=args.username,
    password=read_password(args),
    ca_file=args.cafile,
    debug=args.debug,
    log=logging.getLogger(),
)

# Get the reference to the root service:
system_service = connection.system_service()

# Get the reference to the disks service:
disks_service = connection.system_service().disks_service()

# Find the disk we want to download by the id:
disk_service = disks_service.disk_service(args.disk_uuid)
disk = disk_service.get()

# Find a host for this transfer. This is an optional step allowing optimizing
# the transfer using unix socket when running this code on a oVirt hypervisor
# in the same data center.
sd_id = disk.storage_domains[0].id
sds_service = system_service.storage_domains_service()
storage_domain = sds_service.storage_domain_service(sd_id).get()
host = imagetransfer.find_host(connection, storage_domain.name)

print("Creating image transfer...")

transfer = imagetransfer.create_transfer(
    connection, disk, types.ImageTransferDirection.DOWNLOAD, host=host)

print("Transfer ID: %s" % transfer.id)
print("Transfer host name: %s" % transfer.host.name)

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

print("Downloading image...")

try:
    with client.ProgressBar() as pb:
        client.download(
            download_url,
            args.filename,
            args.cafile,
            fmt=args.format,
            secure=args.secure,
            progress=pb,
            **extra_args)
finally:
    print("Finalizing image transfer...")
    imagetransfer.finalize_transfer(connection, transfer, disk)

# Close the connection to the server:
connection.close()
