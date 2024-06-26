#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2019 Red Hat, Inc.
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

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the vm service for a particular vm:
vms_service = connection.system_service().vms_service()
vm = vms_service.list(search='name=myvm')[0]
vm_service = vms_service.vm_service(vm.id)

# Get the reported-devices service for this vm:
reported_devices_service = vm_service.reported_devices_service()

# Get the guest reported devices
reported_devices = reported_devices_service.list()

# Get and print the IP-addresses used by the VM:
print('VM myvm IP addresses are:')
for reported_device in reported_devices:
    ips = reported_device.ips
    if ips:
        for ip in ips:
            print('   - %s' % ip.address)

# Close the connection to the server:
connection.close()
