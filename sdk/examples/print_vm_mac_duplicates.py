#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2018 Red Hat, Inc.
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

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and print the information about
# the duplicated virtual machine addresses:

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

# Get list of all virtual machines:
vms = vms_service.list()

# Iterate via all virtual machines and print if they have duplicated MAC
# address with any other virtual machine in the system:
vm_nics = {}
for vm in vms:
    vm_service = vms_service.vm_service(vm.id)
    nics_service = vm_service.nics_service()
    for nic in nics_service.list():
        if nic.mac.address in vm_nics:
            print(
                "[%s]: MAC address '%s' is used by following virtual machine already: %s" % (
                    vm.name,
                    nic.mac.address,
                    vm_nics[nic.mac.address]
                )
            )
        else:
            vm_nics[nic.mac.address] = vm.name

# Close the connection to the server:
connection.close()
