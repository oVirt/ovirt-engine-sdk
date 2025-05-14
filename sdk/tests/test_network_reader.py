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
from ovirtsdk4.readers import NetworkReader
from ovirtsdk4.xml import XmlReader


def make_buffer(str):
    """
    Creates an IO object to be used for writing.
    """
    return BytesIO(str.encode('utf-8'))


def test_network_with_no_usages():
    """
    Test given network with no usages element, the usages attribute is None.
    """
    reader = XmlReader(make_buffer('<network/>'))
    result = NetworkReader.read_one(reader)
    reader.close()

    assert result.usages is None


def test_network_with_empty_usages():
    """
    Test given network with empty usages element, the usages attribute is empty list.
    """
    reader = XmlReader(make_buffer('<network><usages/></network>'))
    result = NetworkReader.read_one(reader)
    reader.close()

    assert isinstance(result.usages, list)
    assert len(result.usages) == 0


def test_network_with_one_usages():
    """
    Test given network with no usages element, the usages attribute is None.
    """
    reader = XmlReader(
        make_buffer(
            '<network><usages><usage>vm</usage></usages></network>'
        )
    )
    result = NetworkReader.read_one(reader)
    reader.close()

    assert isinstance(result.usages, list)
    assert len(result.usages) == 1
    assert result.usages[0] == types.NetworkUsage.VM


def test_network_with_two_usages():
    """
    Test given network with no usages element, the usages attribute is None.
    """
    reader = XmlReader(
        make_buffer(
            '<network>'
                '<usages>'
                    '<usage>vm</usage>'
                    '<usage>display</usage>'
                '</usages>'
            '</network>'
        )
    )
    result = NetworkReader.read_one(reader)
    reader.close()

    assert isinstance(result.usages, list)
    assert len(result.usages) == 2
    assert result.usages[0] == types.NetworkUsage.VM
    assert result.usages[1] == types.NetworkUsage.DISPLAY


def test_unsupported_usage_dont_raise_exception():
    """
    Test when given network with unsupported usage element,
    it don't raise exception.
    """
    reader = XmlReader(
        make_buffer(
            '<network>'
                '<usages>'
                    '<usage>ugly</usage>'
                    '<usage>display</usage>'
                '</usages>'
            '</network>'
        )
    )
    result = NetworkReader.read_one(reader)
    reader.close()

    assert isinstance(result.usages, list)
    assert len(result.usages) == 2
    assert result.usages[0] is None
    assert result.usages[1] == types.NetworkUsage.DISPLAY
