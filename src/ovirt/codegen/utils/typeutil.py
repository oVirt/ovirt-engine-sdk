'''
Created on Nov 3, 2011

@author: mpastern
'''

class TypeUtil(object):
    '''
    classdocs
    '''

#    @staticmethod
#    def getValueByKey(name, cache = {}):
#        if cache.has_key(name): return cache[name]
#        return name

    @staticmethod
    def getValueByKeyOrNone(name, cache={}):
        if cache.has_key(name): return cache[name]
        return None
