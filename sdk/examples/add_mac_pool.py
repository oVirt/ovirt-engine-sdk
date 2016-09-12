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

# This example will connect to the server, create a new MAC address pool
# and assign it to a clusterr:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine41.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the service that manages the MAC address pools:
pools_service = connection.system_service().mac_pools_service()

# Add a new MAC pool:
pool = pools_service.add(
    types.MacPool(
        name='mymacpool',
        ranges=[
            types.Range(
                from_='02:00:00:00:00:00',
                to='02:00:00:01:00:00',
            ),
        ],
    ),
)

# Find the service that manages clusters, as we need it in order to
# find the cluster where we want to set the MAC pool:
clusters_service = connection.system_service().clusters_service()

# Find the cluster:
cluster = clusters_service.list(search='name=mycluster')[0]

# Find the service that manages the cluster, as we need it in order to
# do the update:
cluster_service = clusters_service.cluster_service(cluster.id)

# Update the cluster so that it uses the new MAC pool:
cluster_service.update(
    types.Cluster(
        mac_pool=types.MacPool(
            id=pool.id,
        ),
    ),
)

# Close the connection to the server:
connection.close()
