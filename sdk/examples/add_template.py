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

# This example shows how to add a new template, customizing some of its
# characteristics, like the format of the disks.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger()
)

# Get the reference to the root of the services tree:
system_service = connection.system_service()

# Find the original virtual machine:
vms_service = system_service.vms_service()
vm = vms_service.list(search='name=myvm')[0]

# Get the identifiers of the disks attached to the virtual machine. We
# need this because we want to tell the server to create the disks of
# the template using a format different to the format used by the
# original disks.
attachments = connection.follow_link(vm.disk_attachments)
disk_ids = [
    attachment.disk.id
    for attachment in attachments
]

# Send the request to create the template. Note that the way to specify
# the original virtual machine, and the customizations, is to use the
# 'vm' attribute of the 'Template' type. In the customization we
# explicitly indicate that we want COW disks, regardless of what format
# the original disks had.
templates_service = system_service.templates_service()
template = templates_service.add(
    template=types.Template(
        name='mytemplate',
        vm=types.Vm(
            id=vm.id,
            disk_attachments=[
                types.DiskAttachment(
                    disk=types.Disk(
                        id=disk_id,
                        sparse=True,
                        format=types.DiskFormat.COW
                    )
                )
                for disk_id in disk_ids
            ]
        )
    )
)

# Wait till the status of the template is OK, as that means that it is
# completely created and ready to use:
template_service = templates_service.template_service(template.id)
while True:
    time.sleep(5)
    template = template_service.get()
    if template.status == types.TemplateStatus.OK:
        break

# Close the connection to the server:
connection.close()
