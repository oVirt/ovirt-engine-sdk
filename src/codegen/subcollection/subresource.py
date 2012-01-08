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


#============================================================
#=====================SUB COLLECTION RESOURCE================
#============================================================

class SubResource(object):
    @staticmethod
    def resource(sub_res_type, encapsulating_entity, parent, KNOWN_WRAPPER_TYPES={}):
        actual_xml_entity = TypeUtil.getValueByKeyOrNone(encapsulating_entity.lower(), KNOWN_WRAPPER_TYPES)
        actual_sub_res_type = TypeUtil.getValueByKeyOrNone(sub_res_type.lower(), KNOWN_WRAPPER_TYPES)

        sub_collection_resource_template_values = {'encapsulating_entity':actual_sub_res_type if actual_sub_res_type is not None else sub_res_type,
                                                   'sub_res_type': actual_sub_res_type if actual_sub_res_type is not None else \
                                                                                       actual_xml_entity if actual_xml_entity is not None else\
                                                                                       encapsulating_entity,
                                                   'parent':parent.lower(),
                                                   'encapsulated_entity':encapsulating_entity.lower()}

        sub_resource_template = \
        ("class %(encapsulating_entity)s(params.%(sub_res_type)s, Base):\n" + \
        "    def __init__(self, %(parent)s, %(encapsulated_entity)s):\n" + \
        "        self.parentclass = %(parent)s\n" + \
        "        self.superclass  =  %(encapsulated_entity)s\n\n" + \
        "    def __new__(cls, %(parent)s, %(encapsulated_entity)s):\n" + \
        "        if %(encapsulated_entity)s is None: return None\n" + \
        "        obj = object.__new__(cls)\n" + \
        "        obj.__init__(%(parent)s, %(encapsulated_entity)s)\n" + \
        "        return obj\n\n") % sub_collection_resource_template_values

        return sub_resource_template

    @staticmethod
    def action(url, link, action_name, parent_resource_name_lc, body_type, resource_name_lc, method, action_params={}):
        sub_collection_resource_action_template_values = {'url':url,
                                                          'action_name':action_name,
                                                          'method': method,
                                                          'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                                          'body_type':body_type,
                                                          'body_type_lc':body_type.lower(),
                                                          'resource_name_lc':resource_name_lc.lower(),
                                                          'add_method_params' : Resource._addMethodParams(action_params.keys()),
                                                          'add_action_parans' : Resource._addActionParams(action_params)}

        sub_collection_resource_action_template = \
        ("    def %(action_name)s(self%(add_method_params)s, %(body_type_lc)s=params.%(body_type)s()):\n" + \
        "        url = '%(url)s'\n\n" + \
        Documentation.document(link) +
        "        result = self._getProxy().request(method='%(method)s',\n" + \
        "                                          url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
        "                                                                     '{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        "                                          body=ParseHelper.toXml(%(body_type_lc)s))\n\n"
        "        return result\n\n"
        ) % sub_collection_resource_action_template_values

        return sub_collection_resource_action_template

    @staticmethod
    def update(url, link, parent_resource_name_lc, resource_name, returned_type, KNOWN_WRAPPER_TYPES):
        actual_xml_entity = TypeUtil.getValueByKeyOrNone(returned_type.lower(), KNOWN_WRAPPER_TYPES)

        sub_collection_resource_update_template_values = {'url':url,
                                                          'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                                          'resource_name':resource_name,
                                                          'resource_name_lc':resource_name.lower(),
                                                          'returned_type':actual_xml_entity if actual_xml_entity is not None else returned_type}

        sub_collection_resource_update_template = \
        ("    def update(self):\n" + \
         Documentation.document(link) +
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().update(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
        "                                                                     '{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        "                                         body=ParseHelper.toXml(self.superclass))\n\n" + \
        "        return %(returned_type)s(self.parentclass, result)\n\n") % sub_collection_resource_update_template_values

        return sub_collection_resource_update_template

    @staticmethod
    def delete(url, link, parent_resource_name_lc, resource_name_lc, body_type):
        sub_collection_resource_delete_template_values = {'url':url,
                                                          'body_type_lc':body_type.lower() if body_type is not None
                                                                                           else None,
                                                          'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                                          'resource_name_lc':resource_name_lc.lower()}

        forced_sub_collection_resource_delete_template = \
        ("    def delete(self, force=False, grace_period=False):\n" + \
         Documentation.document(link) +
         "        url = '%(url)s'\n\n" + \
         "        if ((force or grace_period) is not False):\n" + \
         "            action = params.Action(force=force, grace_period=grace_period)\n" + \
         "            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
         "                                                                         '{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
         "                                             body=ParseHelper.toXml(action))\n" + \
         "        else:\n" + \
         "            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
         "                                                                         '{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
         "                                             headers={'Content-type':None})\n" + \
         "        return result\n\n") % sub_collection_resource_delete_template_values

        sub_collection_resource_delete_template = \
        ("    def delete(self):\n" + \
         Documentation.document(link) +
         "        url = '%(url)s'\n\n" + \
         "        return self._getProxy().delete(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
         "                                                                   '{%(resource_name_lc)s:id}': self.get_id()}),\n" +
         "                                       headers={'Content-type':None})\n\n"
         ) % sub_collection_resource_delete_template_values

        body_sub_collection_resource_delete_template = \
        ("    def delete(self, %(body_type_lc)s):\n" + \
         Documentation.document(link) +
         "        url = '%(url)s'\n\n" + \
         "        return self._getProxy().delete(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
         "                                                                   '{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
         "                                       body=ParseHelper.toXml(%(body_type_lc)s))\n\n"
         ) % sub_collection_resource_delete_template_values

        if not body_type:
            return sub_collection_resource_delete_template
        elif body_type == 'Action':
            return forced_sub_collection_resource_delete_template
        else:
            return body_sub_collection_resource_delete_template
