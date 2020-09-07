#!/usr/bin/env python
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
Show how to compute an image checksum.

Requires ovirt-imageio-client >= 2.0.10-1
"""

import argparse
import json

from ovirt_imageio import client

parser = argparse.ArgumentParser(description="Compute image checksum")

parser.add_argument(
    "filename",
    help="path to disk image")

parser.add_argument(
    "--member",
    help="if filename is an OVA archive, the disk name in the OVA to "
         "checksum")

args = parser.parse_args()

checksum = client.checksum(args.filename, member=args.member)
print(json.dumps(checksum, indent=2))
