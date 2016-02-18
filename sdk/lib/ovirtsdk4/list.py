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

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class List(list):
    """
    This is the base class for all the list types of the SDK. It contains the
    utility methods used by all of them.
    """

    def __init__(self, href=None, connection=None, is_link=None):
        super(List, self).__init__()
        self._href = href
        self._connection = connection
        self._is_link = is_link

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

    @property
    def connection(self):
        """
        Returns the reference to the connection that created this object.
        """
        return self._connection

    @connection.setter
    def connection(self, value):
        """
        Sets reference to the connection that created this object.
        """
        self._connection = value

    @property
    def is_link(self):
        """
        Indicates if this structure is used as a link. When a structure is
        used as a link only the identifier and the `href` attributes will
        be returned by the server.
        """
        return self._is_link

    @is_link.setter
    def is_link(self, value):
        """
        Sets the value of the flag that indicates if this structure is used as
        a link.
        """
        self__is_link = value

    def follow_link(self):
        """
        Follows the `href` attribute of this structure, retrieves the object
        and returns it.
        """
        # Check that the "href" and "connection" attributes have values, as
        # both are needed in order to retrieve the representation of the
        # object:
        if self._href is None:
            raise Exception(
                'Can\'t follow link because the "href" attribute does\'t' +
                'have a value'
            )
        if self._connection is None:
            raise Exception(
                'Can\'t follow link because the "connection" attribute ' +
                'doesn\'t have a value'
            )

        # Check that the value of the "href" attribute is compatible with the
        # base URL of the connection:
        prefix = urlparse(self._connection.url).path
        if not prefix.endswith('/'):
            prefix += '/'
        if not self._href.startswith(prefix):
            raise Exception(
                'The URL "%s" isn\'t compatible with the base URL of the ' +
                'connection' % self._href
            )

        # Remove the prefix from the URL, follow the path to the relevant
        # service and invoke the "get" method to retrieve its representation:
        path = self._href[len(prefix):]
        service = self._connection.service(path)
        return service.get()
