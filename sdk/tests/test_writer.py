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

from datetime import datetime
from io import BytesIO
from nose.tools import *
from ovirtsdk4 import Error
from ovirtsdk4 import types
from ovirtsdk4.writer import Writer
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


def test_write_string():
    """
    Checks that given an name and a value the `write_string` method
    generates the expected XML text.
    """
    io_buffer = make_buffer()
    xml_writer = XmlWriter(io_buffer)
    Writer.write_string(xml_writer, 'value', 'myvalue')
    xml_writer.flush()
    assert_equals(decode_buffer(io_buffer), '<value>myvalue</value>')


def test_write_boolean_true():
    """
    Checks that given the value `True` the `write_boolean` method generates
    the expected XML text.
    """
    io_buffer = make_buffer()
    xml_writer = XmlWriter(io_buffer)
    Writer.write_boolean(xml_writer, 'value', True)
    xml_writer.flush()
    assert_equals(decode_buffer(io_buffer), '<value>true</value>')


def test_write_boolean_false():
    """
    Checks that given the value `False` the `write_boolean` method generates
    the expected XML text.
    """
    io_buffer = make_buffer()
    xml_writer = XmlWriter(io_buffer)
    Writer.write_boolean(xml_writer, 'value', False)
    xml_writer.flush()
    assert_equals(decode_buffer(io_buffer), '<value>false</value>')


def test_write_integer_0():
    """
    Checks that given the value `0` the `write_integer` method generates
    the expected XML text.
    """
    io_buffer = make_buffer()
    xml_writer = XmlWriter(io_buffer)
    Writer.write_integer(xml_writer, 'value', 0)
    xml_writer.flush()
    assert_equals(decode_buffer(io_buffer), '<value>0</value>')


def test_write_integer_1():
    """
    Checks that given the value `0` the `write_integer` method generates
    the expected XML text.
    """
    io_buffer = make_buffer()
    xml_writer = XmlWriter(io_buffer)
    Writer.write_integer(xml_writer, 'value', 1)
    xml_writer.flush()
    assert_equals(decode_buffer(io_buffer), '<value>1</value>')

def test_write_does_not_require_xml_writer():
    """
    Checks that the generic `write` method doesn't require an XML writer
    paramater.
    """
    vm = types.Vm()
    result = Writer.write(vm)
    assert_equals(result, '<vm/>')

def test_write_uses_alternative_root_tag():
    """
    Checks that the generic `write` method uses the alternative root tag
    if provided.
    """
    vm = types.Vm()
    result = Writer.write(vm, root='list')
    assert_equals(result, '<list/>')

def test_write_accepts_xml_writer():
    """
    Checks that the generic `write` method accepts an XML writer as
    parameter.
    """
    vm = types.Vm()
    writer = XmlWriter(None)
    result = Writer.write(vm, target=writer)
    text = writer.string()
    writer.close()
    assert_is_none(result)
    assert_equals(text, '<vm/>')

def test_write_raises_exception_if_given_list_and_no_root():
    """
    Checks that the generic `write` method raises an exception if it is
    given a list and no root tag.
    """
    with assert_raises(Error) as context:
        Writer.write([])
    assert_regexp_matches(str(context.exception), "root.*mandatory")

def test_write_accepts_empty_lists():
    """
    Checks that the generic `write` method accepts empty lists.
    """
    result = Writer.write([], root='list')
    assert_equals(result, '<list/>')

def test_write_accepts_list_with_one_element():
    """
    Checks that the generic `write` method accets lists with one
    element.
    """
    vm = types.Vm()
    result = Writer.write([vm], root='list')
    assert_equals(result, '<list><vm/></list>')

def test_write_accepts_list_with_two_elements():
    """
    Checks that the generic `write` method accets lists with two
    elements.
    """
    vm = types.Vm()
    result = Writer.write([vm, vm], root='list')
    assert_equals(result, '<list><vm/><vm/></list>')

def test_write_accepts_elements_of_different_types():
    """
    Checks that the generic `write` method accets lists containing
    elements of different types.
    """
    vm = types.Vm()
    disk = types.Disk()
    result = Writer.write([vm, disk], root='list')
    assert_equals(result, '<list><vm/><disk/></list>')
