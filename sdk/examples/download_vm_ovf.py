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
import ovirtsdk4 as sdk

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example fetches the specified VM configuration data and
# saves it into an OVF file.

def get_connection():
    # Create the connection to the server:
    return sdk.Connection(
        url='https://engine40.example.com/ovirt-engine/api',
        username='admin@internal',
        password='redhat123',
        ca_file='ca.pem',
        debug=True,
        log=logging.getLogger(),
    )

if __name__ == "__main__":

    # Set VM name
    vm_name = 'myvm'

    # Create a connection to the server:
    connection = get_connection()

    # Get a reference to the root service:
    system_service = connection.system_service()

    # Get the reference to the "vms" service:
    vms_service = system_service.vms_service()

    # Locate VM service
    try:
        vm = vms_service.list(search="name=%s" % vm_name, all_content=True)[0]
        ovf_filename = "%s.ovf" % vm.id
        with open(ovf_filename, "wb") as ovf_file:
            ovf_file.write(vm.initialization.configuration.data.encode("utf-8"))
    finally:
        # Close the connection to the server:
        connection.close()
