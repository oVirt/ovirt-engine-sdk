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

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and create a new virtual machine
# pool from template:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the "vm pools" service:
vm_pools_service = connection.system_service().vm_pools_service()

# Use the "add" method to create a new virtual machine pool:
vm_pools_service.add(
    pool=types.VmPool(
        name='myvmpool',
        cluster=types.Cluster(
            name='mycluster',
        ),
        template=types.Template(
            name='mytemplate',
        ),
        size=3,
        prestarted_vms=1,
        max_user_vms=1,
        type=types.VmPoolType.AUTOMATIC,
    ),
)

# Close the connection to the server:
connection.close()
