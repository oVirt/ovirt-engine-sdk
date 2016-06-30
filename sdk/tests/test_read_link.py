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

import ovirtsdk4 as sdk
import ovirtsdk4.xml as xml
import ovirtsdk4.readers as readers
import ovirtsdk4.types as types

from io import BytesIO
from nose.tools import (
    assert_is_not_none,
    assert_is_none,
    assert_equals,
    assert_true,
)


def make_reader(text):
    """
    Creates an IO object that reads from the given text.
    """
    return xml.XmlReader(BytesIO(text.encode('utf-8')))


def test_link_href():
    """
    Checks that given an link the corresponding attribute is populate
    """
    reader = make_reader(
        '<vm>' +
          '<link rel="nics" href="/vms/123/nics"/>' +
        '</vm>'
    )
    result = readers.VmReader.read_one(reader)
    assert_is_not_none(result)
    assert_true(isinstance(result, types.Vm))
    assert_is_not_none(result.nics)
    assert_true(isinstance(result.nics, sdk.List))
    assert_equals(result.nics.href, '/vms/123/nics')


def test_element_after_link():
    """
    Check that another attribute after link is read correctly
    """
    reader = make_reader(
        '<vm>' +
          '<link rel="nics" href="/vms/123/nics"/>' +
          '<name>myvm</name>'
        '</vm>'
    )
    result = readers.VmReader.read_one(reader)
    assert_is_not_none(result)
    assert_true(isinstance(result, types.Vm))
    assert_equals(result.name, 'myvm')


def test_link_is_ignored_if_not_exists():
    """
    Check that the link is ignored if there is no such link
    """
    reader = make_reader(
        '<vm>' +
          '<link rel="junks" href="/junks"/>' +
        '</vm>'
    )
    result = readers.VmReader.read_one(reader)
    assert_is_not_none(result)
    assert_true(isinstance(result, types.Vm))
    assert_is_none(result.nics)


def test_link_is_ignored_if_no_rel():
    """
    Check that the link is ignored if there is no rel
    """
    reader = make_reader(
        '<vm>' +
          '<link href="/junks"/>' +
        '</vm>'
    )
    result = readers.VmReader.read_one(reader)
    assert_is_not_none(result)
    assert_true(isinstance(result, types.Vm))
    assert_is_none(result.nics)


def test_link_is_ignored_if_no_href():
    """
    Check that the link is ignored if there is no href
    """
    reader = make_reader(
        '<vm>' +
          '<link rel="nics"/>' +
        '</vm>'
    )
    result = readers.VmReader.read_one(reader)
    assert_is_not_none(result)
    assert_true(isinstance(result, types.Vm))
    assert_is_none(result.nics)



def test_multiple_links():
    """
    Check that the multiple links are read correctly
    """
    reader = make_reader(
        '<vm>' +
          '<link rel="nics" href="/vms/123/nics"/>' +
          '<link rel="cdroms" href="/vms/123/cdroms"/>' +
        '</vm>'
    )
    result = readers.VmReader.read_one(reader)
    assert_is_not_none(result)
    assert_true(isinstance(result, types.Vm))
    assert_is_not_none(result.nics)
    assert_true(isinstance(result.nics, sdk.List))
    assert_equals(result.nics.href, '/vms/123/nics')
    assert_is_not_none(result.cdroms)
    assert_true(isinstance(result.cdroms, sdk.List))
    assert_equals(result.cdroms.href, '/vms/123/cdroms')


def test_attribute_after_multiple_links():
    """
    Check when the multiple links, following attribute is populated correctly
    """
    reader = make_reader(
        '<vm>' +
          '<link rel="nics" href="/vms/123/nics"/>' +
          '<link rel="cdroms" href="/vms/123/cdroms"/>' +
          '<name>myvm</name>' +
        '</vm>'
    )
    result = readers.VmReader.read_one(reader)
    assert_is_not_none(result)
    assert_true(isinstance(result, types.Vm))
    assert_equals(result.name, 'myvm')