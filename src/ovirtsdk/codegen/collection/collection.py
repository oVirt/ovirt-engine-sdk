'''
Created on Oct 24, 2011

@author: mpastern
'''
#============================================================
#=======================COLLECTION RESOURCE==================
#============================================================
from ovirtsdk.utils.parsehelper import ParseHelper
from ovirtsdk.codegen.utils.typeutil import TypeUtil
from ovirtsdk.codegen.doc.documentation import Documentation

class Collection(object):

    @staticmethod
    def collection(collection_name):
        collection_resource_template_values = {'collection_name':collection_name}

        collection_resource_template = \
        ("class %(collection_name)s(Base):\n" + \
        "    def __init__(self):\n" + \
        "        \"\"\"Constructor.\"\"\"\n\n") % collection_resource_template_values

        return collection_resource_template

    @staticmethod
    def get(url, resource_type, link, KNOWN_WRAPPER_TYPES={}):
        actual_resource_type = TypeUtil.getValueByKeyOrNone(resource_type.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(resource_type.lower())).lower()

        collection_get_template_values = {'url':url,
                                          'resource_name_lc':actual_resource_name_lc,
                                          'resource_type' : actual_resource_type if actual_resource_type is not None else resource_type}

        collection_get_template = \
        ("    def get(self, name='*', **kwargs):\n" + \
         Documentation.document(link, {'name: the name of the entity':False,
                                       '**kwargs: property based filtering"': False}) +
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_%(resource_name_lc)s()\n" + \
        "        return %(resource_type)s(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))\n\n") % collection_get_template_values

        return collection_get_template

    @staticmethod
    def list(url, resource_type, link, KNOWN_WRAPPER_TYPES={}):
        actual_resource_type = TypeUtil.getValueByKeyOrNone(resource_type.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(resource_type.lower())).lower()

        collection_list_template_values = {'url':url,
                                           'resource_name_lc':actual_resource_name_lc,
                                           'resource_type' : actual_resource_type if actual_resource_type is not None else resource_type}

        collection_list_template = \
        ("    def list(self, query=None, **kwargs):\n" + \
         Documentation.document(link, {'query: oVirt engine dialect query':False,
                                       '**kwargs: property based filtering"': False}) +
        "        url='%(url)s'\n\n" + \
        "        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_%(resource_name_lc)s()\n" + \
        "        return ParseHelper.toCollection(%(resource_type)s,\n" + \
        "                                        FilterHelper.filter(result, kwargs))\n\n") % collection_list_template_values

        return collection_list_template

    @staticmethod
    def add(url, body_type, response_type, link, KNOWN_WRAPPER_TYPES={}):
        actual_resource_type = TypeUtil.getValueByKeyOrNone(response_type.lower(), KNOWN_WRAPPER_TYPES)

        collection_add_template_values = {'url':url,
                                          'resource_to_add_lc':body_type.lower(),
                                          'resource_type' : actual_resource_type if actual_resource_type is not None else response_type}

        collection_add_template = \
        ("    def add(self, %(resource_to_add_lc)s):\n" + \
         Documentation.document(link) +
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().add(url=url,\n" + \
        "                                      body=ParseHelper.toXml(%(resource_to_add_lc)s))\n" + \
        "        return %(resource_type)s(result)\n\n") % collection_add_template_values

        return collection_add_template

