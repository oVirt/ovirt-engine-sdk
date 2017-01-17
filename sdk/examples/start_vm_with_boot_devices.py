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

import logging
import time

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and start a virtual machine.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the "vms" service:
vms_service = connection.system_service().vms_service()

# Find the virtual machine:
vm = vms_service.list(search='name=myvm')[0]

# Locate the service that manages the virtual machine, as that is where
# the action methods are defined:
vm_service = vms_service.vm_service(vm.id)

# Call the "start" method of the service to start it with
# additional properties in a run once configuration

vm_service.start(
    vm=types.Vm(
        os=types.OperatingSystem(
            boot=types.Boot(
                devices=[
                    types.BootDevice.NETWORK,
                    types.BootDevice.CDROM
                ]
            )
        )
    )
)

# additional documentation about attributes and types that can be changed:
# https://your.rhv.host/ovirt-engine/api/model#types/vm
# https://your.rhv.host/ovirt-engine/api/model#types/operating_system
# https://your.rhv.host/ovirt-engine/api/model#types/boot
# https://your.rhv.host/ovirt-engine/api/model#types/boot_device


# Wait till the virtual machine is up:
while True:
    time.sleep(5)
    vm = vm_service.get()
    if vm.status == types.VmStatus.UP:
        break

# Close the connection to the server:
connection.close()
