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

# This example will connect to the server and change the value of the
# 'lanplus' option of the 'ipmilan' fencing agent of a host.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# The name and value of the option that we want to add or update:
name = 'lanplus'
value = '1'

# Get the reference to the service that manages the hosts:
hosts_service = connection.system_service().hosts_service()

# Find the host:
host = hosts_service.list(search='name=myhost')[0]

# Get the reference to the service that manages the fencing agents used
# by the host that we found in the previous step:
host_service = hosts_service.host_service(host.id)
agents_service = host_service.fence_agents_service()

# The host may have multiple fencing agents, so we need to locate the
# first of type 'ipmilan':
agents = agents_service.list()
agent = next(x for x in agents if x.type == 'ipmilan')

# Get the options of the fencing agent. There may be no options, in that
# case we need to use an empty list:
original = agent.options
if original is None:
    original = []

# Create a list of modified options, containing all the original options
# except the one with the name that we want to modify, as we will add that
# with the right value later:
modified = [x for x in original if x.name != name]

# Add the modified option to the list of modified options:
option = types.Option(
    name=name,
    value=value
)
modified.append(option)

# Find the service that manages the fence agent:
agent_service = agents_service.agent_service(agent.id)

# Send the update request containg the original list of options plus the
# modifications that we did:
agent_service.update(
    agent=types.Agent(
        options=modified
    )
)

# Close the connection to the server:
connection.close()
