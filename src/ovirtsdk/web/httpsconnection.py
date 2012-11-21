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

import httplib
import socket
import ssl


class HTTPSConnection(httplib.HTTPSConnection):
    '''
    This class is httplib.HTTPSConnection decorator providing
    server certificate validation capabilities.
    '''

    def __init__(self, host, port=None, key_file=None, cert_file=None, ca_file=None,
                 strict=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        httplib.HTTPSConnection.__init__(self, host=host, port=port, key_file=key_file,
                                         cert_file=cert_file, strict=strict, timeout=timeout)
        self.ca_file = ca_file

    def connect(self):
        '''
        httplib.HTTPSConnection.connect() clone that connects to a host on a given (SSL) port, 
        but forcing ssl.CERT_REQUIRED if ca_file has been specified.
        '''

        sock = socket.create_connection((self.host, self.port),
                                        self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()

        if self.ca_file:
            self.sock = ssl.wrap_socket(sock,
                                        self.key_file,
                                        self.cert_file,
                                        ca_certs=self.ca_file,
                                        cert_reqs=ssl.CERT_REQUIRED)
        else:
            self.sock = ssl.wrap_socket(sock,
                                        self.key_file,
                                        self.cert_file,
                                        cert_reqs=ssl.CERT_NONE)
