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

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class UrlHelper(object):
    @staticmethod
    def replace(url, args={}):
        for k, v in args.items():
            url = url.replace(k, v)
        return url

    @staticmethod
    def append(url, urlparam):
        if urlparam:
            return url + '/' + urlparam
        return url

    @staticmethod
    def appendParameters(url, args={}):
        '''Appends url params to url'''

        matrix_params=''
        query_params=''

        if (args and len(args) > 0):
            for k, v in args.items():
                if v != None:
                    prms = k.split(':')
                    if len(prms) == 2 and prms[1] == 'matrix':
                        matrix_params += ';' + urlencode({prms[0] : v})
                    else:
                        k = prms[0] if len(prms) == 2 else k
                        query_params += '?' + urlencode({k : v}) if query_params.find('?') is -1 \
                                                                 else '&' + urlencode({k : v})
        return (url + matrix_params + query_params)
