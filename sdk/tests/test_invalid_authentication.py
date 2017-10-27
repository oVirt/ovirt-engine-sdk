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
    assert_equals,
    assert_raises,
)
from .server import TestServer


class InvalidAuthTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.server = TestServer()
        cls.server.start_server()

    @classmethod
    def teardown_class(cls):
        cls.server.stop_server()

    def test_invalid_credentials_oauth(self):
        """
        Test that proper JSON error message is returned when using invalid
        credentials with oauth.
        """
        connection = self.server.connection()
        self.server.set_json_response(
            path='%s/sso/oauth/token' % self.server.prefix(),
            code=401,
            body={
                'error': 'access_denied',
                'error_description': "Cannot authenticate user 'admin@internal': The username or password is incorrect..",
            },
        )
        with assert_raises(sdk.AuthError) as ctx:
            connection.authenticate()
        message = str(ctx.exception)
        assert_equals(
            "Error during SSO authentication access_denied : Cannot authenticate user 'admin@internal': "
            "The username or password is incorrect..",
            message
        )

    def test_invalid_credentials_openid(self):
        """
        Test that proper JSON error message is returned when using invalid
        credentials with openid.
        """
        connection = self.server.connection()
        self.server.set_json_response(
            path='%s/sso/oauth/token' % self.server.prefix(),
            code=401,
            body={
                'error': "Cannot authenticate user 'admin@internal': The username or password is incorrect..",
                'error_code': 'access_denied',
            },
        )
        with assert_raises(sdk.AuthError) as ctx:
            connection.authenticate()
        message = str(ctx.exception)
        assert_equals(
            "Error during SSO authentication access_denied : Cannot authenticate user 'admin@internal': "
            "The username or password is incorrect..",
            message
        )
