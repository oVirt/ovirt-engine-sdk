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
from ovirtsdk.utils.ordereddict import OrderedDict


class HeaderUtils(object):

    @staticmethod
    def generate_method_params(link, HEADERS_EXCLUDE=['Content-Type', 'Filter'], CACHED_HEADERS={}):
        params_str = ''
        headers_str = ''
        if hasattr(link, 'request') and hasattr(link.request, 'headers') and \
           link.request.headers:
            for header_parameter in link.request.headers.header:
                if header_parameter.name not in HEADERS_EXCLUDE:
                    header_name = header_parameter.name.lower().replace('-', '_')
                    if header_name not in CACHED_HEADERS.keys():
                        if header_parameter.required:
                            params_str += header_name  + ', '
                        else:
                            params_str += header_name + '=None, '
                        headers_str += ', "' + header_parameter.name + '":' + header_parameter.name.lower().replace('-', '_')
                    else:
                        headers_str += ', "' + header_parameter.name + '":' + CACHED_HEADERS[header_name]
            headers_str = headers_str[2:] if headers_str != '' else headers_str
        return params_str[:len(params_str) - 2] if params_str != '' else params_str, '{' + headers_str + '}'

    @staticmethod
    def generate_header_params(link, offset):
        holder = OrderedDict()
