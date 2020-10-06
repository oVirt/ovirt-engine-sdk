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
args = parser.parse_args()
common.configure_logging(args)

progress("Removing root checkpoint for VM %r" % args.vm_uuid)

# Create a connection to the server
connection = common.create_connection(args)
with closing(connection):
    progress("Looking up checkpoints %s" % args.vm_uuid)
    system_service = connection.system_service()
    vm_service = system_service.vms_service().vm_service(id=args.vm_uuid)
    checkpoints_service = vm_service.checkpoints_service()

    # Validate that the VM has checkpoints
    checkpoints = checkpoints_service.list()
    if not checkpoints:
        raise RuntimeError("VM {} has no checkpoints".format(args.vm_uuid))

    # Get the first checkpoint in the chain
    root_checkpoint = checkpoints_service.list()[0]
    progress("Removing root checkpoint %r" % root_checkpoint.id)

    # Removing the root checkpoint
    checkpoint_service = checkpoints_service.checkpoint_service(id=root_checkpoint.id)
    checkpoint_service.remove()

    # Validate that the checkpoint removed
    try:
        while checkpoint_service.get():
            time.sleep(1)
    except sdk.NotFoundError:
        progress("Root checkpoint removed successfully")
