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

# This example will connect to the server, search for a tag by name and
# remove it:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Find the service that manages tags:
tags_service = connection.system_service().tags_service()

# Find the tag:
tag = next(tag for tag in tags_service.list() if tag.name == 'mytag')

# Find the service that manages the tag:
tag_service = tags_service.tag_service(tag.id)

# Remove the tag:
tag_service.remove()

# Close the connection to the server:
connection.close()
