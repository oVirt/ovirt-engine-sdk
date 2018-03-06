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

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and assign UserVmManager
# role to myuser1 on virtual machine name myvm1, myvm2 nad myvm3:

# List of virtual machine where user should have assigned permission:
MY_VMS = ['myvm1', 'myvm2', 'myvm3']

# Username of the user, who we want to assign the permissions:
USERNAME = 'user2@internal-authz'

# Role which we want to assign to the user on the virtual machines:
ROLENAME = 'UserVmManager'

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Locate the users service and use it to find the user:
users_service = connection.system_service().users_service()
user = users_service.list(search='usrname=%s' % USERNAME)[0]

# Iterate via the list of virtual machines:
for vm_name in MY_VMS:

    # Locate the virtual machine service and use it to find the specific
    # virtual machines:
    vms_service = connection.system_service().vms_service()
    vm = vms_service.list(search='name=%s' % vm_name)[0]

    # Locate the service that manages the permissions of the virtual machine:
    permissions_service = vms_service.vm_service(vm.id).permissions_service()

    # Use the "add" method to assign UserVmManager role to user on virtual
    # machine:
    permissions_service.add(
        types.Permission(
            user=types.User(
                id=user.id,
            ),
            role=types.Role(
                name=ROLENAME,
            ),
        ),
    )

# Close the connection to the server:
connection.close()
