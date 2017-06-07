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
import os
import time

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This shows how to poll the collection of events.

# In order to make sure that no events are lost it is good idea to write
# in persistent storage the index of the last event that we processed.
# In this example we will store it in a 'index.txt' file. In a real
# world application this should proably be saved in a database.
def write_index(index):
    with open('index.txt', 'w') as fd:
        fd.write(str(index))

def read_index():
    if os.path.exists('index.txt'):
        with open('index.txt', 'r') as fd:
            return int(fd.read())
    else:
        return None

# This is the function that will be called to process the events, it
# will just print the identifier and the description of the event.
def process_event(event):
    print("%s - %s" % (event.id, event.description))

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Find the service that manages the collection of events:
events_service = connection.system_service().events_service()

# If there is no index stored yet, then retrieve the last event and
# start with it. Events are ordered by index, ascending, and 'max=1'
# requests just one event, so we will get the last event.
if read_index() is None:
    events = events_service.list(max=1)
    if len(events) > 0:
        event = events[0]
        process_event(event)
        write_index(int(event.id))

# Do a loop to retrieve events, starting always with the last index, and
# waiting a bit before repeating. Note the use of the 'from' parameter
# to specify that we want to get events newer than the last index that
# we already processed. Note also that we don't use the 'max' parameter
# here because we want to get all the pending events.
while True:
    time.sleep(5)
    events = events_service.list(from_=read_index())
    for event in events:
        process_event(event)
        write_index(int(event.id))

# Close the connection to the server:
connection.close()
