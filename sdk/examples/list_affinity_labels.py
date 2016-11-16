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

# This example will connect to the server and print the names
# and virtual machines of all affinity labels in system:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the affinity labels service:
affinity_labels_service = connection.system_service().affinity_labels_service()

# Use the "list" method of the affinity labels service
# to list all the affinity labels of the system:
affinity_labels = affinity_labels_service.list()

# Print all affinity labels names and virtual machines
# which has assigned that affinity label:
for affinity_label in affinity_labels:
    print("%s:" % affinity_label.name)
    for vm_link in connection.follow_link(affinity_label.vms):
        vm = connection.follow_link(vm_link)
        print(" - %s" % vm.name)

# Close the connection to the server:
connection.close()
