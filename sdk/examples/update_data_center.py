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

# This example will connect to the server and update the description of
# a data center:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the data centers service:
dcs_service = connection.system_service().data_centers_service()

# Retrieve the description of the data center:
dc = dcs_service.list(search='name=mydc')[0]

# In order to update the data center we need a reference to the service
# tht manages it, then we can call the "update" method passing the
# update:
dc_service = dcs_service.data_center_service(dc.id)
dc = dc_service.update(
    types.DataCenter(
        description='Updated description',
    ),
)

# Print the description of the result of the update:
print('%s: %s' % (dc.name, dc.description))

# Note that an alternative way to do this is to update the
# representation of the data center, and then send it:
#
# dc.description = 'Updated description'
# dc_service.update(dc)
#
# But this isn't good practice, because it will send to the server all
# the attributes of the data center, not just those that we want to
# update.

# Close the connection to the server:
connection.close()
