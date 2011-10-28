'''
Created on Oct 23, 2011

@author: mpastern
'''

import threading
from ovirt.infrastructure.errors import ImmutableError

cache = {}
lock = threading.RLock()

class __Item():
    def __init__(self, val, mode):
        self.__val  = val
        self._mode  = mode

    def get_val(self):
        return self.__val


    def get_mode(self):
        return self.__mode

    val  = property(get_val, None, None, None)
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
        
    def __eq__(self,y):
        return self.value == y.value
    
def add(key, val, mode=Mode.RW):
    ''' 
    stores the value in cache
    
    @param key:  is the cache key
    @param val:  is the cache value
    @param mode: is the access mode [r|rw]
    '''
    with lock:
        if (mode is Mode.R and cache.has_key(key)):
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
        if (cache.has_key(key)):
            if (remove):
                item = cache[key]
                if (item.mode is Mode.RW):
                    item = cache.pop(key)
                    return item.val
                else: raise ImmutableError(key)
            else: return cache[key].val
        return None

def remove(key):
    ''' 
    removes the value from cache
    
    @param key: is the cache key
    '''    
    with lock: 
        if (cache.has_key(key)):
            item = cache[key]
            if (item.mode is Mode.RW):
                cache.pop(key)
            else: raise ImmutableError(key)