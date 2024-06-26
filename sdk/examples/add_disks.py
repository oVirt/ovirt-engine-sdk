#!/usr/bin/env python3
#
# Copyright (c) 2021 Red Hat, Inc.
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
Show how to create many disks quickly.
"""

import time
from contextlib import closing

from ovirtsdk4 import types

from helpers import common
from helpers.common import progress
from helpers.units import humansize, GiB

parser = common.ArgumentParser(description="Create disks")

parser.add_argument(
    "--sd-name",
    required=True,
    help="Name of the storage domain.")

parser.add_argument(
    "--size",
    type=humansize,
    default=1 * GiB,
    help="Size of the disk")

parser.add_argument(
    "--format",
    choices=("raw", "qcow2"),
    help="Format of the created disk (default raw).")

parser.add_argument(
    "--sparse",
    action="store_true",
    help="Create sparse disk. Cannot be used with raw format on "
         "iSCSI or FC storage domain.")

parser.add_argument(
    "--count",
    type=int,
    help="Number of disks to create.")

args = parser.parse_args()

if args.format == "raw":
    disk_format = types.DiskFormat.RAW
else:
    disk_format = types.DiskFormat.COW

progress("Connecting...")
connection = common.create_connection(args)
with closing(connection):
    disks_service = connection.system_service().disks_service()

    waiting = set()

    for i in range(args.count):
        disk = disks_service.add(
            disk=types.Disk(
                name="disk-%s" % i,
                content_type=types.DiskContentType.DATA,
                description='Created by add_disks.py',
                format=disk_format,
                provisioned_size=args.size,
                sparse=args.sparse,
                storage_domains=[
                    types.StorageDomain(
                        name=args.sd_name
                    )
                ]
            )
        )

        progress("Created disk %s id=%s" % (i, disk.id))
        waiting.add(disk.id)

    progress("Waiting until disks are ready...")
    while waiting:
        time.sleep(1)
        for disk_id in list(waiting):
            disk = disks_service.disk_service(disk_id).get()
            if disk.status == types.DiskStatus.OK:
                progress("Disk %s is ready" % disk_id)
                waiting.remove(disk_id)

progress("All disks are ready")
