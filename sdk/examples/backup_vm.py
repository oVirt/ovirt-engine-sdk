#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
This example will connect to the server and perform the selected full
backup operation (start backup, finalize backup or download backup disks)
for an existing running VM with the given disks.

Note that this feature API is supported from version 4.3
but the feature is currently in tech-preview until libvirt will
release official release that contains the support for incremental
backup.
Using this example requires a special libvirt version supporting
incremental backup.

Requires the ovirt-imageio-client package.
"""

import inspect
import os
import sys
import time

from contextlib import closing

from ovirt_imageio import client

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

from helpers import common
from helpers import imagetransfer
from helpers import units
from helpers.common import progress


def main():
    parser = common.ArgumentParser(description="Backup VM disks")
    subparsers = parser.add_subparsers(title="commands")

    full_parser = subparsers.add_parser(
        "full",
        help="Run full backup.")

    full_parser.set_defaults(command=cmd_full)

    add_download_args(full_parser)

    full_parser.add_argument(
        "vm_uuid",
        help="UUID of the VM to backup.")

    full_parser.add_argument(
        "--disk-uuid",
        action="append",
        help="Disk UUID to backup. May be used multiple times to backup "
             "multiple disks. If not specified, backup all VM disks."),

    full_parser.add_argument(
        "--skip-download",
        dest="download_backup",
        action="store_false",
        help="Download full backup disks should be skipped. If specified, VM backup will "
             "start and stop without downloading the disks.")

    incremental_parser = subparsers.add_parser(
        "incremental",
        help="Run incremental backup.")

    incremental_parser.set_defaults(command=cmd_incremental)

    add_download_args(incremental_parser)

    incremental_parser.add_argument(
        "vm_uuid",
        help="UUID of the VM to backup.")

    incremental_parser.add_argument(
        "--from-checkpoint-uuid",
        required=True,
        help="Perform incremental backup since the specified checkpoint "
             "UUID.")

    incremental_parser.add_argument(
        "--disk-uuid",
        action="append",
        help="Disk UUID to backup. May be used multiple times to backup "
             "multiple disks. If not specified, backup all VM disks.")

    incremental_parser.add_argument(
        "--skip-download",
        dest="download_backup",
        action="store_false",
        help="Download incremental backup disks should be skipped. If specified, VM backup will "
             "start and stop without downloading the disks.")

    start_parser = subparsers.add_parser(
        "start",
        help="Start VM backup.")

    start_parser.set_defaults(command=cmd_start)

    start_parser.add_argument(
        "vm_uuid",
        help="UUID of the VM to backup.")

    start_parser.add_argument(
        "--disk-uuid",
        action="append",
        help="Disk UUID to backup. May be used multiple times to backup "
             "multiple disks. If not specified, backup all VM disks.")

    start_parser.add_argument(
        "--from-checkpoint-uuid",
        help="Perform incremental backup since the specified checkpoint "
             "UUID.")

    download_parser = subparsers.add_parser(
        "download",
        help="Download VM backup disk.")

    download_parser.set_defaults(command=cmd_download)

    add_download_args(download_parser)

    download_parser.add_argument(
        "vm_uuid",
        help="UUID of the VM for the backup.")

    download_parser.add_argument(
        "--backup-uuid",
        required=True,
        help="UUID of the backup to finalize.")

    download_parser.add_argument(
        "--incremental",
        action="store_true",
        help="Download incremental backup data in qcow2 format. The "
             "downloaded disk should be rebased on the previous backup "
             "to restore the disk contents. Can be used only if the "
             "backup was started with --from-checkpoint-uuid.")

    stop_parser = subparsers.add_parser(
        "stop",
        help="Stop VM backup.")

    stop_parser.set_defaults(command=cmd_stop)

    stop_parser.add_argument(
        "vm_uuid",
        help="UUID of the VM for the backup.")

    stop_parser.add_argument(
        "backup_uuid",
        help="UUID of the backup to finalize.")

    args = parser.parse_args()

    common.configure_logging(args)
    args.command(args)


# Commands

def cmd_full(args):
    """
    Run full backup flow - start, download and stop backup.
    """
    progress("Starting full backup for VM %r" % args.vm_uuid)

    connection = common.create_connection(args)
    with closing(connection):
        args.from_checkpoint_uuid = None
        backup = start_backup(connection, args)
        try:
            download_backup(connection, backup.id, args)
        finally:
            progress("Finalizing backup")
            stop_backup(connection, backup.id, args)

    progress("Full backup completed successfully")


def cmd_incremental(args):
    """
    Run incremental backup flow - start_incremental, download and stop backup.
    """
    progress("Starting incremental backup for VM %r" % args.vm_uuid)

    connection = common.create_connection(args)
    with closing(connection):
        backup = start_backup(connection, args)
        try:
            download_backup(connection, backup.id, args, incremental=True)
        finally:
            progress("Finalizing backup")
            stop_backup(connection, backup.id, args)

    progress("Incremental backup completed successfully")


def cmd_start(args):
    """
    Start backup, printing backup UUID.

    To download the backup run download command.
    To stop the backup run the stop command.
    """
    if args.from_checkpoint_uuid:
        progress(
            "Starting incremental backup since checkpoint %r for VM %r" % (
                args.from_checkpoint_uuid, args.vm_uuid))
    else:
        progress("Starting full backup for VM %r" % args.vm_uuid)

    connection = common.create_connection(args)

    with closing(connection):
        backup = start_backup(connection, args)

    progress("Backup %r is ready" % backup.id)


def cmd_download(args):
    """
    Download backup using the backup UUID printed by the start command.
    """
    progress("Downloading VM %r disks" % args.vm_uuid)

    connection = common.create_connection(args)
    with closing(connection):
        download_backup(
            connection, args.backup_uuid, args, incremental=args.incremental)

    progress("Finished downloading disks")


def cmd_stop(args):
    """
    Stop backup using the backup UUID printed by the start command.
    """
    progress("Finalizing backup %r" % args.backup_uuid)

    connection = common.create_connection(args)
    with closing(connection):
        stop_backup(connection, args.backup_uuid, args)

    progress("Backup %r has been finalized" % args.backup_uuid)


# Argument parsing

def add_download_args(parser):
    parser.add_argument(
        "--max-workers",
        type=int,
        default=4,
        help="maximum number of workers to use for backup. The default "
             "(4) improves performance when backing up a single disk. "
             "You may want to use lower number if you back up many disks "
             "in the same time.")

    parser.add_argument(
        "--buffer-size",
        type=units.humansize,
        default=client.BUFFER_SIZE,
        help="Buffer size per worker. The default ({}) gives good "
             "performance with the default number of workers. If you use "
             "smaller number of workers you may want use larger value."
             .format(client.BUFFER_SIZE))

    parser.add_argument(
        "--backup-dir",
        default="./",
        help="Path to a directory to download backup disks "
             "to (The default is the current directory).")

    parser.add_argument(
        "--timeout-policy",
        choices=('legacy', 'pause', 'cancel'),
        default='cancel',
        help="The action to be made for a timed out transfer.")


# Backup helpers

def start_backup(connection, args):
    verify_vm_exists(connection, args.vm_uuid)

    system_service = connection.system_service()
    vm_service = system_service.vms_service().vm_service(id=args.vm_uuid)

    backups_service = vm_service.backups_service()

    if args.disk_uuid:
        disks = [types.Disk(id=disk_id) for disk_id in args.disk_uuid]
    else:
        disks = get_vm_disks(connection, args.vm_uuid)

    backup = backups_service.add(
        types.Backup(
            disks=disks,
            from_checkpoint_id=args.from_checkpoint_uuid
        )
    )

    progress("Waiting until backup %r is ready" % backup.id)

    backup_service = backups_service.backup_service(backup.id)

    while backup.phase != types.BackupPhase.READY:
        time.sleep(1)
        backup = get_backup(connection, backup_service, backup.id)

    if backup.to_checkpoint_id is not None:
        progress(
            "Created checkpoint %r (to use in --from-checkpoint-uuid "
            "for the next incremental backup)" % backup.to_checkpoint_id)

    return backup


def stop_backup(connection, backup_uuid, args):
    verify_vm_exists(connection, args.vm_uuid)
    verify_backup_exists(connection, args.vm_uuid, backup_uuid)

    backup_service = get_backup_service(connection, args.vm_uuid, backup_uuid)

    backup_service.finalize()

    progress("Waiting until backup is being finalized")

    backup = get_backup(connection, backup_service, backup_uuid)
    while backup.phase != types.BackupPhase.FINALIZING:
        time.sleep(1)
        backup = get_backup(connection, backup_service, backup_uuid)


def download_backup(connection, backup_uuid, args, incremental=False):
    verify_vm_exists(connection, args.vm_uuid)
    verify_backup_exists(connection, args.vm_uuid, backup_uuid)

    if not args.download_backup:
        progress("Skipping download")
        return

    backup_service = get_backup_service(connection, args.vm_uuid, backup_uuid)

    backup = get_backup(connection, backup_service, backup_uuid)
    if backup.phase != types.BackupPhase.READY:
        raise RuntimeError("Backup {} is not ready".format(backup_uuid))

    backup_disks = backup_service.disks_service().list()

    timestamp = time.strftime("%Y%m%d%H%M")
    for disk in backup_disks:
        download_incremental = incremental
        backup_mode = get_disk_backup_mode(connection, disk)
        if download_incremental and backup_mode != types.DiskBackupMode.INCREMENTAL:
            # if the disk wasn't a part of the previous checkpoint a full backup is taken
            progress("The backup that was taken for disk %r is %r" % (disk.id, backup_mode))
            download_incremental = False

        backup_type = "incremental" if download_incremental else "full"
        file_name = "{}.{}.{}.qcow2".format(disk.id, timestamp, backup_type)
        disk_path = os.path.join(args.backup_dir, file_name)
        download_disk(
            connection, backup_uuid, disk, disk_path, args, incremental=download_incremental)


def get_backup_service(connection, vm_uuid, backup_uuid):
    system_service = connection.system_service()
    vms_service = system_service.vms_service()
    backups_service = vms_service.vm_service(id=vm_uuid).backups_service()
    return backups_service.backup_service(id=backup_uuid)


def download_disk(connection, backup_uuid, disk, disk_path, args, incremental=False):
    progress("Creating image transfer for disk %r" % disk.id)
    transfer = imagetransfer.create_transfer(
        connection,
        disk,
        types.ImageTransferDirection.DOWNLOAD,
        backup=types.Backup(id=backup_uuid),
        timeout_policy=types.ImageTransferTimeoutPolicy(args.timeout_policy))
    try:
        progress("Image transfer %r is ready" % transfer.id)
        download_url = transfer.transfer_url

        extra_args = {}

        parameters = inspect.signature(client.download).parameters

        # Use multiple workers to speed up the download.
        if "max_workers" in parameters:
            extra_args["max_workers"] = args.max_workers

        # Use proxy_url if available. Download will use proxy_url if
        # transfer_url is not available.
        if "proxy_url" in parameters:
            extra_args["proxy_url"] = transfer.proxy_url

        with client.ProgressBar() as pb:
            client.download(
                download_url,
                disk_path,
                args.cafile,
                incremental=incremental,
                secure=args.secure,
                buffer_size=args.buffer_size,
                progress=pb,
                **extra_args)
    finally:
        progress("Finalizing image transfer")
        imagetransfer.finalize_transfer(connection, transfer, disk)


# General helpers

def get_vm_disks(connection, vm_id):
    system_service = connection.system_service()
    vm_service = system_service.vms_service().vm_service(id=vm_id)
    disk_attachments = vm_service.disk_attachments_service().list()

    disks = []
    for disk_attachment in disk_attachments:
        disk_id = disk_attachment.disk.id
        disk = system_service.disks_service().disk_service(disk_id).get()
        disks.append(disk)

    return disks


def get_backup_events(connection, search_id):
    events_service = connection.system_service().events_service()

    # Get the backup events arranged from the most recent event to the oldest
    return [dict(code=event.code, description=event.description)
            for event in events_service.list(search=str(search_id))]


def get_disk_backup_mode(connection, disk):
    system_service = connection.system_service()
    disk_info = system_service.disks_service().disk_service(disk.id).get()
    return disk_info.backup_mode


def verify_vm_exists(connection, vm_uuid):
    system_service = connection.system_service()
    vm_service = system_service.vms_service().vm_service(id=vm_uuid)
    try:
        vm_service.get()
    except sdk.NotFoundError:
        progress("VM %r does not exist" % vm_uuid)
        sys.exit(1)


def verify_backup_exists(connection, vm_uuid, backup_uuid):
    backup_service = get_backup_service(connection, vm_uuid, backup_uuid)
    try:
        backup_service.get()
    except sdk.NotFoundError:
        progress("Backup %r not found" % backup_uuid)
        sys.exit(1)


def get_backup(connection, backup_service, backup_uuid):
    try:
        return backup_service.get()
    except sdk.NotFoundError:
        failure_event = get_backup_events(connection, backup_uuid)[0]
        raise RuntimeError(
            "Backup {} failed: {}".format(backup_uuid, failure_event))


if __name__ == "__main__":
    main()
