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

from ovirtsdk4 import AuthError
from ovirtsdk4 import Error
from ovirtsdk4 import NotFoundError
from ovirtsdk4 import http
from ovirtsdk4 import reader
from ovirtsdk4 import types
from ovirtsdk4 import writer


class Future(object):
    """
    Instances of this class are returned for operations that specify the
    `wait=False` parameter.
    """
    def __init__(self, connection, context, code):
        """
        Creates a new future result.

        `connection`:: The connection to be used by this future.
        `context`:: The request that this future will wait for when the `wait`
        method is called.
        `code`:: The function that will be executed to check the response, and
        to convert its body into the right type of object.
        """
        self._connection = connection
        self._context = context
        self._code = code

    def wait(self):
        """
        Waits till the result of the operation that created this future is
        available.
        """
        response = self._connection.wait(self._context)
        return self._code(response)


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
    def _raise_error(response, detail=None):
        """
        Creates and raises an error containing the details of the given HTTP
        response and fault.

        This method is intended for internal use by other components of the
        SDK. Refrain from using it directly, as backwards compatibility isn't
        guaranteed.
        """
        fault = detail if isinstance(detail, types.Fault) else None

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

        if isinstance(detail, six.string_types):
            if msg:
                msg += ' '
            msg = msg + detail + '.'

        class_ = Error
        if response is not None:
            if response.code in [401, 403]:
                class_ = AuthError
            elif response.code == 404:
                class_ = NotFoundError

        error = class_(msg)
        error.code = response.code if response else None
        error.fault = fault
        raise error

    def _check_fault(self, response):
        """
        Reads the response body assuming that it contains a fault message,
        converts it to an exception and raises it.

        This method is intended for internal use by other
        components of the SDK. Refrain from using it directly,
        as backwards compatibility isn't guaranteed.
        """

        body = self._internal_read_body(response)
        if isinstance(body, types.Fault):
            self._raise_error(response, body)
        elif isinstance(body, types.Action) and body.fault:
            self._raise_error(response, body.fault)
        raise Error("Expected a fault, but got %s" % type(body).__name__)

    def _check_action(self, response):
        """
        Reads the response body assuming that it contains an action, checks if
        it contains an fault, and if it does converts it to an exception and
        raises it.

        This method is intended for internal use by other
        components of the SDK. Refrain from using it directly,
        as backwards compatibility isn't guaranteed.
        """

        body = self._internal_read_body(response)
        if isinstance(body, types.Fault):
            self._raise_error(response, body)
        elif isinstance(body, types.Action) and body.fault is not None:
            self._raise_error(response, body.fault)
        elif isinstance(body, types.Action):
            return body
        else:
            raise Error(
                "Expected a fault or action, but got %s" % (
                    type(body).__name__
                )
            )
        return body

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

    def _internal_get(self, headers=None, query=None, wait=None):
        """
        Executes an `get` method.
        """
        # Populate the headers:
        headers = headers or {}

        # Send the request:
        request = http.Request(method='GET', path=self._path, query=query, headers=headers)
        context = self._connection.send(request)

        def callback(response):
            if response.code in [200]:
                return self._internal_read_body(response)
            else:
                self._check_fault(response)

        future = Future(self._connection, context, callback)
        return future.wait() if wait else future

    def _internal_add(self, object, headers=None, query=None, wait=None):
        """
        Executes an `add` method.
        """
        # Populate the headers:
        headers = headers or {}

        # Send the request and wait for the response:
        request = http.Request(method='POST', path=self._path, query=query, headers=headers)
        request.body = writer.Writer.write(object, indent=True)
        context = self._connection.send(request)

        def callback(response):
            if response.code in [200, 201, 202]:
                return self._internal_read_body(response)
            else:
                self._check_fault(response)

        future = Future(self._connection, context, callback)
        return future.wait() if wait else future

    def _internal_update(self, object, headers=None, query=None, wait=None):
        """
        Executes an `update` method.
        """
        # Populate the headers:
        headers = headers or {}

        # Send the request and wait for the response:
        request = http.Request(method='PUT', path=self._path, query=query, headers=headers)
        request.body = writer.Writer.write(object, indent=True)
        context = self._connection.send(request)

        def callback(response):
            if response.code in [200]:
                return self._internal_read_body(response)
            else:
                self._check_fault(response)

        future = Future(self._connection, context, callback)
        return future.wait() if wait else future

    def _internal_remove(self, headers=None, query=None, wait=None):
        """
        Executes an `remove` method.
        """
        # Populate the headers:
        headers = headers or {}

        # Send the request and wait for the response:
        request = http.Request(method='DELETE', path=self._path, query=query, headers=headers)
        context = self._connection.send(request)

        def callback(response):
            if response.code not in [200]:
                self._check_fault(response)

        future = Future(self._connection, context, callback)
        return future.wait() if wait else future

    def _internal_action(self, action, path, member=None, headers=None, query=None, wait=None):
        """
        Executes an action method.
        """
        # Populate the headers:
        headers = headers or {}

        # Send the request and wait for the response:
        request = http.Request(
            method='POST',
            path='%s/%s' % (self._path, path),
            query=query,
            headers=headers,
        )
        request.body = writer.Writer.write(action, indent=True)
        context = self._connection.send(request)

        def callback(response):
            if response.code in [200, 201, 202]:
                result = self._check_action(response)
                if member:
                    return getattr(result, member)
            else:
                self._check_fault(response)

        future = Future(self._connection, context, callback)
        return future.wait() if wait else future

    def _internal_read_body(self, response):
        """
        Checks the content type of the given response, and if it is XML, as
        expected, reads the body and converts it to an object. If it isn't
        XML, then it raises an exception.

        `response`:: The HTTP response to check.
        """
        # First check if the response body is empty, as it makes no sense to check the content type if there is
        # no body:
        if not response.body:
            self._raise_error(response)

        # Check the content type, as otherwise the parsing will fail, and the resulting error message won't be explicit
        # about the cause of the problem:
        self._connection.check_xml_content_type(response)

        # Parse the XML and generate the SDK object:
        return reader.Reader.read(response.body)
