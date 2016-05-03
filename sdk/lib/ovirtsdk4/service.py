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
from ovirtsdk4 import readers
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
        reader = None
        fault = None
        try:
            buf = io.BytesIO(response.body)
            reader = xml.XmlReader(buf)
            fault = readers.FaultReader.read_one(reader)
        finally:
            if reader is not None:
                reader.close()
            if io is not None:
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
        reader = None
        action = None
        try:
            buf = io.BytesIO(response.body)
            reader = xml.XmlReader(buf)
            action = readers.ActionReader.read_one(reader)
        finally:
            if reader is not None:
                reader.close()
            if io is not None:
                buf.close()
        if action is not None and action.fault is not None:
            Service._raise_error(response, action.fault)

        return action
