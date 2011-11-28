'''
Created on Oct 23, 2011

@author: mpastern
'''
from ovirtsdk.infrastructure import contextmanager

class Base(object):
    ''' Returns the proxy to connections pool '''
    def _getProxy(self):
#FIXME: consider creating new proxy for each call so it will be executed
        #on separate thread heap space

#FIXME: manage cache peer API instance  
        return contextmanager.get('proxy')

    def __getattr__(self, item):
        return self.superclass.__getattribute__(item)
