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

Require ovirt-imageio-client >= 2.0.9-1
"""

import os
import lxml.etree
import tarfile
import time

from contextlib import closing

from ovirt_imageio import client

from ovirtsdk4 import types

from helpers import imagetransfer
from helpers import common
from helpers.common import progress


def parse_args():
    parser = common.ArgumentParser(description="Upload disk from OVA")

    # Image options.

    parser.add_argument(
        "ova_file",
        help="Path to OVA file.")

    parser.add_argument(
        "--sd-name",
        required=True,
        help="Name of the storage domain.")

    parser.add_argument(
        "--disk-format",
        choices=("raw", "qcow2"),
        help="Format of the created disk (default image format).")

    parser.add_argument(
        "--enable-backup",
        action="store_true",
        help="Creates a disk that can be used for incremental backup. "
             "Allowed for qcow2 format only.")

    parser.add_argument(
        "--cluster-name",
        required=True,
        help="Name of the cluster.")

    parser.add_argument(
        "--template",
        action="store_true",
        help="Create template or Virtual Machine from an ova file.")


    return parser.parse_args()


def get_disk_info(args, image_info, disk_name, disk_sparse):
    disk_info = {
        "provisioned_size": image_info["virtual-size"],
        "initial_size": None,
        "backup": types.DiskBackup.INCREMENTAL if args.enable_backup else None
    }

    disk_format = image_info["format"]

    # Convert qemu format names to oVirt constants ("raw", "cow").
    if disk_format == "raw":
        disk_info["format"] = types.DiskFormat.RAW
    elif disk_format == "qcow2":
        disk_info["format"] = types.DiskFormat.COW
    else:
        print("Invalid or unsupported disk format %s found in the ovf file..." % disk_format)
        raise

    # Create disk name from image name and disk format.
    basename = os.path.splitext(os.path.basename(disk_name))[0]
    disk_info["name"] = "{}.{}".format(basename, disk_format)

    # The initial size is needed only when creating sparse qcow2 image on block
    # storage. On file storage the initial size is ignored.
    if disk_sparse and disk_format == "qcow2":
        measure = client.measure(
            args.ova_file, disk_format, member=disk_name)
        disk_info["initial_size"] = measure["required"]

    return disk_info


def create_disk(connection, args, disk_info, disk_id, disk_sparse):
    disks_service = connection.system_service().disks_service()

    disk = disks_service.add(
        types.Disk(
            name=disk_info["name"],
            id=disk_id,
            content_type=types.DiskContentType.DATA,
            description='Uploaded from {} by upload_ova_as_template.py'.format(
                os.path.basename(args.ova_file)),
            format=disk_info["format"],
            initial_size=disk_info["initial_size"],
            provisioned_size=disk_info["provisioned_size"],
            sparse=disk_sparse,
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
common.configure_logging(args)

connection = common.create_connection(args)
with closing(connection):
    # Try use local host for optimizing transfer.
    host = imagetransfer.find_host(connection, args.sd_name)

    # Open the OVA file:
    with tarfile.open(args.ova_file) as ova_file:
        # Read the entries within the OVA file
        ova_entries = ova_file.getmembers()

        # Read the OVF configuration from the OVA file (must be the first entry
        # inside the tar file):
        ovf_str = ova_file.extractfile(ova_entries[0]).read()
        # Parse the OVF as XML document:
        ovf = lxml.etree.fromstring(ovf_str)

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

            disk_id=props['diskId']

            disk_sparse = props['volume-type'] == 'Sparse'

            # Find the disk entry among the OVA entries
            disk_entry = ova_file.getmember(props['fileRef'])

            progress("Checking image...")

            image_info = client.info(args.ova_file, member=disk_entry.name)
            disk_info = get_disk_info(args, image_info, disk_entry.name, disk_sparse)

            progress("Image format: {}".format(image_info["format"]))
            progress("Disk name: {}".format(disk_info["name"]))
            progress("Disk format: {}".format(disk_info["format"]))
            progress("Disk provisioned size: {}".format(disk_info["provisioned_size"]))
            progress("Disk initial size: {}".format(disk_info["initial_size"]))
            progress("Disk backup: {}".format(disk_info["backup"]))

            progress("Creating disk...")
            disk = create_disk(connection, args, disk_info, disk_id, disk_sparse)
            progress("Disk ID: {}".format(disk.id))
            progress("Creating image transfer...")
            transfer = imagetransfer.create_transfer(
                connection, disk, types.ImageTransferDirection.UPLOAD, host=host)
            try:
                progress("Transfer ID: {}".format(transfer.id))
                progress("Transfer host name: {}".format(transfer.host.name))

                progress("Uploading disk {} from {}...".format(
                    disk_entry.name, os.path.basename(args.ova_file)))

                with client.ProgressBar() as pb:
                    client.upload(
                        args.ova_file,
                        transfer.transfer_url,
                        args.cafile,
                        secure=args.secure,
                        progress=pb,
                        proxy_url=transfer.proxy_url,
                        member=disk_entry.name)
            except Exception:
                progress("Upload failed, cancelling image transfer...")
                imagetransfer.cancel_transfer(connection, transfer)
                raise

            progress("Finalizing image transfer...")
            imagetransfer.finalize_transfer(connection, transfer, disk)

        progress("Upload completed successfully")

        # Find the name of the entity within the OVF:
        vm_or_template_name = ovf.xpath(
            '/ovf:Envelope/ovf:VirtualSystem/ovf:Name',
            namespaces=namespaces
        )[0].text

        # Add the virtual machine or template, the transferred disks will be attached to
        # this virtual machine or template:
        progress("Adding {} {}".format('template' if args.template else 'virtual machine',
            vm_or_template_name))

        if args.template:
            templates_service = connection.system_service().templates_service()
            template = templates_service.add(
                types.Template(
                    cluster=types.Cluster(
                        name=args.cluster_name,
                    ),
                    initialization=types.Initialization(
                        configuration=types.Configuration(
                            type=types.ConfigurationType.OVA,
                            data=ovf_str.decode("utf-8")
                        )
                    ),
                ),
            )
        else:
            vms_service = connection.system_service().vms_service()
            vm = vms_service.add(
                types.Vm(
                    cluster=types.Cluster(
                        name=args.cluster_name,
                    ),
                    initialization=types.Initialization(
                        configuration=types.Configuration(
                            type=types.ConfigurationType.OVA,
                            data=ovf_str.decode("utf-8")
                        )
                    ),
                ),
            )
