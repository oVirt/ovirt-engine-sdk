#!/usr/bin/env python
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
Show how to download disk snapshots using imageio client.

Requires the ovirt-imageio-client package.
"""

import os
from contextlib import closing

from ovirt_imageio import client

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

from helpers import common
from helpers import imagetransfer
from helpers import units
from helpers.common import progress


def parse_args():
    parser = common.ArgumentParser(description="Download disk snapshot")

    parser.add_argument(
        "sd_name",
        help="Storage domain name.")

    parser.add_argument(
        "disk_snapshot_uuid",
        help="Disk snapshot UUID to download.")

    parser.add_argument(
        "filename",
        help="Path to downloaded image.")

    parser.add_argument(
        "--backing-file",
        help="Download selected disks snapshot data, rebasing on the "
             "given backing file. Specified backing file must include "
             "data from disk snapshot parent disk snapshot.")

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
with closing(connection):

    # Find the storage domain.
    sds_service = connection.system_service().storage_domains_service()
    sds = sds_service.list(search="name={}".format(args.sd_name))
    if not sds:
        raise RuntimeError("No such storage domain: {}".format(args.sd_name))

    storage_domain = sds[0]

    # Find the disk snapshot.
    sd_service = sds_service.storage_domain_service(storage_domain.id)
    dss_service = sd_service.disk_snapshots_service()
    ds_service = dss_service.snapshot_service(args.disk_snapshot_uuid)
    try:
        disk_snapshot = ds_service.get()
    except sdk.NotFoundError:
        raise RuntimeError(
            "No such disk snapshot: {}"
            .format(args.disk_snapshot_uuid)) from None

    # Find a host for this transfer. This is an optional step allowing optimizing
    # the transfer using unix socket when running this code on a oVirt hypervisor
    # in the same data center.
    host = imagetransfer.find_host(connection, storage_domain.name)

    progress("Creating image transfer...")

    transfer = imagetransfer.create_transfer(
        connection,
        disk_snapshot=disk_snapshot,
        direction=types.ImageTransferDirection.DOWNLOAD,
        host=host,
        shallow=bool(args.backing_file),
        timeout_policy=types.ImageTransferTimeoutPolicy(args.timeout_policy))
    try:

        progress("Transfer ID: %s" % transfer.id)
        progress("Transfer host name: %s" % transfer.host.name)

        extra_args = {}

        if args.use_proxy:
            download_url = transfer.proxy_url
        else:
            download_url = transfer.transfer_url
            extra_args["proxy_url"] = transfer.proxy_url

        if args.backing_file:
            extra_args["backing_file"] = os.path.basename(args.backing_file)
            extra_args["backing_format"] = "qcow2"

        progress("Downloading image...")

        with client.ProgressBar() as pb:
            client.download(
                download_url,
                args.filename,
                args.cafile,
                secure=args.secure,
                max_workers=args.max_workers,
                buffer_size=args.buffer_size,
                progress=pb,
                **extra_args)
    finally:
        progress("Finalizing image transfer...")
        imagetransfer.finalize_transfer(
            connection, transfer, disk_snapshot.disk)
