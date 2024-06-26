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

# This example will connect to the server and add LUN disk to virtual machine

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine/ovirt-engine/api',
    username='admin@internal',
    password='123456',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Locate the virtual machines service and use it to find the virtual
# machine:
vms_service = connection.system_service().vms_service()
vm = vms_service.list(search='name=myvm')[0]

# Locate the service that manages the disk attachments of the virtual
# machine:
disk_attachments_service = vms_service.vm_service(vm.id).disk_attachments_service()

# Use the "add" method of the disk attachments service to add the LUN disk.
disk_attachment = disk_attachments_service.add(
    types.DiskAttachment(
        disk=types.Disk(
            name='myiscsidisk',
            lun_storage=types.HostStorage(
                type=types.StorageType.ISCSI,
                logical_units=[
                    types.LogicalUnit(
                        address='192.168.1.1',
                        port=3260,
                        target='iqn.2017-05.org.ovirt:storage',
                        id='36001405d6c6cbba754c4b568d843ff6a',
                        username='username',
                        password='password',
                    )
                ],
            ),
        ),
        interface=types.DiskInterface.VIRTIO,
        bootable=False,
        active=True,
    ),
)

# Close the connection to the server:
connection.close()
