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

import ovirtsdk4.types as types
import unittest

from nose.tools import assert_equal
from .server import TestServer


class IscsiDiscoverTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.server = TestServer()
        cls.server.start_server()
        cls.connection = cls.server.connection()

    @classmethod
    def teardown_class(cls):
        cls.connection.close()
        cls.server.stop_server()

    def test_action_parameters(self):
        """
        Test if action parameters are constructed in correct way.
        """
        self.server.set_xml_response("hosts/123/iscsidiscover", 200, "<action/>")
        hosts_service = self.connection.system_service().hosts_service()
        host_service = hosts_service.host_service('123')
        host_service.iscsi_discover(
            iscsi=types.IscsiDetails(
                address='iscsi.example.com',
                port=3260,
            ),
        )
        assert_equal(
            self.server.last_request_content,
            "<action>" +
              "<iscsi>" +
                "<address>iscsi.example.com</address>" +
                "<port>3260</port>" +
              "</iscsi>" +
            "</action>"
        )
