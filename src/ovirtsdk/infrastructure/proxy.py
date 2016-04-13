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

from lxml import etree
from ovirtsdk.infrastructure import errors
from ovirtsdk.xml import params


class Proxy(object):
    """
    The proxy to web connection
    """

    def __init__(self, pool, persistent_auth=True, prefix=''):
        """
        @param pool: connections pool
        @param prefix: the prefix common to all requests
        @param persistent_auth: persistent authentication flag (default True)
        """
        self.__pool = pool
        self.__persistent_auth = persistent_auth
        self.__prefix = prefix

    def get(self, url, headers=None, cls=None):
        """
        Performs get request
        
        @param url: request URI
        @param body: request body
        @param headers: request headers
        @param cls: the class of the body
        """
        return self.request(method='GET', url=url, headers=headers, cls=cls)

    def delete(self, url, body=None, headers=None, cls=None):
        """
        Performs delete request
        
        @param url: request URI
        @param body: request body
        @param headers: request headers
        @param cls: the class of the body
        """
        return self.request('DELETE', url, body, headers, cls=cls)

    def update(self, url, body=None, headers=None, cls=None):
        """
        Performs update request
        
        @param url: request URI
        @param body: request body
        @param headers: request headers
        @param cls: the class of the body
        """
        return self.request('PUT', url, body, headers, cls=cls)

    def add(self, url, body=None, headers=None, cls=None):
        """
        Performs add request
        
        @param url: request URI
        @param body: request body
        @param headers: request headers
        @param cls: the class of the body
        """
        return self.request('POST', url, body, headers, cls=cls)

    def action(self, url, body=None, headers=None, cls=None):
        """
        Performs action request
        
        @param url: request URI
        @param body: request body
        @param headers: request headers
        @param cls: the class of the body
        """
        return self.request('POST', url, body, headers, cls=cls)

    def request(self, method, url, body=None, headers=None, last=False,
                cls=None):
        """
        Performs HTTP request
        
        @param method: HTTP method
        @param url: request URI
        @param body: request body
        @param headers: request headers
        @param last: disables persistence authentication
        @param cls: the class of the body
        """

        # Create the dictionary of headers if needed, as the rest of the code
        # does not play well with None:
        if headers is None:
            headers = {}

        # The Apache web server ignores the "Expect" header, so if this header
        # was explicitly added by the user, then we need to add the alternative
        # "X-Ovirt-Expect" as well:
        if "Expect" in headers:
            headers["X-Ovirt-Expect"] = headers["Expect"]

        response = self.__pool.do_request(
            method=method,
            url=url,
            body=body,
            headers=headers,
            last=last,
            persistent_auth=self.__persistent_auth
        )

        return self.__xml2py(response, cls)

    def close(self):
        self.__pool.close()

    @staticmethod
    def __xml2py(obj, cls=None):
        """
        Parse XML in to python entity
        """
        if obj is not None and obj is not '':
            try:
                return params.parseClass(obj, cls)
            except etree.XMLSyntaxError:
                # raised when server replies in non-XML format,
                # the motivation for this error is #915036
                raise errors.FormatError
        return obj
