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

from codegen.common.icodegen import ICodegen
from ovirtsdk.infrastructure.context import context

class AbstractXsdCodegen(ICodegen):
    '''
    Providing XDS codegen capabilities abstraction
    '''

    SCHEMA_URI = '/api?schema'

    def __init__(self, path, api):
        '''
        @param path: the codegen path 
        '''
        self.path = path
        self.__api = api
        self.context = self.__api.id

    def _getSchema(self):
        '''
        Downloads XSD schema from the api
        '''
        context.manager[self.context].add('filter', False)
        return context.manager[self.context].get('proxy') \
                                            .request('GET', AbstractXsdCodegen.SCHEMA_URI, noParse=True)

    def generate(self):
        '''
        Generates the code
        '''
        self.doClean(self.path)
        self.doPreGenerate()
        self.doGenerate(self.path)
        self.doPostGenerate()
