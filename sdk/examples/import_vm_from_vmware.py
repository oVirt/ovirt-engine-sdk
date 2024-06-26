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

# This example shows how to import an external virtual machine from an
# VMware:

# Create a connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the service that manages import of external
# virtual machines:
system_service = connection.system_service()
imports_service = system_service.external_vm_imports_service()

# Initiate the import of VM 'myvm' from VMware:
imports_service.add(
    types.ExternalVmImport(
        name='myvm',
        provider=types.ExternalVmProviderType.VMWARE,
        username='wmware_user',
        password='wmware123',
        url='vpx://wmware_user@vcenter-host/DataCenter/Cluster/esxi-host?no_verify=1',
        cluster=types.Cluster(
            name='mycluster'
        ),
        storage_domain=types.StorageDomain(
            name='mydata'
        ),
        sparse=True
    )
)

# Close the connection:
connection.close()
