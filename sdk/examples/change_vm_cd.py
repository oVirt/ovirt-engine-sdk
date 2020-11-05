#!/usr/bin/env python
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

import logging
import time

from contextlib import closing

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

from helpers import common

# This example will connect to the server and change CD of the virtual machine.

parser = common.ArgumentParser(description="Change VM CD-ROM disk")

parser.add_argument(
    "vm_name",
    help="Name of VM.")

parser.add_argument(
    "--disk-id",
    help="ID of the disk to be loaded into CD-ROM. If not specified "
         "the current CD will be ejected.")

parser.add_argument(
    "--permanent",
    dest="current",
    action="store_false",
    help="If specified CD should be changed only after next boot."
         "The change will be permanent.")

args = parser.parse_args()
common.configure_logging(args)
connection = common.create_connection(args)

with closing(connection):
    # Get the reference to the "vms" service:
    vms_service = connection.system_service().vms_service()

    # Find the virtual machine:
    vm = vms_service.list(search="name={}".format(args.vm_name))[0]

    # Locate the service that manages the virtual machine:
    vm_service = vms_service.vm_service(vm.id)

    # Locate the service that manages the CDROM devices of the VM:
    cdroms_service = vm_service.cdroms_service()

    # Get the first found CDROM:
    cdrom = cdroms_service.list()[0]

    # Locate the service that manages the CDROM device found in previous step
    # of the VM:
    cdrom_service = cdroms_service.cdrom_service(cdrom.id)

    # Change the CD of the VM to file with 'disk-id'. By default the change
    # to the disk is visible to the current running virtual machine immediately,
    # but won't be visible to the virtual machine after the next boot. If you
    # want to change CD permanently, use --now=False. Using this option will
    # change the CD permanently, but it will become visible only after next
    # boot.
    cdrom_service.update(
        cdrom=types.Cdrom(
            file=types.File(
                id=args.disk_id
            ),
        ),
        current=args.current,
    )

