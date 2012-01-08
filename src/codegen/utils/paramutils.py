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

from codegen.infrastructure.staticdataholder import PRESERVED_NAMES

class ParamUtils():
    @staticmethod
    def getMethodParamsByUrlParamsMeta(link):
        method_parameters = ''
        method_params = {}
        url_params = {}

        if link.request and link.request.url and link.request.url.parameters_set \
           and len(link.request.url.parameters_set) > 0:
            for parameters_set in link.request.url.parameters_set:
                for param in parameters_set.parameter:
                    url_params[param.name] = param.value
                    if param.name in PRESERVED_NAMES:
                        name_candidate = param.name + '_' + param.value
                    else:
                        name_candidate = param.name
                    if name_candidate == 'search':
                        method_parameters += param.value + '=None, '
                        method_params[param.value] = name_candidate
                    else:
                        method_parameters += name_candidate + '=None, '
                        method_params[name_candidate] = param.value

        return method_parameters[0:len(method_parameters) - 2], method_params, url_params

    @staticmethod
    def toDictStr(names, values):
        if len(names) != len(values): return ''
        output = '{'
        for i in range(len(names)):
            output += '\'' + names[i] + '\'' + ':' + values[i] + ','

        return output[0: len(output) - 1] + '}'
