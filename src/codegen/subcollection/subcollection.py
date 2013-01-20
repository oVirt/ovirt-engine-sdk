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
from codegen.utils.urlutils import UrlUtils
from codegen.utils.headerutils import HeaderUtils

#============================================================
#======================SUB COLLECTION========================
#============================================================

class SubCollection(object):

    @staticmethod
    def collection(sub_collection_name, parent_resource_name_lc):
        sub_collection_get_template_values = {'sub_collection_name'    : sub_collection_name,
                                              'parent_resource_name_lc': parent_resource_name_lc.lower()}

        sub_collection_get_template = \
        (
        "class %(sub_collection_name)s(Base):\n" + \
        "\n" + \
        "    def __init__(self, %(parent_resource_name_lc)s , context):\n" + \
        "        Base.__init__(self, context)\n"
        "        self.parentclass = %(parent_resource_name_lc)s\n\n" + \

        "    def __getProxy(self):\n" + \
        "        proxy = context.manager[self.context].get('proxy')\n" + \
        "        if proxy:\n" + \
        "            return proxy\n" + \
        "        #This may happen only if sdk was explicitly disconnected\n" + \
        "        #using .disconnect() method, but resource instance ref. is\n" + \
        "        #still available at client's code.\n" + \
        "        raise DisconnectedError\n\n"
        ) % sub_collection_get_template_values


        return sub_collection_get_template

    @staticmethod
    def get(url, link, parent_resource_name_lc, encapsulating_resource, actual_resource_name_candidate, KNOWN_WRAPPER_TYPES={}, NAMING_ENTITY_EXCEPTIONS={}):
        actual_encapsulating_resource = TypeUtil.getValueByKeyOrNone(encapsulating_resource.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(actual_encapsulating_resource if actual_encapsulating_resource is not None \
                                                                  else actual_resource_name_candidate.lower())).lower()

        if NAMING_ENTITY_EXCEPTIONS.has_key(actual_resource_name_lc):
            actual_resource_name_lc = NAMING_ENTITY_EXCEPTIONS[actual_resource_name_lc]

        sub_collection_get_template_values = {'url':url,
                                              'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                              'resource_name_lc':encapsulating_resource.lower(),
                                              'actual_resource_name_lc':actual_resource_name_lc,
                                              'encapsulating_resource':actual_encapsulating_resource if actual_encapsulating_resource is not None
                                                                                                     else encapsulating_resource}
        headers_method_params_str, headers_map_params_str = HeaderUtils.generate_method_params(link)
        headers_method_params_str = headers_method_params_str + ', ' \
                                    if headers_method_params_str != '' \
                                    else headers_method_params_str

        sub_collection_get_template = \
        ("    def get(self, name=None, " + headers_method_params_str + "id=None):\n\n" + \
         Documentation.document(link, {'name: string (the name of the entity)': False,
                                       'id  : string (the id of the entity)'  : False}) +
        "        url = '%(url)s'\n\n" + \
        "        if id:\n" +

        "            try :\n" + \
        "                result = self.__getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, " + \
        UrlUtils.generate_url_identifiers_replacments(link,
                                                       "                                                                                           ",
                                                       continues=True, is_collection=True) + \
        "),\n" +
        "                                                                    id),\n"
        "                                               headers=" + headers_map_params_str + ")\n" +
        "                return %(encapsulating_resource)s(self.parentclass, result, self.context)\n" +
        "            except RequestError, err:\n" + \
        "                if err.status and err.status == 404:\n" + \
        "                    return None\n" + \
        "                raise err\n" + \
        "        elif name:\n" +
        "            result = self.__getProxy().get(url=UrlHelper.replace(url, " + \
        UrlUtils.generate_url_identifiers_replacments(link,
                                                       "                                                                      ",
                                                       continues=True, is_collection=True) + \
        "),\n"
        "                                           headers=" + headers_map_params_str + ").get_%(actual_resource_name_lc)s()\n\n" + \
        "            return %(encapsulating_resource)s(self.parentclass,\n" + \
        "                                              FilterHelper.getItem(FilterHelper.filter(result, {'name':name})),\n" + \
        "                                              self.context)\n" + \
        "        else:\n" + \
        "            raise MissingParametersError(['id', 'name'])\n\n") % sub_collection_get_template_values

        return sub_collection_get_template

    @staticmethod
    def list(url, link, parent_resource_name_lc, encapsulating_resource,
             actual_resource_name_candidate, KNOWN_WRAPPER_TYPES={},
             NAMING_ENTITY_EXCEPTIONS={}):

        actual_encapsulating_resource = TypeUtil.getValueByKeyOrNone(encapsulating_resource.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(actual_encapsulating_resource if actual_encapsulating_resource is not None \
                                                                  else actual_resource_name_candidate.lower())).lower()

        if NAMING_ENTITY_EXCEPTIONS.has_key(actual_resource_name_lc):
            actual_resource_name_lc = NAMING_ENTITY_EXCEPTIONS[actual_resource_name_lc]

        sub_collection_list_template_values = {'url':url,
                                               'encapsulating_resource':actual_encapsulating_resource
                                                        if actual_encapsulating_resource is not None
                                                        else encapsulating_resource,
                                               'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                               'actual_resource_name_lc':actual_resource_name_lc}

        prms_str, method_params, url_params = ParamUtils.getMethodParamsByUrlParamsMeta(link)
        headers_method_params_str, headers_map_params_str = HeaderUtils.generate_method_params(link)
        combined_method_params = prms_str + \
                                 (', ' if prms_str != '' and headers_method_params_str != '' else '') + \
                                 headers_method_params_str

        method_params_copy = method_params.copy()
        method_params['**kwargs'] = '**kwargs'

        if prms_str != '' or headers_method_params_str != '':
            return \
            ("    def list(self, " + combined_method_params + ", **kwargs):\n" + \
             Documentation.document(link, {'**kwargs: dict (property based filtering)"': False,
                                           'query: string (oVirt engine search dialect query)':False},
                                    method_params) +
            "        url = '%(url)s'\n\n" + \
            "        result = self.__getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,\n " +
            "                                                                                         args=" +
            UrlUtils.generate_url_identifiers_replacments(link,
                                                          "                                                                                              ",
                                                          continues=True, is_collection=True) + \
             "),\n" + \
            "                                                                    qargs=" + ParamUtils.toDictStr(url_params.keys(), method_params_copy.keys()) +
            "),\n"
            "                                      headers=" + headers_map_params_str + ").get_%(actual_resource_name_lc)s()\n" + \
            "        return ParseHelper.toSubCollection(%(encapsulating_resource)s,\n" + \
            "                                           self.parentclass,\n" + \
            "                                           FilterHelper.filter(result, kwargs),\n" + \
            "                                           context=self.context)\n\n") % sub_collection_list_template_values
        return \
            ("    def list(self, **kwargs):\n" + \
             Documentation.document(link, {'**kwargs: dict (property based filtering)"': False}) +
            "        url = '%(url)s'\n\n" + \
            "        result = self.__getProxy().get(url=UrlHelper.replace(url, " + \
            UrlUtils.generate_url_identifiers_replacments(link,
                                                           "                                                                 ",
                                                           continues=True, is_collection=True) + \
             ")).get_%(actual_resource_name_lc)s()\n\n" + \
            "        return ParseHelper.toSubCollection(%(encapsulating_resource)s,\n" + \
            "                                           self.parentclass,\n" + \
            "                                           FilterHelper.filter(result, kwargs),\n" + \
            "                                           context=self.context)\n\n") % sub_collection_list_template_values

    @staticmethod
    def add(url, link, body_type, parent_resource_name_lc, encapsulating_entity, KNOWN_WRAPPER_TYPES={}):
        actual_encapsulating_entity = TypeUtil.getValueByKeyOrNone(encapsulating_entity.lower(), KNOWN_WRAPPER_TYPES)

        sub_collection_add_template_values = {'resource_to_add':body_type.lower(),
                                              'url':url,
                                              'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                              'encapsulating_entity':actual_encapsulating_entity if actual_encapsulating_entity is not None \
                                                                                                 else encapsulating_entity}
        headers_method_params_str, headers_map_params_str = HeaderUtils.generate_method_params(link)
        headers_method_params_str = ', ' + headers_method_params_str if headers_method_params_str != '' else headers_method_params_str

        sub_collection_add_template = \
        ("    def add(self, %(resource_to_add)s" + headers_method_params_str + "):\n\n" + \
         Documentation.document(link) +
        "        url = '%(url)s'\n\n" + \
        "        result = self.__getProxy().add(url=UrlHelper.replace(url, " + \
        UrlUtils.generate_url_identifiers_replacments(link,
                                                           "                                                                  ",
                                                           continues=True, is_collection=True) + \
        "),\n" + \
        "                                       body=ParseHelper.toXml(%(resource_to_add)s),\n"
        "                                       headers=" + headers_map_params_str + ")\n\n" + \
        "        return %(encapsulating_entity)s(self.parentclass, result, self.context)\n\n") % sub_collection_add_template_values

        return sub_collection_add_template
