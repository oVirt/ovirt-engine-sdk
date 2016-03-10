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


class List(list):
    """
    This is the base class for all the list types of the SDK. It contains the
    utility methods used by all of them.
    """

    def __init__(self, href=None):
        super(List, self).__init__()
        self._href = href

    @property
    def href(self):
        """
        Returns the value of the `href` attribute.
        """
        return self._href

    @href.setter
    def href(self, value):
        """
        Sets the value of the `href` attribute.
        """
        self._href = value
