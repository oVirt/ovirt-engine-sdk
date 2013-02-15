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
from codegen.templates.subcollectiontemplate import SubCollectionTemplate
from codegen.templates.subcollectiongettemplate import SubCollectionGetTemplate
from codegen.templates.subcollectionlisttemplate import SubCollectionListTemplate
from codegen.templates.subcollectionlistwithparamstemplate import SubCollectionListWithParamsTemplate
from codegen.templates.subcollectionaddtemplate import SubCollectionAddTemplate

#============================================================
#======================SUB COLLECTION========================
#============================================================

subcollectiontemplate = SubCollectionTemplate()
subcollectiongettemplate = SubCollectionGetTemplate()
subcollectionlisttemplate = SubCollectionListTemplate()
subcollectionlistwithparamstemplate = SubCollectionListWithParamsTemplate()
subcollectionaddtemplate = SubCollectionAddTemplate()

class SubCollection(object):

    @staticmethod
    def collection(sub_collection_name, parent_resource_name_lc):

        sub_collection_get_template_values = {
          'sub_collection_name'    : sub_collection_name,
          'parent_resource_name_lc': parent_resource_name_lc.lower()
        }

        return subcollectiontemplate\
               .generate(sub_collection_get_template_values)

    @staticmethod
    def get(url, link, parent_resource_name_lc, encapsulating_resource,
            actual_resource_name_candidate, KNOWN_WRAPPER_TYPES={},
            NAMING_ENTITY_EXCEPTIONS={}):

        actual_encapsulating_resource = \
            TypeUtil.getValueByKeyOrNone(
                 encapsulating_resource.lower(),
                 KNOWN_WRAPPER_TYPES
             )

        actual_resource_name_lc = (
           ParseHelper.getXmlTypeInstance(
              actual_encapsulating_resource \
                    if actual_encapsulating_resource is not None \
                    else actual_resource_name_candidate.lower()
              )
           ).lower()

        if NAMING_ENTITY_EXCEPTIONS.has_key(actual_resource_name_lc):
            actual_resource_name_lc = \
                NAMING_ENTITY_EXCEPTIONS[actual_resource_name_lc]

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        headers_method_params_str = \
            headers_method_params_str + ', ' \
                if headers_method_params_str != '' \
                else headers_method_params_str

        sub_collection_get_template_values = {
          'url':url,
          'parent_resource_name_lc':parent_resource_name_lc.lower(),
          'resource_name_lc':encapsulating_resource.lower(),
          'actual_resource_name_lc':actual_resource_name_lc,
          'headers_method_params_str' : headers_method_params_str,
          'headers_map_params_str' : headers_map_params_str,
          'url_params_id' : UrlUtils.generate_url_identifiers_replacments(
                                  link,
                                  "                            ",
                                  continues=True, is_collection=True
                            ),
          'url_params_name' : UrlUtils.generate_url_identifiers_replacments(
                                  link,
                                  "                    ",
                                  continues=True, is_collection=True
                              ),
          'encapsulating_resource':actual_encapsulating_resource \
                if actual_encapsulating_resource is not None
                                                 else encapsulating_resource,
          'docs':  Documentation.document(
                      link,
                      {
                        'name: string (the name of the entity)': False,
                        'id  : string (the id of the entity)'  : False
                      }
                   )
        }

        return subcollectiongettemplate\
               .generate(sub_collection_get_template_values)

    @staticmethod
    def list(url, link, parent_resource_name_lc, encapsulating_resource,
             actual_resource_name_candidate, KNOWN_WRAPPER_TYPES={},
             NAMING_ENTITY_EXCEPTIONS={}):

        actual_encapsulating_resource = \
                TypeUtil.getValueByKeyOrNone(
                         encapsulating_resource.lower(),
                         KNOWN_WRAPPER_TYPES
                 )

        actual_resource_name_lc = (
                   ParseHelper.getXmlTypeInstance(
                        actual_encapsulating_resource \
                           if actual_encapsulating_resource is not None \
                           else actual_resource_name_candidate.lower()
                   )
        ).lower()

        if NAMING_ENTITY_EXCEPTIONS.has_key(actual_resource_name_lc):
            actual_resource_name_lc = NAMING_ENTITY_EXCEPTIONS[
                                           actual_resource_name_lc
                                      ]

        prms_str, method_params, url_params = \
            ParamUtils.getMethodParamsByUrlParamsMeta(link)

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        combined_method_params = prms_str + \
                                 (', ' if prms_str != '' and headers_method_params_str != '' else '') + \
                                 headers_method_params_str

        method_params_copy = method_params.copy()
        method_params['**kwargs'] = '**kwargs'

        sub_collection_list_template_values = {
           'url':url,
           'parent_resource_name_lc':parent_resource_name_lc.lower(),
           'actual_resource_name_lc':actual_resource_name_lc,
           'combined_method_params':combined_method_params,
           'headers_map_params_str':headers_map_params_str,
           'encapsulating_resource':actual_encapsulating_resource
                    if actual_encapsulating_resource is not None
                    else encapsulating_resource,
           'url_query_params': ParamUtils.toDictStr(
                    url_params.keys(),
                    method_params_copy.keys()
                )
        }



        if prms_str != '' or headers_method_params_str != '':
            sub_collection_list_template_values['docs'] = \
                    Documentation.document(
                       link,
                       {
                            '**kwargs: dict (property based filtering)"': False,
                            'query: string (oVirt engine search dialect query)':False
                        },
                        method_params
            )

            sub_collection_list_template_values['url_params'] = \
                UrlUtils.generate_url_identifiers_replacments(
                      link,
                      "                ",
                      continues=True, is_collection=True
                )

            return subcollectionlistwithparamstemplate\
                   .generate(sub_collection_list_template_values)
        else:
            sub_collection_list_template_values['docs'] = \
                Documentation.document(
                               link,
                               {
                                    '**kwargs: dict (property based filtering)"': False
                               }
                )

            sub_collection_list_template_values['url_params'] = \
                UrlUtils.generate_url_identifiers_replacments(
                              link,
                              "                ",
                              continues=True, is_collection=True
                )

            return subcollectionlisttemplate\
                   .generate(sub_collection_list_template_values)

    @staticmethod
    def add(url, link, body_type, parent_resource_name_lc, encapsulating_entity, KNOWN_WRAPPER_TYPES={}):

        actual_encapsulating_entity = \
            TypeUtil.getValueByKeyOrNone(
                 encapsulating_entity.lower(),
                 KNOWN_WRAPPER_TYPES
             )

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        headers_method_params_str = ', ' + headers_method_params_str \
            if headers_method_params_str != '' \
            else headers_method_params_str

        sub_collection_add_template_values = {
          'resource_to_add':body_type.lower(),
          'url':url,
          'headers_map_params_str':headers_map_params_str,
          'headers_method_params_str':headers_method_params_str,
          'parent_resource_name_lc':parent_resource_name_lc.lower(),
          'encapsulating_entity':actual_encapsulating_entity if actual_encapsulating_entity is not None \
                                                             else encapsulating_entity,
          'docs': Documentation.document(link),
          'url_params':UrlUtils.generate_url_identifiers_replacments(link,
                       "                ",
                       continues=True, is_collection=True)
        }

        return subcollectionaddtemplate\
               .generate(sub_collection_add_template_values)
