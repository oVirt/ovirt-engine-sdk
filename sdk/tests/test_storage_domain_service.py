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


class StorageDomainServiceTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.server = TestServer()
        cls.server.start_server()
        cls.connection = cls.server.connection()
        system_service = cls.connection.system_service()
        cls.sd_service = system_service.storage_domains_service()

    @classmethod
    def teardown_class(cls):
        cls.connection.close()
        cls.server.stop_server()

    def test_get_service(self):
        """
        Check that reference to storage domains service is not none
        """
        assert_is_not_none(self.sd_service)

    def test_get_list_of_storage_domains(self):
        """
        Test returning empty storage domains list
        """
        self.server.set_xml_response(
            "storagedomains", 200, "<storage_domains/>"
        )
        storage_domains = self.sd_service.list()
        assert_is_not_none(storage_domains)
        assert_equal(storage_domains, [])

    def test_get_list_of_storage_domains_with_search(self):
        """
        Test returning empty storage domains list
        """
        self.server.set_xml_response(
            "storagedomains", 200, "<storage_domains/>"
        )
        storage_domains = self.sd_service.list(search="name=ugly")
        assert_is_not_none(storage_domains)
        assert_equal(storage_domains, [])

    def test_get_storage_domain_by_id(self):
        """
        Test we don't get null storage domain service for existing
        storage domain id and correct object
        """
        self.server.set_xml_response(
            path="storagedomains/123",
            code=200,
            body="<storage_domain id=\"123\"><name>testsd</name></storage_domain>"
        )
        dc = self.sd_service.storage_domain_service("123").get()
        assert_equal(dc.id, "123")
        assert_equal(dc.name, "testsd")
