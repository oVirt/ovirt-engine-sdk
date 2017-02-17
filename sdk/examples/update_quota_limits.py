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
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example shows how to update the storage quota limits of a
# specific storage domain.

# Create the connection to the server:
connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Find the reference to the root of services:
system_service = connection.system_service()

# Find the data center and the service that manages it:
dcs_service = system_service.data_centers_service()
dc = dcs_service.list(search='name=mydc')[0]
dc_service = dcs_service.data_center_service(dc.id)

# Find the storage domain and the service that manages it:
sds_service = system_service.storage_domains_service()
sd = sds_service.list(search='name=mydata')[0]
sd_service = sds_service.storage_domain_service(sd.id)

# Find the quota and the service that manages it. Note that the service
# that manages the quota doesn't support search, so we need to retrieve
# all the quotas and filter explicitly. If the quota doesn't exist,
# create it.
quotas_service = dc_service.quotas_service()
quotas = quotas_service.list()
quota = next(
    (q for q in quotas if q.name == 'myquota'),
    None
)
if quota is None:
    quota = quotas_service.add(
        quota=types.Quota(
            name='myquota',
            description='My quota',
            cluster_hard_limit_pct=20,
            cluster_soft_limit_pct=80,
            storage_hard_limit_pct=20,
            storage_soft_limit_pct=80
        )
    )
quota_service = quotas_service.quota_service(quota.id)

# Find the quota limit for the storage domain that we are interested on:
limits_service = quota_service.quota_storage_limits_service()
limits = limits_service.list()
limit = next(
    (l for l in limits if l.id == sd.id),
    None
)

# If that limit exists we will delete it:
if limit is not None:
    limit_service = limits_service.limit_service(limit.id)
    limit_service.remove()

# Create the limit again, with the desired value, in this example it will
# be 100 GiB:
limit = limits_service.add(
    limit=types.QuotaStorageLimit(
        name='mydatalimit',
        description='My storage domain limit',
        limit=100,
        storage_domain=types.StorageDomain(
            id=sd.id
        )
    )
)

# Close the connection to the server:
connection.close()
