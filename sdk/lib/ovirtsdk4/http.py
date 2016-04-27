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


class Request(object):
    """
    This class represents an HTTP request.

    This class is intended for internal use by other components of the SDK.
    Refrain from using it directly as there is no backwards compatibility
    guarantee.
    """

    def __init__(
        self,
        method='GET',
        path='',
        query=None,
        headers=None,
        body=None,
    ):
        self.method = method
        self.path = path
        self.query = query if query is not None else {}
        self.headers = headers if headers is not None else {}
        self.body = body


class Response(object):
    """
    This class represents an HTTP response.

    This class is intended for internal use by other components of the SDK.
    Refrain from using it directly as there is no backwards compatibility
    guarantee.
    """

    def __init__(
        self,
        body=None,
        code=None,
        headers=None,
        message=None
    ):
        self.body = body
        self.code = code
        self.headers = headers if headers is not None else {}
        self.message = message
