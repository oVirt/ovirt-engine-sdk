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

from abc import abstractmethod

class ITemplate(object):
    '''
    ITemplate interface
    '''
    @abstractmethod
    def _loadTemplate(self):
        '''
         Loads resource template
    
         @return resource template
        '''
        pass

    def generate(self, params={}):
        '''
         Produces content from the template
        
         @param params: parameters to bind in to the template
         
         @return content
        '''
        pass
