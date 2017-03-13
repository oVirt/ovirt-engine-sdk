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
import os
import time
import uuid

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example shows how the virtual machine backup process.

# The connection details:
API_URL = 'https://engine40.example.com/ovirt-engine/api'
API_USER = 'admin@internal'
API_PASSWORD = 'redhat123'

# The file containing the certificat of the CA used by the server. In
# an usual installation it will be in the file '/etc/pki/ovirt-engine/ca.pem'.
API_CA_FILE = 'ca.pem'

# The name of the application, to be used as the 'origin' of events
# sent to the audit log:
APPLICATION_NAME = 'mybackup'

# The name of the virtual machine that contains the data that we
# want to back-up:
DATA_VM_NAME = 'myvm'

# The name of the virtual machine where we will attach the disks in
# order to actually back-up them. This virtual machine will usually have
# some kind of back-up software installed.
AGENT_VM_NAME = 'myagent'

# Connect to the server:
connection = sdk.Connection(
    url=API_URL,
    username=API_USER,
    password=API_PASSWORD,
    ca_file=API_CA_FILE,
    debug=True,
    log=logging.getLogger(),
)
logging.info('Connected to the server.')

# Get the reference to the root of the services tree:
system_service = connection.system_service()

# Get the reference to the service that we will use to send events to
# the audit log:
events_service = system_service.events_service()

# In order to send events we need to also send unique integer ids. These
# should usually come from an external database, but in this example we
# will just generate them from the current time in seconds since Jan 1st
# 1970.
event_id = int(time.time())

# Get the reference to the service that manages the virtual machines:
vms_service = system_service.vms_service()

# Find the virtual machine that we want to back up. Note that we need to
# use the 'all_content' parameter to retrieve the retrieve the OVF, as
# it isn't retrieved by default:
data_vm = vms_service.list(
    search='name=%s' % DATA_VM_NAME,
    all_content=True,
)[0]
logging.info(
    'Found data virtual machine \'%s\', the id is \'%s\'.',
    data_vm.name, data_vm.id,
)

# Find the virtual machine were we will attach the disks in order to do
# the backup:
agent_vm = vms_service.list(
    search='name=%s' % AGENT_VM_NAME,
)[0]
logging.info(
    'Found agent virtual machine \'%s\', the id is \'%s\'.',
    agent_vm.name, agent_vm.id,
)

# Find the services that manage the data and agent virtual machines:
data_vm_service = vms_service.vm_service(data_vm.id)
agent_vm_service = vms_service.vm_service(agent_vm.id)

# Create an unique description for the snapshot, so that it is easier
# for the administrator to identify this snapshot as a temporary one
# created just for backup purposes:
snap_description = '%s-backup-%s' % (data_vm.name, uuid.uuid4())

# Send an external event to indicate to the administrator that the
# backup of the virtual machine is starting. Note that the description
# of the event contains the name of the virtual machine and the name of
# the temporary snapshot, this way, if something fails, the administrator
# will know what snapshot was used and remove it manually.
events_service.add(
    event=types.Event(
        vm=types.Vm(
          id=data_vm.id,
        ),
        origin=APPLICATION_NAME,
        severity=types.LogSeverity.NORMAL,
        custom_id=event_id,
        description=(
            'Backup of virtual machine \'%s\' using snapshot \'%s\' is '
            'starting.' % (data_vm.name, snap_description)
        ),
    ),
)
event_id += 1

# Save the OVF to a file, so that we can use to restore the virtual
# machine later. The name of the file is the name of the virtual
# machine, followed by a dash and the identifier of the virtual machine,
# to make it unique:
ovf_data = data_vm.initialization.configuration.data
ovf_file = '%s-%s.ovf' % (data_vm.name, data_vm.id)
with open(ovf_file, 'w') as ovs_fd:
    ovs_fd.write(ovf_data.encode('utf-8'))
logging.info('Wrote OVF to file \'%s\'.', os.path.abspath(ovf_file))

# Send the request to create the snapshot. Note that this will return
# before the snapshot is completely created, so we will later need to
# wait till the snapshot is completely created.
# The snapshot will not include memory. Change to True the parameter
# persist_memorystate to get it (in that case the VM will be paused for a while).
snaps_service = data_vm_service.snapshots_service()
snap = snaps_service.add(
    snapshot=types.Snapshot(
        description=snap_description,
        persist_memorystate=False,
    ),
)
logging.info(
    'Sent request to create snapshot \'%s\', the id is \'%s\'.',
    snap.description, snap.id,
)

# Poll and wait till the status of the snapshot is 'ok', which means
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

# Retrieve the descriptions of the disks of the snapshot:
snap_disks_service = snap_service.disks_service()
snap_disks = snap_disks_service.list()

# Attach all the disks of the snapshot to the agent virtual machine, and
# save the resulting disk attachments in a list so that we can later
# detach them easily:
attachments_service = agent_vm_service.disk_attachments_service()
attachments = []
for snap_disk in snap_disks:
    attachment = attachments_service.add(
        attachment=types.DiskAttachment(
            disk=types.Disk(
                id=snap_disk.id,
                snapshot=types.Snapshot(
                    id=snap.id,
                ),
            ),
            active=True,
            bootable=False,
            interface=types.DiskInterface.VIRTIO,
        ),
    )
    attachments.append(attachment)
    logging.info(
        'Attached disk \'%s\' to the agent virtual machine.',
        attachment.disk.id,
    )

# Now the disks are attached to the virtual agent virtual machine, we
# can then ask that virtual machine to perform the backup. Doing that
# requires a mechanism to talk to the backup software that runs inside the
# agent virtual machine. That is outside of the scope of the SDK. But if
# the guest agent is installed in the virtual machine then we can
# provide useful information, like the identifiers of the disks that have
# just been attached.
for attachment in attachments:
    if attachment.logical_name is not None:
        logging.info(
            'Logical name for disk \'%s\' is \'%s\'.',
            attachment.disk.id, attachment.logicalname,
        )
    else:
        logging.info(
            'The logical name for disk \'%s\' isn\'t available. Is the '
            'guest agent installed?',
            attachment.disk.id,
        )

# Insert here the code to contact the backup agent and do the actual
# backup ...
logging.info('Doing the actual backup ...')

# Detach the disks from the agent virtual machine:
for attachment in attachments:
    attachment_service = attachments_service.attachment_service(attachment.id)
    attachment_service.remove()
    logging.info(
        'Detached disk \'%s\' to from the agent virtual machine.',
        attachment.disk.id,
    )

# Remove the snapshot:
snap_service.remove()
logging.info('Removed the snapshot \'%s\'.', snap.description)

# Send an external event to indicate to the administrator that the
# backup of the virtual machine is completed:
events_service.add(
    event=types.Event(
        vm=types.Vm(
          id=data_vm.id,
        ),
        origin=APPLICATION_NAME,
        severity=types.LogSeverity.NORMAL,
        custom_id=event_id,
        description=(
            'Backup of virtual machine \'%s\' using snapshot \'%s\' is '
            'completed.' % (data_vm.name, snap_description)
        ),
    ),
)
event_id += 1

# Close the connection to the server:
connection.close()
