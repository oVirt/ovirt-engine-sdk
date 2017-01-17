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

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will import a VM from an export domain using a
# target domain, the example assumes there is an exported vm in
# the export storage domain

# Create a connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get storage domains service
sds_service = connection.system_service().storage_domains_service()

# Grab the first export domain
export_sd = sds_service.list(search='name=myexport')[0]

# Get the target storage domain, where the VM will be imported to
target_sd = sds_service.list(search='name=mydata')[0]

# Get the cluster service
clusters_service = connection.system_service().clusters_service()

# Find the cluster to be used for the import
cluster = clusters_service.list(search='mycluster')[0]

# Get the storage domain VM service
vms_service = sds_service \
    .storage_domain_service(export_sd.id) \
    .vms_service()

# Get an exported VM, assuming we have one
exported_vm = vms_service.list()[0]

# Import the VM that was exported to the export storage domain and import it to
# the target storage domain which in our case is 'mydata' on the cluster
# 'mycluster'
vms_service.vm_service(exported_vm.id).import_(
    storage_domain=types.StorageDomain(
        id=target_sd.id
    ),
    cluster=types.Cluster(
        id=cluster.id
    ),
    vm=types.Vm(
        id=exported_vm.id
    )
)

# Close the connection
connection.close()
