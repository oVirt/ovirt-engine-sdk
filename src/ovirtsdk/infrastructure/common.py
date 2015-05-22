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

from ovirtsdk.utils.comperator import Comparator
from ovirtsdk.infrastructure.errors import ImmutableError

class Base(object):
    ''' Decorator base class '''

    def __init__(self, context):
        self.__context = context

    @property
    def context(self):
        return self.__context

    def __getattr__(self, item):
        if not 'superclass' in self.__dict__:
            return self.__getattribute__(item)
        return self.superclass.__getattribute__(item)

    def __eq__(self, other):
        return Comparator.compare(self, other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __setattr__(self, name, value):
        if name in ['__context', 'context']:
            raise ImmutableError(name)
        else:
            super(Base, self).__setattr__(name, value)

    def export_(self, outfile, level, namespace_='', name_='', namespacedef_='', pretty_print=True):
        # This empty method is necessary in order to avoid exceptions when the
        # infrastructure tries to invoke it on a collection decorator that is
        # used as a parameter.
        pass
