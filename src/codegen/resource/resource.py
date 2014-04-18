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
from codegen.utils.headerutils import HeaderUtils
from codegen.templates.resourcetemplate import ResourceTemplate
from codegen.templates.resourceactiontemplate import ResourceActionTemplate
from codegen.templates.resourceupdatetemplate import ResourceUpdateTemplate
from codegen.templates.resourcedeletewithparamstemplate import ResourceDeleteWithParamsTemplate
from codegen.templates.resourcedeletewithbodytemplate import ResourceDeleteWithBodyTemplate
from codegen.templates.resourcedeletetemplate import ResourceDeleteTemplate
from codegen.templates.resourcedeletewithbodyandparamstemplate import ResourceDeleteWithBodyAndParamsTemplate

#============================================================
#===========================RESOURCE=========================
#============================================================

resourcetemplate = ResourceTemplate()
resourceactiontemplate = ResourceActionTemplate()
resourceupdatetemplate = ResourceUpdateTemplate()
resourcedeletewithparamstemplate = ResourceDeleteWithParamsTemplate()
resourcedeletewithbodytemplate = ResourceDeleteWithBodyTemplate()
resourcedeletetemplate = ResourceDeleteTemplate()
resourcedeletewithbodyandparamstemplate = ResourceDeleteWithBodyAndParamsTemplate()

class Resource(object):
    SUB_COLLECTIONS_FIXME = "        #SUB_COLLECTIONS"

    @staticmethod
    def resource(xml_entity, sub_collections=[], KNOWN_WRAPPER_TYPES={}):

        actual_xml_entity = TypeUtil.getValueByKeyOrNone(
                                 xml_entity.lower(),
                                 KNOWN_WRAPPER_TYPES
                             )

        resource_template_values = {
            'xml_entity_lc':xml_entity.lower(),
            'sub_collections':sub_collections,
            'fixme' : Resource.SUB_COLLECTIONS_FIXME,
            'xml_entity': actual_xml_entity if actual_xml_entity is not None
                                            else xml_entity
        }

        return resourcetemplate\
               .generate(resource_template_values)

    @staticmethod
    def addSubCollectionInstances(parent, sub_collections={}):

        tmpl = "        self.%s = %s(%s, context)\n"

        new_tmpl = ''
        for k in sorted(sub_collections):
            v = sub_collections[k]
            new_tmpl += tmpl % (k.lower(), v, parent)

        return new_tmpl

    @staticmethod
    def action(url, body_type, link, action_name, resource_name_lc, method, action_params={}):

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        headers_method_params_str = ', ' + \
            headers_method_params_str if headers_method_params_str != '' \
                                      else headers_method_params_str

#        resource_action_template_values['headers_map_params_str'] = headers_map_params_str
#        resource_action_template_values['headers_method_params_str'] = headers_method_params_str

        resource_action_template_values = {
           'url':url,
           'body_type':body_type,
           'body_type_lc':body_type.lower(),
           'action_name':action_name.lower(),
           'method': method,
           'resource_name_lc':resource_name_lc.lower(),
           'method_params': Resource._addMethodParams(action_params.keys()),
           'action_params':Resource._addActionParams(action_params),
           'docs':Documentation.document(link),
           'headers_map_params_str' : headers_map_params_str,
           'headers_method_params_str': headers_method_params_str
       }

        return resourceactiontemplate\
               .generate(resource_action_template_values)

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

        prms_str, method_params, url_params = \
            ParamUtils.getMethodParamsByUrlParamsMeta(link)

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        combined_method_params = prms_str + \
                         (', ' if prms_str != '' and headers_method_params_str != '' else '') + \
                         headers_method_params_str

        body_instance = ParamUtils.getBodyInstance(link)
        body_instance_str = '=' + body_instance if body_instance else ''

        resource_delete_template_values = {
           'url':url,
           'body_type':body_type,
           'resource_name_lc':resource_name.lower(),
           'body_type_lc':body_type.lower() if body_type is not None
                                            else None
        }

        resource_delete_template_values['combined_method_params'] = \
             combined_method_params

        resource_delete_template_values['headers_map_params_str_with_no_ct'] = \
             headers_map_params_str.replace('}', ',"Content-type":None}') \
                                             if headers_map_params_str != '{}' \
                                             else '{"Content-type":None}'

        resource_delete_template_values['url_params'] = \
            ParamUtils.toDictStr(url_params.keys(), method_params.copy().keys())

        resource_delete_template_values['body_instance_str'] = \
            body_instance_str

        resource_delete_template_values['headers_map_params_str'] = \
            headers_map_params_str

        if prms_str != '' or headers_method_params_str != '':
            resource_delete_template_values['docs'] = \
                Documentation.document(link, {}, method_params)


            resource_delete_template = resourcedeletewithparamstemplate\
                                       .generate(resource_delete_template_values)

            body_resource_delete_template = resourcedeletewithbodytemplate\
                                            .generate(resource_delete_template_values)
        else:
            resource_delete_template_values['docs'] = Documentation.document(link)

            resourcedeletetemplate
            resource_delete_template = resourcedeletetemplate\
                                       .generate(resource_delete_template_values)

            body_resource_delete_template = resourcedeletewithbodyandparamstemplate\
                                            .generate(resource_delete_template_values)

        if not body_type:
            return resource_delete_template
        else:
            return body_resource_delete_template

    @staticmethod
    def update(url, resource_name, link, KNOWN_WRAPPER_TYPES={}):

        actual_xml_entity = TypeUtil.getValueByKeyOrNone(
                                     resource_name.lower(),
                                     KNOWN_WRAPPER_TYPES
                             )

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        headers_method_params_str = ', ' + headers_method_params_str\
            if headers_method_params_str != '' \
            else headers_method_params_str

        resource_update_template_values = {
           'url':url,
           'resource_name_lc':resource_name.lower(),
           'docs' : Documentation.document(link),
           'headers_map_params_str': headers_map_params_str,
           'headers_method_params_str' : headers_method_params_str,
           'actual_self_name':actual_xml_entity if actual_xml_entity is not None \
                                                else resource_name
        }

        return resourceupdatetemplate\
               .generate(resource_update_template_values)
