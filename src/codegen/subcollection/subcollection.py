#
# Copyright (c) 2010 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from ovirtsdk.utils.parsehelper import ParseHelper
from codegen.utils.typeutil import TypeUtil
from codegen.doc.documentation import Documentation
from codegen.utils.paramutils import ParamUtils

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
    def get(url, link, parent_resource_name_lc, encapsulating_resource, actual_resource_name_candidate, KNOWN_WRAPPER_TYPES={}):
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
         Documentation.document(link, {'name: the name of the entity':False,
                                       '**kwargs: property based filtering': False}) +
        "        url = '%(url)s'\n\n" + \
        "        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:\n" +

        "            try :\n" + \
        "                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}': self.parentclass.get_id()}),\n" +
        "                                                                   kwargs['id']))\n" +
        "                return %(encapsulating_resource)s(self.parentclass, result)\n" +
        "            except RequestError, err:\n" + \
        "                if err.status and err.status == 404:\n" + \
        "                    return None\n" + \
        "                raise err\n" + \
        "        else:\n" +
        "            if(name is not None): kwargs['name']=name\n" + \
        "            result = self._getProxy().get(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}': self.parentclass.get_id()})).get_%(actual_resource_name_lc)s()\n\n" + \
        "            return %(encapsulating_resource)s(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))\n\n") % sub_collection_get_template_values

        return sub_collection_get_template

    @staticmethod
    def list(url, link, parent_resource_name_lc, encapsulating_resource, actual_resource_name_candidate, KNOWN_WRAPPER_TYPES={}):
        actual_encapsulating_resource = TypeUtil.getValueByKeyOrNone(encapsulating_resource.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(actual_encapsulating_resource if actual_encapsulating_resource is not None \
                                                                  else actual_resource_name_candidate.lower())).lower()


        sub_collection_list_template_values = {'url':url,
                                               'encapsulating_resource':actual_encapsulating_resource if actual_encapsulating_resource is not None
                                                                                                      else encapsulating_resource,
                                               'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                               'actual_resource_name_lc':actual_resource_name_lc}

        prms_str, method_params, url_params = ParamUtils.getMethodParamsByUrlParamsMeta(link)
        method_params_copy = method_params.copy()
        method_params['**kwargs'] = '**kwargs'

        if prms_str != '':
            return \
            ("    def list(self, " + prms_str + ", **kwargs):\n" + \
             Documentation.document(link, {'**kwargs: property based filtering"': False,
                                           'query: oVirt engine search dialect query':False},
                                    method_params) +
            "        url = '%(url)s'\n\n" + \
            "        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,\n " +
            "                                                                                        args={'{%(parent_resource_name_lc)s:id}': self.parentclass.get_id()}),\n" +
            "                                                                   qargs=" + ParamUtils.toDictStr(url_params.keys(), method_params_copy.keys()) +
            ")).get_%(actual_resource_name_lc)s()\n" + \
            "        return ParseHelper.toSubCollection(%(encapsulating_resource)s,\n" + \
            "                                           self.parentclass,\n" + \
            "                                           FilterHelper.filter(result, kwargs))\n\n") % sub_collection_list_template_values
        return \
            ("    def list(self, **kwargs):\n" + \
             Documentation.document(link, {'**kwargs: property based filtering"': False}) +
            "        url = '%(url)s'\n\n" + \
            "        result = self._getProxy().get(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}': self.parentclass.get_id()})).get_%(actual_resource_name_lc)s()\n\n" + \
            "        return ParseHelper.toSubCollection(%(encapsulating_resource)s,\n" + \
            "                                           self.parentclass,\n" + \
            "                                           FilterHelper.filter(result, kwargs))\n\n") % sub_collection_list_template_values



    @staticmethod
    def add(url, link, body_type, parent_resource_name_lc, encapsulating_entity, KNOWN_WRAPPER_TYPES={}):
        actual_encapsulating_entity = TypeUtil.getValueByKeyOrNone(encapsulating_entity.lower(), KNOWN_WRAPPER_TYPES)

        sub_collection_add_template_values = {'resource_to_add':body_type.lower(),
                                              'url':url,
                                              'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                              'encapsulating_entity':actual_encapsulating_entity if actual_encapsulating_entity is not None \
                                                                                                 else encapsulating_entity}



        #url = '/api/vms/{vm:id}/nics'"
        sub_collection_add_template = \
        ("    def add(self, %(resource_to_add)s):\n\n" + \
         Documentation.document(link) +
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().add(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}': self.parentclass.get_id()}),\n" + \
        "                                      body=ParseHelper.toXml(%(resource_to_add)s))\n\n" + \
        "        return %(encapsulating_entity)s(self.parentclass, result)\n\n") % sub_collection_add_template_values

        return sub_collection_add_template
