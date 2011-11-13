'''
Created on Oct 24, 2011

@author: mpastern
'''
#============================================================
#=======================COLLECTION RESOURCE==================
#============================================================
from ovirt.utils.parsehelper import ParseHelper
from ovirt.codegen.utils.typeutil import TypeUtil

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
    def get(url, resource_name_lc, resource_type, KNOWN_WRAPPER_TYPES={}):
        actual_resource_type = TypeUtil.getValueByKeyOrNone(resource_type.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(resource_name_lc.lower())).lower()

        collection_get_template_values = {'url':url,
                                          'resource_name_lc':actual_resource_name_lc,
                                          'resource_type' : actual_resource_type if actual_resource_type is not None else resource_type}

        collection_get_template = \
        ("    def get(self, name='*', **kwargs):\n" + \
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_%(resource_name_lc)s()\n" + \
        "        return %(resource_type)s(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))\n\n") % collection_get_template_values

        return collection_get_template

    @staticmethod
    def list(url, resource_name_lc, resource_type, KNOWN_WRAPPER_TYPES={}):
        actual_resource_type = TypeUtil.getValueByKeyOrNone(resource_type.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(resource_name_lc.lower())).lower()

        collection_list_template_values = {'url':url,
                                           'resource_name_lc':actual_resource_name_lc,
                                           'resource_type' : actual_resource_type if actual_resource_type is not None else resource_type}

        collection_list_template = \
        ("    def list(self, query=None, **kwargs):\n" + \
        "        '''\n" + \
        "        @param query   : oVirt engine dialect query\n" + \
        "        @param **kwargs: used to filter collection members if no search capabilities\n" + \
        "                         available at given collection resource\n" + \
        "        '''\n\n" + \
        "        url='%(url)s'\n\n" + \
        "        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_%(resource_name_lc)s()\n" + \
        "        return ParseHelper.toCollection(%(resource_type)s,\n" + \
        "                                        FilterHelper.filter(result, kwargs))\n\n") % collection_list_template_values

        return collection_list_template

    @staticmethod
    def add(url, resource_to_add_lc, resource_type, KNOWN_WRAPPER_TYPES={}):
        actual_resource_type = TypeUtil.getValueByKeyOrNone(resource_type.lower(), KNOWN_WRAPPER_TYPES)

        collection_add_template_values = {'url':url,
                                          'resource_to_add_lc':resource_to_add_lc.lower(),
                                          'resource_type' : actual_resource_type if actual_resource_type is not None else resource_type}

        collection_add_template = \
        ("    def add(self, %(resource_to_add_lc)s):\n" + \
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().add(url=url,\n" + \
        "                                      body=ParseHelper.toXml(%(resource_to_add_lc)s))\n" + \
        "        return %(resource_type)s(result)\n\n") % collection_add_template_values

        return collection_add_template

