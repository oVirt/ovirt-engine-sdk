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
import time

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and deactivate a VM's disk attachment
# by updating its 'active' property from True to False

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Locate the virtual machines service and use it to find the virtual
# machine:
vms_service = connection.system_service().vms_service()
vm = vms_service.list(search='name=myvm')[0]

# Locate the service that manages the virtual machine:
vm_service = vms_service.vm_service(vm.id)

# Get disks service and find the disk we want:
disks_service = connection.system_service().disks_service()
disk = disks_service.list(search='name=mydisk')[0]

# Find the disk attachment for the disk we are interested on:
disk_attachments_service = vm_service.disk_attachments_service()
disk_attachments = disk_attachments_service.list()
disk_attachment = next(
    (a for a in disk_attachments if a.disk.id == disk.id), None
)

# Deactivate the disk we found
# or print an error if there is no such disk attached:
if disk_attachment is not None:

    # Locate the service that manages the disk attachment that we found
    # in the previous step:
    disk_attachment_service = disk_attachments_service.attachment_service(disk_attachment.id)

    # Deactivate the disk attachment
    disk_attachment_service.update(types.DiskAttachment(active=False))

    # Wait till the disk attachment not active:
    while True:
        time.sleep(5)
        disk_attachment = disk_attachment_service.get()
        if disk_attachment.active == False:
            break

else:
    print ("There's no disk attachment for %s." % disk.name)

# Close the connection to the server:
connection.close()
