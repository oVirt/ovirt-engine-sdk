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
import time

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and create a new iSCSI data
# storage domain with 'Discard After Delete' parameter,
# and will attach it to a data center.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the storage domains service:
sds_service = connection.system_service().storage_domains_service()

# Note that 'myhost' should be in a dc with version >= 4.1 for enabling
# the 'Discard After Delete' (DAD) parameter, since only from that
# version, the host returns the luns' discard related information.
sd = sds_service.add(
    types.StorageDomain(
        name='mydata',
        description='My iSCSI With Discard After Delete',
        type=types.StorageDomainType.DATA,
        discard_after_delete=True,
        data_center=sdk.types.DataCenter(
            name='mydc',
        ),
        host=types.Host(
            name='myhost',
        ),
        storage_format=types.StorageFormat.V4,
        storage=types.HostStorage(
            type=types.StorageType.ISCSI,
            override_luns=True,
            volume_group=sdk.types.VolumeGroup(
                logical_units=[
                    sdk.types.LogicalUnit(
                        id='36001405e396b3d9c9a54284a51685f9a',
                        address='192.168.201.3',
                        port=3260,
                        target='iqn.2014-07.org.ovirt:storage',
                        username='username',
                        password='password',
                    )
                ]
            ),
        ),
    ),
)

# Locate the service that manages the data centers and use it to
# search for the data center:
dcs_service = connection.system_service().data_centers_service()
dc = dcs_service.list(search='name=mydc')[0]

# Locate the service that manages the data center where we want to
# attach the storage domain:
dc_service = dcs_service.data_center_service(dc.id)

# Locate the service that manages the storage domains that are attached
# to the data centers:
attached_sds_service = dc_service.storage_domains_service()

# Use the "add" method of service that manages the attached storage
# domains to attach it.
# Note that attaching this SD to the dc will succeed only if the
# dc version is >= 4.1.
attached_sds_service.add(
    types.StorageDomain(
        id=sd.id,
    ),
)

# Wait till the storage domain is active:
attached_sd_service = attached_sds_service.storage_domain_service(sd.id)
while True:
    time.sleep(5)
    sd = attached_sd_service.get()
    if sd.status == types.StorageDomainStatus.ACTIVE:
        break

# Close the connection to the server:
connection.close()
