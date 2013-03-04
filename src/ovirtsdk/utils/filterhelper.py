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

from ovirtsdk.utils.searchhelper import SearchHelper
from ovirtsdk.infrastructure.errors import AmbiguousQueryError

class FilterHelper():
    @staticmethod
    def filter(collection, kwargs={}):
        '''Filters collection based on **kwargs'''
        return SearchHelper.filterResults(collection, kwargs) if (len(kwargs) is not 0) else collection

    @staticmethod
    def getItem(result=[], query=None):
        '''Returns first item in collection if exist, otherwise None'''

        if len(result) > 1:
            raise AmbiguousQueryError(query)
        return result[0] if result else None
