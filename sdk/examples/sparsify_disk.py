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

# This example will find the disk in a system and sparsify it.

# Create a connection to the server:
connection = sdk.Connection(
    url='https://engine.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get disks service:
disks_service = connection.system_service().disks_service()

# Find the disk we want to sparsify:
my_disk = disks_service.list(search='name=mydisk')[0]

# Locate the service that manage the disk we want to sparsify:
disk_service = disks_service.disk_service(my_disk.id)

# Sparsify the disk. Note that the virtual machine where the disk is attached
# must not be running so the sparsification is executed. If the virtual
# machine will be running the sparsify operation will fail:
disk_service.sparsify()

# Wait till the disk is OK:
while True:
    time.sleep(5)
    disk = disk_service.get()
    if disk.status == types.DiskStatus.OK:
        break

# Close the connection
connection.close()
