#
# Copyright (c) 2010 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from ovirtsdk.infrastructure.contextmanager import ContextManager
from ovirtsdk.infrastructure.errors import ImmutableError


class Context(object):
    """ The oVirt Context container """

    def __init__(self):
        self.__manager = ContextManager()

    def __setattr__(self, name, value):
        if name in ['__manager', 'manager']:
            raise ImmutableError(name)
        else:
            super(Context, self).__setattr__(name, value)

    @property
    def manager(self):
        """ The oVirt context manager """
        return self.__manager

context = Context()
