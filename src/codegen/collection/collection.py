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
from codegen.utils.paramscontainer import ParamsContainer
from codegen.templates.collectiontemplate import CollectionTemplate
from codegen.templates.collectiongetsearchabletemplate import CollectionGetSearchableTemplate
from codegen.templates.collectiongetnotsearchabletemplate import CollectionGetNotSearchableTemplate
from codegen.templates.collectionlistsearchabletemplate import CollectionListSearchableTemplate
from codegen.templates.collectionlistnotsearchabletemplate import CollectionListNotSearchableTemplate
from codegen.templates.collectionaddtemplate import CollectionAddTemplate

collectiontemplate = CollectionTemplate()
collectiongetsearchabletemplate = CollectionGetSearchableTemplate()
collectiongetnotsearchabletemplate = CollectionGetNotSearchableTemplate()
collectionlistsearchabletemplate = CollectionListSearchableTemplate()
collectionlistnotsearchabletemplate = CollectionListNotSearchableTemplate()
collectionaddtemplate = CollectionAddTemplate()

class Collection(object):

    @staticmethod
    def collection(collection_name):

        collection_resource_template_values = {
               'collection_name':collection_name
        }

        return collectiontemplate \
               .generate(collection_resource_template_values)

    @staticmethod
    def get(url, resource_type, link, KNOWN_WRAPPER_TYPES={}):

        actual_resource_type = \
            TypeUtil.getValueByKeyOrNone(
                     resource_type.lower(), KNOWN_WRAPPER_TYPES
             )

        actual_resource_name_lc = (
                ParseHelper.getXmlTypeInstance(
                        resource_type.lower()
                )
        ).lower()

        prms_str, method_params, url_params = \
            ParamUtils.getMethodParamsByUrlParamsMeta(link)

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        headers_method_params_str = headers_method_params_str + ', ' \
                if headers_method_params_str != '' \
                else headers_method_params_str

        collection_get_template_values = {
          'url':url,
          'resource_name_lc':actual_resource_name_lc,
          'headers_method_params_str' : headers_method_params_str,
          'headers_map_params_str' : headers_map_params_str,
          'resource_type' : actual_resource_type \
                if actual_resource_type is not None \
                else resource_type,
          'docs' : Documentation.document(
                          link, {
                            ParamsContainer.NAME_SEARCH_PARAM: False,
                            ParamsContainer.ID_SEARCH_PARAM  : False
                            }
                   )
        }

        # Capabilities resource has unique structure which is not
        # fully comply with RESTful collection pattern, but preserved
        # in sake of backward compatibility
        if url == '/capabilities':
            return CollectionExceptions.get(
                        url,
                        link,
                        prms_str,
                        method_params,
                        url_params,
                        headers_method_params_str,
                        headers_map_params_str,
                        collection_get_template_values
                    )

        # /disks search-by-name paradigm was broken by the engine
        # should be fixed later on
        if url == '/disks':
            return CollectionExceptions.get(
                        url,
                        link,
                        prms_str,
                        method_params,
                        url_params,
                        headers_method_params_str,
                        headers_map_params_str,
                        collection_get_template_values
                    )

        if 'search:query' in url_params:
            return collectiongetsearchabletemplate.generate(
                                            collection_get_template_values
                   )
        else:
            return collectiongetnotsearchabletemplate.generate(
                                           collection_get_template_values
                   )

    @staticmethod
    def list(url, resource_type, link, KNOWN_WRAPPER_TYPES={}):

        actual_resource_type = TypeUtil.getValueByKeyOrNone(
            resource_type.lower(),
            KNOWN_WRAPPER_TYPES
        )

        actual_resource_name_lc = (
           ParseHelper.getXmlTypeInstance(
                          resource_type.lower()
           )
        ).lower()

        prms_str, method_params, url_params = \
            ParamUtils.getMethodParamsByUrlParamsMeta(link)

        headers_method_params_str, headers_map_params_str = \
            HeaderUtils.generate_method_params(link)

        method_params_copy = method_params.copy()
        method_params['**kwargs'] = '**kwargs'

        collection_list_template_values = {
           'url':url,
           'resource_name_lc':actual_resource_name_lc,
           'resource_type' : actual_resource_type \
                if actual_resource_type is not None \
                else resource_type
        }


        # Capabilities resource has unique structure which is not
        # fully comply with RESTful collection pattern, but preserved
        # in sake of backward compatibility
        if url == '/capabilities':

            return CollectionExceptions.list()
        elif prms_str != '' or headers_method_params_str != '':

            combined_method_params = prms_str + (
                ', ' if prms_str != '' and headers_method_params_str != '' \
                     else ''
             ) + headers_method_params_str

            collection_list_template_values['docs'] = \
                    Documentation.document(link, {
                              ParamsContainer.KWARGS_PARAMS: False,
                              ParamsContainer.QUERY_PARAMS:False
                              },
                              method_params
                    )

            collection_list_template_values['url_params'] = \
                    ParamUtils.toDictStr(
                             url_params.keys(),
                             method_params_copy.keys()
                    )

            collection_list_template_values['headers_map_params_str'] = \
                    headers_map_params_str

            collection_list_template_values['combined_method_params'] = \
                    combined_method_params

            return collectionlistsearchabletemplate \
                   .generate(collection_list_template_values)
        else:
            collection_list_template_values['docs'] = \
                    Documentation.document(link, {
                                  ParamsContainer.KWARGS_PARAMS: False
                              }
                    )

            return collectionlistnotsearchabletemplate \
                   .generate(collection_list_template_values)

    @staticmethod
    def add(url, body_type, response_type, link, KNOWN_WRAPPER_TYPES={}):

        actual_resource_type = \
                    TypeUtil.getValueByKeyOrNone(
                             response_type.lower(),
                             KNOWN_WRAPPER_TYPES
                    )

        headers_method_params_str, headers_map_params_str = \
              HeaderUtils.generate_method_params(link)

        headers_method_params_str = ', ' + headers_method_params_str \
              if headers_method_params_str != '' \
              else headers_method_params_str

        collection_add_template_values = {
              'url':url,
              'resource_to_add_lc':body_type.lower(),
              'headers_method_params_str' : headers_method_params_str,
              'docs' : Documentation.document(link),
              'headers_map_params_str': headers_map_params_str,
              'resource_type' : actual_resource_type \
                    if actual_resource_type is not None
                    else response_type
        }

        return collectionaddtemplate\
               .generate(collection_add_template_values)
