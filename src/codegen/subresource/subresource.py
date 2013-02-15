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
from ovirtsdk.utils.parsehelper import ParseHelper
from codegen.utils.urlutils import UrlUtils
from codegen.utils.headerutils import HeaderUtils
from codegen.resource.resource import Resource
from codegen.templates.subresourcetemplate import SubResourceTemplate
from codegen.templates.subresourcecollectionactiontemplate import SubResourceCollectionActionTemplate
from codegen.templates.subresourceactiontemplate import SubResourceActionTemplate
from codegen.templates.subresourceupdatetemplate import SubResourceUpdateTemplate
from codegen.templates.subresourcedeletetemplate import SubResourceDeleteTemplate
from codegen.templates.subresourcedeletewithbodytemplate import SubResourceDeleteWithBodyTemplate
from codegen.templates.subresourcedeletewithurlparamstemplate import SubResourceDeleteWithUrlParamsTemplate
from codegen.templates.subresourcedeletewithurlparamsandbodytemplate import SubResourceDeleteWithUrlParamsAndBodyTemplate


#============================================================
#=====================SUB COLLECTION RESOURCE================
#============================================================

subresourcetemplate = SubResourceTemplate()
subresourcecollectionactiontemplate = SubResourceCollectionActionTemplate()
subresourceactiontemplate = SubResourceActionTemplate()
subresourceupdatetemplate = SubResourceUpdateTemplate()
subresourcedeletetemplate = SubResourceDeleteTemplate()
subresourcedeletewithbodytemplate = SubResourceDeleteWithBodyTemplate()
subresourcedeletewithurlparamstemplate = SubResourceDeleteWithUrlParamsTemplate()
subresourcedeletewithurlparamsandbodytemplate = SubResourceDeleteWithUrlParamsAndBodyTemplate()

class SubResource(object):
    @staticmethod
    def resource(sub_res_type, encapsulating_entity, parent, KNOWN_WRAPPER_TYPES={}):

        actual_xml_entity = TypeUtil.getValueByKeyOrNone(
                                     encapsulating_entity.lower(),
                                     KNOWN_WRAPPER_TYPES
                             )

        actual_xml_type = ParseHelper.getXmlType(encapsulating_entity)

        actual_sub_res_type = TypeUtil.getValueByKeyOrNone(
                                     sub_res_type.lower(),
                                     KNOWN_WRAPPER_TYPES
                             )

        sub_collection_resource_template_values = {
           'encapsulating_entity':actual_sub_res_type \
                    if actual_sub_res_type is not None\
                    else sub_res_type,
           'sub_res_type': actual_sub_res_type \
                    if actual_sub_res_type is not None \
                    else actual_xml_entity \
                        if actual_xml_entity is not None \
                        else actual_xml_type.__name__ \
                            if actual_xml_type is not None \
                            else encapsulating_entity,
           'parent':parent.lower(),
           'encapsulated_entity':encapsulating_entity.lower(),
           'fixme':Resource.SUB_COLLECTIONS_FIXME
       }

        return subresourcetemplate\
                .generate(sub_collection_resource_template_values)

    @staticmethod
    def action(url, link, action_name, parent_resource_name_lc,
               body_type, resource_name_lc, method, action_params={},
               collection_action=False):

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        headers_method_params_str = ', ' + headers_method_params_str \
                if headers_method_params_str != '' \
                else headers_method_params_str


        sub_collection_resource_action_template_values = {
              'url':url,
              'action_name':action_name,
              'method': method,
              'parent_resource_name_lc':parent_resource_name_lc.lower(),
              'body_type':body_type,
              'body_type_lc':body_type.lower(),
              'headers_map_params_str' : headers_map_params_str,
              'headers_method_params_str' : headers_method_params_str,
              'resource_name_lc':resource_name_lc.lower(),
              'docs' : Documentation.document(link),
              'add_method_params' : Resource._addMethodParams(
                                        action_params.keys()
                                    ),
              'add_action_parans' : Resource._addActionParams(
                                        action_params
                                    ),
              'url_params' : UrlUtils.generate_url_identifiers_replacments(
                                           link,
                                           offset="                ",
                                           continues=True
                                      )
        }

        if collection_action == True:
            sub_collection_resource_action_template = \
                subresourcecollectionactiontemplate.generate(
                         sub_collection_resource_action_template_values
                )
        else:
            sub_collection_resource_action_template = \
                subresourceactiontemplate.generate(
                        sub_collection_resource_action_template_values
                )

        return sub_collection_resource_action_template

    @staticmethod
    def update(url, link, parent_resource_name_lc, resource_name,
               returned_type, KNOWN_WRAPPER_TYPES):

        actual_xml_entity = TypeUtil.getValueByKeyOrNone(
                                         returned_type.lower(),
                                         KNOWN_WRAPPER_TYPES
                                     )

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        headers_method_params_str = ', ' + headers_method_params_str \
                if headers_method_params_str != '' \
                else headers_method_params_str

        prms_str, method_params, url_params = \
            ParamUtils.getMethodParamsByUrlParamsMeta(link)

        if prms_str != '' or headers_method_params_str != '':
            combined_method_params = \
            ', ' if prms_str != '' and not prms_str.startswith(',') else ''
            combined_method_params += prms_str + headers_method_params_str

        method_params_copy = method_params.copy()

        url_params = ParamUtils.toDictStr(
                                      url_params.keys(),
                                      method_params_copy.keys()
                                )

        url_identifiers_replacments = \
            UrlUtils.generate_url_identifiers_replacments(
                          link,
                          offset="            ",
                          continues=True
                      )

        sub_collection_resource_update_template_values = {
             'url':url,
            'parent_resource_name_lc':parent_resource_name_lc.lower(),
            'resource_name':resource_name,
            'resource_name_lc':resource_name.lower(),
            'url_identifiers_replacments' : url_identifiers_replacments,
            'headers_map_params_str' : headers_map_params_str,
            'combined_method_params' : combined_method_params,
            'url_params_separator' : (", " + url_params) if url_params != '' else '',
            'docs' : Documentation.document(link, {}, method_params),
            'returned_type':actual_xml_entity if actual_xml_entity is not None
                                              else returned_type
        }

        return subresourceupdatetemplate\
                .generate(sub_collection_resource_update_template_values)

    @staticmethod
    def delete(url, link, parent_resource_name_lc, resource_name_lc, body_type):

        prms_str, method_params, url_params = \
            ParamUtils.getMethodParamsByUrlParamsMeta(link)

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        combined_method_params = prms_str + (', ' \
                                     if prms_str != '' and headers_method_params_str != '' \
                                     else '') + headers_method_params_str

        headers_map_params_str_with_no_ct = \
            headers_map_params_str.replace('}', ',"Content-type":None}') \
                                            if headers_map_params_str != '{}' \
                                            else '{"Content-type":None}'

        body_instance = ParamUtils.getBodyInstance(link)
        body_instance_str = '=' + body_instance if body_instance else ''


        sub_collection_resource_delete_template_values = {
              'url':url,
              'body_type_lc':body_type.lower() if body_type is not None
                                               else None,
              'parent_resource_name_lc':parent_resource_name_lc.lower(),
              'headers_map_params_str_with_no_ct' : headers_map_params_str_with_no_ct,
              'combined_method_params' : combined_method_params,
              'resource_name_lc':resource_name_lc.lower(),
              'body_instance_str' : body_instance_str,
              'headers_map_params_str': headers_map_params_str,
              'url_params' : ParamUtils.toDictStr(
                                          url_params.keys(),
                                          method_params.copy().keys()
                                        )
        }

        if prms_str != '' or headers_method_params_str != '':
            sub_collection_resource_delete_template_values['docs'] = \
                Documentation.document(link, {}, method_params)

            sub_collection_resource_delete_template_values['url_identifyiers'] = \
                UrlUtils.generate_url_identifiers_replacments(
                           link,
                           offset="            "
                         )

            sub_collection_resource_delete_template = \
                subresourcedeletewithurlparamstemplate\
                    .generate(sub_collection_resource_delete_template_values)

            body_sub_collection_resource_delete_template = \
                subresourcedeletewithurlparamsandbodytemplate\
                    .generate(sub_collection_resource_delete_template_values)
        else:
            sub_collection_resource_delete_template_values['docs'] = \
                Documentation.document(link)

            sub_collection_resource_delete_template_values['url_identifyiers'] = \
                UrlUtils.generate_url_identifiers_replacments(
                           link,
                           offset="                ",
                           continues=True
                         )
            sub_collection_resource_delete_template_values['url_identifyiers_with_body'] = \
                UrlUtils.generate_url_identifiers_replacments(
                           link,
                           offset="                                                               "
                         )

            sub_collection_resource_delete_template = \
                subresourcedeletetemplate\
                    .generate(sub_collection_resource_delete_template_values)


            body_sub_collection_resource_delete_template = \
                subresourcedeletewithbodytemplate\
                    .generate(sub_collection_resource_delete_template_values)

        if not body_type:
            return sub_collection_resource_delete_template
        else:
            return body_sub_collection_resource_delete_template
