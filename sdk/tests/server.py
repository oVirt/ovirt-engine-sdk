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

import json
import os.path
import ovirtsdk4 as sdk
import re
import socket
import ssl

try:
  from http.server import HTTPServer, BaseHTTPRequestHandler
  from http.server import SimpleHTTPRequestHandler
except ImportError:
  from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
  from SimpleHTTPServer import SimpleHTTPRequestHandler

from threading import Thread
from time import sleep

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class TestHandler(SimpleHTTPRequestHandler):
    # Path handlers:
    handlers = {}

    def log_message(self, format, *args):
        """
        Empty method, so we don't mix output of HTTP server with tests
        """
        pass

    def do_GET(self):
        params = urlparse(self.path)

        if params.path in self.handlers:
            self.handlers[params.path](self)
        else:
            SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        params = urlparse(self.path)

        if params.path in self.handlers:
            self.handlers[params.path](self)
        else:
            SimpleHTTPRequestHandler.do_POST(self)


class TestServer(object):
    # The authentication details used by the embedded tests web server:
    REALM = 'API'
    USER = 'admin@internal'
    PASSWORD = 'vzhJgfyaDPHRhg'
    TOKEN = 'bvY7txV9ltmmRQ'

    # The host and port and path used by the embedded tests web server:
    HOST = 'localhost'
    PREFIX = '/ovirt-engine'
    PORT = None

    # The embedded web server:
    _httpd = None
    # Thread for http server:
    _thread = None

    def _get_request_content(self, handler):
        content_len = int(handler.headers.get('content-length', 0))
        content = handler.rfile.read(content_len).decode('utf-8')
        content = re.sub(r">\s+<", "><", content)
        return content.strip()

    def set_xml_response(self, path, code, body, delay=0):
        def _handle_request(handler):
            # Store request query parameter:
            self.last_request_query = urlparse(handler.path).query
            # Store request content:
            self.last_request_content = self._get_request_content(handler)
            # Store request headers:
            self.last_request_headers = handler.headers

            authorization = handler.headers.get('Authorization')
            if authorization != "Bearer %s" % self.TOKEN:
                handler.send_response(401)
                handler.wfile.write('')
            else:
                sleep(delay)
                handler.send_response(code)
                handler.send_header('Content-Type', 'application/xml')
                handler.end_headers()

                data = body.encode('utf-8')
                handler.wfile.write(data)

        TestHandler.handlers[
            '%s/api%s' % (self.prefix(), '/%s' % path if path else '')
        ] = _handle_request

    def set_json_response(self, path, code, body):
        def _handle_request(handler):
            handler.send_response(code)
            handler.send_header('Content-Type', 'application/json')
            handler.end_headers()

            data = json.dumps(body, ensure_ascii=False).encode('utf-8')
            handler.wfile.write(data)

        TestHandler.handlers[path] = _handle_request

    def start_server(self, host='localhost'):
        self._httpd = HTTPServer((self.host(), self.port()), TestHandler)
        self._httpd.socket = ssl.wrap_socket(
            self._httpd.socket,
            keyfile=self.__absolute_path('%s.key' % host),
            certfile=self.__absolute_path('%s.crt' % host),
            server_side=True
        )
        # Path handler for username/password authentication service:
        self.set_json_response(
            path='%s/sso/oauth/token' % self.prefix(),
            code=200,
            body={"access_token": self.TOKEN}
        )
        # SSO Logout service:
        self.set_json_response(
            path='%s/services/sso-logout' % self.prefix(),
            code=200,
            body={"access_token": self.TOKEN}
        )
        # Path handler for Kerberos authentication service:
        self.set_json_response(
            path='%s/sso/oauth/token-http-auth' % self.prefix(),
            code=200,
            body={"access_token": self.TOKEN}
        )

        # Server requests in different thread, because it block current thread
        self._thread = Thread(target=self._httpd.serve_forever)
        self._thread.start()

    def stop_server(self):
        self._httpd.shutdown()
        self._thread.join()

    def port(self):
        if self.PORT is None:
            server = None
            for port in range(60000, 61000):
                try:
                    server = HTTPServer(
                        (self.host(), port),
                        BaseHTTPRequestHandler
                    )
                    self.PORT = port
                    break
                except socket.error:
                    pass
            if server is None:
                raise Exception("Can't find a free port")

        return self.PORT

    def prefix(self):
        return self.PREFIX

    def url(self):
        return "https://{host}:{port}{prefix}/api".format(
            host=self.host(),
            port=self.port(),
            prefix=self.prefix(),
        )

    def ca_file(self):
        return self.__absolute_path('ca.crt')

    def user(self):
        return self.USER

    def password(self):
        return self.PASSWORD

    def host(self):
        return self.HOST

    def connection(self, headers=None):
        return sdk.Connection(
            url=self.url(),
            username=self.user(),
            password=self.password(),
            ca_file=self.ca_file(),
            headers=headers,
        )

    def __absolute_path(self, str):
        return os.path.join(os.path.dirname(__file__), 'pki/%s' % str)
