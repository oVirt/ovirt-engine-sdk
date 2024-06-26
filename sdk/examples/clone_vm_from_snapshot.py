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

# This example shows how to clone a virtual machine from an snapshot.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the root of the tree of services:
system_service = connection.system_service()

# Find the virtual machine:
vms_service = system_service.vms_service()
vm = vms_service.list(search='name=myvm')[0]

# Find the service that manages the virtual machine:
vm_service = vms_service.vm_service(vm.id)

# Find the snapshot. Note that the snapshots collection doesn't support
# search, so we need to retrieve the complete list and the look for the
# snapshot that has the description that we are looking for.
snaps_service = vm_service.snapshots_service()
snaps = snaps_service.list()
snap = next(
  (s for s in snaps if s.description == 'mysnap'),
  None
)

# Create a new virtual machine, cloning it from the snapshot:
cloned_vm = vms_service.add(
    vm=types.Vm(
        name='myclonedvm',
        snapshots=[
            types.Snapshot(
                id=snap.id
            )
        ],
        cluster=types.Cluster(
            name='mycluster'
        )
    )
)

# Find the service that manages the cloned virtual machine:
cloned_vm_service = vms_service.vm_service(cloned_vm.id)

# Wait till the virtual machine is down, as that means that the creation
# of the disks of the virtual machine has been completed:
while True:
    time.sleep(5)
    cloned_vm = cloned_vm_service.get()
    if cloned_vm.status == types.VmStatus.DOWN:
        break

# Close the connection to the server:
connection.close()
