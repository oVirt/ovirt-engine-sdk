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
Helpeer functions and constnats for working with various units.
"""

KiB = 1024
MiB = 1024 * KiB
GiB = 1024 * MiB
TiB = 1024 * GiB
PiB = 1024 * TiB

_SUFFIXES = {"k": KiB, "m": MiB, "g": GiB, "t": TiB}


def humansize(s):
    """
    Convert human size (e.g. 2m) to bytes.

    Supports units in _SUFFIXES, case insensitive.
    """
    if s == "":
        raise ValueError("Invalid size: {!r}".format(s))

    unit = _SUFFIXES.get(s[-1].lower())
    if unit:
        return int(s[:-1]) * unit

    return int(s)
