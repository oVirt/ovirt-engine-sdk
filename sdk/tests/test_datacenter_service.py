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

import unittest

from nose.tools import (
    assert_is_not_none,
    assert_equal
)
from .server import TestServer


class DataCenterServiceTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.server = TestServer()
        cls.server.start_server()
        cls.connection = cls.server.connection()
        system_service = cls.connection.system_service()
        cls.data_centers_service = system_service.data_centers_service()

    @classmethod
    def teardown_class(cls):
        cls.connection.close()
        cls.server.stop_server()

    def test_get_service(self):
        """
        Check that reference to data centers service is not none
        """
        assert_is_not_none(self.data_centers_service)

    def test_get_list_of_data_centers(self):
        """
        Test returning empty data centers list
        """
        self.server.set_xml_response("datacenters", 200, "<data_centers/>")
        data_centers = self.data_centers_service.list()
        assert_is_not_none(data_centers)
        assert_equal(data_centers, [])

    def test_get_list_of_data_centers_with_search(self):
        """
        Test returning empty data centers list
        """
        self.server.set_xml_response("datacenters", 200, "<data_centers/>")
        data_centers = self.data_centers_service.list(search="name=ugly")
        assert_is_not_none(data_centers)
        assert_equal(data_centers, [])

    def test_get_data_center_by_id(self):
        """
        Test we don't get null data center service for existing
        data center id and correct object
        """
        self.server.set_xml_response(
            path="datacenters/123",
            code=200,
            body="<data_center id=\"123\"><name>testdc</name></data_center>"
        )
        dc = self.data_centers_service.data_center_service("123").get()
        assert_equal(dc.id, "123")
        assert_equal(dc.name, "testdc")
