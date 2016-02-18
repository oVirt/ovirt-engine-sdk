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
import re

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
            date = datetime.datetime.strptime(text, format)
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
