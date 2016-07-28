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

# This example will connect to the server, retrieve the detail of a
# virtual machine and then it will follow the link to the permissions
# of the virtual machine:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the service that manages virtual machines:
vms_service = connection.system_service().vms_service()

# Find the virtual machine:
vm = vms_service.list(search='name=myvm')[0]

# When the server returns a virtual machine it will return links to
# related objects, like the cluster, the templates and the permissions,
# something like this:
#
# <link href="/api/vms/123/permissions" rel="permissions"/>
# <cluster id="123" href="/api/clusters/123"/>
# <template id="456" href="/api/templates/456"/>
#
# The SDK provides a "follow_link" method that can be used to retrieve
# the complete content of these related objects.
cluster = connection.follow_link(vm.cluster)
template = connection.follow_link(vm.template)
permissions = connection.follow_link(vm.permissions)

# Now we can use the details of the cluster and the template:
print("cluster: %s" % cluster.name)
print("template: %s" % template.name)
for permission in permissions:
    print("role: %s" % permission.role.id)

# Close the connection to the server:
connection.close()
