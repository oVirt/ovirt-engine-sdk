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
import lxml.etree
import re
import ssl
import sys
import tarfile
import time

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

from six.moves.http_client import HTTPSConnection
from six.moves.urllib.parse import urlparse

# This seems to give the best throughput when uploading from my laptop
# SSD to a server that drop the data. You may need to tune this on your
# setup.
BUF_SIZE = 128 * 1024

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example shows how to upload a virtual appliance (OVA) file
# as a virtual machine.

if len(sys.argv) < 2:
    print("Usage: upload_ova_as_vm ova_path [cluster] [storage_domain]")
    sys.exit(1)
else:
    # Path to the OVA file.
    ova_path = sys.argv[1]
    # The name of the cluster where the virtual machine will be created.
    target_cluster_name = "Default"
    if len(sys.argv) > 2:
        target_cluster_name = sys.argv[2]
    # The name of the storage domain where the disks will be uploaded to.
    target_storage_domain_name = "mydata"
    if len(sys.argv) > 3:
        target_storage_domain_name = sys.argv[3]


# Create the connection to the server:
print("Connecting...")

connection = sdk.Connection(
    url='https://engine40.example.com/ovirt-engine/api',
    username='admin@internal',
    password='redhat123',
    ca_file='ca.pem',
    debug=True,
    log=logging.getLogger(),
)

# Get the reference to the root service:
system_service = connection.system_service()

# Open the OVA file:
ova_file = tarfile.open(ova_path)
# Read the entries within the OVA file
ova_entries = ova_file.getmembers()

# Read the OVF configuration from the OVA file (must be the first entry
# inside the tar file):
ovf_str = ova_file.extractfile(ova_entries[0]).read()
# Parse the OVF as XML document:
ovf = lxml.etree.fromstring(ovf_str)

# Get a reference to the service that manages the image
# transfer that was added in the previous step:
transfers_service = system_service.image_transfers_service()

# Create the disks:
disks_service = system_service.disks_service()

# Find the disks section:
namespaces = {
    'ovf': 'http://schemas.dmtf.org/ovf/envelope/1'
}
disk_elements = ovf.xpath(
    '/ovf:Envelope/ovf:DiskSection/ovf:Disk',
    namespaces=namespaces
)

for disk_element in disk_elements:
    # Get disk properties:
    props = {}
    for key, value in disk_element.items():
        key = key.replace('{%s}' % namespaces['ovf'], '')
        props[key] = value

    print("Creating disk...")
    print (props)

    # Determine the volume format
    if props['volume-format'] == 'COW':
        disk_format = types.DiskFormat.COW
    else:
        disk_format = types.DiskFormat.RAW

    # Add the disk:
    disk = disks_service.add(
        disk=types.Disk(
            id=props['diskId'],
            name=props['disk-alias'],
            description=props['description'],
            format=disk_format,
            provisioned_size=int(props['capacity']) * 2**30,
            initial_size=int(props['populatedSize']),
            storage_domains=[
                types.StorageDomain(
                    name=target_storage_domain_name
                )
            ]
        )
    )

    # Wait till the disk is up, as the transfer can't start if the
    # disk is locked:
    disk_service = disks_service.disk_service(disk.id)
    while disk_service.get().status != types.DiskStatus.OK:
        time.sleep(5)

    print("Creating transfer session...")
    # Add a new image transfer:
    transfer = transfers_service.add(
        types.ImageTransfer(
            image=types.Image(
                id=disk.id
            )
        )
    )

    # Get reference to the created transfer service:
    transfer_service = transfers_service.image_transfer_service(transfer.id)

    # After adding a new transfer for the disk, the transfer's status will be
    # INITIALIZING. Wait until the init phase is over. The actual transfer can
    # start when its status is "Transferring".
    while transfer_service.get().phase == types.ImageTransferPhase.INITIALIZING:
        time.sleep(1)

    # At this stage, the SDK granted the permission to start transferring the
    # disk, and the user should choose its preferred tool for doing it -
    # regardless of the SDK. In this example, we will use Python's
    # httplib.HTTPSConnection for transferring the data.
    proxy_url = urlparse(transfer.proxy_url)
    context = ssl.create_default_context()

    # Note that ovirt-imageio-proxy by default checks the certificates,
    # so if you don't have your CA certificate of the engine in the system,
    # you need to pass it to HTTPSConnection.
    context.load_verify_locations(cafile='ca.pem')

    proxy_connection = HTTPSConnection(
        proxy_url.hostname,
        proxy_url.port,
        context=context,
    )

    # Find the disk entry among the OVA entries
    for ova_entry in ova_entries[1:]:
        if ova_entry.name == props['fileRef']:
            disk_entry = ova_entry
            break

    print ("Uploading disk %s..." % disk_entry.name)
    disk_file = ova_file.extractfile(disk_entry)
    image_size = disk_entry.size

    # Send the request head. Note the following:
    #
    # - We must send the Authorzation header with the signed ticket received
    #   from the transfer service.
    #
    # - the server requires Content-Range header even when sending the
    #   entire file.
    #
    # - the server requires also Content-Length.
    #

    proxy_connection.putrequest("PUT", proxy_url.path)
    proxy_connection.putheader('Authorization', transfer.signed_ticket)
    content_range = "bytes %d-%d/%d" % (0, image_size - 1, image_size)
    proxy_connection.putheader('Content-Range', content_range)
    proxy_connection.putheader('Content-Length', "%d" % (image_size,))
    proxy_connection.endheaders()

    # Send the request body. Note the following:
    #
    # - we must send the number of bytes we promised in the Content-Range
    #   header.
    #
    # - we must extend the session, otherwise it will expire and the upload
    #   will fail.

    start = last_progress = time.time()

    pos = 0
    while pos < image_size:
        to_read = min(image_size - pos, BUF_SIZE)
        chunk = disk_file.read(to_read)
        if not chunk:
            transfer_service.pause()
            raise RuntimeError("Unexpected end of file at pos=%d" % pos)
        proxy_connection.send(chunk)
        pos += len(chunk)

        # Extend the transfer session once per minute.
        now = time.time()
        if now - last_progress > 10:
            print("Uploaded %.2f%%" % (float(pos) / image_size * 100))
            last_progress = now

    # Get the response
    response = proxy_connection.getresponse()
    if response.status != 200:
        transfer_service.pause()
        print("Upload failed: %s %s" % (response.status, response.reason))
        sys.exit(1)

    elapsed = time.time() - start
    print("Uploaded %.2fg in %.2f seconds (%.2fm/s)" % (
          image_size / float(1024**3), elapsed, image_size / 1024**2 / elapsed))

    print("Finalizing transfer session...")
    # Successful cleanup
    transfer_service.finalize()

    # Wait until the transfer disk job is completed since
    # only then we can be sure the disk is unlocked:
    try:
        while transfer_service.get():
            time.sleep(1)
    except sdk.NotFoundError:
        pass

    print("Upload disk completed successfully")

# Find the name of the virtual machine within the OVF:
vm_name = ovf.xpath(
    '/ovf:Envelope/ovf:VirtualSystem/ovf:Name',
    namespaces=namespaces
)[0].text

# Add the virtual machine, the transfered disks will be
# attached to this virtual machine:
print ("Adding virtual machine %s" % vm_name)
vms_service = connection.system_service().vms_service()
vm = vms_service.add(
    types.Vm(
        cluster=types.Cluster(
            name=target_cluster_name,
        ),
        initialization=types.Initialization(
            configuration=types.Configuration(
                type=types.ConfigurationType.OVA,
                data=ovf_str
            )
        ),
    ),
)

# Close the OVA file
ova_file.close()

# Close the connection:
connection.close()
