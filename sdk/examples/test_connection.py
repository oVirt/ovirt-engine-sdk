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

# This example will create a connection and call the "test" method:

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Call the test method to check the connectivity with the server. If
# connectivity works this method will return "True". If there is any
# connectivy problem it will either return "False" or raise an exception
# if the "raise_exception" parameter is "True".
if connection.test(raise_exception=False):
    print("Connection works.")
else:
    print("Connection doesn't work.")

# Close the connection to the server:
connection.close()
