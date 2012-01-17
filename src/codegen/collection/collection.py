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


#============================================================
#=======================COLLECTION RESOURCE==================
#============================================================
from ovirtsdk.utils.parsehelper import ParseHelper
from codegen.utils.typeutil import TypeUtil
from codegen.doc.documentation import Documentation
from codegen.utils.paramutils import ParamUtils

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

        prms_str, method_params, url_params = ParamUtils.getMethodParamsByUrlParamsMeta(link)

        if 'search' in url_params:
            return \
            ("    def get(self, name='name', **kwargs):\n" + \
             Documentation.document(link, {'name: the name of the entity':False,
                                           '**kwargs: property based filtering': False}) +
            "        url = '%(url)s'\n\n" + \

            "        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:\n" +
            "            return %(resource_type)s(self._getProxy().get(url=UrlHelper.append(url, kwargs['id'])))\n" +
            "        else:\n" +
            "            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name})).get_%(resource_name_lc)s()\n" + \
            "            return %(resource_type)s(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))\n\n") % collection_get_template_values


        return \
            ("    def get(self, name='*', **kwargs):\n" + \
             Documentation.document(link, {'name: the name of the entity':False,
                                           '**kwargs: property based filtering"': False}) +
            "        url = '%(url)s'\n\n" + \
            "        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:\n" +
            "            return %(resource_type)s(self._getProxy().get(url=UrlHelper.append(url, kwargs['id'])))\n" +
            "        else:\n" +
            "            result = self._getProxy().get(url=url).get_%(resource_name_lc)s()\n" + \
            "            if name != '*': kwargs['name']=name\n"
            "            return %(resource_type)s(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))\n\n") % collection_get_template_values

    @staticmethod
    def list(url, resource_type, link, KNOWN_WRAPPER_TYPES={}):
        actual_resource_type = TypeUtil.getValueByKeyOrNone(resource_type.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(resource_type.lower())).lower()

        collection_list_template_values = {'url':url,
                                           'resource_name_lc':actual_resource_name_lc,
                                           'resource_type' : actual_resource_type if actual_resource_type is not None else resource_type}

        prms_str, method_params, url_params = ParamUtils.getMethodParamsByUrlParamsMeta(link)
        method_params_copy = method_params.copy()
        method_params['**kwargs'] = '**kwargs'

        if prms_str != '':
            return \
            ("    def list(self, " + prms_str + ", **kwargs):\n" + \
             Documentation.document(link, {'**kwargs: property based filtering"': False,
                                           'query: oVirt engine search dialect query':False},
                                    method_params) +
            "        url='%(url)s'\n\n" + \
            "        result = self._getProxy().get(url=SearchHelper.appendQuery(url, " + ParamUtils.toDictStr(url_params.keys(),
                                                                                                              method_params_copy.keys()) +
                                                                                ")).get_%(resource_name_lc)s()\n" + \
            "        return ParseHelper.toCollection(%(resource_type)s,\n" + \
            "                                        FilterHelper.filter(result, kwargs))\n\n") % collection_list_template_values
        return \
        ("    def list(self, **kwargs):\n" + \
         Documentation.document(link, {'**kwargs: property based filtering"': False}) +
        "        url='%(url)s'\n\n" + \
        "        result = self._getProxy().get(url=url).get_%(resource_name_lc)s()\n" + \
        "        return ParseHelper.toCollection(%(resource_type)s,\n" + \
        "                                        FilterHelper.filter(result, kwargs))\n\n") % collection_list_template_values

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

