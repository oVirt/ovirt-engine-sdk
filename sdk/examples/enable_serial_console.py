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

# This example will connect to the server, find a virtual machine and enable the
# serial console if it isn't enabled yet:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine41.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Find the virtual machine. Note the use of the `all_content` parameter, it is
# required in order to obtain additional information that isn't retrieved by
# default, like the configuration of the serial console.
vms_service = connection.system_service().vms_service()
vm = vms_service.list(search='name=myvm', all_content=True)[0]

# Check if the serial console is enabled, and if it isn't then update the
# virtual machine to enable it:
if not vm.console.enabled:
    vm_service = vms_service.vm_service(vm.id)
    vm_service.update(
        types.Vm(
            console=types.Console(
                enabled=True
            )
        )
    )

# Close the connection to the server:
connection.close()
