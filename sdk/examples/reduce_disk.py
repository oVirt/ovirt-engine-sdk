#!/usr/bin/env python
#
# Copyright (c) 2020 Red Hat, Inc.
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
Show how to reduce disk allocation to optimal size.

Reducing a disk is useful after disk on block storage (FC, iSCSI) was
extended and is using more space than needed. The operation deallocates
unneeded space.

This operation is useful after:
- Deleting the last snapshot of a VM
- Moving a VM disk to another storage domain while a VM is running.
- In some cases, after sparsifying a disk.

If a Disk is attached to a VM, the VM must be powered off to reduce the disk.
"""

import time
from contextlib import closing

import ovirtsdk4 as sdk
from ovirtsdk4 import types

from helpers import common
from helpers.common import progress

parser = common.ArgumentParser(description="Reduce disk")

parser.add_argument(
    "disk_id",
    help="disk UUID to reduce")

args = parser.parse_args()

common.configure_logging(args)

progress("Connecting...")
connection = common.create_connection(args)
with closing(connection):

    # Locate the disk service.
    disks_service = connection.system_service().disks_service()
    disk_service = disks_service.disk_service(args.disk_id)
    try:
        disk = disk_service.get()
    except sdk.NotFoundError:
        raise RuntimeError("No such disk: {}".format(args.disk_id)) from None

    # TODO: It would be nice to show here the original allocation before and
    # after the reduce, but engine reports cached value which is not helpful.

    progress("Reducing disk...")
    disk_service.reduce()

    # Wait until the disk is unlocked.
    while True:
        time.sleep(1)
        disk = disk_service.get()
        if disk.status == types.DiskStatus.OK:
            break

    progress("Disk was reduced successfully")
