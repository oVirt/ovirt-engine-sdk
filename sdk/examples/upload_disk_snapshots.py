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

from __future__ import print_function

import json
import logging
import os
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import subprocess
import ssl
import sys
import time

from six.moves.http_client import HTTPSConnection
from six.moves.urllib.parse import urlparse


logging.basicConfig(level=logging.DEBUG, filename='example.log')


# This example will connect to the server, loop over the disk snapshots
# of a specified disk and upload their data into files.
# Note: in order to get the disk's snapshots, we are retrieving *all*
# the snapshots of the storage domain, and filter accordingly.
# Should find a more efficient means in the future.

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

def get_transfer_service(disk_snapshot_id):
    """
    Creates a new ImageTansfer for the specified disk snapshot
    """
    # Get a reference to the service that manages the image transfer:
    transfers_service = system_service.image_transfers_service()

    # Add a new image transfer:
    transfer = transfers_service.add(
        types.ImageTransfer(
            snapshot=types.DiskSnapshot(id=disk_snapshot_id),
            direction=types.ImageTransferDirection.UPLOAD,
        )
    )

    # Get reference to the created transfer service:
    transfer_service = transfers_service.image_transfer_service(transfer.id)

    while transfer.phase == types.ImageTransferPhase.INITIALIZING:
        time.sleep(1)
        transfer = transfer_service.get()

    return transfer_service

def get_proxy_connection(proxy_url):
    """
    Creates a new HTTPSConnection for the specified proxy
    """
    # At this stage, the SDK granted the permission to start transferring the disk, and the
    # user should choose its preferred tool for doing it - regardless of the SDK.
    # In this example, we will use Python's httplib.HTTPSConnection for transferring the data.
    context = ssl.create_default_context()

    # Note that ovirt-imageio-proxy by default checks the certificates, so if you don't have
    # your CA certificate of the engine in the system, you need to pass it to HTTPSConnection.
    context.load_verify_locations(cafile='ca.pem')

    return HTTPSConnection(
        proxy_url.hostname,
        proxy_url.port,
        context=context,
    )

def upload_disk_snapshot(disk_path):
    """
    Upload a single disk snapshot
    """
    disk_snapshot_id = os.path.basename(disk_path)
    transfer_service = get_transfer_service(disk_snapshot_id)

    try:
        transfer = transfer_service.get()
        proxy_url = urlparse(transfer.proxy_url)
        proxy_connection = get_proxy_connection(proxy_url)
        path = disk_path

        # Set needed headers for uploading:
        upload_headers = {
            'Authorization': transfer.signed_ticket,
        }

        with open(path, "rb") as disk:
            size = os.path.getsize(path)
            chunk_size = 1024 * 1024 * 8
            pos = 0
            while pos < size:
                # Extend the transfer session.
                transfer_service.extend()
                # Set the content range, according to the chunk being sent.
                upload_headers['Content-Range'] = "bytes %d-%d/%d" % (pos, min(pos + chunk_size, size) - 1, size)
                # Perform the request.
                proxy_connection.request(
                    'PUT',
                    proxy_url.path,
                    disk.read(chunk_size),
                    headers=upload_headers,
                )
                # Print response
                r = proxy_connection.getresponse()
                print(r.status, r.reason, "Completed", "{:.0%}".format(pos / float(size)))
                # Continue to next chunk.
                pos += chunk_size

        print("Completed", "{:.0%}".format(pos / float(size)))
    finally:
        # Finalize the session.
        transfer_service.finalize()

        # Waiting for finalize to complete
        try:
            while transfer_service.get():
                time.sleep(1)
        except sdk.NotFoundError:
            pass

def create_vm_from_ovf(ovf_file_path, vms_service):
    """
    Creates a new VM from the specified OVF
    """
    ovf_data = open(ovf_file_path, 'r').read()
    vm = vms_service.add(
        types.Vm(
            cluster=types.Cluster(
                name='mycluster',
            ),
            initialization = types.Initialization(
                configuration = types.Configuration(
                    type = types.ConfigurationType.OVF,
                    data = ovf_data
                )
            ),
        ),
    )
    return vm.id

def create_disk(image_info, disk_id, sd_name, disks_service):
    """
    Creates a new disk with the specified disk_id and image_id
    from image_info (to keep the meta-data identical to
    the uploaded disk).
    """
    initial_size = image_info['actual-size']
    provisioned_size = image_info['virtual-size']
    image_id = os.path.basename(image_info['filename'])

    disk = disks_service.add(
        types.Disk(
            id=disk_id,
            image_id=image_id,
            name=disk_id,
            format=types.DiskFormat.RAW,
            provisioned_size=provisioned_size,
            initial_size=initial_size,
            storage_domains=[
                types.StorageDomain(
                    name=sd_name
                )
            ]
        )
    )
    disk_service = disks_service.disk_service(disk.id)
    while True:
        time.sleep(5)
        disk = disk_service.get()
        if disk.status == types.DiskStatus.OK:
            break

    return disk

def create_snapshot(description, image_info, image_id, disk_id, vm_service):
    """
    Creates a new snapshot for the specified disk_id.
    To ensure consistency with the uploaded chain, the sepcified
    image_id will be used for the created image.
    """
    # Locate the service that manages the snapshots of the virtual machine:
    snapshots_service = vm_service.snapshots_service()

    # Add the new snapshot:
    snapshot = snapshots_service.add(
        types.Snapshot(
            description=description,
            disk_attachments=[
                types.DiskAttachment(
                    disk=types.Disk(
                        id=disk_id,
                        image_id=image_id,
                        initial_size=image_info['actual-size']
                    )
                )
            ]
        ),
    )

    # 'Waiting for Snapshot creation to finish'
    snapshot_service = snapshots_service.snapshot_service(snapshot.id)
    while True:
        time.sleep(5)
        snapshot = snapshot_service.get()
        if snapshot.snapshot_status == types.SnapshotStatus.OK:
            break

    return snapshot

def get_volume_info(disk_snapshot_id):
    """
    Returns volume's info using qemu-img
    """
    output = subprocess.check_output([
        'qemu-img',
        'info',
        '--output=json',
        disk_snapshot_id,
    ])
    return json.loads(str(output))

def get_images_chain(disk_path):
    """
    Returns a chain of images of the specified disk.
    The chain is built by fetching the volume info (using qemu-img)
    of each file, and find the backing filename (volume's parent).
    By maintaing a map between parent and child volumes, we can
    construct the chain, starting from base volume.
    """
    volumes_info = {}   # {filename -> vol_info}
    backing_files = {}  # {backing_file (parent) -> vol_info (child)}
    for root, dirs, file_names in os.walk(disk_path):
        for file_name in file_names:
            volume_info = get_volume_info("%s/%s" % (disk_path, file_name))
            volumes_info[file_name] = volume_info
            if 'full-backing-filename' in volume_info:
                backing_files[volume_info['full-backing-filename']] = volume_info

    base_volume = [v for v in volumes_info.values() if 'full-backing-filename' not in v ][0]
    child = backing_files[base_volume['filename']]
    images_chain = [base_volume]
    while child != None:
        images_chain.append(child)
        parent = child
        if parent['filename'] in backing_files:
            child = backing_files[parent['filename']]
        else:
            child = None

    return images_chain

if __name__ == "__main__":

    # Set storage domain name
    sd_name = 'mydata'

    # Set OVF file path
    ovf_file_path = 'c3a8e806-106d-4aff-b59a-3a113eabf5a9.ovf'

    # Disk to upload
    disk_path = 'disks/f87c133f-3ef6-43b9-a061-d66722bf341d'
    disk_id = os.path.basename(disk_path)

    # Create a connection to the server:
    connection = get_connection()

    # Get a reference to the root service:
    system_service = connection.system_service()

    # Get the reference to the "vms" service:
    vms_service = system_service.vms_service()

    # Get images chain (snapshots)
    images_chain = get_images_chain(disk_path)

    try:
        # Create disk by base volume info
        base_volume = images_chain[0]
        disks_service = system_service.disks_service()
        print("Creating disk: %s" % disk_id)
        disk = create_disk(base_volume, disk_id, sd_name, disks_service)

        # Add VM from saved OVF file
        print("Creating VM from OVF: %s" % ovf_file_path)
        vmId = create_vm_from_ovf(ovf_file_path, vms_service)

        # Locate VM service
        vm_service = vms_service.vm_service(vmId)

        # Creating a snapshot for each image
        for image in images_chain[1:]:
            image_id = os.path.basename(image['filename'])
            print("Creating snapshot - Image: %s, Disk: %s" % (image_id, disk_id))
            create_snapshot("description", image, image_id, disk_id, vm_service)

        # Uploading images
        for image in images_chain:
            image_path = image['filename']
            print("Uploading image %s" % image_path)
            upload_disk_snapshot(image_path)
    finally:
        # Close the connection to the server:
        connection.close()
