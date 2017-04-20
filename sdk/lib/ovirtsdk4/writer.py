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

from ovirtsdk4 import Error
from ovirtsdk4 import xml


class Writer(object):
    """
    This is the base class for all the writers of the SDK. It contains
    the utility methods used by all of them.
    """

    def __init__(self):
        pass

    # This dictionary stores for each known type a reference to the
    # method that writes the XML document corresponding for that type.
    # For example, for the `Vm` type it will contain a reference to the
    # `VmWriter.write_one` method.
    _writers = {}

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

    @staticmethod
    def write_date(writer, name, value):
        """
        Writes an element with the given name and date value.
        """
        return writer.write_element(name, Writer.render_date(value))

    @classmethod
    def register(cls, typ, writer):
        """
        Registers a write method.

        `typ`:: The type.

        `writer`:: The reference to the method that writes the XML
        object corresponding to the type.
        """
        cls._writers[typ] = writer

    @classmethod
    def write(cls, obj, target=None, root=None, indent=False):
        """
        Writes one object, determining the writer method to use based on
        the type. For example, if the type of the object is `Vm` then it
        will write the `vm` tag, with its contents.

        `obj`:: The object to write.

        `target`:: The XML writer where the output will be written. If
        this parameter isn't given, or if the value is `None` the method
        will return a string containing the XML document.

        `root`:: The name of the root tag of the generated XML document.
        This isn't needed when writing single objects, as the tag is
        calculated from the type of the object. For example, if the
        object isa virtual machine then the tag will be `vm`. But when
        writing lists of objects the it is needed, because the list may
        be empty, or have different types of objects. In this case, for
        lists, if it isn't provided an exception will be raised.

        `indent`:: Indicates if the output should be indented, for
        easier reading by humans.
        """
        # If the target is `None` then create a temporary XML writer to
        # write the output:
        cursor = None
        if target is None:
            cursor = xml.XmlWriter(None, indent)
        elif type(target) == xml.XmlWriter:
            cursor = target
        else:
            raise Error(
                'Expected an \'XmlWriter\', but got \'%s\'' %
                type(target)
            )

        # Do the actual write, and make sure to always close the XML
        # writer if we created it:
        try:
            if type(obj) == list:
                # For lists we can't decide which tag to use, so the
                # 'root' parameter is mandatory in this case:
                if root is None:
                    raise Error(
                        'The \'root\' parameter is mandatory when '
                        'writing lists.'
                    )

                # Write the root tag, and then recursively call the
                # method to write each of the items of the list:
                cursor.write_start(root)
                for item in obj:
                    cls.write(item, target=cursor)
                cursor.write_end()
            else:
                # Select the specific writer according to the type:
                typ = type(obj)
                writer = cls._writers.get(typ)
                if writer is None:
                    raise Error(
                        'Can\'t find a writer for type \'%s\'' %
                        typ
                    )

                # Write the object using the specific method:
                writer(obj, cursor, root)

            # If no XML cursor was explicitly given, and we created it,
            # then we need to return the generated XML text:
            if target is None:
                return cursor.string()
        finally:
            if cursor is not None and cursor != target:
                cursor.close()
