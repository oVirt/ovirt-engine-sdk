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

import socket
from ovirtsdk.infrastructure.errors import RequestError, ConnectionError
from ovirtsdk.xml import params

class Proxy():
    '''
    The proxy to web connection
    '''
    def __init__(self, connections_pool):
        """Constructor."""
        self.__connections_pool = connections_pool

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

    def request(self, method, url, body=None, headers={}):
        return self.__doRequest(method, \
                                url, \
                                body=body, \
                                headers=headers, \
                                conn=self.getConnectionsPool().getConnection())

    def __doRequest(self, method, url, conn, body=None, headers={}):
        try:
            conn.doRequest(method=method, url=url, body=body, headers=headers)
            response = conn.getResponse()
            if response.status < 400:
                res = response.read()
                return params.parseString(res) if res is not None and res is not '' else res
            else:
                raise RequestError, response
        except socket.error, e:
            raise ConnectionError, str(e)
        finally:
            conn.close()

    def get_url(self):
        return self.getConnectionsPool().get_url()

    @staticmethod
    def instance(connections_pool):
        Proxy(connections_pool)
