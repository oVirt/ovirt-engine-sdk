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

# This example will connect to the server list the images available in
# the 'ovirt-image-repository' Glance storge domain that is available by
# default in every oVirt installation.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the root of the services tree:
system_service = connection.system_service()

# Find the Glance storage domain that is available for default in any
# oVirt installation:
sds_service = system_service.storage_domains_service()
sd = sds_service.list(search='name=ovirt-image-repository')[0]

# Find the service that manages the Glance storage domain:
sd_service = sds_service.storage_domain_service(sd.id)

# Find the service that manages the images available in that storage
# domain:
images_service = sd_service.images_service()

# List the images available in the storage domain:
images = images_service.list()
for image in images:
    print(image.name)

# Close the connection to the server:
connection.close()
