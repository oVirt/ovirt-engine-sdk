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

import six

from io import BytesIO
from nose.tools import *
from ovirtsdk4.xml import XmlReader


def make_reader(text):
    """
    Creates an IO objec that reads from the given text.
    """
    if six.PY3:
        text = text.encode('utf-8')
    return XmlReader(BytesIO(text))


def test_get_attribute_with_value():
    """
    Checks that given an attribute with a value the `get_attribute`
    method returns the value.
    """
    reader = make_reader('<root id="123"/>')
    assert_equals(reader.get_attribute('id'), '123')


def test_get_empty_attribute():
    """
    Checks that given an empty attribute the `get_attribute` method
    returns an empty string.
    """
    reader = make_reader('<root id=""/>')
    assert_equals(reader.get_attribute('id'), '')


def test_get_non_existent_attribute():
    """
    Checks that given a non existing attribute the `get_attribute`
    method returns `None`.
    """
    reader = make_reader('<root/>')
    assert_equals(reader.get_attribute('id'), None)


def test_read_empty_element():
    """
    Checks that given an empty element the `read_element` method
    returns `None`.
    """
    reader = make_reader('<root/>')
    assert_equals(reader.read_element(), None)


def test_read_blank_element():
    """
    Checks that given an blank element the `read_element` method
    returns an empty string.
    """
    reader = make_reader('<root></root>')
    assert_equals(reader.read_element(), '')


def test_read_empty_list():
    """
    Checks that given an empty element the `read_elements` method
    returns an empty list.
    """
    reader = make_reader('<list></list>')
    assert_equals(reader.read_elements(), [])


def test_read_list_with_empty_element():
    """
    Checks that given a list with an empty element the `read_elements` method
    returns a list containing `None`.
    """
    reader = make_reader('<list><item/></list>')
    assert_equals(reader.read_elements(), [None])


def test_read_list_with_blank_element():
    """
    Checks that given a list with an blank element the `read_elements` method
    returns a list containing an empty string.
    """
    reader = make_reader('<list><item></item></list>')
    assert_equals(reader.read_elements(), [''])


def test_read_list_one_element():
    """
    Checks that given a list with an one element the `read_elements` method
    returns a list containing it.
    """
    reader = make_reader('<list><item>first</item></list>')
    assert_equals(reader.read_elements(), ['first'])


def test_read_list_two_element():
    """
    Checks that given a list with an two elements the `read_elements` method
    returns a list containing them.
    """
    reader = make_reader("""
        <list>
            <item>first</item>
            <item>second</item>
        </list>
    """)
    assert_equals(reader.read_elements(), ['first', 'second'])


def test_forward_with_preceding_test():
    """
    Checks that given some text before an element, the `forward` method
    skips the text and returns `True`.
    """
    reader = make_reader('<root>text<target/></root>')
    reader.read()
    assert_equals(reader.forward(), True)
    assert_equals(reader.node_name(), 'target')


def test_forward_end_of_document():
    """
    Checks that when positioned at the end of the document the `forward`
    method returns `False`.
    """
    reader = make_reader('<root/>')
    reader.read()
    assert_equals(reader.forward(), False)


def test_forward_with_empty_element():
    """
    Checks that when positioned at an empty element the `forward` method
    returns `True` and stays at the empty element.
    """
    reader = make_reader('<root><target/></root>')
    reader.read()
    assert_equals(reader.forward(), True)
    assert_equals(reader.node_name(), 'target')
    assert_equals(reader.empty_element(), True)


def test_read_element_after_empty_list():
    """
    Checks that given an empty list without a close element the
    `read_elements` method returns an empty list and the next element
    can be read with the `read_element` method.
    """
    reader = make_reader('<root><list/><value>next</value></root>')
    reader.read()
    assert_equals(reader.read_elements(), [])
    assert_equals(reader.read_element(), 'next')


def test_read_accents():
    """
    Checks that reading text that is already encoded using UTF-8
    works correctly.
    """
    reader = make_reader('<root>áéíóúÁÉÍÓÚ</root>')
    assert_equals(reader.read_element(), 'áéíóúÁÉÍÓÚ')
