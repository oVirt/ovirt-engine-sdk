'''
Created on Oct 25, 2011

@author: mpastern
'''

class Collection(object):
    '''
    The Collection data holder
    '''
    def __init__(self, name, body):
        self.name = name
        self.body = body
        # methods{name:body}
        self.methods = {}
        self.resource = None

    def getResource(self):
        return self.resource

    def setResource(self, value):
        self.resource = value

    def hasResource(self, value):
        return self.resource is not None

    def addMethod(self, name, body):
        self.methods[name] = body

    def hasMethod(self, name):
        return self.methods.has_key(name)

    def getMethod(self, name):
        if self.hasMethod(name):
            return self.methods[name]
        return None
