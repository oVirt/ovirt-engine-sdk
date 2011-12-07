'''
Created on Oct 24, 2011

@author: mpastern
'''
from ovirtsdk.utils.parsehelper import ParseHelper
from ovirtsdk.codegen.utils.typeutil import TypeUtil

#============================================================
#======================SUB COLLECTION========================
#============================================================

class SubCollection(object):
    @staticmethod
    def collection(sub_collection_name, parent_resource_name_lc):
        sub_collection_get_template_values = {'sub_collection_name'    : sub_collection_name,
                                              'parent_resource_name_lc': parent_resource_name_lc.lower()}

        sub_collection_get_template = \
        ("class %(sub_collection_name)s(Base):\n" + \
        " \n" + \
        "    def __init__(self, %(parent_resource_name_lc)s):\n" + \
        "        self.parentclass = %(parent_resource_name_lc)s\n\n") % sub_collection_get_template_values


        return sub_collection_get_template

    @staticmethod
    def get(url, parent_resource_name_lc, encapsulating_resource, actual_resource_name_candidate, KNOWN_WRAPPER_TYPES={}):
        actual_encapsulating_resource = TypeUtil.getValueByKeyOrNone(encapsulating_resource.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(actual_encapsulating_resource if actual_encapsulating_resource is not None \
                                                                  else actual_resource_name_candidate.lower())).lower()

        sub_collection_get_template_values = {'url':url,
                                              'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                              'resource_name_lc':encapsulating_resource.lower(),
                                              'actual_resource_name_lc':actual_resource_name_lc,
                                              'encapsulating_resource':actual_encapsulating_resource if actual_encapsulating_resource is not None
                                                                                                     else encapsulating_resource}

        #url = '/api/vms/{vm:id}/nics'" 

        sub_collection_get_template = \
        ("    def get(self, name=None, **kwargs):\n\n" + \
        "        url = '%(url)s'\n\n" + \
        "        if(name is not None): kwargs['name']=name\n" + \
        "        result = self._getProxy().get(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}': self.parentclass.get_id()})).get_%(actual_resource_name_lc)s()\n\n" + \
        "        return %(encapsulating_resource)s(self.parentclass,\n" + \
        "                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))\n\n") % sub_collection_get_template_values

        return sub_collection_get_template

    @staticmethod
    def list(url, parent_resource_name_lc, encapsulating_resource, actual_resource_name_candidate, KNOWN_WRAPPER_TYPES={}):
        actual_encapsulating_resource = TypeUtil.getValueByKeyOrNone(encapsulating_resource.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(actual_encapsulating_resource if actual_encapsulating_resource is not None \
                                                                  else actual_resource_name_candidate.lower())).lower()


        sub_collection_list_template_values = {'url':url,
                                               'encapsulating_resource':actual_encapsulating_resource if actual_encapsulating_resource is not None
                                                                                                      else encapsulating_resource,
                                               'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                               'actual_resource_name_lc':actual_resource_name_lc}

        #url = '/api/vms/{vm:id}/nics'"+\
        sub_collection_list_template = \
        ("    def list(self, **kwargs):\n" + \
        "        '''\n" + \
        "        @param **kwargs: used to filter collection members if no search capabilities\n" + \
        "                         available at given collection resource\n" + \
        "        '''\n\n" + \
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().get(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}': self.parentclass.get_id()})).get_%(actual_resource_name_lc)s()\n\n" + \
        "        return ParseHelper.toSubCollection(%(encapsulating_resource)s,\n" + \
        "                                           self.parentclass,\n" + \
        "                                           FilterHelper.filter(result, kwargs))\n\n") % sub_collection_list_template_values

        return sub_collection_list_template

    @staticmethod
    def add(url, body_type, parent_resource_name_lc, encapsulating_entity, KNOWN_WRAPPER_TYPES={}):
        actual_encapsulating_entity = TypeUtil.getValueByKeyOrNone(encapsulating_entity.lower(), KNOWN_WRAPPER_TYPES)

        sub_collection_add_template_values = {'resource_to_add':body_type.lower(),
                                              'url':url,
                                              'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                              'encapsulating_entity':actual_encapsulating_entity if actual_encapsulating_entity is not None \
                                                                                                 else encapsulating_entity}



        #url = '/api/vms/{vm:id}/nics'"
        sub_collection_add_template = \
        ("    def add(self, %(resource_to_add)s):\n\n" + \
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().add(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}': self.parentclass.get_id()}),\n" + \
        "                                      body=ParseHelper.toXml(%(resource_to_add)s))\n\n" + \
        "        return %(encapsulating_entity)s(self.parentclass, result)\n\n") % sub_collection_add_template_values

        return sub_collection_add_template
