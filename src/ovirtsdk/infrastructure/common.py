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

from ovirtsdk.infrastructure import contextmanager
from ovirtsdk.utils.comperator import Comparator
from ovirtsdk.infrastructure.errors import DisconnectedError

class Base(object):
    ''' Returns the proxy to connections pool '''
    def _getProxy(self):
#FIXME: manage cache peer API instance  
        proxy = contextmanager.get('proxy')
        if proxy:
            return proxy
        #This may happen if sdk got explicitly disconnected
        #using .disconnect() method, but resource instance is
        #still available at client's code.
        raise DisconnectedError

    def __getattr__(self, item):
        if not self.__dict__.has_key('superclass'):
            return self.__getattribute__(item)
        return self.superclass.__getattribute__(item)

    def __eq__(self, other):
        return Comparator.compare(self, other)

    def __ne__(self, other):
        return not self.__eq__(other)
