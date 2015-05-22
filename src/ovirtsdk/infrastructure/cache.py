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

import threading
from ovirtsdk.infrastructure.errors import ImmutableError
import types


class Item():
    """ Cache item """

    def __init__(self, val, mode):
        self.__val = val
        self.__mode = mode

    def get_val(self):
        return self.__val

    def get_mode(self):
        return self.__mode

    val = property(get_val, None, None, None)
    mode = property(get_mode, None, None, None)

class Mode():
    """ Cache mode """

    RW, R = range(2)

    def __init__(self, Type):
        self.value = Type

    def __str__(self):
        if self.value == Mode.RW:
            return 'ReadWrite'
        if self.value == Mode.R:
            return 'Read'

    def __eq__(self, y):
        return self.value == y.value

class Cache(object):
    """ The oVirt cache container """

    def __init__(self):
        self.__cache = {}
        self.__lock = threading.RLock()

    def add(self, key, val, mode=Mode.RW, typ=None):
        '''
        Stores the value in cache

        @param key:  is the cache key
        @param val:  is the cache value
        [@param mode: is the access mode [r|rw]]
        [@param typ: type to cast value to]

        @raise TypeError: when value cannot be cast to the typ
        '''
        with self.__lock:
            if mode is Mode.R and key in self.__cache:
                raise ImmutableError(key)
            elif typ:
                try:
                    if typ == bool and type(val) == str \
                        and val not in ['True', 'False']:
                        raise ValueError(val)
                    self.__cache[key] = Item(typ(val), mode)
                except ValueError:
                    raise TypeError(
                             key + "=" + val,
                             str(typ) + ' is expected.'
                          )
            else:
                self.__cache[key] = Item(val, mode)

    def pop(self, key, force=False):
        '''
        Retrieves and then removes the value from the cache

        @param key: is the cache key
        '''

        return self.get(key=key, remove=True)

    def get(self, key, remove=False):
        '''
        Retrieves the value from the cache

        @param key: is the cache key
        [@param remove: removes the value from cache [true|false]]
        '''
        with self.__lock:
            if key in self.__cache:
                if  remove:
                    item = self.__cache[key]
                    if item.mode is Mode.RW:
                        item = self.__cache.pop(key)
                        return item.val
                    else: raise ImmutableError(key)
                else: return self.__cache[key].val
            return None

    def clear(self, force=False):
        '''
        Removes all items from the cache

        [@param force: force remove regardless cache mode]
        '''
        with self.__lock:
            # We need to make a copy of the list of keys, as it will be
            # modified as we iterate and that causes exceptions in
            # Python 3:
            keys = list(self.__cache.keys())
            for item in keys:
                self.remove(key=item, force=force)

    def remove(self, key, force=False):
        '''
        Removes the value from cache

        @param key: is the cache key
        [@param force: force remove regardless cache mode]
        '''
        with self.__lock:
            if key in self.__cache:
                item = self.__cache[key]
                if (item.mode is Mode.RW) or force:
                    self.__cache.pop(key)
                else: raise ImmutableError(key)
