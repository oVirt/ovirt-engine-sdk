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

import io

from ovirtsdk4 import Error
from ovirtsdk4 import reader
from ovirtsdk4 import readers
from ovirtsdk4 import types
from ovirtsdk4 import xml


class Service(object):
    """
    This is the base class for all the services of the SDK. It contains the
    utility methods used by all of them.
    """

    def __init__(self, connection, path):
        """
        Creates a new service that will use the given connection and path.
        """
        self._connection = connection
        self._path = path

    @staticmethod
    def _raise_error(response, fault):
        """
        Creates and raises an error containing the details of the given HTTP
        response and fault.

        This method is intended for internal use by other components of the
        SDK. Refrain from using it directly, as backwards compatibility isn't
        guaranteed.
        """

        msg = ''
        if fault:
            if fault.reason:
                if msg:
                    msg += ' '
                msg = msg + 'Fault reason is "%s".' % fault.reason
            if fault.detail:
                if msg:
                    msg += ' '
                msg = msg + 'Fault detail is "%s".' % fault.detail
        if response:
            if response.code:
                if msg:
                    msg += ' '
                msg = msg + 'HTTP response code is %s.' % response.code
            if response.message:
                if msg:
                    msg += ' '
                msg = msg + 'HTTP response message is "%s".' % response.message
        raise Error(msg)

    @staticmethod
    def _check_fault(response):
        """
        Reads the response body assuming that it contains a fault message,
        converts it to an exception and raises it.

        This method is intended for internal use by other
        components of the SDK. Refrain from using it directly,
        as backwards compatibility isn't guaranteed.
        """

        buf = None
        xmlreader = None
        fault = None
        try:
            if response.body:
                buf = io.BytesIO(response.body)
                xmlreader = xml.XmlReader(buf)
                fault = readers.FaultReader.read_one(xmlreader)
        finally:
            if xmlreader is not None:
                xmlreader.close()
            if buf is not None:
                buf.close()
        if fault is not None:
            Service._raise_error(response, fault)

    @staticmethod
    def _check_action(response):
        """
        Reads the response body assuming that it contains an action, checks if
        it contains an fault, and if it does converts it to an exception and
        raises it.

        This method is intended for internal use by other
        components of the SDK. Refrain from using it directly,
        as backwards compatibility isn't guaranteed.
        """

        buf = None
        xmlreader = None
        result = None
        try:
            buf = io.BytesIO(response.body)
            xmlreader = xml.XmlReader(buf)
            result = reader.Reader.read(xmlreader)
        finally:
            if xmlreader is not None:
                xmlreader.close()
            if io is not None:
                buf.close()

        if result is not None:
            if isinstance(result, types.Fault):
                Service._raise_error(response, result)
            elif isinstance(result, types.Action) and result.fault is not None:
                Service._raise_error(response, result.fault)

        return result

    @staticmethod
    def _check_types(tuples):
        """
        Receives a list of tuples with three elements: the name of a
        parameter, its value and its expected type. For each tuple it
        checks that the value is either `None` or a valid value of
        the given types. If any of the checks fails, it raises an
        exception.

        This method is intended for internal use by other
        components of the SDK. Refrain from using it directly,
        as backwards compatibility isn't guaranteed.
        """

        messages = []
        for name, value, expected in tuples:
            if value is not None:
                actual = type(value)
                if actual != expected:
                    messages.append((
                        "The '{name}' parameter should be of type "
                        "'{expected}', but it is of type \'{actual}\'."
                    ).format(
                        name=name,
                        expected=expected.__name__,
                        actual=actual.__name__,
                    ))
        if len(messages) > 0:
            raise TypeError(' '.join(messages))
