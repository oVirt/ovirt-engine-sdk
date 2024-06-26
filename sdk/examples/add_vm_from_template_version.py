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

# This example will connect to the server, and create a virtual machine
# from a specific version of a template and specify storage domain where
# virtual machine disk should be created.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine41.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger()
)

# Get the reference to the root of the tree of services:
system_service = connection.system_service()

# Get the reference to the service that manages the storage domains:
storage_domains_service = system_service.storage_domains_service()

# Find the storage domain we want to be used for virtual machine disks:
storage_domain = storage_domains_service.list(search='name=mydata')[0]

# Get the reference to the service that manages the templates:
templates_service = system_service.templates_service()

# When a template has multiple versions they all have the same name, so
# we need to explicitly find the one that has the version name or
# version number that we want to use. In this case we want to use
# version 3 of the template.
templates = templates_service.list(search='name=mytemplate')
template_id = None
for template in templates:
    if template.version.version_number == 3:
        template_id = template.id
        break

# Find the template disk we want be created on specific storage domain
# for our virtual machine:
template_service = templates_service.template_service(template_id)
disk_attachments = connection.follow_link(template_service.get().disk_attachments)
disk = disk_attachments[0].disk

# Get the reference to the service that manages the virtual machines:
vms_service = system_service.vms_service()

# Add a new virtual machine explicitly indicating the identifier of the
# template version that we want to use and indicating that template disk
# should be created on specific storage domain for the virtual machine:
vm = vms_service.add(
    types.Vm(
        name='myvm',
        cluster=types.Cluster(
            name='mycluster'
        ),
        template=types.Template(
            id=template_id
        ),
        disk_attachments=[
            types.DiskAttachment(
                disk=types.Disk(
                    id=disk.id,
                    format=types.DiskFormat.COW,
                    storage_domains=[
                        types.StorageDomain(
                            id=storage_domain.id,
                        ),
                    ],
                ),
            ),
        ],
    )
)

# Get a reference to the service that manages the virtual machine that
# was created in the previous step:
vm_service = vms_service.vm_service(vm.id)

# Wait till the virtual machine is down, which indicats that all the
# disks have been created:
while True:
    time.sleep(5)
    vm = vm_service.get()
    if vm.status == types.VmStatus.DOWN:
        break

# Close the connection to the server:
connection.close()
