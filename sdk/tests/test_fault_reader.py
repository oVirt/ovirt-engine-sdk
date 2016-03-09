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

from io import BytesIO
from nose.tools import *
from ovirtsdk4 import types
from ovirtsdk4 import readers
from ovirtsdk4.xml import XmlReader


def make_reader(text):
    """
    Creates an IO objec that reads from the given text.
    """
    return XmlReader(BytesIO(text.encode('utf-8')))


def test_read_one_with_empty_xml():
    """
    Checks that given an empty XML element the `read_one` method creates
    creates the expected fault.
    """
    reader = make_reader('<fault/>')
    result = readers.FaultReader.read_one(reader)
    reader.close()
    assert_is_not_none(result)
    assert_is(type(result), types.Fault)
    assert_is_none(result.reason)
    assert_is_none(result.detail)


def test_read_one_with_reason_only():
    """
    Checks that given an an XML with only the reason element the
    `read_one` method creates creates the expected fault.
    """
    reader = make_reader('<fault><reason>myreason</reason></fault>')
    result = readers.FaultReader.read_one(reader)
    reader.close()
    assert_is_not_none(result)
    assert_is(type(result), types.Fault)
    assert_equals(result.reason, 'myreason')
    assert_is_none(result.detail)


def test_read_one_with_detail_only():
    """
    Checks that given an an XML with only the detail element the
    `read_one` method creates creates the expected fault.
    """
    reader = make_reader('<fault><detail>mydetail</detail></fault>')
    result = readers.FaultReader.read_one(reader)
    reader.close()
    assert_is_not_none(result)
    assert_is(type(result), types.Fault)
    assert_is_none(result.reason)
    assert_equals(result.detail, 'mydetail')


def test_read_one_with_reason_and_detail():
    """
    Checks that given an an XML with only the reason and deetail
    elements `read_one` method creates creates the expected fault.
    """
    reader = make_reader("""
        <fault>
            <reason>myreason</reason>
            <detail>mydetail</detail>
        </fault>
    """)
    result = readers.FaultReader.read_one(reader)
    reader.close()
    assert_is_not_none(result)
    assert_is(type(result), types.Fault)
    assert_equals(result.reason, 'myreason')
    assert_equals(result.detail, 'mydetail')

