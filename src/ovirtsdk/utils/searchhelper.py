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
        '''Appends search query to url'''

        if (qargs and len(qargs) > 0):
            for k, v in qargs.items():
                if v != None:
                    url += '?' + urlencode({k : v}) if url.find('?') is -1 \
                                                    else '&' + urlencode({k : v})
        return url

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
                    value = getattr(value, at, None)
                    if value is None:
                        break
                if not hasattr(match, 'match') and value != match:
                    break
                if hasattr(match, 'match') and (value is None or not match.match(str(value))):
                    break
            else:
                matched.append(res)
        return matched
