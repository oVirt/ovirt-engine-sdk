
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

import urlparse


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
