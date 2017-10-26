#!/usr/bin/python

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
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server, create a snapshot of 
# an existing virtual machine, restore the VM to that
# snapshot, and then remove the snapshot:

# Create the connection to the server:
connection = sdk.Connection(
  url='https://engine40.example.com/ovirt-engine/api',
  username='admin@internal',
  password='redhat123',
  ca_file='ca.pem',
  debug=True,
  log=logger.getLogger(),
)

# Locate the virtual machines service and use it to find the virtual
# machine:
vms_service = connection.system_service().vms_service()
vm = vms_service.list(search='name=myvm')[0]

# Locate the service that manages the snapshots of the virtual machine:
snapshots_service = vms_service.vm_service(vm.id).snapshots_service()

# Add the new snapshot:
snapshots_service.add(
  types.Snapshot(
    description='My snapshot',
  ),
)
logging.info(
    'Sent request to create snapshot \'%s\', the id is \'%s\'.',
    snap.description, snap.id,
)

# Poll and wait till the status of the snapshot is 'OK', which means
# that it is completely created:
snap_service = snaps_service.snapshot_service(snap.id)
while snap.snapshot_status != types.SnapshotStatus.OK:
    logging.info(
        'Waiting till the snapshot is created, the satus is now \'%s\'.',
        snap.snapshot_status,
    )
    time.sleep(1)
    snap = snap_service.get()
logging.info('The snapshot is now complete.')

# Power off VM to enable snapshot restoration
vm_service.stop()

# Poll and wait until the status of the VM is 'DOWN' before
# attempting to restore the snapshot
while vm_status.status != types.VmStatus.DOWN:
    logging.info(
        'Powering off the VM, the status is now \'%s\'.',
        vm_status.status,
    )
    time.sleep(1)
    vm_status = vm_service.get()
logging.info('The VM has been powered off.')

try:
    # Restore the snapshot
    snap_service.restore(
        async=False,
        restore_memory=False
    )
except:
    logging.info('VM could not be restored to previous snapshot.')

# Poll and wait until the status of the VM is 'DOWN', meaning
# that the snapshot has successfully been restored
vm_status = vm_service.get()
while vm_status.status != types.VmStatus.DOWN:
    logging.info(
        'Waiting for VM to be powered Down, the status is now \'%s\'.',
        vm_status.status,
    )
    time.sleep(1)
    vm_status = vm_service.get()
logging.info('The VM has been restored.')

# Remove the snapshot
snap_service.remove()
logging.info('Removed snapshot named \'%s\'.', snap.description)

# Close the connection to the server:
connection.close()
