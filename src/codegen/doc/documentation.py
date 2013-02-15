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


class Documentation():
    ''' Documentation '''
    DOC_OFFSET = '        '
    OVERLOAD_TEMPLATE = 'Overload'

    @staticmethod
    def document(link, custom_params={}, mapper={}, HEADERS_EXCLUDE=['Content-Type', 'Filter']):
        '''
        @param body: request body
        @param custom_params: custom params to add {param:required=true|false}
        @param custom_params: mapper params to add {param:required=true|false}
        
        
        @return: method documentation
        '''

        i = 0
        offset = Documentation.DOC_OFFSET

        doc_str = ""
        doc_str_in = offset + "'''\n"
        doc_str_out = offset + "'''\n"

        type_doc = offset + "@type %s:\n\n" % Documentation._getRequestType(link)
        return_doc = offset + "@return %s:\n" % Documentation._getResponseType(link)

        parameters_set_template = offset + Documentation.OVERLOAD_TEMPLATE + " %s:\n"
        parameters_set_offset = '  '
        collection_parameters_set_offset = '  '
        mand_param_doc_template = "@param %s: %s\n"
        opt_param_doc_template = "[@param %s: %s]\n"
        mand_ivar_doc_template = "@ivar %s: %s\n"
        opt_ivar_doc_template = "[@ivar %s: %s]\n"

        custom_mand_param_doc_template = "@param %s\n"
        custom_opt_param_doc_template = "[@param %s]\n"

        doc_str += doc_str_in
        doc_str += type_doc if type_doc.find('@type None:') == -1 else ''
        if hasattr(link, 'request') and hasattr(link.request, 'body') and hasattr(link.request.body, 'parameters_set'):
            for parameters_set in link.request.body.parameters_set:
                if len(link.request.body.parameters_set) > 1:
                    i += 1
                    mand_params = ''
                    opt_params = ''
                    doc_str += parameters_set_template % str(i)

                    mand_params, opt_params = Documentation._do_doc_sub_resource(mand_params, opt_params, parameters_set, offset,
                                                                                 collection_parameters_set_offset, parameters_set_offset,
                                                                                 mand_param_doc_template, opt_param_doc_template,
                                                                                 mand_ivar_doc_template, opt_ivar_doc_template)
                else:
                    mand_params = ''
                    opt_params = ''
                    mand_params, opt_params = Documentation._do_doc_resource(parameters_set, mand_params, opt_params,
                                                                             offset, collection_parameters_set_offset,
                                                                             mand_param_doc_template, opt_param_doc_template,
                                                                             mand_ivar_doc_template, opt_ivar_doc_template)

                doc_str += mand_params
                doc_str += opt_params

        for k in custom_params.keys():  # TODO: revisit - not optimal in terms of overload
            if len(mapper) == 0 or Documentation._isMapperHasKey(mapper, k) == True:
                if custom_params[k] == True:
                    doc_str += offset + custom_mand_param_doc_template % k
                else:
                    doc_str += offset + custom_opt_param_doc_template % k

        for k, v in mapper.items():
            if doc_str.find(k + ':') == -1:
                doc_str += offset + opt_param_doc_template % (k, v)

        # document http header params
        if hasattr(link, 'request') and hasattr(link.request, 'headers') and \
           link.request.headers:
            for header_parameter in link.request.headers.header:
                header_name = header_parameter.name.lower().replace('-', '_')
                if header_parameter.name not in HEADERS_EXCLUDE:
                    if header_parameter.required:
                        doc_str += Documentation.DOC_OFFSET + mand_param_doc_template % \
                                                              (header_name,
                                                               header_parameter.value)
                    else:
                        doc_str += Documentation.DOC_OFFSET + opt_param_doc_template % \
                                                              (header_name,
                                                               header_parameter.value)

        doc_str += (('\n' + return_doc) if doc_str != offset + "'''\n"
                                        else return_doc)
        doc_str += doc_str_out

        return doc_str

    @staticmethod
    def _isMapperHasKey(mapper, k):
        if mapper and len(mapper) > 0:
            for key in mapper.keys():
                if k.startswith(key + ':'):
                    return True
        return False

    @staticmethod
    def _getRequestType(link):
        if link.rel != 'update' and hasattr(link, 'request') and hasattr(link.request, 'body') and hasattr(link.request.body, 'type_'):
            return link.request.body.type_
        return None

    @staticmethod
    def _getResponseType(link):
        if hasattr(link, 'response') and hasattr(link.response, 'type_'):
            return link.response.type_
        return None

    @staticmethod
    def _do_doc_sub_resource(mand_params, opt_params, parameters_set, offset,
                collection_parameters_set_offset, parameters_set_offset,
                mand_param_doc_template, opt_param_doc_template, mand_ivar_doc_template,
                opt_ivar_doc_template):
        for parameter in parameters_set.parameter:
            if parameter.type_ == 'collection':
                if parameter.parameters_set and parameter.parameters_set.parameter:
                    if parameter.required == True:
                        mand_params += offset + \
                                       collection_parameters_set_offset + \
                                       mand_param_doc_template % (parameter.name,
                                                                  parameter.type_.replace('xs:', ''))
                        mand_params += offset + parameters_set_offset + '{\n'

                    else:
                        opt_params += offset + \
                                      collection_parameters_set_offset + \
                                      opt_param_doc_template % (parameter.name,
                                                                parameter.type_.replace('xs:', ''))
                        opt_params += offset + parameters_set_offset + '{\n'

                    for collection_parameter in parameter.parameters_set.parameter:
                        if parameter.required == True:
                            mand_params += offset + \
                                           parameters_set_offset + collection_parameters_set_offset + \
                                           mand_ivar_doc_template % (collection_parameter.name,
                                                                      collection_parameter.type_.replace('xs:', ''))
                        else:
                            opt_params += offset + \
                                          parameters_set_offset + collection_parameters_set_offset + \
                                          opt_ivar_doc_template % (collection_parameter.name,
                                                                    collection_parameter.type_.replace('xs:', ''))

                        if collection_parameter.type_ == 'collection':
                            if parameter.required == True:
                                mand_params += offset + collection_parameters_set_offset + parameters_set_offset + '{\n'
                            else:
                                opt_params += offset + collection_parameters_set_offset + parameters_set_offset + '{\n'

                            mand_params, opt_params = Documentation._do_doc_sub_resource(mand_params, opt_params,
                                                                                         collection_parameter.parameters_set,
                                                                                         offset + collection_parameters_set_offset + collection_parameters_set_offset,
                                                                                         collection_parameters_set_offset,
                                                                                         parameters_set_offset, mand_param_doc_template,
                                                                                         opt_param_doc_template, mand_ivar_doc_template,
                                                                                         opt_ivar_doc_template)

                            if parameter.required == True:
                                mand_params += offset + collection_parameters_set_offset + parameters_set_offset + '}\n'
                            else:
                                opt_params += offset + collection_parameters_set_offset + parameters_set_offset + '}\n'

                    if parameter.required == True:
                        mand_params += offset + parameters_set_offset + '}\n'
                    else:
                        opt_params += offset + parameters_set_offset + '}\n'
            else:
                if parameter.required == True:
                    mand_params += offset + \
                                   parameters_set_offset + \
                                   mand_param_doc_template % (parameter.name, parameter.type_.replace('xs:', ''))
                else:
                    opt_params += offset + \
                                  parameters_set_offset + \
                                  opt_param_doc_template % (parameter.name, parameter.type_.replace('xs:', ''))

        return mand_params, opt_params

    @staticmethod
    def _do_doc_resource(parameters_set, mand_params, opt_params, offset, collection_parameters_set_offset,
                         mand_param_doc_template, opt_param_doc_template, mand_ivar_doc_template,
                         opt_ivar_doc_template):
        for parameter in parameters_set.parameter:
            if parameter.type_ == 'collection':
                if parameter.parameters_set and parameter.parameters_set.parameter:
                    if parameter.required == True:
                        mand_params += offset + \
                                       mand_param_doc_template % (parameter.name,
                                                                  parameter.type_.replace('xs:', ''))
                        mand_params += offset + '{\n'

                    else:
                        opt_params += offset + \
                                      opt_param_doc_template % (parameter.name,
                                                                parameter.type_.replace('xs:', ''))
                        opt_params += offset + '{\n'
                    for collection_parameter in parameter.parameters_set.parameter:
                        if parameter.required == True:
                            mand_params += offset + collection_parameters_set_offset + \
                                           mand_ivar_doc_template % (collection_parameter.name,
                                                                      collection_parameter.type_.replace('xs:', ''))
                        else:
                            opt_params += offset + collection_parameters_set_offset + \
                                          opt_ivar_doc_template % (collection_parameter.name,
                                                                    collection_parameter.type_.replace('xs:', ''))

                        if collection_parameter.type_ == 'collection':
                            if parameter.required == True:
                                mand_params += offset + collection_parameters_set_offset + '{\n'
                            else:
                                opt_params += offset + collection_parameters_set_offset + '{\n'

                            mand_params, opt_params = Documentation._do_doc_resource(collection_parameter.parameters_set,
                                                                                     mand_params, opt_params,
                                                                                     offset + collection_parameters_set_offset + collection_parameters_set_offset,
                                                                                     collection_parameters_set_offset,
                                                                                     mand_param_doc_template, opt_param_doc_template,
                                                                                     mand_ivar_doc_template, opt_ivar_doc_template)

                            if parameter.required == True:
                                mand_params += offset + collection_parameters_set_offset + '}\n'
                            else:
                                opt_params += offset + collection_parameters_set_offset + '}\n'

                    if parameter.required == True:
                        mand_params += offset + '}\n'
                    else:
                        opt_params += offset + '}\n'

            else:
                if parameter.required == True:
                    mand_params += offset + \
                                   mand_param_doc_template % (parameter.name, parameter.type_.replace('xs:', ''))
                else:
                    opt_params += offset + \
                                  opt_param_doc_template % (parameter.name, parameter.type_.replace('xs:', ''))

        return mand_params, opt_params
