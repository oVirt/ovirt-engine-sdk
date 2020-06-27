#!/usr/bin/python3
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
Upload disk from OVA file.

Require ovirt-imageio-client >= 2.0.9
"""

import argparse
import getpass
import logging
import os
import time

from contextlib import closing

from ovirt_imageio import client

import ovirtsdk4 as sdk
import ovirtsdk4.types as types
from helpers import imagetransfer


def parse_args():
    parser = argparse.ArgumentParser(description="Upload disk from OVA")

    # Common options.

    parser.add_argument(
        "--engine-url",
        required=True,
        help="oVirt engine URL (e.g. https://engine_fqdn:port)")

    parser.add_argument(
        "--username",
        required=True,
        help="username of engine API")

    parser.add_argument(
        "--password-file",
        help="file containing password of the specified by user (if file is "
             "not specified, read from standard input)")

    parser.add_argument(
        "-c", "--cafile",
        help="path to oVirt engine certificate for verifying server.")

    parser.add_argument(
        "--insecure",
        dest="secure",
        action="store_false",
        default=False,
        help=("do not verify server certificates and host name (not "
              "recommended)."))

    parser.add_argument(
        "--debug",
        action="store_true",
        help="log debug level messages to example.log")

    # Image options.

    parser.add_argument(
        "ova_file",
        help="path to OVA file")

    parser.add_argument(
        "--ova-disk-name",
        required=True,
        help="name of the disk in the OVA file")

    # Disk options.

    parser.add_argument(
        "--sd-name",
        required=True,
        help="name of the storage domain.")

    parser.add_argument(
        "--disk-format",
        choices=("raw", "qcow2"),
        help="format of the created disk (default image format)")

    parser.add_argument(
        "--disk-sparse",
        action="store_true",
        help="create sparse disk (raw sparse not supported on block storage)")

    parser.add_argument(
        "--enable-backup",
        action="store_true",
        help="creates a disk that can be used for incremental backup. "
             "Allowed for disk with qcow2 format only")

    return parser.parse_args()


def read_password(args):
    if args.password_file:
        with open(args.password_file) as f:
            # ovirt doesn't support empty lines in password
            return f.read().rstrip('\n')
    else:
        return getpass.getpass()


def create_connection(args):
    return sdk.Connection(
        url=args.engine_url + '/ovirt-engine/api',
        username=args.username,
        password=read_password(args),
        ca_file=args.cafile,
        debug=args.debug,
        log=logging.getLogger(),
    )


def get_disk_info(args, image_info):
    disk_info = {
        "provisioned_size": image_info["virtual-size"],
        "initial_size": None,
        "backup": types.DiskBackup.INCREMENTAL if args.enable_backup else None
    }

    disk_format = args.disk_format or image_info["format"]

    # Convert qemu format names to oVirt constants ("raw", "cow").
    if disk_format == "raw":
        disk_info["format"] = types.DiskFormat.RAW
    elif disk_format == "qcow2":
        disk_info["format"] = types.DiskFormat.COW

    # Create disk name from image name and disk format.
    basename = os.path.splitext(os.path.basename(args.ova_disk_name))[0]
    disk_info["name"] = "{}.{}".format(basename, disk_format)

    # The initial size is needed only when creating sparse qcow2 image on block
    # storage. On file storage the initial size is ignored.
    if args.disk_sparse and disk_format == "qcow2":
        measure = client.measure(
            args.ova_file, disk_format, member=args.ova_disk_name)
        disk_info["initial_size"] = measure["required"]

    return disk_info


def create_disk(connection, args, disk_info):
    disks_service = connection.system_service().disks_service()

    disk = disks_service.add(
        types.Disk(
            name=disk_info["name"],
            content_type=types.DiskContentType.DATA,
            description='Uploaded from {} by upload_from_ova.py'.format(
                os.path.basename(args.ova_file)),
            format=disk_info["format"],
            initial_size=disk_info["initial_size"],
            provisioned_size=disk_info["provisioned_size"],
            sparse=args.disk_sparse,
            backup=disk_info["backup"],
            storage_domains=[
                types.StorageDomain(name=args.sd_name)
            ]
        )
    )

    # Wait till the disk is OK, as the transfer can't start if the disk is
    # locked.
    disk_service = disks_service.disk_service(disk.id)
    while True:
        time.sleep(1)
        disk = disk_service.get()
        if disk.status == types.DiskStatus.OK:
            break

    return disk


args = parse_args()

logging.basicConfig(
    level=logging.DEBUG if args.debug else logging.INFO,
    filename="example.log",
    format=("%(asctime)s %(levelname)-7s (%(threadName)s) [%(name)s] "
            "%(message)s")
)

print("Checking image...")

image_info = client.info(args.ova_file, member=args.ova_disk_name)
disk_info = get_disk_info(args, image_info)

print("Image format: {}".format(image_info["format"]))
print("Disk name: {}".format(disk_info["name"]))
print("Disk format: {}".format(disk_info["format"]))
print("Disk provisioned size: {}".format(disk_info["provisioned_size"]))
print("Disk initial size: {}".format(disk_info["initial_size"]))
print("Disk backup: {}".format(disk_info["backup"]))

connection = create_connection(args)
with closing(connection):
    print("Creating disk...")
    disk = create_disk(connection, args, disk_info)
    print("Disk ID: {}".format(disk.id))

    # Try use local host for optimizing transfer.
    host = imagetransfer.find_host(connection, args.sd_name)

    print("Creating image transfer...")
    transfer = imagetransfer.create_transfer(
        connection, disk, types.ImageTransferDirection.UPLOAD, host=host)
    try:
        print("Transfer ID: {}".format(transfer.id))
        print("Transfer host name: {}".format(transfer.host.name))

        print("Uploading disk {} from {}...".format(
            args.ova_disk_name, os.path.basename(args.ova_file)))

        with client.ProgressBar() as pb:
            client.upload(
                args.ova_file,
                transfer.transfer_url,
                args.cafile,
                secure=args.secure,
                progress=pb,
                proxy_url=transfer.proxy_url,
                member=args.ova_disk_name)
    except Exception:
        print("Upload failed, cancelling image transfer...")
        imagetransfer.cancel_transfer(connection, transfer)
        raise

    print("Finalizing image transfer...")
    imagetransfer.finalize_transfer(connection, transfer, disk)

    print("Upload completed successfully")
