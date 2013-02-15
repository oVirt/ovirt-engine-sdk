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
import abc

class AbstractRsdlCodegen(ICodegen):
    '''
    Providing RSDL codegen capabilities abstraction
    '''

    __metaclass__ = abc.ABCMeta

    def __init__(self, path):
        '''
        @param path: the codegen path 
        '''
        self.path = path

    def generate(self):
        '''
        Cleans the package and generates the code
        '''
        self.doClean(self.path)
        self.doPreGenerate()
        self.doGenerate(self.path)
        self.doPostGenerate()
