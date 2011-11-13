'''
Created on Oct 25, 2011

@author: mpastern
'''

class Resource(object):

    def __init__(self, name, body):
        self.name = name
        self.body = body
        # methods{name:body}
        self.methods = {}
        self.subcollections = {}

    def addMethod(self, name, body):
        self.methods[name] = body

    def hasMethod(self, name):
        return self.methods.has_key(name)

    def getMethod(self, name):
        if self.hasMethod(name):
            return self.methods[name]
        return None
    def addSubCollection(self, name, sub_collection):
        self.subcollections[name] = sub_collection

    def hasSubCollection(self, name):
        return self.subcollections.has_key(name)

    def getSubCollection(self, name):
        if self.hasSubCollection(name):
            return self.subcollections[name]
        return None
