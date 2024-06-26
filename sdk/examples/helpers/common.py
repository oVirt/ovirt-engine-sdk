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
Engine connection helper for SDK examples, such as parsing command line arguments
and create connection to engine server.
"""

import argparse
import configparser
import getpass
import logging
import os
import time

import ovirtsdk4 as sdk


class ArgumentParser:

    def __init__(self, **kwargs):
        self._parser = argparse.ArgumentParser(**kwargs)

        self._parser.add_argument(
            "-c", "--config",
            required=True,
            help="Use engine connection details from [CONFIG] section in "
                 "~/.config/ovirt.conf.")

        self._parser.add_argument(
            "--debug",
            action="store_true",
            help="Log debug level messages to logfile.")

        self._parser.add_argument(
            "--logfile",
            default="example.log",
            help="Log file name (default example.log).")

    def add_argument(self, *args, **kwargs):
        self._parser.add_argument(*args, **kwargs)

    def add_subparsers(self, *args, **kwargs):
        return self._parser.add_subparsers(*args, **kwargs)

    def parse_args(self):
        args = self._parser.parse_args()

        config = configparser.ConfigParser(interpolation=None)
        config.read([os.path.expanduser("~/.config/ovirt.conf")])

        # Required options.

        args.engine_url = config.get(args.config, "engine_url")
        args.username = config.get(args.config, "username")

        # Optional options.

        if config.has_option(args.config, "secure"):
            args.secure = config.getboolean(args.config, "secure")
        else:
            args.secure = True

        if config.has_option(args.config, "cafile"):
            args.cafile = config.get(args.config, "cafile")
        else:
            args.cafile = ""

        if config.has_option(args.config, "password"):
            args.password = config.get(args.config, "password")
        else:
            args.password = getpass.getpass()

        return args


def create_connection(args):
    """
    Usage:
        connection = common.create_connection(args)
        with closing(connection):
            # use the connection. It will be closed when
            # exiting this block.
    """
    return sdk.Connection(
        url=args.engine_url + '/ovirt-engine/api',
        username=args.username,
        password=args.password,
        ca_file=args.cafile,
        debug=args.debug,
        log=logging.getLogger(),
    )


def progress(msg, start_time=time.monotonic()):
    print("[ %5.1f ] %s" % (time.monotonic() - start_time, msg))


def configure_logging(args):
    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        filename=args.logfile,
        format="%(asctime)s %(levelname)-7s (%(threadName)s) [%(name)s] %(message)s")
