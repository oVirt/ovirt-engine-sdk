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

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example shows how to pin a virtual machine to a host, so that it
# will always run in that host.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the root of the tree of services:
system_service = connection.system_service()

# Find the virtual machine:
vms_service = system_service.vms_service()
vm = vms_service.list(search='name=myvm')[0]

# Update the placement policy of the virtual machine so that it is
# pinned to the host.
vm_service = vms_service.vm_service(vm.id)
vm_service.update(
    vm=types.Vm(
        placement_policy=types.VmPlacementPolicy(
            hosts=[
                types.Host(
                    name='myhost'
                )
            ]
        )
    )
)

# Close the connection to the server:
connection.close()
