'''
Created on Oct 23, 2011

@author: mpastern
'''
from ovirt.infrastructure import contextmanager

class Base(object):
    ''' Returns the proxy to connections pool '''
    def _getProxy(self):
#FIXME: consider creating new proxy for each call so it will be executed
        #on separate thread heap space
        
#FIXME: manage cache peer API instance  
        return contextmanager.get('proxy')
    
    def __getattr__(self, item):
        return self.superclass.__getattribute__(item)
    
    def __setattr__(self,  item, value):
#FIXME: find better solution than predefining the sub-collection
        if item is not 'superclass'\
            and item is not 'parentclass'\
            and self.__dict__.has_key('superclass')\
            and not self.__dict__.has_key(item)\
            and self.__dict__['superclass'].__dict__.has_key(item):
            self.__dict__['superclass'].__dict__[item] = value
        else:
            self.__dict__[item] = value