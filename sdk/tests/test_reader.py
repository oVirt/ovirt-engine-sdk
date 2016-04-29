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
from nose.tools import (
    assert_equals,
    raises,
)
from ovirtsdk4.xml import XmlReader
from ovirtsdk4.reader import Reader, TZ


def make_buffer(str):
    """
    Creates an IO object to be used for writing.
    """
    return BytesIO(str)


def test_read_boolean_false():
    """
    Test given 'false' return False
    """
    io_buffer = make_buffer('<value>false</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), False)


def test_read_boolean_FALSE():
    """
    Test given 'FALSE' return False
    """
    io_buffer = make_buffer('<value>FALSE</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), False)


def test_read_boolean_0():
    """
    Test given '0' return False
    """
    io_buffer = make_buffer('<value>0</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), False)


def test_read_boolean_true():
    """
    Test given 'true' return True
    """
    io_buffer = make_buffer('<value>true</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), True)


def test_read_boolean_TRUE():
    """
    Test given 'TRUE' return True
    """
    io_buffer = make_buffer('<value>TRUE</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), True)


def test_read_boolean_1():
    """
    Test given '1' return True
    """
    io_buffer = make_buffer('<value>1</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), True)


@raises(ValueError)
def test_read_boolean_invalid_value():
    """
    Test given 'ugly' raises error
    """
    io_buffer = make_buffer('<value>ugly</value>')
    xml_reader = XmlReader(io_buffer)
    Reader.read_boolean(xml_reader)


def test_read_booleans_empty_list_with_close_tag():
    """
    Test given no values with close tag returns empty list
    """
    io_buffer = make_buffer('<list></list>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_booleans(xml_reader), [])


def test_read_booleans_empty_list_without_close_tag():
    """
    Test given no values without close tag returns empty list
    """
    io_buffer = make_buffer('<list/>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_booleans(xml_reader), [])


def test_read_booleans_with_one_value():
    """
    Test given one value returns list containing one value
    """
    io_buffer = make_buffer('<list><value>false</value></list>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_booleans(xml_reader), [False])


def test_read_booleans_with_two_values():
    """
    Test given two values returns list containing two values
    """
    io_buffer = make_buffer(
        '<list><value>false</value><value>true</value></list>'
    )
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_booleans(xml_reader), [False, True])


def test_read_integer_with_valid_value():
    """
    Test given valid value returns that value
    """
    io_buffer = make_buffer('<value>0</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_integer(xml_reader), 0)


@raises(ValueError)
def test_read_integer_with_invalid_value():
    """
    Test given invalid value raises error
    """
    io_buffer = make_buffer('<value>ugly</value>')
    xml_reader = XmlReader(io_buffer)
    Reader.read_integer(xml_reader)


def test_read_integers_empty_list_with_close_tag():
    """
    Test given no values with close tag returns empty list
    """
    io_buffer = make_buffer('<list></list>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_integers(xml_reader), [])


def test_read_integers_empty_list_without_close_tag():
    """
    Test given no values without close tag returns empty list
    """
    io_buffer = make_buffer('<list/>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_integers(xml_reader), [])


def test_read_integers_with_one_value():
    """
    Test given one value returns list containing one value
    """
    io_buffer = make_buffer('<list><value>0</value></list>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_integers(xml_reader), [0])


def test_read_integers_with_two_values():
    """
    Test given two values returns list containing two values
    """
    io_buffer = make_buffer('<list><value>0</value><value>1</value></list>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_integers(xml_reader), [0, 1])


def test_read_decimal_with_valid_value():
    """
    Test given valid value returns that value
    """
    io_buffer = make_buffer('<value>1.1</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_decimal(xml_reader), 1.1)


@raises(ValueError)
def test_read_decimal_with_invalid_value():
    """
    Test given invalid value raises error
    """
    io_buffer = make_buffer('<value>ugly</value>')
    xml_reader = XmlReader(io_buffer)
    Reader.read_decimal(xml_reader)


def test_read_decimals_empty_list_with_close_tag():
    """
    Test given no values with close tag returns empty list
    """
    io_buffer = make_buffer('<list></list>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_decimals(xml_reader), [])


def test_read_decimals_empty_list_without_close_tag():
    """
    Test given no values without close tag returns empty list
    """
    io_buffer = make_buffer('<list/>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_decimals(xml_reader), [])


def test_read_decimals_with_one_value():
    """
    Test given one value returns list containing one value
    """
    io_buffer = make_buffer('<list><value>1.1</value></list>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_decimals(xml_reader), [1.1])


def test_read_decimals_with_two_values():
    """
    Test given two values returns list containing two values
    """
    io_buffer = make_buffer(
        '<list><value>1.1</value><value>2.2</value></list>'
    )
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_decimals(xml_reader), [1.1, 2.2])


def test_read_date_with_valid_value():
    """
    Test given valid value returns that value
    """
    io_buffer = make_buffer('<value>2015-12-10T22:00:30+01:00</value>')
    xml_reader = XmlReader(io_buffer)
    date = datetime(2015, 12, 10, 22, 0, 30, tzinfo=TZ(60, None))
    assert_equals(Reader.read_date(xml_reader), date)


@raises(ValueError)
def test_read_date_with_invalid_value():
    """
    Test given invalid value raises error
    """
    io_buffer = make_buffer('<value>ugly</value>')
    xml_reader = XmlReader(io_buffer)
    Reader.read_date(xml_reader)


def test_read_dates_empty_list_with_close_tag():
    """
    Test given no values with close tag returns empty list
    """
    io_buffer = make_buffer('<list></list>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_dates(xml_reader), [])


def test_read_dates_empty_list_without_close_tag():
    """
    Test given no values without close tag returns empty list
    """
    io_buffer = make_buffer('<list/>')
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    assert_equals(Reader.read_dates(xml_reader), [])


def test_read_dates_with_one_value():
    """
    Test given one value returns list containing one value
    """
    io_buffer = make_buffer(
        '<list><value>2015-12-10T22:00:30+01:00</value></list>'
    )
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    date = datetime(2015, 12, 10, 22, 0, 30, tzinfo=TZ(60, None))
    assert_equals(Reader.read_dates(xml_reader), [date])


def test_read_dates_with_two_values():
    """
    Test given two values returns list containing two values
    """
    io_buffer = make_buffer(
        '<list>'
        '<value>2015-12-10T22:00:30+01:00</value>'
        '<value>2016-12-10T22:00:30+01:00</value>'
        '</list>'
    )
    xml_reader = XmlReader(io_buffer)
    xml_reader.read()
    date1 = datetime(2015, 12, 10, 22, 0, 30, tzinfo=TZ(60, None))
    date2 = datetime(2016, 12, 10, 22, 0, 30, tzinfo=TZ(60, None))
    assert_equals(Reader.read_dates(xml_reader), [date1, date2])
