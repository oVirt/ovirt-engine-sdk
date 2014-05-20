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

from ovirtsdk.infrastructure.errors import RequestError, ConnectionError, FormatError
from ovirtsdk.xml import params
from lxml import etree

class Proxy():
    '''
    The proxy to web connection
    '''

    def __init__(self, connections_pool, persistent_auth=True, prefix=''):
        '''
        @param connections_pool: connections pool
        @param prefix: the prefix common to all requests
        @param persistent_auth: persistent authentication flag (default True)
        '''
        self.__connections_pool = connections_pool
        self._persistent_auth = persistent_auth
        self.__prefix = prefix

        # In order to create the cookies adapter we need to extract from the
        # URL the host name, so that we can accept cookies only from that host:
        self._url = self.__connections_pool.get_url()

    def getConnectionsPool(self):
        '''
        Returns connections pool
        '''
        return self.__connections_pool

    def getPrefix(self):
        """Returns the prefix common to all requests."""
        return self.__prefix

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
                                noParse=noParse,
                                persistent_auth=self._persistent_auth)

    def __doRequest(self, method, url, conn, body=None, headers={}, last=False, noParse=False, persistent_auth=True):
        '''
        Performs HTTP request
        
        @param method: HTTP method
        @param url: request URI
        @param conn: connection to invoke request on
        @param body: request body
        @param headers: request headers
        @param last: disables persistence authentication
        @param noParse: disables xml2py conversion
        @param persistent_auth: session based auth
        '''

        # The Apache web server ignores the "Expect" header, so if this header
        # was explicitly added by the user, then we need to add the alternative
        # "X-Ovirt-Expect" as well:
        if "Expect" in headers:
            headers["X-Ovirt-Expect"] = headers["Expect"]

        response = conn.doRequest(
                   method=method,
                   url=self.__prefix + url,
                   body=body,
                   headers=headers,
                   last=last,
                   persistent_auth=persistent_auth
            )

        if not noParse:
            return self.__xml2py(response)
        return response

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
