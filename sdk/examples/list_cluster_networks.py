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

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and list the networks attached to
# a cluster:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the "clusters" service:
clusters_service = connection.system_service().clusters_service()

# Find the cluster:
cluster = clusters_service.list(search='name=mycluster')[0]

# Locate the service that manages the cluster:
cluster_service = clusters_service.cluster_service(cluster.id)

# Locate the service that manages the networks of the cluster:
networks_service = cluster_service.networks_service()

# Retrieve the list of networks, and print the network details:
networks = networks_service.list()
for network in networks:
    print("name: %s" % network.name)
    print("id: %s" % network.id)
    print("required: %s" % network.required)
    print("mtu: %s" % network.mtu)
    print("usages: %s" % ', '.join([str(usage) for usage in network.usages]))

# Close the connection to the server:
connection.close()
