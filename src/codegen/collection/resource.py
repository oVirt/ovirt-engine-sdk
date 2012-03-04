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
from codegen.doc.documentation import Documentation
from codegen.utils.paramutils import ParamUtils

#============================================================
#===========================RESOURCE=========================
#============================================================

class Resource(object):
    SUB_COLLECTIONS_FIXME = "        #SUB_COLLECTIONS"

    @staticmethod
    def resource(xml_entity, sub_collections=[], KNOWN_WRAPPER_TYPES={}):
        actual_xml_entity = TypeUtil.getValueByKeyOrNone(xml_entity.lower(), KNOWN_WRAPPER_TYPES)

        resource_template_values = {'xml_entity': actual_xml_entity if actual_xml_entity is not None else xml_entity,
                                    'xml_entity_lc':xml_entity.lower(),
                                    'sub_collections':sub_collections}

        resource_template = \
        ("class %(xml_entity)s(params.%(xml_entity)s, Base):\n" + \
        "    def __init__(self, %(xml_entity_lc)s):\n" + \
        #Resource.__addSubCollectionInstances(xml_entity.lower(), sub_collections)+\
        Resource.SUB_COLLECTIONS_FIXME + "\n" + \
        "        self.superclass = %(xml_entity_lc)s\n\n" + \
        "    def __new__(cls, %(xml_entity_lc)s):\n" + \
        "        if %(xml_entity_lc)s is None: return None\n" + \
        "        obj = object.__new__(cls)\n" + \
        "        obj.__init__(%(xml_entity_lc)s)\n" + \
        "        return obj\n\n") % resource_template_values

        return resource_template

    @staticmethod
    def addSubCollectionInstances(parent, sub_collections={}):
        tmpl = "        self.%s = %s(%s)\n"

        new_tmpl = ''
        for k, v in sub_collections.items():
            new_tmpl += tmpl % (k.lower(), v, parent)

        return new_tmpl

    @staticmethod
    def action(url, body_type, link, action_name, resource_name_lc, method, action_params={}):
        resource_action_template_values = {'url':url,
                                           'body_type':body_type,
                                           'body_type_lc':body_type.lower(),
                                           'action_name':action_name.lower(),
                                           'method': method,
                                           'resource_name_lc':resource_name_lc.lower(),
                                           'method_params': Resource._addMethodParams(action_params.keys()),
                                           'action_params':Resource._addActionParams(action_params)}

        #FIXME: check if there are more params to put to Action
        #"      action = params.Action(vm=self.superclass)"

        resource_action_template = \
        ("    def %(action_name)s(self%(method_params)s, %(body_type_lc)s=params.%(body_type)s()):\n" + \
         Documentation.document(link) +
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().request(method='%(method)s',\n" + \
        "                                          url=UrlHelper.replace(url, {'{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        "                                          body=ParseHelper.toXml(%(body_type_lc)s))\n" + \
        "        return result\n\n"
        ) % resource_action_template_values

        return resource_action_template

    @staticmethod
    def _addActionParams(kwargs={}):
        res = ''
        for k, v in kwargs.items():
            res += "        action." + k + "=" + v + "\n"
        return res

    @staticmethod
    def _addMethodParams(params=[]):
        res = ''
        for item in params:
            res += ', ' + item
        return res

    @staticmethod
    def delete(url, body_type, link, resource_name):
        resource_delete_template_values = {'url':url,
                                           'body_type':body_type,
                                           'body_type_lc':body_type.lower() if body_type is not None
                                                                            else None,
                                           'resource_name_lc':resource_name.lower()}


        prms_str, method_params, url_params = ParamUtils.getMethodParamsByUrlParamsMeta(link)

        if prms_str != '':
            resource_delete_template = \
            ("    def delete(self, " + prms_str + "):\n" + \
             Documentation.document(link, {}, method_params) +
            "        url = UrlHelper.replace('%(url)s',\n" + \
            "                                {'{%(resource_name_lc)s:id}': self.get_id()})\n\n" + \
            "        return self._getProxy().delete(url=SearchHelper.appendQuery(url, " + ParamUtils.toDictStr(url_params.keys(),
                                                                                                               method_params.copy().keys()) +
                                                                                "),\n" +
            "                                       headers={'Content-type':None})\n\n"
            ) % resource_delete_template_values


            body_resource_delete_template = \
            ("    def delete(self, %(body_type_lc)s, " + prms_str + "):\n" + \
             Documentation.document(link, {}, method_params) +
            "        url = UrlHelper.replace('%(url)s',\n" + \
            "                                {'{%(resource_name_lc)s:id}': self.get_id()})\n\n" + \
            "        return self._getProxy().delete(url=SearchHelper.appendQuery(url, " + ParamUtils.toDictStr(url_params.keys(),
                                                                                                               method_params.copy().keys()) +
                                                                                "),\n" + \
            "                                       body=ParseHelper.toXml(%(body_type_lc)s))\n\n"
            ) % resource_delete_template_values
        else:
            resource_delete_template = \
            ("    def delete(self):\n" + \
             Documentation.document(link) +
            "        url = '%(url)s'\n\n" + \
            "        return self._getProxy().delete(url=UrlHelper.replace(url, {'{%(resource_name_lc)s:id}': self.get_id()}),\n" +
            "                                       headers={'Content-type':None})\n\n"
            ) % resource_delete_template_values


            body_resource_delete_template = \
            ("    def delete(self, %(body_type_lc)s):\n" + \
             Documentation.document(link) +
            "        url = '%(url)s'\n\n" + \
            "        return self._getProxy().delete(url=UrlHelper.replace(url, {'{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
            "                                       body=ParseHelper.toXml(%(body_type_lc)s))\n\n"
            ) % resource_delete_template_values

        if not body_type:
            return resource_delete_template
        else:
            return body_resource_delete_template

    @staticmethod
    def update(url, resource_name, link, KNOWN_WRAPPER_TYPES={}):

        actual_xml_entity = TypeUtil.getValueByKeyOrNone(resource_name.lower(), KNOWN_WRAPPER_TYPES)

        resource_update_template_values = {'url':url,
                                           'resource_name_lc':resource_name.lower(),
                                           'actual_self_name':actual_xml_entity if actual_xml_entity is not None else resource_name}

        resource_update_template = \
        ("    def update(self):\n" + \
         Documentation.document(link) +
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().update(url=UrlHelper.replace(url, {'{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        "                                         body=ParseHelper.toXml(self.superclass))\n" + \
        "        return %(actual_self_name)s(result)\n\n") % resource_update_template_values

        return resource_update_template
