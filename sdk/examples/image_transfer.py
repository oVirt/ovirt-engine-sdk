#!/usr/bin/env python
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
Show how to start and stop image transfer, and keep the transfer alive.

imageio server will time out client connection after 60 seconds if the client
does not send any request. If you need to delay the transfer for some reason,
but want to keep the connection open, you can send some request to keep the
connection alive.

How to use this example
-----------------------

1. Create a new empty disk in engine

Find the disk uuid, assuming e2b9464e-6d9d-4f92-8375-2e5e087c5674 in this
example.

2. Run the image_transfer.py

$ ./image_transfer.py -c engine3 upload e2b9464e-6d9d-4f92-8375-2e5e087c5674
[   0.0 ] Connecting to engine...
[   0.0 ] Looking up disk e2b9464e-6d9d-4f92-8375-2e5e087c5674
[   0.3 ] Creating image transfer for upload
[   2.5 ] Transfer ID: da289f12-3513-467e-9da4-5e1a5d11c15f
[   2.5 ] Transfer host name: host4
[   2.5 ] Transfer URL: https://host4:54322/images/5916515f-d628-4311-8ce2-614c9d09731e
[   2.5 ] Proxy URL: https://engine3:54323/images/5916515f-d628-4311-8ce2-614c9d09731e
[   2.5 ] Conneted to imageio server

While the script is running, you can use Transfer URL or Proxy URL to access
imageio server.

$ curl -k https://host4:54322/images/5916515f-d628-4311-8ce2-614c9d09731e/extents | jq
[
  {
    "start": 0,
    "length": 6442450944,
    "zero": true,
    "hole": false
  }
]

You can also use imageio example client from imageio source:

$ git clone https://github.com/oVirt/ovirt-imageio.git
$ cd ovirt-imageio
$ make

$ examles/imageio-client upload \
    /var/tmp/fedora-32.img \
    https://host4:54322/images/5916515f-d628-4311-8ce2-614c9d09731e
[ 100.00% ] 6.00 GiB, 4.01 seconds, 1.50 GiB/s

$ curl -sk https://host4:54322/images/5916515f-d628-4311-8ce2-614c9d09731e/extents | jq
[
  {
    "start": 0,
    "length": 65536,
    "zero": false,
    "hole": false
  },
  {
    "start": 65536,
    "length": 983040,
    "zero": true,
    "hole": false
  },
...

To finalize the transfer, interrupt the script.

You can also cancel the transfer from engine UI, which will delete the disk
used by the image transfer.

Requires ovirt-imageio-client >= 2.0.10-1
"""

import time

from contextlib import closing

from ovirtsdk4 import types

from helpers import common
from helpers import imagetransfer
from helpers.common import progress

from ovirt_imageio.client import ImageioClient


parser = common.ArgumentParser(description="Run an image transfer")

parser.add_argument(
    "direction",
    choices=["upload", "download"],
    help="Transfer direction.")

parser.add_argument(
    "disk_uuid",
    help="Disk UUID for transfer.")

parser.add_argument(
    "--shallow",
    action="store_true",
    help="Transfer only specified image instead of entire image chain.")

parser.add_argument(
    "--inactivity-timeout",
    type=int,
    help="Keep the transfer alive for specified number of seconds if "
         "the client is not active. (default 60)")

parser.add_argument(
    "--read-delay",
    type=int,
    default=50,
    help="Keep the connection alive by reading from the server every "
         "read-delay seconds (default 50).")

args = parser.parse_args()
common.configure_logging(args)

progress("Connecting to engine...")
connection = common.create_connection(args)
with closing(connection):

    progress("Looking up disk %s" % args.disk_uuid)
    system_service = connection.system_service()
    disks_service = connection.system_service().disks_service()
    disk_service = disks_service.disk_service(args.disk_uuid)
    disk = disk_service.get()

    progress("Creating image transfer for %s" % args.direction)
    if args.direction == "upload":
        direction = types.ImageTransferDirection.UPLOAD
    else:
        direction = types.ImageTransferDirection.DOWNLOAD

    transfer = imagetransfer.create_transfer(
        connection, disk, direction,
        shallow=args.shallow,
        inactivity_timeout=args.inactivity_timeout)
    try:
        progress("Transfer ID: %s" % transfer.id)
        progress("Transfer host name: %s" % transfer.host.name)
        progress("Transfer URL: %s" % transfer.transfer_url)
        progress("Proxy URL: %s" % transfer.proxy_url)

        # The client will use transfer_url if possible, or fallback to
        # proxy_url.
        with ImageioClient(
                transfer.transfer_url,
                cafile=args.cafile,
                proxy_url=transfer.proxy_url) as client:
            progress("Conneted to imageio server")

            # Keep the connection alive by reading from server.
            buf = bytearray(4096)
            while True:
                progress("Reading from server...")
                client.read(0, buf)
                time.sleep(args.read_delay)
    except KeyboardInterrupt:
        print()
    finally:
        progress("Finalizing image transfer...")
        imagetransfer.finalize_transfer(connection, transfer, disk)
