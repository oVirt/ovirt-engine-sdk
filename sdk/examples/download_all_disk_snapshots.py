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

import logging
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import ssl
import sys
import time

from six.moves.http_client import HTTPSConnection
from six.moves.urllib.parse import urlparse


logging.basicConfig(level=logging.DEBUG, filename='example.log')


# This example will connect to the server, loop over the disk snapshots
# of a specified disk and download their data into files.
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
    # Get a reference to the service that manages the image transfer:
    transfers_service = system_service.image_transfers_service()

    # Add a new image transfer:
    transfer = transfers_service.add(
        types.ImageTransfer(
            snapshot=types.DiskSnapshot(id=disk_snapshot_id),
            direction=types.ImageTransferDirection.DOWNLOAD,
        )
    )

    # Get reference to the created transfer service:
    transfer_service = transfers_service.image_transfer_service(transfer.id)

    while transfer.phase == types.ImageTransferPhase.INITIALIZING:
        time.sleep(1)
        transfer = transfer_service.get()

    return transfer_service

def get_proxy_connection(proxy_url):
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

def download_disk_snapshot(disk_snapshot):
    print("Downloading disk snapshot %s" % disk_snapshot.id)

    transfer_service = None
    try:
        transfer_service = get_transfer_service(disk_snapshot.id)
        transfer = transfer_service.get()
        proxy_url = urlparse(transfer.proxy_url)
        proxy_connection = get_proxy_connection(proxy_url)
        path = disk_snapshot.id

        with open(path, "wb") as mydisk:
            # Set needed headers for downloading:
            transfer_headers = {
                'Authorization': transfer.signed_ticket,
            }

            # Perform the request.
            proxy_connection.request(
                'GET',
                proxy_url.path,
                headers=transfer_headers,
            )
            # Get response
            r = proxy_connection.getresponse()

            # Check the response status:
            if r.status >= 300:
                print("Error: %s" % r.read())

            bytes_to_read = int(r.getheader('Content-Length'))
            chunk_size = 64 * 1024 * 1024

            print("Disk snapshot size: %s bytes" % str(bytes_to_read))

            while bytes_to_read > 0:
                # Calculate next chunk to read
                to_read = min(bytes_to_read, chunk_size)

                # Read next chunk
                chunk = r.read(to_read)

                if chunk == "":
                    raise RuntimeError("Socket disconnected")

                # Write the content to file:
                mydisk.write(chunk)

                # Update bytes_to_read
                bytes_to_read -= len(chunk)

                completed = 1 - (bytes_to_read / float(r.getheader('Content-Length')))

                print("Completed", "{:.0%}".format(completed))
    finally:
        # Finalize the session.
        if transfer_service is not None:
            transfer_service.finalize()

            # Waiting for finalize to complete
            try:
                while transfer_service.get():
                    time.sleep(1)
            except sdk.NotFoundError:
                pass

if __name__ == "__main__":

    # Set relevant disk and stroage domain IDs
    disk_id = 'ccdd6487-0a8f-40c8-9f45-40e0e2b30d79'
    sd_name = 'mydata'

    # Create a connection to the server:
    connection = get_connection()

    # Get a reference to the root service:
    system_service = connection.system_service()

    # Get a reference to the storage domains service:
    storage_domains_service = system_service.storage_domains_service()

    # Look up fot the storage domain by name:
    storage_domain = storage_domains_service.list(search='name=%s' % sd_name)[0]

    # Get a reference to the storage domain service in which the disk snapshots reside:
    storage_domain_service = storage_domains_service.storage_domain_service(storage_domain.id)

    # Get a reference to the disk snapshots service:
    # Note: we are retrieving here *all* the snapshots of the storage domain.
    # Should find a more efficient means in the future.
    disk_snapshot_service = storage_domain_service.disk_snapshots_service()

    # Get a list of disk snapshots by a disk ID
    all_disk_snapshots = disk_snapshot_service.list()

    # Filter disk snapshots list by disk id
    disk_snapshots = [s for s in all_disk_snapshots if s.disk.id == disk_id]

    # Download disk snapshots
    for disk_snapshot in disk_snapshots:
        download_disk_snapshot(disk_snapshot)

    # Close the connection to the server:
    connection.close()
