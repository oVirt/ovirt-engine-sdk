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
Show how to list disk snapshots.
"""

import json
from contextlib import closing

import ovirtsdk4 as sdk
from helpers import common


def parse_args():
    parser = common.ArgumentParser(description="List disk snapshots")

    parser.add_argument(
        "disk_id",
        help="Disk ID to query.")

    return parser.parse_args()


args = parse_args()
common.configure_logging(args)

connection = common.create_connection(args)
with closing(connection):

    # Find the disk.
    disks_service = connection.system_service().disks_service()
    disk_service = disks_service.disk_service(args.disk_id)

    try:
        disk = disk_service.get()
    except sdk.NotFoundError:
        raise RuntimeError("No such disk: {}".format(args.disk_id)) from None

    # Find the storage domain service.
    sd_id = disk.storage_domains[0].id
    sds_service = connection.system_service().storage_domains_service()
    sd_service = sds_service.storage_domain_service(sd_id)

    # Find the disk snapshots using the disk snapshots service.
    # TODO: Use disk's snapshots service to get filter the snapshot on the
    # server side.
    disk_snapshots_service = sd_service.disk_snapshots_service()

    # Create mapping from snapshot parent to snapshot, used to reconstruct the
    # snapshot chain.
    snapshots = {}
    for s in disk_snapshots_service.list(include_active=True):
        if s.disk.id != disk.id:
            continue
        parent = s.parent.id if s.parent else None
        child = {
            "actual_size": s.actual_size,
            "format": str(s.format),
            "id": s.id,
            "parent": parent,
            "status": str(s.status),
        }
        snapshots[parent] = child

    # Create snapshots chain using parent links.
    chain = []
    parent = None
    while snapshots:
        child = snapshots.pop(parent)
        chain.append(child)
        parent = child["id"]

    print(json.dumps(chain, indent=2))
