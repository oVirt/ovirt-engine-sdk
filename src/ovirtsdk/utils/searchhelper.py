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

from urllib import urlencode
import re
import fnmatch

class SearchHelper():

    @staticmethod
    def appendQuery(url, qargs={}):
        '''Appends url params to url'''

        matrix_params=''
        query_params=''
        
        if (qargs and len(qargs) > 0):
            for k, v in qargs.items():
                if v != None:
                    prms = k.split(':')
                    if len(prms) == 2 and prms[1] == 'matrix':
                        matrix_params += ';' + urlencode({prms[0] : v})
                    else:
                        k = prms[0] if len(prms) == 2 else k
                        query_params += '?' + urlencode({k : v}) if query_params.find('?') is -1 \
                                                                 else '&' + urlencode({k : v})
        return (url + matrix_params + query_params)

    @staticmethod
    def filterResults(result, constraints={}):
        '''Provides filtering capabilities base on custom constraint'''
        matched = [];
        compiled = []
        for attr in constraints:
            match = constraints[attr]
            if isinstance(match, str):
                match = re.compile(fnmatch.translate(match))
            compiled.append((attr.split('.'), match))
        for res in result:
            for attr, match in compiled:
                value = res
                for at in attr:
                    if type(value) is list:
                        values = []
                        for one_val in value:
                             val = getattr(one_val, at, None)
                             if val is not None:
                                 values.append(val)
                        value = values
                    else:
                        value = getattr(value, at, None)
                    if value is None:
                        break
                if type(value) is list:
                    for val in value:
                         if hasattr(match, 'match') and (val is not None and match.match(str(val))):
                             matched.append(res)
                             break
                if not hasattr(match, 'match') and value != match:
                    break
                if hasattr(match, 'match') and (value is None or not match.match(str(value))):
                    break
            else:
                matched.append(res)
        return matched
