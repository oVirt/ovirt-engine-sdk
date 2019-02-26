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

from six.moves import zip_longest

# This example shows how to use the asynchronous and pipelining capabilities
# of the SDK to download from the server large amounts of data in an efficient
# way. A typical use case for this is the download of the complete inventory
# of hosts and virtual machines.

# This combination of pipeline size and number of connections gives good
# results in large scale environments:
pipeline = 40
connections = 10

# Requests are sent in blocks, and the size of each block should be the number
# of connections multiplied by the size of the pipeline:
block = connections * pipeline

# This method is taken from itertools recipes:
# https://docs.python.org/3/library/itertools.html
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

# This function takes a list of objects and creates a hash where the keys are
# the identifiers and the values are the objects. We will use it to create
# indexes that we can use to speed up things like finding the disks
# corresponding to a virtual machine, given their identifiers.
def index(vals):
    return {item.id: item for item in vals}

# In order to download large collections of objects, it is convenient to use a
# different HTTP connection for each of them, so that they are downloaded in
# parallel. To achieve that we need to configure the connection so that it uses
# multiple HTTP connections, but not pipelining, as otherwise those requests
# will be pipelined and executed serially by the server.
connection = sdk.Connection(
    url='https://engine41.example.com/ovirt-engine/api',
    username='admin@internal',
    password='123456',
    debug=True,
    ca_file='ca.pem',
    log=logging.getLogger(),
    connections=connections,
    pipeline=0,
)

# Get the reference to root of the services tree:
system_service = connection.system_service()

# Send requests for all the collections, but don't wait for the results. This
# way the requests will be sent simultaneously, using the multiple connections
print('Requesting data...')
dcs_future = system_service.data_centers_service().list(wait=False)
clusters_future = system_service.clusters_service().list(wait=False)
sds_future = system_service.storage_domains_service().list(wait=False)
nets_future = system_service.networks_service().list(wait=False)
hosts_future = system_service.hosts_service().list(wait=False)
vms_future = system_service.vms_service().list(wait=False)
disks_future = system_service.disks_service().list(wait=False)

# Wait for the results of the requests that we sent. The calls to the `wait`
# method will perform all the work, for all the pending requests, and will
# eventually return the requested data.
print('Waiting for data centers ...')
dcs = dcs_future.wait()
print("Loaded %s data centers." % len(dcs))

print('Waiting for clusters...')
clusters = clusters_future.wait()
print("Loaded %s clusters." % len(clusters))

print('Waiting for storage domains...')
sds = sds_future.wait()
print("Loaded %s storage domains." % len(sds))

print('Waiting for networks ...')
nets = nets_future.wait()
print("Loaded %s networks." % len(nets))

print('Waiting for hosts ...')
hosts = hosts_future.wait()
print("Loaded %s hosts." % len(hosts))

print('Waiting for VMs ...')
vms = vms_future.wait()
vms_index = index(vms)
print("Loaded %s VMs." % len(vms))

print('Waiting for disks ...')
disks = disks_future.wait()
disks_index = index(disks)
print("Loaded %s disks." % len(disks))

# Close the connection that we used for large collections of objects, as we
# need a new one, configured differently, for the small objects:
connection.close()

# For small objects we are going to send many small requests, and in this case
# we want to use multiple connections *and* pipelining:
connection = sdk.Connection(
    url='https://engine41.example.com/ovirt-engine/api',
    username='admin@internal',
    password='123456',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
    connections=connections,
    pipeline=pipeline,
)

# Note that when the previous connection was closed, all the references to
# services obtained from it were also invalidated, so we need to get them
# again.
system_service = connection.system_service()
vms_service = system_service.vms_service()

# We need now to iterate the collection of VMs that we already have in memory,
# block by block, and for each block send the requests to get the disks
# attachments, without waiting for the responses. This way those requests will
# distributed amongst the multiple connections, and will be added to the
# pipelines. It is necessary to do this block by block because otherwise, if
# we send all the requests at once, the requests that can't be added to the
# pipelines of the connections wold be queued in memory, wasting expensive
# resources of the underlying library. After sending each block of requests,
# we need to wait for the responses.
print('Loading VM disk attachments ...')
for vms_slice in grouper(vms, block):
    atts_futures = {}
    for vm in vms_slice:
        if vm is None:
            break
        vm_service = vms_service.vm_service(vm.id)
        atts_service = vm_service.disk_attachments_service()
        atts_future = atts_service.list(wait=False)
        atts_futures[vm.id] = atts_future

    for vm_id, atts_future in atts_futures.iteritems():
        vm = vms_index[vm_id]
        vm.disk_attachments = atts_future.wait()
        for att in vm.disk_attachments:
            att.disk = disks_index[att.disk.id]
            print("Loaded disk attachments of VM '%s'." % vm.name)
print('Loaded VM disk attachments.')

# Load the VM NICs:
print('Loading VM NICs ...')
for vms_slice in grouper(vms, block):
    nics_futures = {}
    for vm in vms_slice:
        if vm is None:
            break
        vm_service = vms_service.vm_service(vm.id)
        nics_service = vm_service.nics_service()
        nics_future = nics_service.list(wait=False)
        nics_futures[vm.id] = nics_future

    for vm_id, nics_future in nics_futures.iteritems():
        vm = vms_index[vm_id]
        vm.nics = nics_future.wait()
        print("Loaded NICs of VM '%s'." % vm.name)
print('Loaded VM NICs.')

# Load the VM reported devices:
print('Loading VM reported devices ...')
for vms_slice in grouper(vms, block):
    devices_futures = {}
    for vm in vms_slice:
        if vm is None:
            break
        vm_service = vms_service.vm_service(vm.id)
        devices_service = vm_service.reported_devices_service()
        devices_future = devices_service.list(wait=False)
        devices_futures[vm.id] = devices_future

    for vm_id, devices_future in devices_futures.iteritems():
        vm = vms_index[vm_id]
        vm.reported_devices = devices_future.wait()
        print("Loaded reported devices of VM '%s'." % vm.name)
print('Loaded VM reported devices.')

# Close the connection:
connection.close()
