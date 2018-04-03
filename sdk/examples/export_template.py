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
import time

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example shows how to export a virtual machine template to
# an export storage domain.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='/etc/pki/ovirt-engine/ca.pem',
    debug=True,
    log=logging.getLogger()
)

# Get the reference to the root of the services tree:
system_service = connection.system_service()

# Find the virtual machine template:
templates_service = system_service.templates_service()
template = templates_service.list(search='name=mytemplate')[0]

# Export the virtual machine template. Note that the 'exclusive'
# parameter is optional, and only required if you want to overwrite
# a virtual machine template that has already been exported before.
template_service = templates_service.template_service(template.id)
template_service.export(
    exclusive=True,
    storage_domain=types.StorageDomain(
        name='myexport'
    )
)

# Close the connection to the server:
connection.close()
