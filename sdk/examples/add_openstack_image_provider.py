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

# This example will connect to the server and add a Glance storage
# domain:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# The name of the storage domain:
name = 'myglance'

# Get the root of the services tree:
system_service = connection.system_service()

# Get the list of OpenStack image providers (a.k.a. Glance providers)
# that match the name that we want to use:
providers_service = system_service.openstack_image_providers_service()
providers = [
    provider for provider in providers_service.list()
    if provider.name == name
]

# If there is no such provider, then add it:
if len(providers) == 0:
    providers_service.add(
        provider=types.OpenStackImageProvider(
            name=name,
            description='My Glance',
            url='http://glance.ovirt.org:9292',
            requires_authentication=False
        )
    )

# Note that the provider that we are using in this example is public
# and doesn't require any authentication. If your provider requires
# authentication then you will need to specify additional security
# related attributes:
#
#  types.OpenStackImageProvider(
#    name=name,
#    description='My private Glance',
#    url='http://myglance',
#    requires_authentication=True,
#    authentication_url='http://mykeystone',
#    username='myuser',
#    password='mypassword',
#    tenant_name='mytenant'
#  )

# Close the connection to the server:
connection.close()
