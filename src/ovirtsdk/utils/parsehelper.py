'''
Created on Oct 18, 2011

@author: mpastern
'''

import StringIO
from ovirtsdk.xml import params

class ParseHelper():
    '''Provides parsing capabilities'''

    @staticmethod
    def toXml(entity):
        '''Parse entity to corresponding XML representation'''
        output = StringIO.StringIO()
        type_name = type(entity).__name__.lower()
        entity.export(output, 0, name_=ParseHelper.getXmlTypeInstance(type_name))
        return output.getvalue()

    @staticmethod
    def getXmlWrapperType(type_name):
        tn = type_name.lower()
        for k, v in params._rootClassMap.items():
            if v.__name__.lower() == tn:
                return v.__name__
        return type_name

    @staticmethod
    def getXmlTypeInstance(type_name):
        tn = type_name.lower()
        for k, v in params._rootClassMap.items():
            if v.__name__.lower() == tn:
                return k
        return type_name

    @staticmethod
    def getSingularXmlTypeInstance(type_name):
        instance = ParseHelper.getXmlTypeInstance(type_name)
        if instance.endswith('s'):
            return instance[0 : len(instance) - 1]
        return instance

    @staticmethod
    def toType(fromItem, toType):
        '''Encapsulates the entity with the broker instance.'''
        return toType(fromItem)

    @staticmethod
    def toCollection(toType, fromItems=[]):
        '''Encapsulates the entities collection with the broker instance collection.'''
        new_coll = []
        for item in fromItems:
            new_coll.append(ParseHelper.toType(item, toType))
        return new_coll

    @staticmethod
    def toSubType(fromItem, toType, parent):
        '''Encapsulates the sub-entity with the broker instance.'''
        return toType(parent, fromItem)

    @staticmethod
    def toSubTypeFromCollection(toType, parent, fromItems=[]):
        '''Encapsulates the sub-entity collection element with the broker instance.'''
        return toType(parent, fromItems[0]) if(fromItems is not None and len(fromItems) > 0) else None

    @staticmethod
    def toTypeFromCollection(toType, fromItems=[]):
        '''Encapsulates the entity collection element with the broker instance.'''
        #return toType(fromItems[0]) if(fromItems is not None and len(fromItems) > 0) else None
        return toType(fromItems[0] if(fromItems is not None and len(fromItems) > 0) else None)

    @staticmethod
    def toSubCollection(toType, parent, fromItems=[]):
        '''Encapsulates the sub-entities collection with the broker instance collection.'''
        new_coll = []
        for fromItem in fromItems:
            new_coll.append(ParseHelper.toSubType(fromItem, toType, parent))
        return new_coll
