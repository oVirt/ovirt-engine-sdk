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
from codegen.utils.headerutils import HeaderUtils
from codegen.collection.collectionexceptions import CollectionExceptions

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
        headers_method_params_str, headers_map_params_str = HeaderUtils.generate_method_params(link)
        headers_method_params_str = headers_method_params_str + ', ' if headers_method_params_str != '' else headers_method_params_str

        #Capabilities resource has unique structure which is not
        #fully comply with RESTful collection pattern, but preserved
        #in sake of backward compatibility
        if url == '/api/capabilities':
            return CollectionExceptions.get(url, link, prms_str, method_params, url_params,
                                            headers_method_params_str, headers_map_params_str,
                                            collection_get_template_values)

        #/api/disks search-by-name paradigm was broken by the engine
        #should be fixed later on
        if url == '/api/disks':
            return CollectionExceptions.get(url, link, prms_str, method_params, url_params,
                                            headers_method_params_str, headers_map_params_str,
                                            collection_get_template_values)

        if 'search:query' in url_params:
            return \
            ("    def get(self, name=None, " + headers_method_params_str + "id=None):\n" + \
             Documentation.document(link, {'name: string (the name of the entity)': False,
                                           'id  : string (the id of the entity)'  : False}) +
            "        url = '%(url)s'\n\n" + \

            "        if id:\n" +
            "            try :\n" + \
            "                return %(resource_type)s(self._getProxy().get(url=UrlHelper.append(url, id),\n"
            "                                                              headers=" + headers_map_params_str + "))\n" +
            "            except RequestError, err:\n" + \
            "                if err.status and err.status == 404:\n" + \
            "                    return None\n" + \
            "                raise err\n" + \
            "        elif name:\n" +
            "            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':'name='+name,'max:matrix':-1}),\n"
            "                                          headers=" + headers_map_params_str + ").get_%(resource_name_lc)s()\n" + \
            "            return %(resource_type)s(FilterHelper.getItem(result))\n" + \
            "        else:\n" + \
            "            raise MissingParametersError(['id', 'name'])\n\n") % collection_get_template_values


        return \
            ("    def get(self, name=None, " + headers_method_params_str + "id=None):\n" + \
             Documentation.document(link, {'name: string (the name of the entity)': False,
                                           'id  : string (the id of the entity)'  : False}) +
            "        url = '%(url)s'\n\n" + \
            "        if id:\n" +
            "            try :\n" + \
            "                return %(resource_type)s(self._getProxy().get(url=UrlHelper.append(url, id),\n" + \
            "                                                              headers=" + headers_map_params_str + "))\n" +
            "            except RequestError, err:\n" + \
            "                if err.status and err.status == 404:\n" + \
            "                    return None\n" + \
            "                raise err\n" + \
            "        elif name:\n" +
            "            result = self._getProxy().get(url=url,\n"
            "                                          headers=" + headers_map_params_str + ").get_%(resource_name_lc)s()\n" + \
            "            return %(resource_type)s(FilterHelper.getItem(FilterHelper.filter(result, {'name':name})))\n" + \
            "        else:\n" + \
            "            raise MissingParametersError(['id', 'name'])\n\n") % collection_get_template_values

    @staticmethod
    def list(url, resource_type, link, KNOWN_WRAPPER_TYPES={}):
        actual_resource_type = TypeUtil.getValueByKeyOrNone(resource_type.lower(), KNOWN_WRAPPER_TYPES)
        actual_resource_name_lc = (ParseHelper.getXmlTypeInstance(resource_type.lower())).lower()

        collection_list_template_values = {'url':url,
                                           'resource_name_lc':actual_resource_name_lc,
                                           'resource_type' : actual_resource_type if actual_resource_type is not None else resource_type}

        prms_str, method_params, url_params = ParamUtils.getMethodParamsByUrlParamsMeta(link)
        headers_method_params_str, headers_map_params_str = HeaderUtils.generate_method_params(link)
        method_params_copy = method_params.copy()
        method_params['**kwargs'] = '**kwargs'

        #Capabilities resource has unique structure which is not
        #fully comply with RESTful collection pattern, but preserved
        #in sake of backward compatibility
        if url == '/api/capabilities':
            return \
"""
    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return [VersionCaps]:
        '''

        url='/api/capabilities'

        result = self._getProxy().get(url=url).version
        return ParseHelper.toCollection(VersionCaps,
                                        FilterHelper.filter(result, kwargs))
"""
        if prms_str != '' or headers_method_params_str != '':
            combined_method_params = prms_str + \
                                     (', ' if prms_str != '' and headers_method_params_str != '' else '') + \
                                     headers_method_params_str
            return \
            ("    def list(self, " + combined_method_params + ", **kwargs):\n" + \
             Documentation.document(link, {'**kwargs: dict (property based filtering)': False,
                                           'query: string (oVirt engine search dialect query)':False},
                                    method_params) +
            "        url='%(url)s'\n\n" + \
            "        result = self._getProxy().get(url=SearchHelper.appendQuery(url, " + ParamUtils.toDictStr(url_params.keys(),
                                                                                                              method_params_copy.keys()) +
                                                                                "),\n"
            "                                      headers=" + headers_map_params_str + ").get_%(resource_name_lc)s()\n" + \
            "        return ParseHelper.toCollection(%(resource_type)s,\n" + \
            "                                        FilterHelper.filter(result, kwargs))\n\n") % collection_list_template_values
        return \
        ("    def list(self, **kwargs):\n" + \
         Documentation.document(link, {'**kwargs: dict (property based filtering)': False}) +
        "        url='%(url)s'\n\n" + \
        "        result = self._getProxy().get(url=url).get_%(resource_name_lc)s()\n" + \
        "        return ParseHelper.toCollection(%(resource_type)s,\n" + \
        "                                        FilterHelper.filter(result, kwargs))\n\n") % collection_list_template_values

    @staticmethod
    def add(url, body_type, response_type, link, KNOWN_WRAPPER_TYPES={}):
        actual_resource_type = TypeUtil.getValueByKeyOrNone(response_type.lower(), KNOWN_WRAPPER_TYPES)

        collection_add_template_values = {'url':url,
                                          'resource_to_add_lc':body_type.lower(),
                                          'resource_type' : actual_resource_type if actual_resource_type is not None
                                                                                 else response_type}
        headers_method_params_str, headers_map_params_str = HeaderUtils.generate_method_params(link)
        headers_method_params_str = ', ' + headers_method_params_str if headers_method_params_str != '' else headers_method_params_str

        collection_add_template = \
        ("    def add(self, %(resource_to_add_lc)s" + headers_method_params_str + "):\n" + \
         Documentation.document(link) +
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().add(url=url,\n" + \
        "                                      body=ParseHelper.toXml(%(resource_to_add_lc)s),\n"
        "                                      headers=" + headers_map_params_str + ")\n" + \
        "        return %(resource_type)s(result)\n\n") % collection_add_template_values

        return collection_add_template
