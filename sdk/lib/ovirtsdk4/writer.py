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


class Writer(object):
    """
    This is the base class for all the writers of the SDK. It contains
    the utility methods used by all of them.
    """

    def __init__(self):
        pass

    @staticmethod
    def write_string(writer, name, value):
        """
        Writes an element with the given name and string value.
        """
        return writer.write_element(name, value)

    @staticmethod
    def render_boolean(value):
        """
        Converts the given boolean value to a string.
        """
        if type(value) != bool:
            raise TypeError('The \'value\' parameter must be a boolean')
        return 'true' if value else 'false'

    @staticmethod
    def write_boolean(writer, name, value):
        """
        Writes an element with the given name and boolean value.
        """
        return writer.write_element(name, Writer.render_boolean(value))

    @staticmethod
    def render_integer(value):
        """
        Converts the given integer value to a string.
        """
        if type(value) != int:
            raise TypeError('The \'value\' parameter must be an integer')
        return str(value)

    @staticmethod
    def write_integer(writer, name, value):
        """
        Writes an element with the given name and integer value.
        """
        return writer.write_element(name, Writer.render_integer(value))

    @staticmethod
    def render_decimal(value):
        """
        Converts the given decimal value to a string.
        """
        if type(value) != float:
            raise TypeError('The \'value\' parameter must be a decimal')
        return str(value)

    @staticmethod
    def write_decimal(writer, name, value):
        """
        Writes an element with the given name and decimal value.
        """
        return writer.write_element(name, Writer.render_decimal(value))

    @staticmethod
    def render_date(value):
        """
        Converts the given date value to a string.
        """
        if type(value) != datetime.datetime:
            raise TypeError('The \'value\' parameter must be a date')
        return value.isoformat()
