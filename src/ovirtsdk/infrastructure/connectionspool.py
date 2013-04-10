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

from Queue import Queue
import thread
import cookielib
import urlparse

from cookielib import DefaultCookiePolicy

from ovirtsdk.web.connection import Connection
from ovirtsdk.infrastructure.errors import ImmutableError
from ovirtsdk.utils.synchronizationhelper import synchronized


class ConnectionsPool(object):
    '''
    ConnectionsManager used to manage pool of web connections
    '''
    def __init__(self, url, port, key_file, cert_file, ca_file, strict, timeout,
                 username, password, context, count=20, insecure=False, validate_cert_chain=True,
                 debug=False):

        self.__free_connections = Queue(0)
        self.__busy_connections = {}

        self.__plock = thread.allocate_lock()
        self.__rlock = thread.allocate_lock()

        self.__url = url
        self.__context = context

        # Create the cookies policy and jar:
        self.__cookies_jar = cookielib.CookieJar(
                 policy=cookielib.DefaultCookiePolicy(
                       strict_ns_domain=DefaultCookiePolicy.DomainStrictNoDots,
                       allowed_domains=self.__getAllowedDomains(url)
                 )
            )

        for _ in range(count):
            self.__free_connections.put(item=Connection(url=url, \
                                                        port=port, \
                                                        key_file=key_file, \
                                                        cert_file=cert_file, \
                                                        ca_file=ca_file, \
                                                        strict=strict, \
                                                        timeout=timeout, \
                                                        username=username, \
                                                        password=password,
                                                        manager=self,
                                                        insecure=insecure,
                                                        validate_cert_chain=validate_cert_chain,
                                                        debug=debug))
    def getConnection(self, get_ttl=100):
#        try:
            with self.__plock:
                conn = self.__free_connections.get(block=True, timeout=get_ttl)
                self.__busy_connections[conn.get_id()] = conn
                return conn
#        except Empty, e:
#                self.__extendQueue()
#                return self.getConnection(get_ttl)

#    def __extendQueue(self):
# TODO: add more connections if needed
#        continue

    def getCookiesJar(self):
        """
        returns cookies container
        """
        return self.__cookies_jar

    @synchronized
    def addCookieHeaders(self, request_adapter):
        """
        Adds the stored cookie/s to the request adapter:
        """
        self.getCookiesJar().add_cookie_header(request_adapter)

    @synchronized
    def storeCookies(self, response_adapter, request_adapter):
        """
        Stores the cookie/s located in the response adapter in request adapter:
        """
        self.getCookiesJar().extract_cookies(response_adapter, request_adapter)

    def get_url(self):
        return self.__url

    @property
    def context(self):
        return self.__context

    @synchronized
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

    def _freeResource(self, conn):
        with self.__rlock:
            conn = self.__busy_connections.pop(conn.get_id())
            self.__free_connections.put_nowait(conn)

    def __setattr__(self, name, value):
        if name in ['__context', 'context']:
            raise ImmutableError(name)
        else:
            super(ConnectionsPool, self).__setattr__(name, value)
