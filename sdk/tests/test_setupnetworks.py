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


class SetupNetworksTest(unittest.TestCase):

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
        self.server.set_xml_response("hosts/123/setupnetworks", 200, "<action/>")
        hosts_service = self.connection.system_service().hosts_service()
        host_service = hosts_service.host_service('123')
        host_service.setup_networks(
            modified_bonds=[
                types.HostNic(
                    name='bond0',
                    bonding=types.Bonding(
                        options=[
                            types.Option(
                                name="mode",
                                type="4",
                            ),
                        ],
                        slaves=[
                            types.HostNic(
                                name='eth1',
                            ),
                            types.HostNic(
                                name='eth2',
                            ),
                        ],
                    ),
                ),
            ]
        )
        assert_equal(
            self.server.last_request_content,
            "<action>" +
              "<modified_bonds>" +
                "<host_nic>" +
                  "<bonding>" +
                    "<options>" +
                      "<option>" +
                        "<name>mode</name>" +
                        "<type>4</type>" +
                      "</option>" +
                    "</options>" +
                    "<slaves>" +
                      "<host_nic>" +
                        "<name>eth1</name>" +
                      "</host_nic>" +
                      "<host_nic>" +
                        "<name>eth2</name>" +
                      "</host_nic>" +
                    "</slaves>" +
                  "</bonding>" +
                  "<name>bond0</name>" +
                "</host_nic>" +
              "</modified_bonds>" +
            "</action>"
        )
