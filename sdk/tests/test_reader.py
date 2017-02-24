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
    assert_is_none,
    assert_raises,
    assert_true,
    raises,
)
from ovirtsdk4 import Error
from ovirtsdk4 import types
from ovirtsdk4.reader import Reader, TZ
from ovirtsdk4.xml import XmlReader


def make_buffer(str):
    """
    Creates an IO object to be used for writing.
    """
    return BytesIO(str.encode('utf-8'))


def test_read_boolean_false():
    """
    Test given 'false' return False.
    """
    io_buffer = make_buffer('<value>false</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), False)


def test_read_boolean_FALSE():
    """
    Test given 'FALSE' return False.
    """
    io_buffer = make_buffer('<value>FALSE</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), False)


def test_read_boolean_0():
    """
    Test given '0' return False.
    """
    io_buffer = make_buffer('<value>0</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), False)


def test_read_boolean_true():
    """
    Test given 'true' return True.
    """
    io_buffer = make_buffer('<value>true</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), True)


def test_read_boolean_TRUE():
    """
    Test given 'TRUE' return True.
    """
    io_buffer = make_buffer('<value>TRUE</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), True)


def test_read_boolean_1():
    """
    Test given '1' return True.
    """
    io_buffer = make_buffer('<value>1</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_boolean(xml_reader), True)


@raises(ValueError)
def test_read_boolean_invalid_value():
    """
    Test given 'ugly' raises error.
    """
    io_buffer = make_buffer('<value>ugly</value>')
    xml_reader = XmlReader(io_buffer)
    Reader.read_boolean(xml_reader)


def test_read_booleans_empty_list_with_close_tag():
    """
    Test given no values with close tag returns empty list.
    """
    io_buffer = make_buffer('<list></list>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_booleans(xml_reader), [])


def test_read_booleans_empty_list_without_close_tag():
    """
    Test given no values without close tag returns empty list.
    """
    io_buffer = make_buffer('<list/>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_booleans(xml_reader), [])


def test_read_booleans_with_one_value():
    """
    Test given one value returns list containing one value.
    """
    io_buffer = make_buffer('<list><value>false</value></list>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_booleans(xml_reader), [False])


def test_read_booleans_with_two_values():
    """
    Test given two values returns list containing two values.
    """
    io_buffer = make_buffer(
        '<list><value>false</value><value>true</value></list>'
    )
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_booleans(xml_reader), [False, True])


def test_read_integer_with_valid_value():
    """
    Test given valid value returns that value.
    """
    io_buffer = make_buffer('<value>0</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_integer(xml_reader), 0)


@raises(ValueError)
def test_read_integer_with_invalid_value():
    """
    Test given invalid value raises error.
    """
    io_buffer = make_buffer('<value>ugly</value>')
    xml_reader = XmlReader(io_buffer)
    Reader.read_integer(xml_reader)


def test_read_integers_empty_list_with_close_tag():
    """
    Test given no values with close tag returns empty list.
    """
    io_buffer = make_buffer('<list></list>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_integers(xml_reader), [])


def test_read_integers_empty_list_without_close_tag():
    """
    Test given no values without close tag returns empty list.
    """
    io_buffer = make_buffer('<list/>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_integers(xml_reader), [])


def test_read_integers_with_one_value():
    """
    Test given one value returns list containing one value.
    """
    io_buffer = make_buffer('<list><value>0</value></list>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_integers(xml_reader), [0])


def test_read_integers_with_two_values():
    """
    Test given two values returns list containing two values.
    """
    io_buffer = make_buffer('<list><value>0</value><value>1</value></list>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_integers(xml_reader), [0, 1])


def test_read_decimal_with_valid_value():
    """
    Test given valid value returns that value.
    """
    io_buffer = make_buffer('<value>1.1</value>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_decimal(xml_reader), 1.1)


@raises(ValueError)
def test_read_decimal_with_invalid_value():
    """
    Test given invalid value raises error.
    """
    io_buffer = make_buffer('<value>ugly</value>')
    xml_reader = XmlReader(io_buffer)
    Reader.read_decimal(xml_reader)


def test_read_decimals_empty_list_with_close_tag():
    """
    Test given no values with close tag returns empty list.
    """
    io_buffer = make_buffer('<list></list>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_decimals(xml_reader), [])


def test_read_decimals_empty_list_without_close_tag():
    """
    Test given no values without close tag returns empty list.
    """
    io_buffer = make_buffer('<list/>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_decimals(xml_reader), [])


def test_read_decimals_with_one_value():
    """
    Test given one value returns list containing one value.
    """
    io_buffer = make_buffer('<list><value>1.1</value></list>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_decimals(xml_reader), [1.1])


def test_read_decimals_with_two_values():
    """
    Test given two values returns list containing two values.
    """
    io_buffer = make_buffer(
        '<list><value>1.1</value><value>2.2</value></list>'
    )
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_decimals(xml_reader), [1.1, 2.2])


def test_read_date_with_valid_value():
    """
    Test given valid value returns that value.
    """
    io_buffer = make_buffer('<value>2015-12-10T22:00:30+01:00</value>')
    xml_reader = XmlReader(io_buffer)
    date = datetime(2015, 12, 10, 22, 0, 30, tzinfo=TZ(60, None))
    assert_equals(Reader.read_date(xml_reader), date)


@raises(ValueError)
def test_read_date_with_invalid_value():
    """
    Test given invalid value raises error.
    """
    io_buffer = make_buffer('<value>ugly</value>')
    xml_reader = XmlReader(io_buffer)
    Reader.read_date(xml_reader)


def test_read_dates_empty_list_with_close_tag():
    """
    Test given no values with close tag returns empty list.
    """
    io_buffer = make_buffer('<list></list>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_dates(xml_reader), [])


def test_read_dates_empty_list_without_close_tag():
    """
    Test given no values without close tag returns empty list.
    """
    io_buffer = make_buffer('<list/>')
    xml_reader = XmlReader(io_buffer)
    assert_equals(Reader.read_dates(xml_reader), [])


def test_read_dates_with_one_value():
    """
    Test given one value returns list containing one value.
    """
    io_buffer = make_buffer(
        '<list><value>2015-12-10T22:00:30+01:00</value></list>'
    )
    xml_reader = XmlReader(io_buffer)
    date = datetime(2015, 12, 10, 22, 0, 30, tzinfo=TZ(60, None))
    assert_equals(Reader.read_dates(xml_reader), [date])


def test_read_dates_with_two_values():
    """
    Test given two values returns list containing two values.
    """
    io_buffer = make_buffer(
        '<list>'
        '<value>2015-12-10T22:00:30+01:00</value>'
        '<value>2016-12-10T22:00:30+01:00</value>'
        '</list>'
    )
    xml_reader = XmlReader(io_buffer)
    date1 = datetime(2015, 12, 10, 22, 0, 30, tzinfo=TZ(60, None))
    date2 = datetime(2016, 12, 10, 22, 0, 30, tzinfo=TZ(60, None))
    assert_equals(Reader.read_dates(xml_reader), [date1, date2])


def test_read_with_io():
    """
    Test if read method accepts io object.
    """
    Reader.read(make_buffer('<vm/>'))


def test_read_with_xml_reader():
    """
    Test if read method accepts xml reader.
    """
    cursor = XmlReader(make_buffer('<vm/>'))
    Reader.read(cursor)
    cursor.close()


def test_read_leaves_position():
    """
    Test if read method leaves it positioned in the next element.
    """
    cursor = XmlReader(make_buffer('<root><vm/><next/></root>'))
    cursor.read()
    Reader.read(cursor)
    assert_equals(cursor.node_name(), 'next')
    cursor.close()


@raises(AttributeError)
def test_read_given_incorrect_type():
    """
    Test if read give incorrect type, it raises exception.
    """
    Reader.read(0)


@raises(Exception)
def test_read_given_incorrect_reader():
    """
    Test if given incorrect input data, read method raises an exception.
    """
    Reader.read(make_buffer('<ugly/>'))


def test_read_given_vm():
    """
    Test if given vm, it creates VM object.
    """
    object = Reader.read(make_buffer('<vm/>'))
    assert_true(isinstance(object, types.Vm))


def test_read_given_two_vms():
    """
    Test if given two vms, it creates list of VMs.
    """
    vms = Reader.read(make_buffer('<vms><vm/><vm/></vms>'))
    assert_true(isinstance(vms, list))
    assert_equals(len(vms), 2)
    assert_true(isinstance(vms[0], types.Vm))
    assert_true(isinstance(vms[1], types.Vm))


def test_read_given_disk():
    """
    Test if given disk, it creates disk object.
    """
    disk = Reader.read(make_buffer('<disk/>'))
    assert_true(isinstance(disk, types.Disk))


def test_read_given_two_disks():
    """
    Test if given two disks, it creates list of Disks.
    """
    disks = Reader.read(make_buffer('<disks><disk/><disk/></disks>'))
    assert_true(isinstance(disks, list))
    assert_equals(len(disks), 2)
    assert_true(isinstance(disks[0], types.Disk))
    assert_true(isinstance(disks[1], types.Disk))


def test_read_given_openstack_image_provider():
    """
    Test if given Openstack image provider, it creates Openstack
    image provider object.
    """
    openstack_image_provider = Reader.read(
        make_buffer(
            '<openstack_image_provider>' +
                '<name>myprovider</name>' +
            '</openstack_image_provider>'
        )
    )
    assert_true(
        isinstance(openstack_image_provider, types.OpenStackImageProvider)
    )
    assert_equals(openstack_image_provider.name, "myprovider")


def test_read_given_two_openstack_image_providers():
    """
    Test if given two Openstack image provider, it creates list
    of Openstack image providers object.
    """
    openstack_image_providers = Reader.read(
        make_buffer(
            '<openstack_image_providers>' +
                '<openstack_image_provider/>' +
                '<openstack_image_provider/>' +
            '</openstack_image_providers>'
        )
    )
    assert_true(isinstance(openstack_image_providers, list))
    assert_equals(len(openstack_image_providers), 2)
    assert_true(isinstance(openstack_image_providers[0], types.OpenStackImageProvider))
    assert_true(isinstance(openstack_image_providers[1], types.OpenStackImageProvider))


def test_read_given_two_different_objects():
    """
    Test if given two different consecutive objects, they can be read with two calls.
    """
    cursor = XmlReader(make_buffer('<root><vm/><disk/></root>'))
    cursor.read()
    vm = Reader.read(cursor)
    disk = Reader.read(cursor)
    assert_true(isinstance(vm, types.Vm))
    assert_true(isinstance(disk, types.Disk))


def test_read_given_two_different_objects():
    """
    Test if given given an empty document, read returns None.
    """
    cursor = XmlReader(make_buffer('<root/>'))
    cursor.read()
    object = Reader.read(cursor)
    assert_is_none(object)


def test_read_unknonw_tag():
    """
    Test that when an unknonw tag is received an exception with a
    message is generated.
    """
    cursor = XmlReader(make_buffer('<html>blah<html>'))
    cursor.read()
    with assert_raises(Error) as context:
        Reader.read(cursor)
    assert_equals(str(context.exception), "Can't find a reader for tag 'html'")

def test_read_supports_strings():
    """
    Test that the generic `read` methods supports strings as parameters.
    """
    vm = Reader.read('<vm/>')
    assert_true(isinstance(vm, types.Vm))
