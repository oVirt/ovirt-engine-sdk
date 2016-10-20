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

# This example will connect to the server and assign GlusterAdmin
# role to user on network:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Locate the networks service and use it to find the network:
networks_service = connection.system_service().networks_service()
network = networks_service.list(search='name=mynetwork')[0]

# Locate the users service and use it to find the user:
users_service = connection.system_service().users_service()
user = users_service.list(search='usrname=myuser@mydomain-authz')[0]

# Locate the service that manages the permissions of the network:
permissions_service = networks_service.network_service(network.id).permissions_service()

# Use the "add" method to assign GlusterAdmin role to user on network:
permissions_service.add(
    types.Permission(
        user=types.User(
            id=user.id,
        ),
        role=types.Role(
            name='GlusterAdmin'
        ),
    ),
)

# Close the connection to the server:
connection.close()
