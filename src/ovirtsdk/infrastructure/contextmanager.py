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

cache = {}
lock = threading.RLock()

class __Item():
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

def add(key, val, mode=Mode.RW):
    ''' 
    stores the value in cache
    
    @param key:  is the cache key
    @param val:  is the cache value
    @param mode: is the access mode [r|rw]
    '''
    with lock:
        if mode is Mode.R and cache.has_key(key):
            raise ImmutableError(key)
        else:
            cache[key] = __Item(val, mode)

def get(key, remove=False):
    ''' 
    retrieves the value from the cache
    
    @param key: is the cache key
    @param remove: removes the value from cache [true|false]
    '''
    with lock:
        if cache.has_key(key):
            if  remove:
                item = cache[key]
                if item.mode is Mode.RW:
                    item = cache.pop(key)
                    return item.val
                else: raise ImmutableError(key)
            else: return cache[key].val
        return None

def _clear(force=False):
    ''' 
    removes all items from the cache
    
    @param force: force remove regardless cache mode
    '''
    with lock:
        from ovirtsdk.infrastructure import contextmanager
        for item in cache.keys():
            contextmanager._remove(key=item, force=force)

def _remove(key, force=False):
    ''' 
    removes the value from cache
    
    @param key: is the cache key
    @param force: force remove regardless cache mode
    '''
    with lock:
        if cache.has_key(key):
            item = cache[key]
            if (item.mode is Mode.RW) or force:
                cache.pop(key)
            else: raise ImmutableError(key)
