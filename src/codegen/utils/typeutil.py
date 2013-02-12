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

from ovirtsdk.utils.ordereddict import OrderedDict

class TypeUtil(object):
    '''
    Providing type related services
    '''

    @staticmethod
    def getValueByKeyOrNone(name, cache={}):
        '''
        Returns key if exist or None
        
        @param name: key name
        @param cache: map to look at 
        '''
        if cache.has_key(name):
            return cache[name]
        return None

    @staticmethod
    def toOrderedMap(lst=[]):
        '''
        Formats list in to map preserving list order in map
        
        @param lst: list to convert
        '''
        dct = OrderedDict()
        for i in range(len(lst)):
            if (i % 2 is 0):
                coll = lst[i]
                res = lst[i + 1] if ((i + 1 < len(lst))) else None
                dct[coll] = res
        return dct
