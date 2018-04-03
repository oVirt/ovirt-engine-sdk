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

# This example shows how to export a virtual machine template as
# a Virtual Appliance (OVA) file to a specified path on a host.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='/etc/pki/ovirt-engine/ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Find the virtual machine template:
templates_service = connection.system_service().templates_service()
template = templates_service.list(search='name=mytemplate')[0]
template_service = templates_service.template_service(template.id)

# Find the host where the OVA will be exported:
hosts_service = connection.system_service().hosts_service()
host = hosts_service.list(search='name=myhost')[0]

# Export the virtual machine template. Note that the 'filename'
# parameter is optional, and only required if you want to specify
# a name for the  generated OVA file that is different from
# <template_name>.ova.
# Note that this operation is only available since version 4.2.3
# of the engine and since version 4.2.5 of the SDK.
template_service.export_to_path_on_host(
    host=types.Host(id=host.id),
    directory='/tmp',
    filename='mytemplate2.ova'
)

# Close the connection to the server:
connection.close()
