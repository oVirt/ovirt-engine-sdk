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
    assert_equal,
)
from .server import TestServer


class ClusterServiceTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.server = TestServer()
        cls.server.start_server()
        cls.connection = cls.server.connection()
        system_service = cls.connection.system_service()
        cls.clusters_service = system_service.clusters_service()

    @classmethod
    def teardown_class(cls):
        cls.connection.close()
        cls.server.stop_server()

    def test_get_service(self):
        """
        Check that reference to clusters service is not none
        """
        assert_is_not_none(self.clusters_service)

    def test_get_list_of_clusters(self):
        """
        Test returning empty clusters list
        """
        self.server.set_xml_response("clusters", 200, "<clusters/>")
        clusters = self.clusters_service.list()
        assert_is_not_none(clusters)
        assert_equal(clusters, [])

    def test_get_list_of_clusters_with_search(self):
        """
        Test returning empty clusters list
        """
        self.server.set_xml_response("clusters", 200, "<clusters/>")
        clusters = self.clusters_service.list(search="name=ugly")
        assert_is_not_none(clusters)
        assert_equal(clusters, [])

    def test_get_cluster_by_id(self):
        """
        Test we don't get null cluster service for existing
        cluster id and correct object
        """
        self.server.set_xml_response(
            path="clusters/123",
            code=200,
            body="<cluster id=\"123\"><name>testcluster</name></cluster>"
        )
        cluster = self.clusters_service.cluster_service("123").get()
        assert_equal(cluster.id, "123")
        assert_equal(cluster.name, "testcluster")
