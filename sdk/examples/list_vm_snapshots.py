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

#
# This example will connect to the server and list all the snapshots
# that exist on the system. The output will be simimar to this:
#
# myvm:My first snapshot:mydisk:mydata
# myvm:My second snapshot:mydisk:mydata
# yourvm:Your first snapshot:yourdisk:yourdata
# ...
#
# The first column is the name of the virtual machine. The second is the
# name of the snapshot. The third one is the name of the disk. The
# fourth one is the name of the storage domain where the disk is stored.
#

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the root service:
system_service = connection.system_service()

# Find all the virtual machines and store the id and name in a
# dictioanry, so that looking them up later will be faster:
vms_service = system_service.vms_service()
vms_map = {
    vm.id: vm.name
    for vm in vms_service.list()
}

# Same for storage domains:
sds_service = system_service.storage_domains_service()
sds_map = {
    sd.id: sd.name
    for sd in sds_service.list()
}

# For each virtual machine find its snapshots, then for each snapshot
# find its disks:
for vm_id, vm_name in vms_map.iteritems():
    vm_service = vms_service.vm_service(vm_id)
    snaps_service = vm_service.snapshots_service()
    snaps_map = {
        snap.id: snap.description
        for snap in snaps_service.list()
    }
    for snap_id, snap_description in snaps_map.iteritems():
        snap_service = snaps_service.snapshot_service(snap_id)
        disks_service = snap_service.disks_service()
        for disk in disks_service.list():
            if len(disk.storage_domains) > 0:
                sd_id = disk.storage_domains[0].id
                sd_name = sds_map[sd_id]
                print("{vm}:{snap}:{disk}:{sd}".format(
                    vm=vm_name,
                    snap=snap_description,
                    disk=disk.alias,
                    sd=sd_name,
                ))

# Close the connection to the server:
connection.close()
