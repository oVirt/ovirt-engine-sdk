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
import os
import pycurl
import sys
import threading

try:
    from urllib.parse import quote_plus, urlencode, urlparse
except ImportError:
    from urllib import quote_plus, urlencode
    from urlparse import urlparse

from ovirtsdk4 import version


class Request(object):
    """
    This class represents an HTTP request.

    This class is intended for internal use by other components of the SDK.
    Refrain from using it directly as there is no backwards compatibility
    guarantee.
    """

    def __init__(self,
        method='GET',
        path='',
        matrix=None,
        query=None,
        headers=None,
        body=None,
    ):
        self.method = method
        self.path = path
        self.matrix = matrix if matrix is not None else {}
        self.query = query if query is not None else {}
        self.headers = headers if headers is not None else {}
        self.body = body


class Response(object):
    """
    This class represents an HTTP response.

    This class is intended for internal use by other components of the SDK.
    Refrain from using it directly as there is no backwards compatibility
    guarantee.
    """

    def __init__(
        self,
        body=None,
        code=None,
        headers=None,
        message=None
    ):
        self.body = body
        self.code = code
        self.headers = headers if headers is not None else {}
        self.message = message


class Connection(object):
    """
    This class is responsible for managing an HTTP connection to the engine
    server. It is intended as the entry point for the SDK, and it provides
    access to the `system` service and, from there, to the rest of the
    services provided by the API.
    """

    def __init__(
        self,
        url=None,
        username=None,
        password=None,
        insecure=False,
        ca_file=None,
        debug=False,
        log=None,
        kerberos=False,
        timeout=0,
    ):
        """
        Creates a new connection to the API server.

        This method supports the following parameters:

        `url`:: A string containing the base URL of the server, usually
        something like `https://server.example.com/ovirt-engine/api`.

        `username`:: The name of the user, something like `admin@internal`.

        `password`:: The name password of the user.

        `insecure`:: A boolean flag that indicates if the server TLS
        certificate and host name should be checked.

        `ca_file`:: A PEM file containing the trusted CA certificates. The
        certificate presented by the server will be verified using these CA
        certificates.

        `debug`:: A boolean flag indicating if debug output should be
        generated. If the values is `True` all the data sent to and received
        from the server will be written to `stdout`. Be aware that user names
        and passwords will also be written, so handle it with care.

        `log`:: The log file where the debug output will be written. The
        value can be a string contaiing a file name or an IO object. If
        it is a filename then the file will be created if it doesn't
        exist, and the debug output will be added to the end. The file
        will be closed when the connection is closed. If it is an IO
        object then the debug output will be written directly, and it
        won't be closed.

        `kerberos`:: A boolean flag indicating if Kerberos
        authentication should be used instead of the default basic
        authentication.

        `timeout`:: The maximum total time to wait for the response, in
        seconds. A value of zero (the default) means wait for ever. If
        the timeout expires before the response is received an exception
        will be raised.
        """

        # Check mandatory parameters:
        if url is None:
            raise Exception('The \'url\' parameter is mandatory')
        if not insecure and ca_file is None:
            raise Exception('The \'ca_file\' is mandatory in secure mode')

        # Check that the CA file exists:
        if ca_file is not None and not os.path.exists(ca_file):
            raise Exception('The CA file \'%s\' doesn\'t exist' % ca_file)

        # Save the URL:
        self._url = url

        # Save the credentials:
        self._username = username
        self._password = password
        self._kerberos = kerberos

        # The curl object can be used by several threads, but not
        # simultaneously, so we need a lock to prevent that:
        self._curl_lock = threading.Lock()

        # Create the curl handle that manages the pool of connections:
        self._curl = pycurl.Curl()
        self._curl.setopt(pycurl.COOKIEFILE, '/dev/null')
        self._curl.setopt(pycurl.COOKIEJAR, '/dev/null')

        # Configure TLS parameters:
        if url.startswith('https'):
            self._curl.setopt(pycurl.SSL_VERIFYPEER, 0 if insecure else 1)
            self._curl.setopt(pycurl.SSL_VERIFYHOST, 0 if insecure else 2)
            if ca_file is not None:
                self._curl.setopt(pycurl.CAINFO, ca_file)

        # Configure timeouts:
        self._curl.setopt(pycurl.TIMEOUT, timeout)

        # Configure debug mode:
        self._close_log = False
        if debug:
            if log is None:
                self._log = sys.stdout
            elif type(log) == str:
                self._log = open(log, 'a')
                self._close_log = True
            else:
                self._log = log
            self._curl.setopt(pycurl.VERBOSE, 1)
            self._curl.setopt(pycurl.DEBUGFUNCTION, self._curl_debug)

        # Initialize the reference to the system service:
        self.__system_service = None

    def send(self, request, last=False):
        """
        Sends an HTTP request and waits for the response.

        This method is intended for internal use by other components of the
        SDK. Refrain from using it directly, as backwards compatibility isn't
        guaranteed.

        This method supports the following parameters.

        `request`:: The Request object containing the details of the HTTP
        request to send.

        `last`:: A boolean flag indicating if this is the last request.

        The returned value is a Request object containing the details of the
        HTTP response received.
        """

        with self._curl_lock:
            return self.__send(request, last)

    def __send(self, request, last=False):
        # Set the method:
        self._curl.setopt(pycurl.CUSTOMREQUEST, request.method)

        # Build the URL:
        url = self._build_url(
            path=request.path,
            query=request.query,
            matrix=request.matrix,
        )
        self._curl.setopt(pycurl.URL, url)

        # Basic credentials should be sent only if there isn't a session:
        if self._kerberos:
            self._curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_GSSNEGOTIATE)
            self._curl.setopt(pycurl.USERPWD, ':')
        else:
            authorization = '%s:%s' % (self._username, self._password)
            self._curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
            self._curl.setopt(pycurl.USERPWD, authorization)

        # Add headers, avoiding those that have no value:
        header_lines = []
        for header_name, header_value in request.headers.items():
            if header_value is not None:
                header_lines.append('%s: %s' % (header_name, header_value))
        header_lines.append('User-Agent: PythonSDK/%s' % version.VERSION)
        header_lines.append('Version: 4')
        header_lines.append('Content-Type: application/xml')
        header_lines.append('Accept: application/xml')

        # Every request except the last one should indicate that we prefer
        # to use persistent authentication:
        if not last:
            header_lines.append('Prefer: persistent-auth')

        # Copy headers and the request body to the curl object:
        self._curl.setopt(pycurl.HTTPHEADER, header_lines)
        body = request.body
        if body is None:
            body = ''
        self._curl.setopt(pycurl.POSTFIELDS, body)

        # Prepare the buffers to receive the response:
        body_buf = io.BytesIO()
        headers_buf = io.BytesIO()
        self._curl.setopt(pycurl.WRITEFUNCTION, body_buf.write)
        self._curl.setopt(pycurl.HEADERFUNCTION, headers_buf.write)

        # Send the request and wait for the response:
        self._curl.perform()

        # Extract the response code and body:
        response = Response()
        response.code = self._curl.getinfo(pycurl.HTTP_CODE)
        response.body = body_buf.getvalue()

        # The response code can be extracted directly, but cURL doesn't
        # have a method to extract the response message, so we have to
        # parse the first header line to find it:
        response.reason = ""
        headers_text = headers_buf.getvalue().decode('ascii')
        header_lines = headers_text.split('\n')
        if len(header_lines) >= 1:
            response_line = header_lines[0]
            response_fields = response_line.split()
            if len(response_fields) >= 3:
                response.reason = ' '.join(response_fields[2:])

        # Return the response:
        return response

    @property
    def url(self):
        """
        Returns a string containing the base URL used by this connection.
        """

        return self._url

    def system_service(self):
        """
        Returns the reference to the root of the services tree.

        The returned value is an instance of the `SystemService` class.
        """

        if self.__system_service is None:
            from ovirtsdk4.services import SystemService
            self.__system_service = SystemService(self, '')
        return self.__system_service

    def service(self, path):
        """
        Returns a reference to the service corresponding to the given
        path. For example, if the `path` parameter is `vms/123/disks`
        then it will return a reference to the service that manages the
        disks for the virtual machine with identifier `123`.

        If there is no service corresponding to the given path an exception
        will be raised.
        """

        return self.system_service().service(path)

    def test(self, raise_exception=False):
        """
        Tests the connectivity with the server. If connectivity works
        correctly it returns `True`. If there is any connectivy problem
        it will either return `False` or raise an exception if the
        `raise_exception` parameter is `True`.
        """

        try:
            self.system_service().get()
            return True
        except Exception as exception:
            if raise_exception:
                raise exception
            return False

    def is_link(self, obj):
        """
        Indicates if the given object is a link. An object is a link if
        it has an `href` attribute.
        """

        return obj.href is not None

    def follow_link(self, obj):
        """
        Follows the `href` attribute of this object, retrieves the object
        and returns it.
        """

        # Check that the "href" attribute has a values, as it is needed
        # in order to retrieve the representation of the object:
        href = obj.href
        if href is None:
            raise Exception(
                "Can't follow link because the 'href' attribute does't " +
                "have a value"
            )

        # Check that the value of the "href" attribute is compatible with the
        # base URL of the connection:
        prefix = urlparse(self._url).path
        if not prefix.endswith('/'):
            prefix += '/'
        if not href.startswith(prefix):
            raise Exception(
                "The URL '%s' isn't compatible with the base URL of the " +
                "connection" % href
            )

        # Remove the prefix from the URL, follow the path to the relevant
        # service and invoke the "get" method to retrieve its representation:
        path = href[len(prefix):]
        service = self.service(path)
        return service.get()

    def close(self):
        """
        Releases the resources used by this connection.
        """

        # Send the last request to indicate the server that the session should
        # be closed:
        request = Request(method='GET')
        self.send(request, last=True)

        # Close the log file, if we did open it:
        if self._close_log:
            self._log.close()

        # Release resources used by the cURL handle:
        with self._curl_lock:
            self._curl.close()

    def _build_url(self, path='', query=None, matrix=None):
        """
        Builds a request URL from a path, and the sets of matrix and query
        parameters.

        This method is intended for internal use by other components of the
        SDK. Refrain from using it directly, as backwards compatibility isn't
        guaranteed.

        This method supports the following parameters:

        `path`:: The path that will be added to the base URL. The default is an
        empty string.

        `query`:: A dictionary containing the query parameters to add to the
        URL. The keys of the dictionary should be strings containing the names
        of the parameters, and the values should be strings containing the
        values.

        `matrix`:: A dictionary containing the matrix parameters to add to the
        URL. The keys of the dictionary should be strings containing the names
        of the parameters, and the values should be strings containing the
        values.

        The returned value is an string containing the URL.
        """

        # Add the path and the parameters:
        url = '%s%s' % (self._url, path)
        if matrix:
            for key, value in matrix.items():
                url = '%s;%s=%s' % (url, key, quote_plus(value))
        if query:
            url = '%s?%s' % (url, urlencode(query))
        return url

    def _curl_debug(self, debug_type, debug_message):
        """
        This is the implementation of the cURL debug callback.
        """

        prefix = '* '
        if debug_type == pycurl.INFOTYPE_DATA_IN:
            prefix = '< '
        elif debug_type == pycurl.INFOTYPE_DATA_OUT:
            prefix = '> '
        elif debug_type == pycurl.INFOTYPE_HEADER_IN:
            prefix = '< '
        elif debug_type == pycurl.INFOTYPE_HEADER_OUT:
            prefix = '> '
        lines = debug_message.replace('\r\n', '\n').strip().split('\n')
        for line in lines:
            self._log.write('%s%s\n' % (prefix, line))
