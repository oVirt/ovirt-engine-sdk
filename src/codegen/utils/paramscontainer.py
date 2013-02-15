#
# Copyright (c) 2012 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


class ParamsContainer(object):
    NAME_SEARCH_PARAM = 'name: string (the name of the entity)'
    ID_SEARCH_PARAM = 'id  : string (the id of the entity)'
    KWARGS_PARAMS = '**kwargs: dict (property based filtering)'
    QUERY_PARAMS = 'query: string (oVirt engine search dialect query)'
