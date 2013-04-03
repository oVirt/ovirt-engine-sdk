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

import cookielib
import socket
import urlparse

from ovirtsdk.infrastructure.errors import RequestError, ConnectionError, \
    FormatError
from ovirtsdk.xml import params
from cookielib import DefaultCookiePolicy
from lxml import etree

class CookieJarAdapter():
    """
    This class is an adapter that implements the methods that the CookieJar
    expects and needs in order to add the cookie headers to an HTTP request.

    From the point of view of the CookieJar it looks like a urllib2 request and
    also like a response, but it just saves the headers to a list that will later
    be retrieved by the proxy.
    """
    def __init__(self, url, headers):
        # Save the URL and the headers:
        self._url = url
        self._headers = headers

        # Extract the scheme and the host name from the URL:
        parsed_url = urlparse.urlparse(self._url)
        self._scheme = parsed_url.scheme
        self._host = parsed_url.hostname

    # The following methods are needed to simulate the behaviour of an urllib2
    # request class:
    def get_full_url(self):
        return self._url

    def get_host(self):
        return self._host

    def get_type(self):
        return self._scheme

    def is_unverifiable(self):
        return False

    def get_origin_req_host(self):
        return self._host

    def has_header(self, header):
        return header.lower() in self._headers

    def get_header(self, header_name, default=None):
        return self._headers.get(header_name.lower(), default)

    def header_items(self):
        return self._headers.items()

    def add_unredirected_header(self, key, val):
        self._headers[key.lower()] = val

    # The following method is needed to simulate the behaviour of an urllib2
    # response class:
    def info(self):
        return self

    # This methods simulates the object returned by the info method of the
    # urllib2 response class:
    def getheaders(self, name):
        result = []
        for key, value in self._headers.items():
            if key.lower() == name.lower():
                result.append(value)
        return result

class Proxy():
    '''
    The proxy to web connection
    '''

    def __init__(self, connections_pool, persistent_auth=True):
        '''
        @param connections_pool: connections pool
        @param persistent_auth: persistent authentication flag (default True)
        '''
        self.__connections_pool = connections_pool
        self._persistent_auth = persistent_auth

        # In order to create the cookies adapter we need to extract from the
        # URL the host name, so that we can accept cookies only from that host:
        self._url = self.__connections_pool.get_url()

        # Create the cookies policy and jar:
        cookies_policy = cookielib.DefaultCookiePolicy(
                   strict_ns_domain=DefaultCookiePolicy.DomainStrictNoDots,
                   allowed_domains=self.__getAllowedDomains(self._url))
        self._cookies_jar = cookielib.CookieJar(policy=cookies_policy)

    def __getAllowedDomains(self, url):
        '''
        fetches allowed domains for cookie
        '''

        LOCAL_HOST = 'localhost'
        parsed_url = urlparse.urlparse(url)
        domains = [parsed_url.hostname]

        if parsed_url.hostname == LOCAL_HOST:
            return domains.append(LOCAL_HOST + '.local')

        return domains

    def getConnectionsPool(self):
        '''
        Returns connections pool
        '''
        return self.__connections_pool

    def get(self, url, headers={}):
        '''
        Performs get request
        
        @param url: request URI
        @param body: request body
        @param headers: request headers
        '''
        return self.request(method='GET', url=url, headers=headers)

    def delete(self, url, body=None, headers={}):
        '''
        Performs delete request
        
        @param url: request URI
        @param body: request body
        @param headers: request headers
        '''
        return self.request('DELETE', url, body, headers)

    def update(self, url, body=None, headers={}):
        '''
        Performs update request
        
        @param url: request URI
        @param body: request body
        @param headers: request headers
        '''
        return self.request('PUT', url, body, headers)

    def add(self, url, body=None, headers={}):
        '''
        Performs add request
        
        @param url: request URI
        @param body: request body
        @param headers: request headers
        '''
        return self.request('POST', url, body, headers)

    def action(self, url, body=None, headers={}):
        '''
        Performs action request
        
        @param url: request URI
        @param body: request body
        @param headers: request headers
        '''
        return self.request('POST', url, body, headers)

    def request(self, method, url, body=None, headers={}, last=False, noParse=False):
        '''
        Performs HTTP request
        
        @param method: HTTP method
        @param url: request URI
        @param body: request body
        @param headers: request headers
        @param last: disables persistence authentication
        @param noParse: disables xml2py conversion
        '''
        return self.__doRequest(method, \
                                url, \
                                body=body, \
                                headers=headers, \
                                conn=self.getConnectionsPool().getConnection(), \
                                last=last,
                                noParse=noParse)

    def __doRequest(self, method, url, conn, body=None, headers={}, last=False, noParse=False):
        '''
        Performs HTTP request
        
        @param method: HTTP method
        @param url: request URI
        @param conn: connection to invoke request on
        @param body: request body
        @param headers: request headers
        @param last: disables persistence authentication
        @param noParse: disables xml2py conversion
        '''
        try:
            # Copy request headers to avoid by-ref lookup after
            # JSESSIONID has been injected
            request_headers = headers.copy()

            # Add cookie headers as needed:
            request_adapter = CookieJarAdapter(self._url + url, request_headers)
            self._cookies_jar.add_cookie_header(request_adapter)

            # Every request except the last one should indicate that we prefer
            # to use persistent authentication:
            if self._persistent_auth and not last:
                request_headers["Prefer"] = "persistent-auth"

            # Send the request and wait for the response:
            conn.doRequest(
                   method=method,
                   url=url,
                   body=body,
                   headers=request_headers,
                   no_auth=self._persistent_auth and \
                        self.__isSetJsessionCookie(self._cookies_jar)
            )

            response = conn.getResponse()

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
            response_adapter = CookieJarAdapter(self._url, response_headers)
            self._cookies_jar.extract_cookies(response_adapter, request_adapter)

            # Parse the body:
            response_body = response.read()

            # Print response body (if in debug mode)
            self.__do_debug(conn, response_body)

            if not noParse:
                return self.__xml2py(response_body)
            return response_body

        except socket.error, e:
            raise ConnectionError, str(e)
        finally:
            conn.close()

    def __isSetJsessionCookie(self, cookies_jar):
        '''
        Checks if JSESSIONID cookie is set

        @param cookies_jar: cookies container
        '''
        if cookies_jar and len(cookies_jar._cookies) > 0:
            for key in cookies_jar._cookies.keys():
                if cookies_jar._cookies[key].has_key('/api') and \
                    cookies_jar._cookies[key]['/api'].has_key('JSESSIONID'):
                    return True
        return False

    def __xml2py(self, obj):
        '''
        Parse XML in to python entity
        '''
        if obj is not None and obj is not '':
            try:
                return params.parseString(obj)
            except etree.XMLSyntaxError:
                # raised when server replies in non-XML format,
                # the motivation for this error is #915036
                raise FormatError
        return obj

    def __do_debug(self, conn, body):
        '''
        Prints request body (when in debug) to STDIO
        '''
        if conn.getConnection().debuglevel:
                print 'body:\n' + body if body else ''

    def get_url(self):
        '''
        Returns entry point URI
        '''
        return self.getConnectionsPool().get_url()

    @staticmethod
    def instance(connections_pool):
        '''
        Produces Proxy instance
        '''
        Proxy(connections_pool)
