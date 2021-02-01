#
# Copyright (c) 2020 Red Hat, Inc.
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
"""
Image transfer helpers
"""

import logging
import time

import ovirtsdk4 as sdk
from ovirtsdk4 import types

log = logging.getLogger("helpers")


def find_host(connection, sd_name):
    """
    Check if we can preform a transfer using the local host and return a host
    instance. Return None if we cannot use this host.

    Using the local host for an image transfer allows optimizing the connection
    using unix socket. This speeds up the transfer significantly and minimizes
    the network bandwidth.

    However using the local host is possible only if:
    - The local host is a oVirt host
    - The host is Up
    - The host is in the same DC of the storage domain

    Consider this setup:

        laptop1

        dc1
            host1 (down)
            host2 (up)
            sd1
                disk1

        dc2
            host3 (up)
            sd2
                disk2

    - If we run on laptop1 we cannot use the local host for any transfer.
    - If we run on host1, we cannot use the local host for any transfer.
    - If we run on host2, we can use use host2 for transferring disk1.
    - If we run on host3, we can use host3 for transferring disk2.

    Arguments:
        connection (ovirtsdk4.Connection): Connection to ovirt engine
        sd_name (str): Storage domain name

    Returns:
        ovirtsdk4.types.Host
    """

    # Try to read this host hardware id.

    try:
        with open("/etc/vdsm/vdsm.id") as f:
            vdsm_id = f.readline().strip()
    except FileNotFoundError:
        log.debug("Not running on oVirt host, using any host")
        return None
    except OSError as e:
        # Unexpected error when running on ovirt host. Since choosing a host is
        # an optimization, log and continue.
        log.warning("Cannot read /etc/vdsm/vdsm.id, using any host: %s", e)
        return None

    log.debug("Found host hardware id: %s", vdsm_id)

    # Find the data center by storage domain name.

    system_service = connection.system_service()
    data_centers = system_service.data_centers_service().list(
        search='storage.name=%s' % sd_name,
        case_sensitive=True,
    )
    if len(data_centers) == 0:
        raise RuntimeError(
            "Storage domain {} is not attached to a DC"
            .format(sd_name))

    data_center = data_centers[0]
    log.debug("Found data center: %s", data_center.name)

    # Validate that this host is up and in data center.

    hosts_service = system_service.hosts_service()
    hosts = hosts_service.list(
        search="hw_id={} and datacenter={} and status=Up".format(
            vdsm_id, data_center.name),
        case_sensitive=True,
    )
    if len(hosts) == 0:
        log.debug(
            "Cannot use host with hardware id %s, host is not up, or does "
            "not belong to data center %s",
            vdsm_id, data_center.name)
        return None

    host = hosts[0]
    log.debug("Using host id %s", host.id)

    return host


def create_transfer(
        connection, disk=None, direction=types.ImageTransferDirection.UPLOAD,
        host=None, backup=None, inactivity_timeout=None, timeout=60,
        disk_snapshot=None, shallow=None,
        timeout_policy=types.ImageTransferTimeoutPolicy.LEGACY):
    """
    Create image transfer for upload to disk or download from disk.

    Arguments:
        connection (ovirtsdk4.Connection): connection to ovirt engine
        disk (ovirtsdk4.types.Disk): disk object. Not needed if disk_snaphost
            is specified.
        direction (ovirtsdk4.typles.ImageTransferDirection): transfer
            direction (default UPLOAD)
        host (ovirtsdk4.types.Host): host object that should perform the
            transfer. If not specified engine will pick a random host.
        backup (ovirtsdk4.types.Backup): When downloading backup, the backup
            object owning the disks.
        inactivity_timeout (int): Number of seconds engine will wait for client
            activity before pausing the transfer. If not set, use engine
            default value.
        timeout (float, optional): number of seconds to wait for transfer
            to become ready.
        disk_snapshot (ovirtsdk4.types.DiskSnapshot): transfer a disk snapshot
            instead of current data of the disk.
        shallow (bool): Download only the specified image instead of the entire
            image chain. When downloading a disk transfer only the active disk
            snapshot data. When downloading a disk snapshot, transfer only the
            specified disk snaphost data.
        timeout_policy (ovirtsdk4.types.ImageTransferTimeoutPolicy): the action
            to take after inactivity timeout.

    Returns:
        ovirtsdk4.types.ImageTransfer in phase TRANSFERRING
    """
    log.info(
        "Creating image transfer for %s=%s, direction=%s host=%s backup=%s "
        "shallow=%s timeout_policy=%s",
        "disk_snapshot" if disk_snapshot else "disk",
        disk_snapshot.id if disk_snapshot else disk.id,
        direction,
        host,
        backup,
        shallow,
        timeout_policy,
    )

    # Create image transfer for disk or snapshot.

    transfer = types.ImageTransfer(
        host=host,
        direction=direction,
        backup=backup,
        inactivity_timeout=inactivity_timeout,
        timeout_policy=timeout_policy,

        # format=raw uses the NBD backend, enabling:
        # - Transfer raw guest data, regardless of the disk format.
        # - Automatic format conversion to remote disk format. For example,
        #   upload qcow2 image to raw disk, or raw image to qcow2 disk.
        # - Collapsed qcow2 chains to single raw file.
        # - Extents reporting for qcow2 images and raw images on file storage,
        #   speeding up downloads.
        format=types.DiskFormat.RAW,

        shallow=shallow,
    )

    if disk_snapshot:
        transfer.snapshot = types.DiskSnapshot(id=disk_snapshot.id)
    else:
        transfer.disk = types.Disk(id=disk.id)

    transfers_service = connection.system_service().image_transfers_service()

    # Add the new transfer to engine. This starts the transfer and retruns a
    # transfer ID that can be used to track this image transfer.
    transfer = transfers_service.add(transfer)

    # You can use the transfer id to locate logs for this transfer.
    log.info("Transfer ID %s", transfer.id)

    # At this point the transfer owns the disk and will delete the disk if the
    # transfer is canceled, or if finalizing the transfer fails.

    transfer_service = transfers_service.image_transfer_service(transfer.id)
    start = time.time()

    while True:
        time.sleep(1)
        try:
            transfer = transfer_service.get()
        except sdk.NotFoundError:
            # The system has removed the disk and the transfer.
            raise RuntimeError("Transfer {} was removed".format(transfer.id))

        if transfer.phase == types.ImageTransferPhase.FINISHED_FAILURE:
            # The system will remove the disk and the transfer soon.
            raise RuntimeError("Transfer {} has failed".format(transfer.id))

        if transfer.phase == types.ImageTransferPhase.PAUSED_SYSTEM:
            transfer_service.cancel()
            raise RuntimeError(
                "Transfer {} was paused by system".format(transfer.id))

        if transfer.phase == types.ImageTransferPhase.TRANSFERRING:
            break

        if transfer.phase != types.ImageTransferPhase.INITIALIZING:
            transfer_service.cancel()
            raise RuntimeError(
                "Unexpected transfer {} phase {}"
                .format(transfer.id, transfer.phase))

        if time.time() > start + timeout:
            log.info("Cancelling transfer %s", transfer.id)
            transfer_service.cancel()
            raise RuntimeError(
                "Timed out waiting for transfer {}".format(transfer.id))

    log.info("Transfer initialized in %.3f seconds", time.time() - start)

    # Log the transfer host name. This is very useful for troubleshooting.
    hosts_service = connection.system_service().hosts_service()
    host_service = hosts_service.host_service(transfer.host.id)
    transfer.host = host_service.get()

    log.info("Transfer host name: %s", transfer.host.name)

    return transfer


def cancel_transfer(connection, transfer):
    """
    Cancel a transfer and remove the disk for upload transfer.

    There is not need to cancel a download transfer, it can always be
    finalized.
    """
    log.info("Cancelling transfer %s", transfer.id)
    transfer_service = (connection.system_service()
                            .image_transfers_service()
                            .image_transfer_service(transfer.id))
    transfer_service.cancel()


def finalize_transfer(connection, transfer, disk, timeout=60):
    """
    Finalize a transfer, making the transfer disk available.

    If finalizing succeeds, transfer's phase will change to FINISHED_SUCCESS
    and the transfer's disk status will change to OK.  On upload errors, the
    transfer's phase will change to FINISHED_FAILURE and the disk status will
    change to ILLEGAL and it will be removed. In both cases the transfer entity
    will be removed shortly after.

    If oVirt fails to finalize the transfer, transfer's phase will change to
    PAUSED_SYSTEM. In this case the disk's status will change to ILLEGAL and it
    will not be removed.

    For simplicity, we track only disk's status changes.

    For more info see:
    - http://ovirt.github.io/ovirt-engine-api-model/4.4/#services/image_transfer
    - http://ovirt.github.io/ovirt-engine-sdk/master/types.m.html#ovirtsdk4.types.ImageTransfer

    Arguments:
        connection (ovirtsdk4.Connection): connection to ovirt engine
        transfer (ovirtsdk4.types.ImageTransfer): image transfer to finalize
        disk (ovirtsdk4.types.Disk): disk associated with the image transfer
        timeout (float, optional): number of seconds to wait for transfer
            to finalize.
    """
    log.info("Finalizing transfer %s for disk %s", transfer.id, disk.id)

    transfer_service = (connection.system_service()
                            .image_transfers_service()
                            .image_transfer_service(transfer.id))

    start = time.time()

    transfer_service.finalize()

    disk_service = (connection.system_service()
                        .disks_service()
                        .disk_service(disk.id))

    while True:
        time.sleep(1)
        try:
            disk = disk_service.get()
        except sdk.NotFoundError:
            # Disk verification failed and the system removed the disk.
            raise RuntimeError(
                "Transfer {} failed: disk {} was removed"
                .format(transfer.id, disk.id))

        if disk.status == types.DiskStatus.ILLEGAL:
            # Disk verification failed or transfer was paused by the system.
            raise RuntimeError(
                "Transfer {} failed: disk {} is ILLEGAL"
                .format(transfer.id, disk.id))

        if disk.status == types.DiskStatus.OK:
            break

        if time.time() > start + timeout:
            raise RuntimeError(
                "Timed out waiting for transfer {} to finalize"
                .format(transfer.id))

    log.info("Transfer finalized in %.3f seconds", time.time() - start)
