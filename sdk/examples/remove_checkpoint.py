#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
This example will connect to the server and perform removal of a
VM checkpoint.

Note that this feature API is supported from version 4.4
but the feature is currently in tech-preview until libvirt will
release official release that contains the support for incremental
backup.
"""
import time

from contextlib import closing

import ovirtsdk4 as sdk
from helpers import common
from helpers.common import progress

parser = common.ArgumentParser(description="Remove VM checkpoint")
parser.add_argument("vm_uuid", help="VM UUID for removing checkpoint.")
parser.add_argument("checkpoint_uuid", help="The removed checkpoint UUID.")
args = parser.parse_args()
common.configure_logging(args)

progress("Removing VM %r checkpoint %r" % (args.vm_uuid, args.checkpoint_uuid))

# Create a connection to the server
connection = common.create_connection(args)
with closing(connection):
    system_service = connection.system_service()
    vm_service = system_service.vms_service().vm_service(id=args.vm_uuid)
    checkpoints_service = vm_service.checkpoints_service()
    checkpoint_service = checkpoints_service.checkpoint_service(id=args.checkpoint_uuid)

    # Validate that the VM has the requested checkpoint
    try:
        checkpoint_service.get()
    except sdk.NotFoundError:
        raise RuntimeError("VM {} has no checkpoint {}".format(args.vm_uuid, args.checkpoint_uuid))

    # Removing the checkpoint
    checkpoint_service.remove()

    # Validate that the checkpoint removed
    try:
        while checkpoint_service.get():
            time.sleep(1)
    except sdk.NotFoundError:
        progress("Checkpoint %r removed successfully" % args.checkpoint_uuid)
