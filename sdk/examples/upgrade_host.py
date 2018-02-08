#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2018 Red Hat, Inc.
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

# This example will connect to the server and check if there are any available
# updates on the host and if so it will upgrade the host

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the service that manages the hosts:
hosts_service = connection.system_service().hosts_service()

# Get the reference to the service that manages the events:
events_service = connection.system_service().events_service()

# Find the host:
host = hosts_service.list(search='name=myhost')[0]

# Get the reference to the service that manages the host
host_service = hosts_service.host_service(host.id)

# Check if the host has available update, if not run check for
# upgrade action:
if not host.update_available:
    # Run the check for upgrade action:
    host_service.upgrade_check()

    # Wait until event with id 839 or 887 occur, which means
    # that check for upgrade action failed.
    # Or wait until event with id 885 occured, which means
    # that check for upgrade action succeed.
    last_event = events_service.list(max=1)[0]
    timeout = 180
    while timeout > 0:
        events = [
            event.code for event in events_service.list(
                from_=int(last_event.id),
                search='host.name=%s' % host.name,
            )
        ]
        if 839 in events or 887 in events:
            print("Check for upgrade failed.")
            break
        if 885 in events:
            print("Check for upgrade done.")
            break
        time.sleep(2)
        timeout = timeout - 2

# Refresh the host object and run the upgrade action
# if host has available updates:
host = host_service.get()
if host.update_available:
    host_service.upgrade()

# Close the connection to the server:
connection.close()
