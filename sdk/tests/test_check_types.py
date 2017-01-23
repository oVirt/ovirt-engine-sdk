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

import ovirtsdk4.services as services
import ovirtsdk4.types as types
import unittest

from nose.tools import (
    assert_in,
    assert_raises,
)
from .server import TestServer


class CheckTypesTest(unittest.TestCase):

    def test_service_type_error(self):
        """
        Test that calling a method with multiple wrong parameter types
        generates an informative exception.
        """
        vm_service = services.VmService(None, None)
        with assert_raises(TypeError) as context:
            vm_service.start(
                use_cloud_init='true',
                vm=types.Disk(),
            )
        message = str(context.exception)
        assert_in(
            "The 'use_cloud_init' parameter should be of type 'bool', "
            "but it is of type 'str'",
            message
        )
        assert_in(
            "The 'vm' parameter should be of type 'Vm', but it is of "
            "type 'Disk'",
            message
        )

    def test_locator_type_error(self):
        """
        Test that calling a service locator with a wrong parameter type
        generates an informative exception.
        """
        vms_service = services.VmsService(None, None)
        with assert_raises(TypeError) as context:
            vms_service.vm_service(types.Vm())
        message = str(context.exception)
        assert_in(
            "The 'id' parameter should be of type 'str', but it is of "
            "type 'Vm'.",
            message
        )
