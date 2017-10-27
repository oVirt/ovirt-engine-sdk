# -*- coding: utf-8 -*-

#
# Copyright (c) 2017 Red Hat, Inc.
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

from nose.tools import raises
from .server import TestServer


class ConnectionErrorTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.server = TestServer()
        cls.server.start_server()

    @classmethod
    def teardown_class(cls):
        cls.server.stop_server()

    @raises(sdk.ConnectionError)
    def test_incorrect_server_fqdn(self):
        """
        Fail if server has incorrect FQDN.
        """
        connection = sdk.Connection(
            username=self.server.user(),
            password=self.server.password(),
            insecure=True,
            url='https://300.300.300.300/ovirt-engine/api',
        )
        connection.test(raise_exception=True)
        connection.close()

    @raises(sdk.ConnectionError)
    def test_incorrect_server_address(self):
        """
        Fail if server has incorrect address.
        """
        connection = sdk.Connection(
            username=self.server.user(),
            password=self.server.password(),
            insecure=True,
            url='https://bad.host/ovirt-engine/api',
        )
        connection.test(raise_exception=True)
        connection.close()

