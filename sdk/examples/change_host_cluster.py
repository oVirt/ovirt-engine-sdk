#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2018 Red Hat, Inc.
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

# This example will connect to the server and check change the cluster of the
# host

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='123456',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the service that manages the hosts:
hosts_service = connection.system_service().hosts_service()

# Find the host:
host = hosts_service.list(search='name=myhost')[0]

# Get the reference to the service that manages the host
host_service = hosts_service.host_service(host.id)

# Put host into maintenance:
if host.status != types.HostStatus.MAINTENANCE:
    host_service.deactivate()
    # Wait till the host is in maintenance:
    while True:
        time.sleep(5)
        host = host_service.get()
        if host.status == types.HostStatus.MAINTENANCE:
            break

# Change the host cluster:
host_service.update(
    types.Host(
        cluster=types.Cluster(name='mycluster'),
    ),
)

# Activate the host again:   
host_service.activate()
while True:
    time.sleep(5)
    host = host_service.get()
    if host.status == types.HostStatus.UP:
        break

# Close the connection to the server:
connection.close()
