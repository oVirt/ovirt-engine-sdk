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
Cancel a paused transfer that was started using the API.
"""

import argparse
import logging

from contextlib import closing

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

from helpers import imagetransfer


def parse_args():
    parser = argparse.ArgumentParser(description="Cancel paused transfer")

    # Common options.

    parser.add_argument(
        "--engine-url",
        required=True,
        help="transfer URL (e.g. https://engine_fqdn:port)")

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

    # Script options.

    parser.add_argument(
        "transfer_id",
        help="transfer UUID to cancel")

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


args = parse_args()

logging.basicConfig(
    level=logging.DEBUG if args.debug else logging.INFO,
    filename="example.log",
    format="%(asctime)s %(levelname)-7s (%(threadName)s) [%(name)s] %(message)s"
)

connection = create_connection(args)
with closing(connection):
    imagetransfer.cancel_transfer(
        connection, types.ImageTransfer(id=args.transfer_id))
    print("Transfer cancelled")
