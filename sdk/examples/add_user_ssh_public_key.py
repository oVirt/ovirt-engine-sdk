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

# This example will connect to the server, find a user by name and add a
# public SSH key.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine41.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger()
)

# Get the reference to the root of the tree of services:
system_service = connection.system_service()

# Get the reference to the service that manages the users:
users_service = system_service.users_service()

# Find the user:
user = users_service.list(search='name=myuser')[0]

# Get the reference to the service that manages the user that we
# found in the previous step:
user_service = users_service.user_service(user.id)

# Get a reference to the service that manages the public SSH keys
# of the user:
keys_service = user_service.ssh_public_keys_service()

# Add a new SSH public key:
keys_service.add(
    key=types.SshPublicKey(
        content='ssh-rsa AAA...mu9 myuser@example.com'
    )
)

# Note that the above operation will fail because the example SSH public
# key is not valid, make sure to use a valid key.

# Close the connection to the server:
connection.close()
