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

class ICodegen():
    '''
    Providing codegen interface'''

    def generate(self):
        '''
        Cleans the package and generates the code
        '''
        pass

    def doGenerate(self, path):
        '''
        Generates the code
        
        @param path: path to generate the code at
        '''
        pass

    def doPreGenerate(self):
        '''
        Pre-generate call
        '''
        pass

    def doPostGenerate(self):
        '''
        Post-generate call
        '''
        pass

    def doClean(self, path):
        '''
        Performs Pre-generate cleanup
        
        @param path: path to perform cleanup at
        '''
        pass
