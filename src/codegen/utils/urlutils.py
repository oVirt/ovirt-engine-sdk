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


class UrlUtils(object):

    @staticmethod
    def __get_replacement_candidates(resources):
        cands = []
        for item in resources.values():
            if item and item.endswith(':id}'): cands.append(item)
        return cands

    @staticmethod
    def get_periods(link):
        assert link != None

        url = link.href
        s_url = url.split('/')
        s_url.pop(0)
        s_url.pop(0)

        return UrlUtils.__list_to_dict(s_url)

    @staticmethod
    def __list_to_dict(lst):
        dct = OrderedDict()
        for i in range(len(lst)):
            if (i % 2 is 0):
                coll = lst[i]
                res = lst[i + 1] if ((i + 1 < len(lst))) else None
                dct[coll] = res
        return dct

    @staticmethod
    def period_len(link):
        '''
        Retrieves amount of coll/res periods in url
        '''

        assert link != None

        url = link.href
        s_url = url.split('/')
        s_url.pop(0)
        s_url.pop(0)

        if url.endswith('/' + link.rel):
            s_url.reverse()
            s_url.remove(link.rel)

        return len(s_url) / 2

    @staticmethod
    def __generate_parentclass_identifiers(num):
        assert num != None

        res = 'self'
        for _ in range(num):
            res += '.parentclass'
        res += '.get_id()'

        return res

    @staticmethod
    def generate_url_identifiers_replacments(link, offset, continues=False, is_collection=False):
        '''Replaces identifiers with real names'''

        url = ''
        replacement_candidates = UrlUtils.__get_replacement_candidates(UrlUtils.get_periods(link))
        replacement_candidates_len = len(replacement_candidates)
        if replacement_candidates:
            for i in range(replacement_candidates_len):
                if len(replacement_candidates) == 1:
                        url += (offset if not continues else "") + "{'" + replacement_candidates[i] + "': " + \
                               UrlUtils.__generate_parentclass_identifiers(replacement_candidates_len - i) + "}"
                        return url
                else:
                    if not is_collection:
                        replacement_offset = i + 1
                    else:
                        replacement_offset = i
                    if i == 0:
                        url += (offset if not continues else "") + "{'" + replacement_candidates[i] + "' : " + \
                               UrlUtils.__generate_parentclass_identifiers(replacement_candidates_len - replacement_offset)
                        if len(replacement_candidates) == 1:return url
                    elif i != (replacement_candidates_len - 1):
                        url += ",\n"
                        url += offset + " '" + replacement_candidates[i] + "': " + \
                               UrlUtils.__generate_parentclass_identifiers(replacement_candidates_len - replacement_offset)
                    else:
                        url += ",\n"
                        url += offset + " '" + replacement_candidates[i] + "': " + \
                               UrlUtils.__generate_parentclass_identifiers(replacement_candidates_len - replacement_offset) + "}"# "self.get_id()}"

        return url
