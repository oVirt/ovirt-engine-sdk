#
# Copyright (c) 2010 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import types
import urllib
import urlparse
import base64
import socket
import logging

from httplib import HTTPConnection

from ovirtsdk.web.cookiejaradapter import CookieJarAdapter
from ovirtsdk.infrastructure.context import context
from ovirtsdk.web.httpsconnection import HTTPSConnection
from ovirtsdk.infrastructure.errors import NoCertificatesError, ImmutableError, RequestError, ConnectionError


class Connection(object):
    '''
    The oVirt api connection proxy
    '''
    def __init__(self, url, port, key_file, cert_file, ca_file, strict, timeout, username,
                 password, manager, insecure=False, validate_cert_chain=True, debug=False):

        self.__connection = self.__createConnection(url=url,
                                                    port=port,
                                                    key_file=key_file,
                                                    cert_file=cert_file,
                                                    ca_file=ca_file,
                                                    insecure=insecure,
                                                    validate_cert_chain=validate_cert_chain,
                                                    strict=strict,
                                                    timeout=timeout)

        self.__url = url
        self.__connection.set_debuglevel(int(debug))
        self.__headers = self.__createStaticHeaders(username, password)
        self.__manager = manager
        self.__id = id(self)
        self.__insecure = insecure
        self.__validate_cert_chain = validate_cert_chain
        self.__context = manager.context

    def get_id(self):
        return self.__id

    def getConnection(self):
        return self.__connection

    def getDefaultHeaders(self, no_auth=False):
        '''
        Fetches headers to be used on request

        @param no_auth: do not authorize request (authorization is done via cookie)
        '''

        AUTH_HEADER = 'Authorization'

        headers = self.__headers.copy()
        headers.update(self.__createDynamicHeaders())
        renew_session = context.manager[self.context].get('renew_session')

        # remove AUTH_HEADER
        if no_auth and not renew_session and headers.has_key(AUTH_HEADER):
            headers.pop(AUTH_HEADER)

        return headers

    def doRequest(self, method, url, body=urllib.urlencode({}), headers={}, last=False, persistent_auth=True):
        '''
        Performs HTTP request

        @param method: HTTP method
        @param url: URL to invoke the request on
        @param body: request body
        @param headers: request headers
        @param last: disables persistence authentication
        @param persistent_auth: session based auth
        '''

        try:
            # Copy request headers to avoid by-ref lookup after
            # JSESSIONID has been injected
            request_headers = headers.copy()

            # Add cookie headers as needed:
            request_adapter = CookieJarAdapter(self.__url + url, request_headers)
            self.__manager.addCookieHeaders(request_adapter)

            # Every request except the last one should indicate that we prefer
            # to use persistent authentication:
            if persistent_auth and not last:
                request_headers["Prefer"] = "persistent-auth"

            # Send the request and wait for the response:
            response = self.__connection.request(
                         method,
                         url,
                         body,
                         self.getHeaders(request_headers,
                                         no_auth=
                                            persistent_auth and \
                                            self.__isSetJsessionCookie(
                                                   self.__manager.getCookiesJar()
                                            ),
                         )
                       )

            response = self.getResponse()

            # Read the response headers (there is always a response,
            # even for error responses):
            response_headers = dict(response.getheaders())

            # Parse the received body only if there are no errors reported by
            # the server (this needs review, as less than 400 doesn't garantee
            # a correct response, it could be a redirect, and many other
            # things):
            if response.status >= 400:
                raise RequestError, response

            # Copy the cookies from the response:
            response_adapter = CookieJarAdapter(self.__url, response_headers)
            self.__manager.storeCookies(response_adapter, request_adapter)

            # Parse the body:
            response_body = response.read()

            # Print response body (if in debug mode)
            self.__do_debug(self, response_body)

            return response_body

        except socket.error, e:
            raise ConnectionError, str(e)
        finally:
            self.close()

    def __do_debug(self, conn, body):
        '''
        Prints request body (when in debug) to STDIO
        '''
        if conn.getConnection().debuglevel:
                print 'body:\n' + body if body else ''

    def __isSetJsessionCookie(self, cookies_jar):
        '''
        Checks if JSESSIONID cookie is set

        @param cookies_jar: cookies container
        '''
        if cookies_jar and len(cookies_jar._cookies) > 0:
            for key in cookies_jar._cookies.keys():
                if key and len(cookies_jar._cookies[key]) > 0:
                    for value in cookies_jar._cookies[key].values():
                        if value and 'JSESSIONID' in value.keys():
                            return True
        return False

    def getHeaders(self, headers={}, no_auth=False):
        headers.update(self.getDefaultHeaders(no_auth))
        extended_headers = {}
        for k in headers.keys():
            if (headers[k] is None and extended_headers.has_key(k)):
                extended_headers.pop(k)
            elif headers[k] != None:
                if type(headers[k]) != types.StringType:
                    extended_headers[k] = str(headers[k])
                else:
                    extended_headers[k] = headers[k]

        return extended_headers

    def getResponse(self):
        return self.__connection.getresponse()

    def setDebugLevel(self, level):
        self.__connection.set_debuglevel(level)

    def setTunnel(self, host, port=None, headers=None):
        self.__connection.set_tunnel(host, port, headers)

    def close(self):
        self.__connection.close()
# FIXME: create connection watchdog to close it on idle-ttl expiration, rather than after the call
        if (self.__manager is not None):
            self.__manager._freeResource(self)

    def state(self):
        return self.__connection.__state

    @property
    def context(self):
        return self.__context

    def __parse_url(self, url):
        if not url.startswith('http'):
            url = "https://" + url
        return urlparse.urlparse(url)


    def __createConnection(self, url, key_file=None, cert_file=None,
                           ca_file=None, insecure=False, validate_cert_chain=True, port=None,
                           strict=None, timeout=None):

        u = self.__parse_url(url)

        if(u.scheme == 'https'):
            if validate_cert_chain:
                if not insecure and not ca_file:
                    raise NoCertificatesError
            else:
                ca_file = None

            return HTTPSConnection(
                       host=u.hostname,
                       port=u.port,
                       key_file=key_file,
                       cert_file=cert_file,
                       ca_file=ca_file,
                       strict=strict,
                       timeout=timeout,
                       insecure=insecure
                   )
        return HTTPConnection(
                  host=u.hostname,
                  port=u.port,
                  strict=strict,
                  timeout=timeout
              )

    def __createStaticHeaders(self, username, password):
        auth = base64.encodestring("%s:%s" % (username, password)).replace("\n", "")
        return {"Content-type" : "application/xml",
                "Accept"       : "application/xml",
                "Authorization": "Basic %s" % auth}

    def __injectFilterHeader(self, headers):
        filter_header = context.manager[self.context].get('filter')
        if filter_header != None:
            if type(filter_header) == types.BooleanType:
                headers['Filter'] = filter_header
            else:
                logging.error(
                      TypeError(
                        "filter_header" + str(filter_header),
                        str(types.BooleanType) + ' is expected.'
                       )
                )

    def __injectAuthSessionHeader(self, headers):
        session_timeout = context.manager[self.context].get('session_timeout')
        if session_timeout != None:
            if type(session_timeout) == types.IntType:
                headers['Session-TTL'] = session_timeout
            else:
                logging.error(
                      TypeError(
                        "session_timeout" + str(session_timeout),
                        str(types.IntType) + ' is expected.'
                      )
                )

    def __createDynamicHeaders(self):
        headers = {}

        self.__injectFilterHeader(headers)
        self.__injectAuthSessionHeader(headers)

        return headers

    def __setattr__(self, name, value):
        if name in ['__context', 'context']:
            raise ImmutableError(name)
        else:
            super(Connection, self).__setattr__(name, value)

    id = property(get_id, None, None, None)

    def isInsecure(self):
        '''
        signals to not demand site trustworthiness for ssl enabled connection (default is False)
        '''
        return self.__insecure

    def isValidateCertChain(self):
        '''
        validate the server's certificate (default is True)
        '''
        return self.__validate_cert_chain
