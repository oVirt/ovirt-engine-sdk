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

# This example configures the networking of a host, adding a bonded
# interface and attaching it to a network with an static IP address.

# Connect to the host:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='/etc/pki/ovirt-engine/ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Find the service that manages the collection of hosts:
hosts_service = connection.system_service().hosts_service()

# Find the host:
host = hosts_service.list(search='name=myhost')[0]

# Find the service that manages the host:
host_service = hosts_service.host_service(host.id)

# Configure the network adding a bond with two slaves and attaching it to a
# network with an static IP address:
host_service.setup_networks(
    modified_bonds=[
        types.HostNic(
            name='bond0',
            bonding=types.Bonding(
                options=[
                    types.Option(
                        name='mode',
                        value='1',
                    ),
                    types.Option(
                        name='miimon',
                        value='100',
                    ),
                ],
                slaves=[
                    types.HostNic(
                        name='eth1',
                    ),
                    types.HostNic(
                        name='eth2',
                    ),
                ],
            ),
        ),
    ],
    modified_network_attachments=[
        types.NetworkAttachment(
            network=types.Network(
                name='mynetwork',
            ),
            host_nic=types.HostNic(
                name='bond0',
            ),
            ip_address_assignments=[
                types.IpAddressAssignment(
                    assignment_method=types.BootProtocol.STATIC,
                    ip=types.Ip(
                        address='192.168.122.100',
                        netmask='255.255.255.0',
                    ),
                ),
            ],
        ),
    ],
)

# After modifying the network configuration it is very important to make it
# persistent:
host_service.commit_net_config()

# Close the connection to the server:
connection.close()
