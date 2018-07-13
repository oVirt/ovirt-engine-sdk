#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2016 Red Hat, Inc.
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
import operator

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and update the description of
# a virtual machine:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the virtual machines service:
vms_service = connection.system_service().vms_service()

# Retrieve the description of the virtual machine:
vm = vms_service.list(search='name=myvm')[0]

# In order to update the virtual machine we need a reference to the service
# tht manages it:
vm_service = vms_service.vm_service(vm.id)

# Get the reference to the numa nodes service of the virtual machine:
vm_nodes_service = vm_service.numa_nodes_service()

# For each numa node of the virtual machine we call the remove method
# to remove the numa node. Note that we must remove the numa nodes from
# highest numa node index to lowest numa node index:
for node in sorted(
    vm_nodes_service.list(), key=operator.attrgetter('index'), reverse=True
):
    print("Removing node with id '%s'" % node.id)
    vm_node_service = vm_nodes_service.node_service(node.id)
    vm_node_service.remove()

# Close the connection to the server:
connection.close()
