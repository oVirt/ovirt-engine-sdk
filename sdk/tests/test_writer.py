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
from ovirtsdk4.xml import XmlWriter
from ovirtsdk4.writer import Writer


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
