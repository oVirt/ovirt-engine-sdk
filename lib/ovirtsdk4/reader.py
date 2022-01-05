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

import datetime
import time
import io
import re
import six

from ovirtsdk4 import Error
from ovirtsdk4 import xml


# Regular expression used to check if the representation of a date contains a
# time zone offset:
TZ_OFFSET_RE = re.compile(
    r'(?P<sign>[+-])(?P<hours>\d{2}):(?P<minutes>\d{2}$)'
)

# Regular expression used to check if the representation of the date contains
# the number of microseconds:
TZ_USEC_RE = re.compile(
    r'\.\d+$'
)


class TZ(datetime.tzinfo):
    """
    This is a simple implementation of the `tzinfo` class, that contains a
    fixed offset.
    """

    def __init__(self, minutes, name):
        super(TZ, self).__init__()
        self._delta = datetime.timedelta(minutes=minutes)
        self._name = name

    def dst(self, date_time):
        return None

    def tzname(self, date_time):
        return self._name

    def utcoffset(self, date_time):
        return self._delta


class Reader(object):
    """
    This is the base class for all the readers of the SDK. It contains
    the utility methods used by all of them.
    """

    # This dictionary stores for each known tag a reference to the method
    # that read the object corresponding for that tag. For example, for the
    # `vm` tag it will contain a reference to the `VmReader.read_one` method,
    # and for the `vms` tag it will contain a reference to the
    # `VmReader.read_many` method.
    _readers = {}

    def __init__(self):
        pass

    @staticmethod
    def read_string(reader):
        """
        Reads a string value, assuming that the cursor is positioned at the
        start element that contains the value.
        """
        return reader.read_element()

    @staticmethod
    def read_strings(reader):
        """
        Reads a list of string values, assuming that the cursor is positioned
        at the start element of the element that contains the first value.
        """
        return reader.read_elements()

    @staticmethod
    def parse_boolean(text):
        """
        Converts the given text to a boolean value.
        """
        if text is None:
            return None
        text = text.lower()
        if text == 'false' or text == '0':
            return False
        if text == 'true' or text == '1':
            return True
        raise ValueError('The text \'%s\' isn\'t a valid boolean value' % text)

    @staticmethod
    def read_boolean(reader):
        """
        Reads a boolean value, assuming that the cursor is positioned at the
        start element that contains the value.
        """
        return Reader.parse_boolean(reader.read_element())

    @staticmethod
    def read_booleans(reader):
        """
        Reads a list of boolean values, assuming that the cursor is positioned
        at the start element of the element that contains the first value.
        """
        return list(map(Reader.parse_boolean, reader.read_elements()))

    @staticmethod
    def parse_integer(text):
        """
        Converts the given text to an integer value.
        """
        if text is None:
            return None
        try:
            return int(text)
        except ValueError:
            raise ValueError(
                'The text \'%s\' isn\'t a valid integer value' % text
            )

    @staticmethod
    def read_integer(reader):
        """
        Reads an integer value, assuming that the cursor is positioned at the
        start element that contains the value.
        """
        return Reader.parse_integer(reader.read_element())

    @staticmethod
    def read_integers(reader):
        """
        Reads a list of integer values, assuming that the cursor is positioned
        at the start element of the element that contains the first value.
        """
        return list(map(Reader.parse_integer, reader.read_elements()))

    @staticmethod
    def parse_decimal(text):
        """
        Converts the given text to a decimal value.
        """
        if text is None:
            return None
        try:
            return float(text)
        except ValueError:
            raise ValueError(
                'The text \'%s\' isn\'t a valid decimal value' % text
            )

    @staticmethod
    def read_decimal(reader):
        """
        Reads a decimal value, assuming that the cursor is positioned at the
        start element that contains the value.
        """
        return Reader.parse_decimal(reader.read_element())

    @staticmethod
    def read_decimals(reader):
        """
        Reads a list of decimal values, assuming that the cursor is positioned
        at the start element of the element that contains the first value.
        """
        return list(map(Reader.parse_decimal, reader.read_elements()))

    @staticmethod
    def parse_date(text):
        """
        Converts the given text to a date value.
        """

        # Check the text has a value:
        if text is None:
            return None

        # Extract the time zone:
        tz = None
        if text[-1] == 'Z':
            tz = TZ(0, 'UTC')
            text = text[:-1]
        else:
            match = TZ_OFFSET_RE.search(text)
            if match:
                name = match.group(0)
                sign = match.group('sign')
                hours = int(match.group('hours'))
                minutes = int(match.group('minutes'))
                offset = hours * 60 + minutes
                if sign == '-':
                    offset *= -1
                tz = TZ(offset, name)
                text = text[:-len(name)]

        # Parse the rest of the date:
        format = '%Y-%m-%dT%H:%M:%S'
        if TZ_USEC_RE.search(text):
            format += '.%f'
        try:
            try:
                date = datetime.datetime.strptime(text, format)
            except TypeError:
                # when have TypeError: attribute of type 'NoneType'
                #  workaround to treat a issue of python module: https://bugs.python.org/issue27400
                date = datetime.datetime.fromtimestamp(time.mktime(time.strptime(text, format)))
        except ValueError:
            raise ValueError(
                'The text \'%s\' isn\'t a valid date value' % text
            )

        # Set the time zone:
        if tz is not None:
            date = date.replace(tzinfo=tz)

        return date

    @staticmethod
    def read_date(reader):
        """
        Reads a date value, assuming that the cursor is positioned at the
        start element that contains the value.
        """
        return Reader.parse_date(reader.read_element())

    @staticmethod
    def read_dates(reader):
        """
        Reads a list of date values, assuming that the cursor is positioned
        at the start element of the element that contains the first value.
        """
        return list(map(Reader.parse_date, reader.read_elements()))

    @staticmethod
    def parse_enum(enum_type, text):
        """
        Converts the given text to an enum.
        """
        if text is None:
            return None
        try:
            return enum_type(text)
        except ValueError:
            return None

    @staticmethod
    def read_enum(enum_type, reader):
        """
        Reads a enum value, assuming that the cursor is positioned at the
        start element that contains the value.
        """
        return Reader.parse_enum(enum_type, reader.read_element())

    @staticmethod
    def read_enums(enum_type, reader):
        """
        Reads a list of enum values, assuming that the cursor is positioned
        at the start element of the element that contains the first value.
        """
        return [
            Reader.parse_enum(enum_type, e) for e in reader.read_elements()
        ]

    @classmethod
    def register(cls, tag, reader):
        """
        Registers a read method.

        :param tag: The tag name.
        :param reader: The reference to the method that reads the object corresponding to the `tag`.
        """
        cls._readers[tag] = reader

    @classmethod
    def read(cls, source):
        """
        Reads one object, determining the reader method to use based on the
        tag name of the first element. For example, if the first tag name
        is `vm` then it will create a `Vm` object, if it the tag is `vms`
        it will create an array of `Vm` objects, so on.

        :param source: The string, IO or XML reader where the input will be taken from.
        """
        # If the source is a string or IO object then create a XML reader from it:
        cursor = None
        if isinstance(source, str):
            # In Python 3 str is a list of 16 bits characters, so it
            # needs to be converted to an array of bytes, using UTF-8,
            # before trying to parse it.
            if six.PY3:
                source = source.encode('utf-8')
            cursor = xml.XmlReader(io.BytesIO(source))
        elif isinstance(source, bytes):
            cursor = xml.XmlReader(io.BytesIO(source))
        elif isinstance(source, io.BytesIO):
            cursor = xml.XmlReader(source)
        elif isinstance(source, xml.XmlReader):
            cursor = source
        else:
            raise AttributeError(
                "Expected a 'str', 'BytesIO' or 'XmlReader', but got '{source}'".format(
                    source=type(source)
                )
            )

        try:
            # Do nothing if there aren't more tags:
            if not cursor.forward():
                return None

            # Select the specific reader according to the tag:
            tag = cursor.node_name()
            reader = cls._readers.get(tag)
            if reader is None:
                raise Error(
                    "Can't find a reader for tag '{tag}'".format(tag=tag)
                )

            # Read the object using the specific reader:
            return reader(cursor)
        finally:
            if cursor is not None and cursor != source:
                cursor.close()
