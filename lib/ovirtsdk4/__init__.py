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
import json
import os
import pycurl
import re
import six
import sys
import threading

try:
    from urllib.parse import urlencode, urlparse
except ImportError:
    from urllib import urlencode
    from urlparse import urlparse

from ovirtsdk4 import version
from ovirtsdk4.http import Response


class Error(Exception):
    """
    General exception which is thrown by SDK,
    indicates that some exception happened in SDK.
    """

    def __init__(self, message, code=None, fault=None):
        """
        Creates an instance of Error class.

        `message`:: The exception message.

        `code`:: An error code associated to the error. For HTTP related
        errors, this will be the HTTP response code returned by the server.
        For example, if retrieving of a virtual machine fails because it
        doesn't exist this attribute will contain the integer value 404. Note
        that this may be `nil` if the error is not HTTP related.

        `fault`:: The `Fault` object associated to the error.
        """
        super(Error, self).__init__(message)
        self.code = code
        self.fault = fault


class AuthError(Error):
    """
    This class of error indicates that an authentiation or authorization
    problem happenend, like incorrect user name, incorrect password, or
    missing permissions.
    """
    pass


class ConnectionError(Error):
    """
    This class of error indicates that the name of the server or the name of
    the proxy can't be resolved to an IP address, or that the connection
    can't be stablished because the server is down or unreachable.

    Note that for this class of error the `code` and `fault` attributes will
    always be empty, as no response from the server will be available to
    populate them.
    """
    pass


class NotFoundError(Error):
    """
    This class of error indicates that an object can't be found.
    """
    pass


class TimeoutError(Error):
    """
    This class of error indicates that an operation timed out.

    Note that for this class of error the `code` and `fault` attributes will
    always be empty, as no response from the server will be available to
    populate them.
    """
    pass


class List(list):
    """
    This is the base class for all the list types of the SDK. It contains the
    utility methods used by all of them.
    """

    def __init__(self, href=None):
        super(List, self).__init__()
        self._href = href

    @property
    def href(self):
        """
        Returns the value of the `href` attribute.
        """
        return self._href

    @href.setter
    def href(self, value):
        """
        Sets the value of the `href` attribute.
        """
        self._href = value


class Struct(object):
    """
    This is the base class for all the struct types of the SDK. It contains
    the utility methods used by all of them.
    """

    def __init__(self, href=None):
        super(Struct, self).__init__()
        self._href = href

    @property
    def href(self):
        """
        Returns the value of the `href` attribute.
        """
        return self._href

    @href.setter
    def href(self, value):
        """
        Sets the value of the `href` attribute.
        """
        self._href = value

    @staticmethod
    def _check_type(attribute, value, expected):
        """
        Checks that the given types match, and generates an exception if
        they don't.
        """
        if value is not None:
            actual = type(value)
            if not actual == expected:
                raise TypeError((
                    "The type '{actual}' isn't valid for "
                    "attribute '{attribute}', it must be "
                    "'{expected}'"
                ).format(
                    attribute=attribute,
                    actual=actual.__name__,
                    expected=expected.__name__,
                ))


class Connection(object):
    """
    This class is responsible for managing an HTTP connection to the engine
    server. It is intended as the entry point for the SDK, and it provides
    access to the `system` service and, from there, to the rest of the
    services provided by the API.
    """

    # Regular expression used to check XML content type.
    __XML_CONTENT_TYPE_RE = re.compile(r"^\s*(application|text)/xml\s*(;.*)?$")

    # Regular expression used to check JSON content type.
    __JSON_CONTENT_TYPE_RE = re.compile(r"^\s*(application|text)/json\s*(;.*)?$")

    # The typical URL path, used just to generate informative error messages.
    __TYPICAL_PATH = '/ovirt-engine/api'

    # Debug types that we know how to handle. Everything else will be
    # silently ignored.
    __KNOWN_DEBUG_TYPES = [
        pycurl.INFOTYPE_TEXT,
        pycurl.INFOTYPE_HEADER_IN,
        pycurl.INFOTYPE_HEADER_OUT,
        pycurl.INFOTYPE_DATA_IN,
        pycurl.INFOTYPE_DATA_OUT,
    ]

    # Prefixes to use for debug data types:
    __DEBUG_PREFIXES = {
        pycurl.INFOTYPE_TEXT: '* ',
        pycurl.INFOTYPE_HEADER_IN: '> ',
        pycurl.INFOTYPE_HEADER_OUT: '< ',
        pycurl.INFOTYPE_DATA_IN: '> ',
        pycurl.INFOTYPE_DATA_OUT: '< ',
    }

    def __init__(
        self,
        url=None,
        username=None,
        password=None,
        token=None,
        insecure=False,
        ca_file=None,
        debug=False,
        log=None,
        kerberos=False,
        timeout=0,
        compress=True,
        sso_url=None,
        sso_revoke_url=None,
        sso_token_name='access_token',
        headers=None,
        pipeline=0,
        connections=0,
    ):
        """
        Creates a new connection to the API server.

        This method supports the following parameters:

        `url`:: A string containing the base URL of the server, usually
        something like `https://server.example.com/ovirt-engine/api`.

        `username`:: The name of the user, something like `admin@internal`.

        `password`:: The name password of the user.

        `token`:: : The token to be used to access API. Optionally, user can
        use token, instead of username and password to access API. If user
        don't specify `token` parameter, SDK will automatically create one.

        `insecure`:: A boolean flag that indicates if the server TLS
        certificate and host name should be checked.

        `ca_file`:: A PEM file containing the trusted CA certificates. The
        certificate presented by the server will be verified using these CA
        certificates. If `ca_file` parameter is not set, system wide
        CA certificate store is used.

        `debug`:: A boolean flag indicating if debug output should be
        generated. If the value is `True` and the `log` parameter isn't
        `None` then the data sent to and received from the server will
        be written to the log. Be aware that user names and passwords will
        also be written, so handle it with care.

        `log`:: The logger where the log messages will be written.

        `kerberos`:: A boolean flag indicating if Kerberos
        authentication should be used instead of the default basic
        authentication.

        `timeout`:: The maximum total time to wait for the response, in
        seconds. A value of zero (the default) means wait for ever. If
        the timeout expires before the response is received an exception
        will be raised.

        `compress`:: A boolean flag indicating if the SDK should ask
        the server to send compressed responses. The default is `True`.
        Note that this is a hint for the server, and that it may return
        uncompressed data even when this parameter is set to `True`.
        Note that compression will be disabled if user pass `debug`
        parameter set to `true`, so the debug messages are in plain text.

        `sso_url`:: A string containing the base SSO URL of the serve.
        Default SSO url is computed from the `url` if no `sso_url` is provided.

        `sso_revoke_url`:: A string containing the base URL of the SSO
        revoke service. This needs to be specified only when using
        an external authentication service. By default this URL
        is automatically calculated from the value of the `url` parameter,
        so that SSO token revoke will be performed using the SSO service
        that is part of the engine.

        `sso_token_name`:: The token name in the JSON SSO response returned
        from the SSO server. Default value is `access_token`.

        `headers`:: A dictionary with headers which should be send with every
        request.

        `connections`:: The maximum number of connections to open to the host.
        If the value is `0` (the default) then the number of connections will
        be unlimited.

        `pipeline`:: The maximum number of request to put in an HTTP pipeline
        without waiting for the response. If the value is `0` (the default)
        then pipelining is disabled.
        """

        # Check mandatory parameters:
        if url is None:
            raise Error('The \'url\' parameter is mandatory')

        # Check that the CA file exists if insecure is not set:
        if not insecure:
            if ca_file is not None and not os.path.exists(ca_file):
                raise Error('The CA file \'%s\' doesn\'t exist' % ca_file)

        # Save the URL:
        self._url = url

        # Save the logger:
        self._log = log

        # Save the credentials:
        self._username = username
        self._password = password
        self._sso_token = token
        self._kerberos = kerberos
        self._ca_file = ca_file
        self._insecure = insecure
        self._timeout = timeout
        self._debug = debug
        self._compress = compress

        # The curl object can be used by several threads, but not
        # simultaneously, so we need a lock to prevent that:
        self._curl_lock = threading.Lock()

        # Set SSO attributes:
        self._sso_url = sso_url
        self._sso_revoke_url = sso_revoke_url
        self._sso_token_name = sso_token_name

        # Headers:
        self._headers = headers or {}

        # Create the curl handle that manages the pool of connections:
        self._multi = pycurl.CurlMulti()
        self._multi.setopt(pycurl.M_PIPELINING, bool(pipeline))
        # Since libcurl 7.30.0:
        if hasattr(pycurl, 'M_MAX_PIPELINE_LENGTH'):
            self._multi.setopt(pycurl.M_MAX_PIPELINE_LENGTH, pipeline)
            self._multi.setopt(pycurl.M_MAX_HOST_CONNECTIONS, connections)

        # Connections:
        self._curls = set()

        # Initialize the reference to the system service:
        self.__system_service = None

    def send(self, request):
        """
        Sends an HTTP request and waits for the response.

        This method is intended for internal use by other components of the
        SDK. Refrain from using it directly, as backwards compatibility isn't
        guaranteed.

        This method supports the following parameters.

        `request`:: The Request object containing the details of the HTTP
        request to send.

        The returned value is a Request object containing the details of the
        HTTP response received.
        """

        with self._curl_lock:
            return self.__send(request)

    def authenticate(self):
        """
        Return token which can be used for authentication instead of credentials.
        It will be created, if it not exists, yet. By default the token will be
        revoked when the connection is closed, unless the `logout` parameter of
        the `close` method is `False`.
        """
        try:
            if self._sso_token is None:
                self._sso_token = self._get_access_token()
            return self._sso_token
        except pycurl.error as e:
            self.__parse_error(e)

    def __send(self, request):
        # Create SSO token if needed:
        self.authenticate()

        # Init curl easy:
        curl = pycurl.Curl()
        curl.setopt(pycurl.COOKIEFILE, "")

        # Configure TLS parameters:
        if self._url.startswith('https'):
            curl.setopt(pycurl.SSL_VERIFYPEER, 0 if self._insecure else 1)
            curl.setopt(pycurl.SSL_VERIFYHOST, 0 if self._insecure else 2)
            if self._ca_file is not None:
                curl.setopt(pycurl.CAINFO, self._ca_file)

        # Configure timeouts:
        curl.setopt(pycurl.TIMEOUT, self._timeout)

        # Configure compression of responses (setting the value to a zero
        # length string means accepting all the compression types that
        # libcurl supports):
        if self._compress and not self._debug:
            curl.setopt(pycurl.ENCODING, '')

        # Configure debug mode:
        if self._debug and self._log is not None:
            curl.setopt(pycurl.VERBOSE, 1)
            curl.setopt(pycurl.DEBUGFUNCTION, self._curl_debug)

        # Set the method:
        curl.setopt(pycurl.CUSTOMREQUEST, request.method)

        # Build the URL:
        url = self._build_url(
            path=request.path,
            query=request.query,
        )
        curl.setopt(pycurl.URL, url)

        # Older versions of the engine (before 4.1) required the
        # 'all_content' parameter as an HTTP header instead of a query
        # parameter. In order to better support these older versions of
        # the engine we need to check if this parameter is included in
        # the request, and add the corresponding header.
        if request.query is not None:
            all_content = request.query.get('all_content')
            if all_content is not None:
                request.headers['All-Content'] = all_content

        # Add global headers:
        headers_dict = self._headers.copy()

        # Add headers, avoiding those that have no value:
        header_lines = []
        for header_name, header_value in request.headers.items():
            if header_value is not None:
                headers_dict[header_name] = header_value

        for header_name, header_value in headers_dict.items():
            header_lines.append('%s: %s' % (header_name, header_value))

        header_lines.append('User-Agent: PythonSDK/%s' % version.VERSION)
        header_lines.append('Version: 4')
        header_lines.append('Content-Type: application/xml')
        header_lines.append('Accept: application/xml')
        header_lines.append('Authorization: Bearer %s' % self._sso_token)

        # Make sure headers values are strings, because
        # pycurl version 7.19.0 supports only string in headers
        for i, header in enumerate(header_lines):
            try:
                header_lines[i] = header.encode('ascii')
            except (UnicodeEncodeError, UnicodeDecodeError):
                header_name, header_value = header.split(':')
                raise Error(
                    "The value '{header_value}' of header '{header_name}' "
                    "contains characters that can't be encoded using ASCII, "
                    "as required by the HTTP protocol.".format(
                        header_value=header_value,
                        header_name=header_name,
                    )
                )

        # Copy headers and the request body to the curl object:
        curl.setopt(pycurl.HTTPHEADER, header_lines)
        body = request.body
        if body is None:
            body = ''

        # HTTP pipelining is valid only for idempotent operations,
        # pycurl automatically disables pipelining if COPYPOSTFIELDS
        # is set, even if pipelining is explicitly set.
        if request.method in ['POST', 'PUT']:
            curl.setopt(pycurl.COPYPOSTFIELDS, body.encode('utf-8'))

        # Prepare the buffers to receive the response:
        body_buf = io.BytesIO()
        headers_buf = io.BytesIO()
        curl.setopt(pycurl.WRITEFUNCTION, body_buf.write)
        curl.setopt(pycurl.HEADERFUNCTION, headers_buf.write)

        # Add the curl easy to the multi handle:
        self._multi.add_handle(curl)

        return curl, body_buf, headers_buf, request

    def wait(self, context, failed_auth=False):
        with self._curl_lock:
            try:
                return self.__wait(context, failed_auth)
            except pycurl.error as e:
                self.__parse_error(e)

    def __wait(self, context, failed_auth=False):
        while True:
            while True:
                ret, _ = self._multi.perform()
                if ret != pycurl.E_CALL_MULTI_PERFORM:
                    break
            while True:
                num_q, ok_list, err_list = self._multi.info_read()
                self._curls = self._curls.union(set(ok_list))
                if err_list:
                    raise Error("Failed to read response: {}".format(err_list))
                elif context[0] in self._curls:
                    # Remove the curl:
                    self._curls.remove(context[0])
                    self._multi.remove_handle(context[0])

                    # Read the response:
                    response = self._read_reponse(context)

                    # If the request failed because of authentication, and it
                    # wasn't a request to the SSO service, then the most likely
                    # cause is an expired SSO token. In this case we need to
                    # request a new token, and try the original request again, but
                    # only once. It if fails again, we just return the failed
                    # response.
                    if response.code == 401 and not failed_auth:
                        self._sso_token = self._get_access_token()
                        context = self.__send(context[3])
                        response = self.__wait(context, True)
                    return response
                elif num_q == 0:
                    break
            self._multi.select(1.0)

    @property
    def url(self):
        """
        Returns a string containing the base URL used by this connection.
        """

        return self._url

    def _revoke_access_token(self):
        """
        Revokes access token
        """

        # Build the SSO revoke URL:
        if self._sso_revoke_url is None:
            url = urlparse(self._url)
            self._sso_revoke_url = (
                '{url}/ovirt-engine/services/sso-logout'
            ).format(
                url='{scheme}://{netloc}'.format(
                    scheme=url.scheme,
                    netloc=url.netloc
                )
            )

        # Construct POST data:
        post_data = {
            'scope': 'ovirt-app-api',
            'token': self._sso_token,
        }

        # Send SSO request:
        sso_response = self._get_sso_response(self._sso_revoke_url, post_data)

        if isinstance(sso_response, list):
            sso_response = sso_response[0]

        if 'error' in sso_response:
            sso_error = self._get_sso_error(sso_response)
            raise AuthError(
                'Error during SSO revoke %s : %s' % (
                    sso_error[0],
                    sso_error[1]
                )
            )

    def _get_access_token(self):
        """
        Creates access token which reflect authentication method.
        """

        # Build SSO URL:
        if self._kerberos:
            entry_point = 'token-http-auth'
            grant_type = 'urn:ovirt:params:oauth:grant-type:http'
        else:
            entry_point = 'token'
            grant_type = 'password'

        if self._sso_url is None:
            url = urlparse(self._url)
            self._sso_url = (
                '{url}/ovirt-engine/sso/oauth/{entry_point}'
            ).format(
                url='{scheme}://{netloc}'.format(
                    scheme=url.scheme,
                    netloc=url.netloc
                ),
                entry_point=entry_point,
            )

        # Construct POST data:
        post_data = {
            'grant_type': grant_type,
            'scope': 'ovirt-app-api',
        }
        if not self._kerberos:
            post_data.update({
                'username': self._username,
                'password': self._password,
            })

        # Send SSO request:
        sso_response = self._get_sso_response(self._sso_url, post_data)

        if isinstance(sso_response, list):
            sso_response = sso_response[0]

        if 'error' in sso_response:
            sso_error = self._get_sso_error(sso_response)
            raise AuthError(
                'Error during SSO authentication %s : %s' % (
                    sso_error[0],
                    sso_error[1]
                )
            )

        return sso_response[self._sso_token_name]

    def _get_sso_error(self, sso_response):
        # OpenId define `error_description` field, OAuth doesn't:
        if 'error_description' in sso_response:
            sso_error = (sso_response.get('error'), sso_response.get('error_description'))
        else:
            sso_error = (sso_response.get('error_code'), sso_response.get('error'))

        return sso_error

    def _get_sso_response(self, url, params=''):
        """
        Perform SSO request and return response body data.
        """

        # Set HTTP method and URL:
        curl = pycurl.Curl()
        curl.setopt(pycurl.CUSTOMREQUEST, 'POST')
        curl.setopt(pycurl.URL, url)

        # Set proper Authorization header if using kerberos:
        if self._kerberos:
            curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_GSSNEGOTIATE)
            curl.setopt(pycurl.USERPWD, ':')

        # Configure debug mode:
        if self._debug and self._log is not None:
            curl.setopt(pycurl.VERBOSE, 1)
            curl.setopt(pycurl.DEBUGFUNCTION, self._curl_debug)

        # Configure TLS parameters:
        if self._url.startswith('https'):
            curl.setopt(pycurl.SSL_VERIFYPEER, 0 if self._insecure else 1)
            curl.setopt(pycurl.SSL_VERIFYHOST, 0 if self._insecure else 2)
            if self._ca_file is not None:
                curl.setopt(pycurl.CAINFO, self._ca_file)

        # Prepare headers:
        header_lines = [
            'User-Agent: PythonSDK/%s' % version.VERSION,
            'Accept: application/json'
        ]
        curl.setopt(pycurl.HTTPHEADER, header_lines)
        curl.setopt(pycurl.COPYPOSTFIELDS, urlencode(params))

        # Prepare the buffer to receive the response:
        body_buf = io.BytesIO()
        headers_buf = io.BytesIO()

        # We ignore all headers which are received before the last response
        # from the server, because we can be forwarded by apache, and we
        # are interested only in last response:
        def write_header(buf):
            if buf.startswith(b'HTTP/'):
                headers_buf.truncate(0)
                headers_buf.seek(0)
            headers_buf.write(buf)

        curl.setopt(pycurl.WRITEFUNCTION, body_buf.write)
        curl.setopt(pycurl.HEADERFUNCTION, write_header)

        # Send the request and wait for the response:
        curl.perform()
        curl.close()

        # Get headers:
        headers_text = headers_buf.getvalue().decode('ascii')
        header_lines = headers_text.split('\n')

        # Check the returned content type:
        self._check_content_type(self.__JSON_CONTENT_TYPE_RE, 'JSON', header_lines)

        return json.loads(body_buf.getvalue().decode('utf-8'))

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
        path. For example, if the `path` parameter is
        `vms/123/diskattachments` then it will return a reference to
        the service that manages the disk attachments for the virtual
        machine with identifier `123`.

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
        except Error:
            if raise_exception:
                six.reraise(*sys.exc_info())
            return False
        except Exception as exception:
            if raise_exception:
                raise Error(exception)
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
            raise Error(
                "Can't follow link because the 'href' attribute does't "
                "have a value"
            )

        # Check that the value of the "href" attribute is compatible with the
        # base URL of the connection:
        prefix = urlparse(self._url).path
        if not prefix.endswith('/'):
            prefix += '/'
        if not href.startswith(prefix):
            raise Error(
                "The URL '%s' isn't compatible with the base URL of the "
                "connection" % href
            )

        # Remove the prefix from the URL, follow the path to the relevant
        # service and invoke the "get", or "list method to retrieve its representation:
        path = href[len(prefix):]
        service = self.service(path)
        if isinstance(obj, List):
            return service.list()
        else:
            return service.get()

    def close(self, logout=True):
        """
        Releases the resources used by this connection.

        `logout`:: A boolean, which specify if token should be revoked,
        and so user should be logged out.
        """

        # Revoke access token:
        if logout and self._sso_token is not None:
            self._revoke_access_token()

        # Release resources used by the cURL handle:
        with self._curl_lock:
            self._multi.close()

    def _build_url(self, path='', query=None):
        """
        Builds a request URL from a path, and the set of query parameters.

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

        The returned value is an string containing the URL.
        """

        # Add the path and the parameters:
        url = '%s%s' % (self._url, path)
        if query:
            url = '%s?%s' % (url, urlencode(sorted(query.items())))
        return url

    def check_xml_content_type(self, response):
        """
         Checks that the content type of the given response is XML. If it is
         XML then it does nothing. If it isn't XML then it raises an
         exception.

         `response`:: The HTTP response to check.
        """
        return self._check_content_type(
            self.__XML_CONTENT_TYPE_RE,
            'XML',
            response.headers
        )

    def check_json_content_type(self, response):
        """
         Checks that the content type of the given response is JSON. If it is
         JSON then it does nothing. If it isn't JSON then it raises an
         exception.

         `response`:: The HTTP response to check.
        """
        return self._check_content_type(
            self.__JSON_CONTENT_TYPE_RE,
            'JSON',
            response.headers
        )

    def _check_content_type(self, expected_re, expected_name, headers):
        """
        Checks the given content type and raises an exception if it isn't the
        expected one.

        `expected_re`:: The regular expression used to check the expected
                        content type.
        `expected_name`:: The name of the expected content type.
        `headers`:: The HTTP headers to check.
        """
        content_type = self._get_header_value(headers, 'content-type')
        if expected_re.match(content_type) is None:
            msg = "The response content type '{}' isn't the expected {}".format(
                content_type,
                expected_name,
            )
            url = urlparse(self._url)
            if url.path != self.__TYPICAL_PATH:
                msg += (
                    ". Is the path '{}' included in the 'url' "
                    "parameter correct?"
                ).format(url.path)
                msg += " The typical one is '{}'".format(self.__TYPICAL_PATH)
            raise Error(msg)

    def _read_reponse(self, context):
        """
        Read the response.

        `context`:: tuple which contains cur easy, response body,
        response headers, original request
        """
        # Extract the response code and body:
        response = Response()
        response.code = context[0].getinfo(pycurl.HTTP_CODE)
        response.body = context[1].getvalue()

        # The response code can be extracted directly, but cURL doesn't
        # have a method to extract the response message, so we have to
        # parse the first header line to find it:
        response.reason = ""
        headers_text = context[2].getvalue().decode('ascii')
        header_lines = headers_text.split('\n')
        response.headers = header_lines
        if len(header_lines) >= 1:
            response_line = header_lines[0]
            response_fields = response_line.split()
            if len(response_fields) >= 3:
                response.reason = ' '.join(response_fields[2:])

        context[0].close()
        # Return the response:
        return response

    def __parse_error(self, error):
        e_code = error.args[0]
        clazz = Error
        error_msg = "Error while sending HTTP request: {}".format(error)

        if e_code in [
            pycurl.E_COULDNT_CONNECT, pycurl.E_COULDNT_RESOLVE_HOST
        ]:
            clazz = ConnectionError
        elif e_code == pycurl.E_OPERATION_TIMEOUTED:
            clazz = TimeoutError

        six.reraise(clazz, clazz(error_msg), sys.exc_info()[2])

    def _get_header_value(self, headers, name):
        """
        Return header value by its name.

        `headers`:: list of headers
        `name`:: name of the header
        """
        return next(
            (h.split(':')[1].strip() for h in headers if h.lower().startswith(name)),
            None
        )

    def _curl_debug(self, debug_type, data):
        """
        This is the implementation of the cURL debug callback.
        """

        # Exclude all types of debug data that we don't know how to
        # handle, as trying to decode and manipulate that data as
        # strings will likely fail.
        if debug_type not in self.__KNOWN_DEBUG_TYPES:
            return

        # Some versions of PycURL provide the debug data as strings, and
        # some as arrays of bytes, so we need to check the type of the
        # provided data and convert it to strings before trying to
        # manipulate it with the "replace", "strip" and "split" methods:
        text = data.decode('utf-8') if type(data) == bytes else data

        # Split the debug data into lines and send a debug message for
        # each line:
        lines = text.replace('\r\n', '\n').strip().split('\n')
        prefix = self.__DEBUG_PREFIXES.get(debug_type)
        for line in lines:
            if prefix is not None:
                line = prefix + line
            self._log.debug(line)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


class ConnectionBuilder(object):
    """
    This class is a mechanism to simplify the repeated creation of
    multiple connections. It stores the connection parameters given
    in its constructor, and has a single `build` method that is
    equivalent to calling the constructor of the `Connection`
    class. Typical use will be like this:

    [source,python]
    ----
    # Create the builder once:
    builder = ConnectionBuilder(
        url='https://enginer40.example.com/ovirt-engine/api',
        username='admin@internal',
        password='redhat123',
        ca_file='ca.pem',
    )

    # Create and use first connection:
    with builder.build() as connection:
       ...

    # Create and use a second connection:
    with builder.build() as connection:
       ...
    ----
    """

    def __init__(self, **kwargs):
        """
        Creates a new connection builder. The parameters are the same
        accepted by the constructor of the `Connnection` class.
        """

        self._kwargs = kwargs

    def build(self):
        """
        Creates a new connection using the parameters passed to the
        constructor, and returns it.
        """

        return Connection(**self._kwargs)


# We need to import readers and writers here, so the generic
# writer and reader are initialized. This has also benefit that
# the readers/writers/types/services can be used right after the
# top level sdk module import, for example:
#
#   import ovirtsdk4 as sdk
#   vm = sdk.types.Vm()
#
from ovirtsdk4 import readers  # noqa: F401
from ovirtsdk4 import services  # noqa: F401
from ovirtsdk4 import types  # noqa: F401
from ovirtsdk4 import writers  # noqa: F401
