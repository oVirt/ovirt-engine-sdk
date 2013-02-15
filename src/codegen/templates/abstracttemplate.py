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

import os
from codegen.utils.fileutils import FileUtils
from codegen.templates.itemplate import ITemplate
import abc


class AbstractTemplate(ITemplate):
    '''
    Providing template abstraction services
    '''

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        '''
        @param noCopyrightTemplate
                   true/false (use this param when no need to fetch CopyrightTemplate)
        '''
        self.name = self.__getTemplateName()
        self.path = self.__getTemplatePath()
        self.template = self._loadTemplate();

    def __initResources(self):
        self.name = None
        self.template = None
        self.copyrightTemplate = None

    def __getTemplateName(self):
        '''
        Retrives template name
        '''

        return self.__class__.__name__

    def __getTemplatePath(self):
        '''
        Builds template path
        '''

        pathArr = __file__.split(os.path.sep)
        pathArr[-1] = self.name.lower()
        return os.path.sep.join(pathArr)


    def _loadTemplate(self):
        '''
        Loads template in given context

        @return template
        '''
        ITemplate._loadTemplate(self)

        try:
            return self.__readFileTemplate()
        except Exception, e:
            raise Exception("Template \"" + self.getName() + "\" not found.", e);

    def generate(self, params={}):
        '''
         Produces content from the template
        
         @param params: parameters to bind in to the template
         
         @return content
        '''

        ITemplate.generate(self, params=params)

        return self.getTemplate() % params

    def __readFileTemplate(self):
        '''
        Reads actual template file
        
        @return template content
        '''
        return FileUtils.getContent(self.path);

    def getName(self):
        '''
        @return template name
        '''

        return self.name;

    def getTemplate(self):
        '''
        @return abstract template form
        '''

        return self.template;
