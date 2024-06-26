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

# This example demonstrates how to use multiple connections, using the
# connection builder class and the Python "with" mechanism.

# Multiple connections can be created just calling the constructor
# multiple times, but then it is necessary to store the connection
# parameters somewhere. The "ConnectionBuilder" class simplifies it a
# bit, as it servers at the place to store these parameters:
builder = sdk.ConnectionBuilder(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Creating the connection builder doesn't do anything, it just stores
# the parameter. To actually create the connection it is necessary to
# call the "build" method, and it is very convenient to combine this
# with the "with" mechanism of Python:
with builder.build() as connection:
   for vm in connection.system_service().vms_service().list():
       print(vm.name)

# The connection has been closed automatically. If there is the need to
# create another connection, the builder object can be reused:
with builder.build() as connection:
   for host in connection.system_service().hosts_service().list():
       print(host.name)
