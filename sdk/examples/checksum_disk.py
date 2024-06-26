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
Show how to compute a disk checksum.

Requires ovirt-imageio-client >= 2.0.10-1
"""

import json
import ssl

from contextlib import closing
from http import client
from urllib.parse import urlparse

from ovirtsdk4 import types
from helpers import common
from helpers import imagetransfer

parser = common.ArgumentParser(description="Compute disk checksum")

parser.add_argument("disk_uuid", help="Disk UUID.")

args = parser.parse_args()
common.configure_logging(args)

connection = common.create_connection(args)
with closing(connection):
    system_service = connection.system_service()
    disks_service = connection.system_service().disks_service()
    disk_service = disks_service.disk_service(args.disk_uuid)
    disk = disk_service.get()

    transfer = imagetransfer.create_transfer(
        connection, disk, types.ImageTransferDirection.DOWNLOAD)
    try:
        url = urlparse(transfer.transfer_url)
        con = client.HTTPSConnection(
            url.netloc,
            context=ssl.create_default_context(cafile=args.cafile))
        with closing(con):
            con.request("GET", url.path + "/checksum")
            res = con.getresponse()

            if res.status != client.OK:
                error = res.read().decode("utf-8", "replace")
                raise RuntimeError(
                    "Error computing checksum: {}".format(error))

            result = json.loads(res.read())
            print(json.dumps(result, indent=4))
    finally:
        imagetransfer.finalize_transfer(connection, transfer, disk)
