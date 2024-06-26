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

# This example will connect to the server, add fence agent to a host
# and enable power management and kdump, if it isn't enabled:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine41.example.com/ovirt-engine/api',
    username='admin@internal',
    password='123456',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Find the host:
hosts_service = connection.system_service().hosts_service()
host = hosts_service.list(search='name=myhost')[0]
host_service = hosts_service.host_service(host.id)

# Using fence agent service of the host, add ipmilan fence
# agent:
fence_agents_service = host_service.fence_agents_service()
fence_agents_service.add(
    types.Agent(
        address='1.2.3.4',
        type='ipmilan',
        username='myusername',
        password='mypassword',
        options=[
            types.Option(
                name='myname',
                value='myvalue',
            ),
        ],
        order=0,
    )
)

# Prepare the update host object:
host_update = types.Host()

# If power management isn't enabled, enable it. Note that
# power management can be enabled only if at least one fence
# agent exists for host:
if not host.power_management.enabled:
    host_update.power_management = types.PowerManagement(enabled=True)

# If kdump isn't enabled, enable it. Note that kdump
# can be enabled only if power management on the host
# is enabled:
kdump_enabled = False
if not host.power_management.kdump_detection:
    kdump_enabled = True
    host_update.power_management.kdump_detection = True

# Send the update request:
host_service.update(host_update)

# Note that after kdump integration is enabled the host must be
# reinstalled so the kdump will take effect. First we need to
# switch host to maintenance, because host must be in maintenance
# mode, for reinstall process:
if kdump_enabled:
    host_service.deactivate()
    time.sleep(5)  # Wait a bit so the host status is updated in API
    while host_service.get().status != types.HostStatus.MAINTENANCE:
        time.sleep(2)

    # Then we can execute the reinstall process:
    host_service.install(
        ssh=types.Ssh(
            authentication_method=types.SshAuthenticationMethod.PUBLICKEY,
        ),
    )
    time.sleep(5)  # Wait a bit so the host status is updated in API
    while host_service.get().status != types.HostStatus.MAINTENANCE:
        time.sleep(10)

    # Activate the host after reinstall:
    host_service.activate()
    time.sleep(5)  # Wait a bit so the host status is updated in API
    while host_service.get().status != types.HostStatus.UP:
        time.sleep(2)

# Close the connection to the server:
connection.close()
