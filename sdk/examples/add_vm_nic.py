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

# This example will connect to the server and add a network interface
# card to an existing virtual machine.

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
system_service = connection.system_service()
vms_service = system_service.vms_service()
vm = vms_service.list(search='name=myvm')[0]

# In order to specify the network that the new interface will be
# connected to we need to specify the identifier of the virtual network
# interface profile, so we need to find it. We can have duplicate names
# for vnic profiles in different clusters, so we must also find first the
# network by datacenter and cluster:
cluster = system_service.clusters_service().cluster_service(vm.cluster.id).get()
dcs_service = connection.system_service().data_centers_service()
dc = dcs_service.list(search='Clusters.name=%s' % cluster.name)[0]
networks_service = dcs_service.service(dc.id).networks_service()
network = next(
    (n for n in networks_service.list()
     if n.name == 'mynetwork'),
    None
)
profiles_service = connection.system_service().vnic_profiles_service()
profile_id = None
for profile in profiles_service.list():
    if profile.name == 'mynetwork':
        profile_id = profile.id
        break

# Locate the service that manages the network interface cards of the
# virtual machine:
nics_service = vms_service.vm_service(vm.id).nics_service()

# Use the "add" method of the network interface cards service to add the
# new network interface card:
nics_service.add(
    types.Nic(
        name='mynic',
        description='My network interface card',
        vnic_profile=types.VnicProfile(
            id=profile_id,
        ),
    ),
)

# Close the connection to the server:
connection.close()
