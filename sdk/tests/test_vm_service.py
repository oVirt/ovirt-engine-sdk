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

from nose.tools import (
    assert_is_not_none,
    assert_equal
)
from .server import TestServer


class VmServiceTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.server = TestServer()
        cls.server.start_server()
        cls.connection = cls.server.connection()
        system_service = cls.connection.system_service()
        cls.vms_service = system_service.vms_service()

    @classmethod
    def teardown_class(cls):
        cls.connection.close()
        cls.server.stop_server()

    def test_get_service(self):
        """
        Check that reference to vm service is not none
        """
        assert_is_not_none(self.vms_service)

    def test_get_list_of_vms(self):
        """
        Test returning empty vm list
        """
        self.server.set_xml_response("vms", 200, "<vms/>")
        vms = self.vms_service.list()
        assert_is_not_none(vms)
        assert_equal(vms, [])

    def test_get_list_of_storage_domains_with_search(self):
        """
        Test returning empty vms list
        """
        self.server.set_xml_response("vms", 200, "<vms/>")
        vms = self.vms_service.list(search="name=ugly")
        assert_is_not_none(vms)
        assert_equal(vms, [])

    def test_get_vm_by_id(self):
        """
        Test we don't get null vm service for existing
        vm id and correct object
        """
        self.server.set_xml_response(
            path="vms/123",
            code=200,
            body="<vm id=\"123\"><name>testvm</name></vm>"
        )
        dc = self.vms_service.vm_service("123").get()
        assert_equal(dc.id, "123")
        assert_equal(dc.name, "testvm")

    def test_add_vm_with_clone_parameter(self):
        """
        Test when adding clone vm the query with this parameter is sent.
        """
        self.server.set_xml_response("vms", 201, "<vm/>")
        self.vms_service.add(types.Vm(), clone=True)
        assert_equal(self.server.last_request_query, 'clone=true')

    def test_add_vm_with_clone_and_clone_permissions_parameters(self):
        """
        Test when adding vm clone and clone_permissions the query with
        those parameters is sent.
        """
        self.server.set_xml_response("vms", 201, "<vm/>")
        self.vms_service.add(
            types.Vm(),
            clone=True,
            clone_permissions=True
        )
        assert_equal(
            self.server.last_request_query,
            'clone=true&clone_permissions=true'
        )

    def test_response_200_not_raise_exception(self):
        """
        Test when server return response with 200 code,
        the SDK don't raise exception.
        """
        self.server.set_xml_response("vms", 200, "<vm/>")
        self.vms_service.add(types.Vm())

    def test_response_201_not_raise_exception(self):
        """
        Test when server return response with 201 code,
        the SDK don't raise exception.
        """
        self.server.set_xml_response("vms", 201, "<vm/>")
        self.vms_service.add(types.Vm())

    def test_response_202_not_raise_exception(self):
        """
        Test when server return response with 202 code,
        the SDK don't raise exception.
        """
        self.server.set_xml_response("vms", 202, "<vm/>")
        self.vms_service.add(types.Vm())


    def test_start_with_custom_parameter(self):
        """
        Test that sending one parameter a request is sent with that parameter.
        """
        self.server.set_xml_response("vms/123/start", 200, "<action/>")
        self.vms_service.vm_service("123").start(query={'my': 'value'})
        assert_equal(self.server.last_request_query, 'my=value')

    def test_start_with_two_custom_parameters(self):
        """
        Test that sending two parameters a request is sent with that two parameters.
        """
        self.server.set_xml_response("vms/123/start", 200, "<action/>")
        self.vms_service.vm_service("123").start(
            query={'my': 'value', 'your': 'value'}
        )
        assert_equal(self.server.last_request_query, 'my=value&your=value')

    def test_start_with_custom_header(self):
        """
        Test that sending one header a request is sent with that header.
        """
        self.server.set_xml_response("vms/123/start", 200, "<action/>")
        self.vms_service.vm_service("123").start(headers={'my': 'value'})
        assert_equal(self.server.last_request_headers.get('my'), 'value')

    def test_start_with_two_custom_headers(self):
        """
        Test that sending two headers a request is sent with that two headers.
        """
        self.server.set_xml_response("vms/123/start", 200, "<action/>")
        self.vms_service.vm_service("123").start(
            headers={'my': 'value', 'your': 'value'}
        )
        assert_equal(self.server.last_request_headers.get('my'), 'value')
        assert_equal(self.server.last_request_headers.get('your'), 'value')

    def test_add_vm_with_custom_parameter(self):
        """
        Test that adding a VM with one parameter a request is sent with that parameter.
        """
        self.server.set_xml_response("vms", 201, "<vm/>")
        self.vms_service.add(types.Vm(), query={'my': 'value'})
        assert_equal(self.server.last_request_query, 'my=value')

    def test_add_vm_with_two_custom_parameters(self):
        """
        Test that adding a VM with two parameters a request is sent with that two parameters.
        """
        self.server.set_xml_response("vms", 201, "<vm/>")
        self.vms_service.add(types.Vm(), query={'my': 'value', 'your': 'value'})
        assert_equal(self.server.last_request_query, 'my=value&your=value')

    def test_add_vm_with_custom_header(self):
        """
        Test that adding a VM with one header a request is sent with that header.
        """
        self.server.set_xml_response("vms", 201, "<vm/>")
        self.vms_service.add(types.Vm(), headers={'my': 'value'})
        assert_equal(self.server.last_request_headers.get('my'), 'value')

    def test_add_vm_with_two_custom_headers(self):
        """
        Test that adding a VM with two headers a request is sent with that two headers.
        """
        self.server.set_xml_response("vms", 201, "<vm/>")
        self.vms_service.add(types.Vm(), headers={'my': 'value', 'your': 'value'})
        assert_equal(self.server.last_request_headers.get('my'), 'value')
        assert_equal(self.server.last_request_headers.get('your'), 'value')