# -*- coding: utf-8 -*-

#
# Copyright (c) 2016 Red Hat, Inc.
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

import ovirtsdk4.types as types

from io import BytesIO
from nose.tools import (
    assert_equals,
    assert_is_none,
    assert_true,
)
from ovirtsdk4.writers import NetworkWriter
from ovirtsdk4.xml import XmlWriter


def make_buffer():
    """
    Creates an IO object to be used for writing.
    """
    return BytesIO()


def decode_buffer(io_buffer):
    """
    Extracts the text stored in the given bytes buffer and generates an
    Unicode string.
    """
    return io_buffer.getvalue().decode('utf-8')


def test_write_network_with_no_usages():
    """
    Test given network with usages attribute set to None,
    the usages isn't written to output xml
    """
    network = types.Network()
    buf = make_buffer()
    writer = XmlWriter(buf, indent=True)
    NetworkWriter.write_one(network, writer)
    writer.flush()
    assert_equals(decode_buffer(buf), '<network/>\n')


def test_write_network_with_empty_usages():
    """
    Test given network with usages attribute set empty list,
    the usages empty element is written to output xml
    """
    network = types.Network(
        usages=[],
    )
    buf = make_buffer()
    writer = XmlWriter(buf, indent=True)
    NetworkWriter.write_one(network, writer)
    writer.flush()
    assert_equals(
        decode_buffer(buf),
        '<network>\n' +
        '  <usages/>\n' +
        '</network>\n'
    )


def test_write_network_with_one_usages():
    """
    Test given network with usages attribute set list with one value,
    the usages element with one value is written to output xml
    """
    network = types.Network(
        usages=[
            types.NetworkUsage.VM
        ],
    )
    buf = make_buffer()
    writer = XmlWriter(buf, indent=True)
    NetworkWriter.write_one(network, writer)
    writer.flush()
    assert_equals(
        decode_buffer(buf),
        '<network>\n' +
        '  <usages>\n' +
        '    <usage>vm</usage>\n' +
        '  </usages>\n' +
        '</network>\n'
    )


def test_write_network_with_two_usages():
    """
    Test given network with usages attribute set list with one value,
    the usages element with one value is written to output xml
    """
    network = types.Network(
        usages=[
            types.NetworkUsage.VM,
            types.NetworkUsage.DISPLAY,
        ],
    )
    buf = make_buffer()
    writer = XmlWriter(buf, indent=True)
    NetworkWriter.write_one(network, writer)
    writer.flush()
    assert_equals(
        decode_buffer(buf),
        '<network>\n' +
        '  <usages>\n' +
        '    <usage>vm</usage>\n' +
        '    <usage>display</usage>\n' +
        '  </usages>\n' +
        '</network>\n'
    )
