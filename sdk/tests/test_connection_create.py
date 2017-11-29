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

import ovirtsdk4 as sdk
import unittest

from nose.tools import (
    assert_true,
    raises
)
from .server import TestServer


class ConnectionCreateTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.server = TestServer()
        cls.server.set_xml_response("", 200, "<api/>")
        cls.server.start_server()

    @classmethod
    def teardown_class(cls):
        cls.server.stop_server()

    @raises(sdk.Error)
    def test_secure_mode_without_ca(self):
        """
        Test connection can be created when no CA is provided
        """
        connection = sdk.Connection(
            url=self.server.url(),
            username=self.server.user(),
            password=self.server.password(),
            ca_file='ugly.pem'
        )
        connection.authenticate()
        connection.close()

    def test_secure_mode_with_ca(self):
        """
        Test no exception is thrown when CA is provided to connection
        """
        connection = sdk.Connection(
            url=self.server.url(),
            username=self.server.user(),
            password=self.server.password(),
            ca_file=self.server.ca_file(),
        )
        connection.authenticate()
        connection.close()

    def test_insecure_mode_without_ca(self):
        """
        Test that CA isn't required in insecure mode
        """
        connection = sdk.Connection(
            url=self.server.url(),
            username=self.server.user(),
            password=self.server.password(),
            insecure=True,
        )
        connection.authenticate()
        connection.close()

    def test_kerberos_auth(self):
        """
        Test creation of kerberos connection
        """
        connection = sdk.Connection(
            url=self.server.url(),
            kerberos=True,
            ca_file=self.server.ca_file(),
        )
        connection.authenticate()
        connection.close()

    @raises(sdk.Error)
    def test_invalid_header(self):
        """
        When invalid header is used Error should be raised
        """
        request = sdk.http.Request(
            method='GET',
            headers={'X-header': 'žčě'},
        )
        connection = self.server.connection()
        connection.send(request)

    def test_valid_header(self):
        """
        When valid header is properly encoded and sent
        """
        request = sdk.http.Request(
            method='GET',
            headers={
                'X-header1': u'ABCDEF123',
                'X-header2': 'ABCDEF123',
            },
        )
        connection = self.server.connection()
        connection.send(request)
        connection.close()
