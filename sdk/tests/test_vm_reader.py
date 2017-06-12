# -*- coding: utf-8 -*-

#
# Copyright (c) 2017 Red Hat, Inc.
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

import six

import ovirtsdk4.types as types

from io import BytesIO
from nose.tools import (
    assert_equals,
    assert_true,
)
from ovirtsdk4.readers import VmReader
from ovirtsdk4.xml import XmlReader


def make_buffer(text):
    """
    Creates an IO object to be used for writing.
    """
    if six.PY3:
        text = text.encode('utf-8')
    return BytesIO(text)


def test_reading_of_INHERITABLE_BOOLEAN_FALSE():
    """
    Test reading the InheritableBoolean enum false value.
    """
    reader = XmlReader(make_buffer(
        '<vm>'
        '<migration>'
        '<auto_converge>false</auto_converge>'
        '</migration>'
        '</vm>'
    ))
    result = VmReader.read_one(reader)
    reader.close()

    assert_true(isinstance(result, types.Vm))
    assert_equals(result.migration.auto_converge, types.InheritableBoolean.FALSE)



def test_reading_of_INHERITABLE_BOOLEAN_TRUE():
    """
    Test reading the InheritableBoolean enum true value.
    """
    reader = XmlReader(make_buffer(
        '<vm>'
        '<migration>'
        '<auto_converge>true</auto_converge>'
        '</migration>'
        '</vm>'
    ))
    result = VmReader.read_one(reader)
    reader.close()

    assert_true(isinstance(result, types.Vm))
    assert_equals(result.migration.auto_converge, types.InheritableBoolean.TRUE)

def test_reading_of_INHERITABLE_BOOLEAN_INHERIT():
    """
    Test reading the InheritableBoolean enum inherit value.
    """
    reader = XmlReader(make_buffer(
        '<vm>'
        '<migration>'
        '<auto_converge>inherit</auto_converge>'
        '</migration>'
        '</vm>'
    ))
    result = VmReader.read_one(reader)
    reader.close()

    assert_true(isinstance(result, types.Vm))
    assert_equals(result.migration.auto_converge, types.InheritableBoolean.INHERIT)

def test_reading_of_INHERITABLE_BOOLEAN_unsupported_value():
    """
    Test reading the InheritableBoolean enum unsupported value return None.
    """
    reader = XmlReader(make_buffer(
        '<vm>'
        '<migration>'
        '<auto_converge>ugly</auto_converge>'
        '</migration>'
        '</vm>'
    ))
    result = VmReader.read_one(reader)
    reader.close()

    assert_true(isinstance(result, types.Vm))
    assert_equals(result.migration.auto_converge, None)

def test_reading_name_with_accents():
    """
    Test that reading a VM that has a name with accents works correctly.
    """
    reader = XmlReader(make_buffer(
        '<vm>'
        '<name>áéíóúÁÉÍÓÚ</name>'
        '</vm>'
    ))
    result = VmReader.read_one(reader)
    reader.close()

    assert_true(isinstance(result, types.Vm))
    assert_equals(result.name, 'áéíóúÁÉÍÓÚ')
