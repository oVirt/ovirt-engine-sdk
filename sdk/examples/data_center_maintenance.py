#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2019 Red Hat, Inc.
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

# This example does the following:
# 1. Shutdown all VMs of the Data-Center
# 2. Maintenance mode all SDs
# 3. Maintenance mode all Hosts

connection = sdk.Connection(
    url='https://engine.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat',
    ca_file='/etc/pki/ovirt-engine/ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the data centers service:
dcs_service = connection.system_service().data_centers_service()

# Retrieve the data center service:
dc = dcs_service.list(search='name=Default')[0]
dc_service = dcs_service.data_center_service(dc.id)

# Find all clusters of the data center:
shutdown_clusters = [c.id for c in dc_service.clusters_service().list()]

# 1. Shutdown all VMs of these clusters
print("Shutting down all Virtual Machines")
is_hosted_engine = False
vms_service = connection.system_service().vms_service()
for vm in vms_service.list():
    if vm.cluster.id not in shutdown_clusters:
        continue
    if vm.status == types.VmStatus.DOWN:
        continue
    vm_service = vms_service.vm_service(vm.id)
    # Detect HostedEngine environments and switch it to HA Maintenance
    if vm.name == "HostedEngine":
        is_hosted_engine = True
        vm_service.maintenance(maintenance_enabled=True)
        continue
    vm_service.shutdown()

# Wait for all VMs to reach down state
while True:
    vms = [vm.id for vm in vms_service.list()
           if vm.status != types.VmStatus.DOWN]
    if (len(vms) == 1 and is_hosted_engine) or not vms:
        break
    print("waiting for %d VMs to reach DOWN state..." % len(vms))
    time.sleep(10)

# 2. Switch all storage to maintenance
sds_service = dc_service.storage_domains_service()
for sd in sds_service.list():
    if sd.name == "hosted_storage":
        continue
    if sd.status not in (types.StorageDomainStatus.ACTIVE,
                         types.StorageDomainStatus.MIXED):
        continue
    sd_service = sds_service.storage_domain_service(sd.id)
    sd_service.deactivate()

# Wait for all SDs to reach maintenance state
print("Setting maintenance mode on Storage Domains")
while True:
    sds = [sd.id for sd in sds_service.list()
           if sd.status != types.StorageDomainStatus.MAINTENANCE]
    if (len(sds) == 1 and is_hosted_engine) or not sds:
        break
    print("waiting for %d SDs to reach Maintenance state..." % len(sds))
    time.sleep(10)

# 3. Switch all hosts to maintenance state
print("Setting maintenance mode on Hosts")
hosts_service = connection.system_service().hosts_service()
for host in hosts_service.list():
    if host.cluster.id not in shutdown_clusters:
        continue
    if host.status != types.HostStatus.UP:
        continue
    # Is running HE, SPM role may switch to this host
    if is_hosted_engine and host.summary.total:
        continue
    host_service = hosts_service.host_service(host.id)
    host_service.deactivate()

connection.close()
