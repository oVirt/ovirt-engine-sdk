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

from ovirtsdk.infrastructure.errors import RequestError, ConnectionError
from ovirtsdk.xml import params
from cookielib import DefaultCookiePolicy

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
        """Constructor."""
        self.__connections_pool = connections_pool
        self._persistent_auth = persistent_auth

        # In order to create the cookies adapter we need to extract from the
        # URL the host name, so that we can accept cookies only from that host:
        self._url = self.__connections_pool.get_url()
        parsed_url = urlparse.urlparse(self._url)

        # Create the cookies policy and jar:
        cookies_policy = cookielib.DefaultCookiePolicy(allowed_domains=[parsed_url.hostname])
        self._cookies_jar = cookielib.CookieJar(policy=cookies_policy)

    def getConnectionsPool(self):
        return self.__connections_pool

    def get(self, url, headers={}):
        return self.request(method='GET', url=url, headers=headers)

    def delete(self, url, body=None, headers={}):
        return self.request('DELETE', url, body, headers)

    def update(self, url, body=None, headers={}):
        return self.request('PUT', url, body, headers)

    def add(self, url, body=None, headers={}):
        return self.request('POST', url, body, headers)

    def action(self, url, body=None, headers={}):
        return self.request('POST', url, body, headers)

    def request(self, method, url, body=None, headers={}, last=False):
        return self.__doRequest(method, \
                                url, \
                                body=body, \
                                headers=headers, \
                                conn=self.getConnectionsPool().getConnection(), \
                                last=last)

    def __doRequest(self, method, url, conn, body=None, headers={}, last=False):
        try:
            # Add cookie headers as needed:
            request_adapter = CookieJarAdapter(self._url, headers)
            self._cookies_jar.set_policy(
                     cookielib.DefaultCookiePolicy(
                           strict_ns_domain=DefaultCookiePolicy.DomainStrictNoDots))
            self._cookies_jar.add_cookie_header(request_adapter)

            # Every request except the last one should indicate that we prefer
            # to use persistent authentication:
            if self._persistent_auth and not last:
                headers["Prefer"] = "persistent-auth"

            # Send the request and wait for the response:
            conn.doRequest(method=method, url=url, body=body, headers=headers)
            response = conn.getResponse()

            # Read the response headers (there is always a response,
            # even for error responses):
            headers = dict(response.getheaders())

            # Parse the received body only if there are no errors reported by
            # the server (this needs review, as less than 400 doesn't garantee
            # a correct response, it could be a redirect, and many other
            # things):
            if response.status >= 400:
                raise RequestError, response

            # Copy the cookies from the response:
            response_adapter = CookieJarAdapter(self._url, headers)
            self._cookies_jar.extract_cookies(response_adapter, request_adapter)

            # Parse the body:
            response_body = response.read()
            return params.parseString(response_body) if response_body is not None and response_body is not '' \
                                                     else response_body
        except socket.error, e:
            raise ConnectionError, str(e)
        finally:
            conn.close()

    def get_url(self):
        return self.getConnectionsPool().get_url()

    @staticmethod
    def instance(connections_pool):
        Proxy(connections_pool)
