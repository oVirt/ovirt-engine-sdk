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

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and list the disks attached to
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

# Get the reference to the "vms" service:
vms_service = connection.system_service().vms_service()

# Find the virtual machine:
vm = vms_service.list(search='name=myvm')[0]

# Locate the service that manages the virtual machine:
vm_service = vms_service.vm_service(vm.id)

# Locate the service that manages the disk attachments of the virtual
# machine:
disk_attachments_service = vm_service.disk_attachments_service()

# Retrieve the list of disks attachments, and print the disk details.
# Note that each attachment contains a link to the corresponding disk,
# but not the actual disk data. In order to retrieve the actual disk
# data we use the `follow_link` method.
disk_attachments = disk_attachments_service.list()
for disk_attachment in disk_attachments:
    disk = connection.follow_link(disk_attachment.disk)
    print("name: %s" % disk.name)
    print("id: %s" % disk.id)
    print("status: %s" % disk.status)
    print("provisioned_size: %s" % disk.provisioned_size)

# Close the connection to the server:
connection.close()
