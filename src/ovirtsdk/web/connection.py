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

import base64
from httplib import HTTPConnection
import urllib
import urlparse
from ovirtsdk.web.httpsconnection import HTTPSConnection
from ovirtsdk.infrastructure.errors import NoCertificatesError, ImmutableError
import types
from ovirtsdk.infrastructure.context import context

class Connection(object):
    '''
    The oVirt api connection proxy
    '''
    def __init__(self, url, port, key_file, cert_file, ca_file, strict, timeout, username, password, manager, insecure=False, debug=False):
        self.__connection = self.__createConnection(url=url,
                                                    port=port,
                                                    key_file=key_file,
                                                    cert_file=cert_file,
                                                    ca_file=ca_file,
                                                    insecure=insecure,
                                                    strict=strict,
                                                    timeout=timeout)

        self.__connection.set_debuglevel(int(debug))
        self.__headers = self.__createStaticHeaders(username, password)
        self.__manager = manager
        self.__id = id(self)
        self.__insecure = insecure
        self.__context = manager.context

    def get_id(self):
        return self.__id

    def getConnection(self):
        return self.__connection

    def getDefaultHeaders(self):
        headers = self.__headers.copy()
        headers.update(self.__createDynamicHeaders())
        return headers

    def doRequest(self, method, url, body=urllib.urlencode({}), headers={}):
        return self.__connection.request(method, url, body, self.getHeaders(headers))

    def getHeaders(self, headers):
        extended_headers = self.getDefaultHeaders()
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
#FIXME: create connection watchdog to close it on idle-ttl expiration, rather than after the call
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


    def __createConnection(self, url, key_file=None, cert_file=None, ca_file=None, insecure=False, port=None, strict=None, timeout=None):
        u = self.__parse_url(url)

        if(u.scheme == 'https'):
            if not insecure and not ca_file:
                raise NoCertificatesError

            return HTTPSConnection(host=u.hostname,
                                   port=u.port,
                                   key_file=key_file,
                                   cert_file=cert_file,
                                   ca_file=ca_file,
                                   strict=strict,
                                   timeout=timeout)

        return HTTPConnection(host=u.hostname,
                              port=u.port,
                              strict=strict,
                              timeout=timeout)

    def __createStaticHeaders(self, username, password):
        auth = base64.encodestring("%s:%s" % (username, password)).strip()
        return {"Content-type" : "application/xml",
                "Authorization": "Basic %s" % auth}

    def __createDynamicHeaders(self):
        return {'Filter' : str(context.manager[self.context].get('filter'))}

    def __setattr__(self, name, value):
        if name in ['__context', 'context']:
            raise ImmutableError(name)
        else:
            super(Connection, self).__setattr__(name, value)

    id = property(get_id, None, None, None)
