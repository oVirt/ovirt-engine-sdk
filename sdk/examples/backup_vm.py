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

Requires the ovirt-imageio-common package > 2.0.0.
"""

from __future__ import print_function

import argparse
import getpass
import logging
import os
import time

from contextlib import closing

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

from ovirt_imageio import client
from ovirt_imageio import ui

logging.basicConfig(level=logging.WARNING)

start_time = time.time()


def main():
    parser = argparse.ArgumentParser(description="Backup VM disks")
    subparsers = parser.add_subparsers(title="commands")

    full_parser = subparsers.add_parser(
        "full",
        help="Run full backup.")

    full_parser.set_defaults(command=cmd_full)

    add_common_args(full_parser)

    full_parser.add_argument(
        "vm_uuid",
        help="UUID of the VM to backup.")

    full_parser.add_argument(
        "--disk-uuid",
        action="append",
        help="Disk UUID to backup. May be used multiple times to backup "
             "multiple disks. If not specified, backup all vm disks."),

    full_parser.add_argument(
        "--backup-dir",
        default="./",
        help="Path to a directory to download backup disks"
             "to (default current directory)")

    start_parser = subparsers.add_parser(
        "start",
        help="Start VM backup.")

    start_parser.set_defaults(command=cmd_start)

    add_common_args(start_parser)

    start_parser.add_argument(
        "vm_uuid",
        help="UUID of the VM to backup.")

    start_parser.add_argument(
        "--disk-uuid",
        action="append",
        help="Disk UUID to backup. May be used multiple times to backup "
             "multiple disks. If not specified, backup all vm disks."),

    download_parser = subparsers.add_parser(
        "download",
        help="Download VM backup disk.")

    download_parser.set_defaults(command=cmd_download)

    add_common_args(download_parser)

    download_parser.add_argument(
        "--backup-dir",
        default="./",
        help="Path to a directory to download backup disks"
             "to (default current directory).")

    download_parser.add_argument(
        "vm_uuid",
        help="UUID of the VM for the backup.")

    download_parser.add_argument(
        "backup_uuid",
        help="UUID of the backup to finalize.")

    stop_parser = subparsers.add_parser(
        "stop",
        help="Stop VM backup.")

    stop_parser.set_defaults(command=cmd_stop)

    add_common_args(stop_parser)

    stop_parser.add_argument(
        "vm_uuid",
        help="UUID of the VM for the backup.")

    stop_parser.add_argument(
        "backup_uuid",
        help="UUID of the backup to finalize.")

    args = parser.parse_args()
    args.command(args)


# Commands

def cmd_full(args):
    """
    Run full backup flow - start, download and stop backup.
    """
    progress("Starting full backup for vm %s" % args.vm_uuid)

    connection = connect_engine(args)
    with closing(connection):
        backup = start_backup(connection, args)
        try:
            download_backup(connection, backup.id, args)
        finally:
            stop_backup(connection, backup.id, args)

    progress("Backup completed successfully")


def cmd_start(args):
    """
    Start backup, printing backup UUID.

    To download the backup run download command.
    To stop the backup run the stop command.
    """
    progress("Starting backup for vm %s" % args.vm_uuid)

    connection = connect_engine(args)

    with closing(connection):
        backup = start_backup(connection, args)

    progress("Backup %s is ready" % backup.id)


def cmd_download(args):
    """
    Download backup using the backup UUID printed by the start command.
    """
    progress("Downloading vm %s disks" % args.vm_uuid)

    connection = connect_engine(args)
    with closing(connection):
        download_backup(connection, args.backup_uuid, args)

    progress("Finished downloading disks")


def cmd_stop(args):
    """
    Stop backup using the backup UUID printed by the start command.
    """
    progress("Finalizing backup %s" % args.backup_uuid)

    connection = connect_engine(args)
    with closing(connection):
        stop_backup(connection, args.backup_uuid, args)

    progress("Backup %s has finalized" % args.backup_uuid)


# Argument parsing

def add_common_args(parser):
    parser.add_argument(
        "--engine-url",
        help="URL to the engine server (e.g. https://engine_fqdn:port)")

    parser.add_argument(
        "--username",
        help="username of engine API")

    parser.add_argument(
        "--password-file",
        help="password of engine API (if a file is not specified, read from standard input)")

    parser.add_argument(
        "-c", "--cafile",
        help="path to oVirt engine certificate for verifying server.")

    parser.add_argument(
        "--insecure",
        dest="secure",
        action="store_false",
        help=("do not verify server certificates and host name "
              "(not recommended)."))


# Backup helpers

def start_backup(connection, args):
    system_service = connection.system_service()
    vm_service = system_service.vms_service().vm_service(id=args.vm_uuid)
    backups_service = vm_service.backups_service()

    if args.disk_uuid:
        disks = [types.Disk(id=disk_id) for disk_id in args.disk_uuid]
    else:
        disks = get_vm_disks(connection, args.vm_uuid)

    backup = backups_service.add(
        types.Backup(
            disks=disks
        )
    )

    progress("Waiting until backup %s is ready" % backup.id)

    backup_service = backups_service.backup_service(backup.id)

    while backup.phase != types.BackupPhase.READY:
        time.sleep(1)
        try:
            backup = backup_service.get()
        except sdk.NotFoundError:
            raise RuntimeError("Backup {} failed".format(backup.id))

    return backup


def stop_backup(connection, backup_uuid, args):
    backup_service = get_backup_service(connection, args.vm_uuid, backup_uuid)

    backup_service.finalize()

    # TODO: Wait until backup is finalized.
    backup = backup_service.get()
    while backup.phase != types.BackupPhase.FINALIZING:
        time.sleep(1)
        backup = backup_service.get()


def download_backup(connection, backup_uuid, args):
    backup_service = get_backup_service(connection, args.vm_uuid, backup_uuid)

    try:
        backup = backup_service.get()
    except sdk.NotFoundError:
        raise RuntimeError("Backup {} not found".format(backup_uuid))

    if backup.phase != types.BackupPhase.READY:
        raise RuntimeError("Backup {} is not ready".format(backup_uuid))

    backup_disks = backup_service.disks_service().list()

    for disk in backup_disks:
        disk_path = os.path.join(args.backup_dir, disk.id + ".qcow2")
        download_disk(connection, backup_uuid, disk, disk_path, args)


def get_backup_service(connection, vm_uuid, backup_uuid):
    system_service = connection.system_service()
    vms_service = system_service.vms_service()
    backups_service = vms_service.vm_service(id=vm_uuid).backups_service()
    return backups_service.backup_service(id=backup_uuid)


def download_disk(connection, backup_uuid, disk, disk_path, args):
    transfer = create_transfer(connection, backup_uuid, disk)
    try:
        # We must use the daemon for downloading a backup disk.
        download_url = transfer.transfer_url
        with ui.ProgressBar() as pb:
            client.download(
                download_url,
                disk_path,
                args.cafile,
                secure=args.secure,
                progress=pb)
    finally:
        finalize_transfer(connection, transfer)


def create_transfer(connection, backup_uuid, disk):
    progress("Creating image transfer for disk %s" % disk.id)
    transfers_service = connection.system_service().image_transfers_service()

    transfer = transfers_service.add(
        types.ImageTransfer(
            disk=disk,
            # required for when downloading backup disks
            backup=types.Backup(id=backup_uuid),
            direction=types.ImageTransferDirection.DOWNLOAD,
            # required for when downloading backup disks
            format=types.DiskFormat.RAW,
        )
    )

    progress("Waiting until transfer %s will be ready" % transfer.id)

    transfer_service = transfers_service.image_transfer_service(transfer.id)

    while transfer.phase == types.ImageTransferPhase.INITIALIZING:
        time.sleep(1)
        transfer = transfer_service.get()

    progress("Image transfer %s is ready" % transfer.id)
    progress("Transfer url: %s" % transfer.transfer_url)

    return transfer


def finalize_transfer(connection, transfer):
    progress("Finalizing transfer %s" % transfer.id)
    transfers_service = connection.system_service().image_transfers_service()
    transfer_service = transfers_service.image_transfer_service(transfer.id)
    transfer_service.finalize()

    # TODO: Wait until transfer is finalized and handle failures.


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


# General helpers

def get_pass(args):
    if args.password_file:
        with open(args.password_file) as f:
            password = f.read().rstrip('\n')
    else:
        password = getpass.getpass()

    return password


def connect_engine(args):
    return sdk.Connection(
        url=args.engine_url + '/ovirt-engine/api',
        username=args.username,
        password=get_pass(args),
        ca_file=args.cafile,
        insecure=not args.secure,
    )


def progress(msg):
    print("[ %5.1f ] %s" % (time.time() - start_time, msg))


if __name__ == "__main__":
    main()
