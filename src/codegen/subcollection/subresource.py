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


from codegen.utils.typeutil import TypeUtil
from codegen.collection.resource import Resource
from codegen.doc.documentation import Documentation
from codegen.utils.paramutils import ParamUtils
from ovirtsdk.utils.parsehelper import ParseHelper
from codegen.utils.urlutils import UrlUtils
from codegen.utils.headerutils import HeaderUtils


#============================================================
#=====================SUB COLLECTION RESOURCE================
#============================================================

class SubResource(object):
    @staticmethod
    def resource(sub_res_type, encapsulating_entity, parent, KNOWN_WRAPPER_TYPES={}):
        actual_xml_entity = TypeUtil.getValueByKeyOrNone(encapsulating_entity.lower(), KNOWN_WRAPPER_TYPES)
        actual_xml_type = ParseHelper.getXmlType(encapsulating_entity)
        actual_sub_res_type = TypeUtil.getValueByKeyOrNone(sub_res_type.lower(), KNOWN_WRAPPER_TYPES)

        sub_collection_resource_template_values = {'encapsulating_entity':actual_sub_res_type if actual_sub_res_type is not None else sub_res_type,
                                                   'sub_res_type': actual_sub_res_type if actual_sub_res_type is not None else \
                                                                                       actual_xml_entity if actual_xml_entity is not None else\
                                                                                       actual_xml_type.__name__ if \
                                                                                       actual_xml_type is not None else \
                                                                                       encapsulating_entity,
                                                   'parent':parent.lower(),
                                                   'encapsulated_entity':encapsulating_entity.lower()}

        sub_resource_template = \
        ("class %(encapsulating_entity)s(params.%(sub_res_type)s, Base):\n" + \
        "    def __init__(self, %(parent)s, %(encapsulated_entity)s):\n" + \
        "        self.parentclass = %(parent)s\n" + \
        "        self.superclass  =  %(encapsulated_entity)s\n\n" + \
        Resource.SUB_COLLECTIONS_FIXME + "\n" + \
        "    def __new__(cls, %(parent)s, %(encapsulated_entity)s):\n" + \
        "        if %(encapsulated_entity)s is None: return None\n" + \
        "        obj = object.__new__(cls)\n" + \
        "        obj.__init__(%(parent)s, %(encapsulated_entity)s)\n" + \
        "        return obj\n\n") % sub_collection_resource_template_values

        return sub_resource_template

    @staticmethod
    def action(url, link, action_name, parent_resource_name_lc, body_type, resource_name_lc, method, action_params={}, collection_action=False):
        sub_collection_resource_action_template_values = {'url':url,
                                                          'action_name':action_name,
                                                          'method': method,
                                                          'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                                          'body_type':body_type,
                                                          'body_type_lc':body_type.lower(),
                                                          'resource_name_lc':resource_name_lc.lower(),
                                                          'add_method_params' : Resource._addMethodParams(action_params.keys()),
                                                          'add_action_parans' : Resource._addActionParams(action_params)}
        headers_method_params_str, headers_map_params_str = HeaderUtils.generate_method_params(link)
        headers_method_params_str = ', ' + headers_method_params_str if headers_method_params_str != '' else headers_method_params_str

        if collection_action == True:
            sub_collection_resource_action_template = \
            ("    def %(action_name)s(self%(add_method_params)s, %(body_type_lc)s=params.%(body_type)s()" + headers_method_params_str + "):\n" + \
            Documentation.document(link) +
            "        url = '%(url)s'\n\n" + \
            "        result = self._getProxy().request(method='%(method)s',\n" + \
            "                                          url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id()}),\n" + \
#TODO: support action on sub-collection
            "                                          body=ParseHelper.toXml(%(body_type_lc)s),\n"
            "                                          headers=" + headers_map_params_str + ")\n\n"
            "        return result\n\n"
            ) % sub_collection_resource_action_template_values
        else:
            sub_collection_resource_action_template = \
            ("    def %(action_name)s(self%(add_method_params)s, %(body_type_lc)s=params.%(body_type)s()" + headers_method_params_str + "):\n" + \
            Documentation.document(link) +
            "        url = '%(url)s'\n\n" + \
            "        result = self._getProxy().request(method='%(method)s',\n" + \
			"                                          url=UrlHelper.replace(url, " + \
            UrlUtils.generate_url_identifiers_replacments(link,
                                                           offset="                                                                    ",
                                                           continues=True) + \
            "),\n" + \
            "                                          body=ParseHelper.toXml(%(body_type_lc)s),\n"
            "                                          headers=" + headers_map_params_str + ")\n\n"
            "        return result\n\n"
            ) % sub_collection_resource_action_template_values

#            "                                                                {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
#            "                                                                 '{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        return sub_collection_resource_action_template

    @staticmethod
    def update(url, link, parent_resource_name_lc, resource_name, returned_type, KNOWN_WRAPPER_TYPES):
        actual_xml_entity = TypeUtil.getValueByKeyOrNone(returned_type.lower(), KNOWN_WRAPPER_TYPES)
        sub_collection_resource_update_template_values = {'url':url,
                                                          'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                                          'resource_name':resource_name,
                                                          'resource_name_lc':resource_name.lower(),
                                                          'returned_type':actual_xml_entity if actual_xml_entity is not None else returned_type}
        headers_method_params_str, headers_map_params_str = HeaderUtils.generate_method_params(link)
        headers_method_params_str = ', ' + headers_method_params_str if headers_method_params_str != '' else headers_method_params_str

        sub_collection_resource_update_template = \
        ("    def update(self" + headers_method_params_str + "):\n" + \
         Documentation.document(link) +
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().update(url=UrlHelper.replace(url, " + \
        UrlUtils.generate_url_identifiers_replacments(link,
                                                           offset="                                                                    ",
                                                           continues=True) + \
		"),\n" + \
        "                                         body=ParseHelper.toXml(self.superclass),\n"
        "                                         headers=" + headers_map_params_str + ")\n\n" + \
        "        return %(returned_type)s(self.parentclass, result)\n\n") % sub_collection_resource_update_template_values


        return sub_collection_resource_update_template

    @staticmethod
    def delete(url, link, parent_resource_name_lc, resource_name_lc, body_type):
        sub_collection_resource_delete_template_values = {'url':url,
                                                          'body_type_lc':body_type.lower() if body_type is not None
                                                                                           else None,
                                                          'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                                          'resource_name_lc':resource_name_lc.lower()}

        prms_str, method_params, url_params = ParamUtils.getMethodParamsByUrlParamsMeta(link)
        headers_method_params_str, headers_map_params_str = HeaderUtils.generate_method_params(link)
        combined_method_params = prms_str + \
                                 (', ' if prms_str != '' and headers_method_params_str != '' else '') + \
                                 headers_method_params_str
        headers_map_params_str_with_no_ct = headers_map_params_str.replace('}',
                                                                          ',"Content-type":None}') \
                                                                 if headers_map_params_str != '{}' \
                                                                 else '{"Content-type":None}'


        if prms_str != '' or headers_method_params_str != '':
            sub_collection_resource_delete_template = \
            ("    def delete(self, " + combined_method_params + "):\n" + \
             Documentation.document(link, {}, method_params) +
             "        url = UrlHelper.replace('%(url)s',\n" + \
            UrlUtils.generate_url_identifiers_replacments(link,
                                                           offset="                                ") + \
             ")\n\n" + \
             "        return self._getProxy().delete(url=SearchHelper.appendQuery(url, " + ParamUtils.toDictStr(url_params.keys(),
                                                                                                                method_params.copy().keys()) +
                                                                                    "),\n" +
             "                                       headers=" + headers_map_params_str_with_no_ct + ")\n\n"
             ) % sub_collection_resource_delete_template_values

            body_sub_collection_resource_delete_template = \
            ("    def delete(self, %(body_type_lc)s, " + combined_method_params + "):\n" + \
             Documentation.document(link, {}, method_params) +
             "        url = UrlHelper.replace('%(url)s',\n" + \
            UrlUtils.generate_url_identifiers_replacments(link,
                                                           offset="                                ") + \
             ")\n\n" + \
             "        return self._getProxy().delete(url=SearchHelper.appendQuery(url, " + ParamUtils.toDictStr(url_params.keys(),
                                                                                                                method_params.copy().keys()) +
                                                                                    "),\n" + \
             "                                       body=ParseHelper.toXml(%(body_type_lc)s),\n"
             "                                       headers=" + headers_map_params_str + ")\n\n"
             ) % sub_collection_resource_delete_template_values
        else:
            sub_collection_resource_delete_template = \
            ("    def delete(self):\n" + \
             Documentation.document(link) +
             "        url = '%(url)s'\n\n" + \
             "        return self._getProxy().delete(url=UrlHelper.replace(url, " + \
            UrlUtils.generate_url_identifiers_replacments(link,
                                                           offset="                                                                  ",
                                                           continues=True) + \
             "),\n" + \
             "                                       headers={'Content-type':None})\n\n"
             ) % sub_collection_resource_delete_template_values

            body_sub_collection_resource_delete_template = \
            ("    def delete(self, %(body_type_lc)s):\n" + \
             Documentation.document(link) +
             "        url = '%(url)s'\n\n" + \
             "        return self._getProxy().delete(url=UrlHelper.replace(url,\n" + \
            UrlUtils.generate_url_identifiers_replacments(link,
                                                           offset="                                                             ") + \
             "),\n" + \
             "                                       body=ParseHelper.toXml(%(body_type_lc)s))\n\n"
             ) % sub_collection_resource_delete_template_values

        if not body_type:
            return sub_collection_resource_delete_template
        else:
            return body_sub_collection_resource_delete_template
