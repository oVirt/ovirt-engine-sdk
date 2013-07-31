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

from codegen.xsd.abstractxsdcodegen import AbstractXsdCodegen
from codegen.utils.fileutils import FileUtils
from codegen.xsd.genparams import paramsHandle
import py_compile

class XsdCodegen(AbstractXsdCodegen):
    '''
    Providing XSD codegen capabilities
    '''

    XML_PARAMS_FILE = '../ovirtsdk/xml/params.py'
    XML_PARAMS_TMP_FILE = '/tmp/params.py'
    SCHEMA_TMP_FILE = '/tmp/schema.py'

    def __init__(self, api):
        '''
        @param path: codegen path
        '''
        AbstractXsdCodegen.__init__(self, XsdCodegen.XML_PARAMS_FILE, api)

    def doGenerate(self, path):
        '''
        Generates the code
        
        @param path: path to generate the code at
        '''
        AbstractXsdCodegen.doGenerate(self, path)

        with open(XsdCodegen.SCHEMA_TMP_FILE, 'w') as f:
            f.write('%s' % self._getSchema())

        paramsHandle(XsdCodegen.SCHEMA_TMP_FILE,
                     XsdCodegen.XML_PARAMS_FILE,
                     XsdCodegen.XML_PARAMS_TMP_FILE)

    def doClean(self, path):
        '''
        Performs Pre-generate cleanup
        
        @param path: path to perform cleanup at
        '''
        AbstractXsdCodegen.doClean(self, path)

        FileUtils.delete(XsdCodegen.XML_PARAMS_FILE)

    def doPostGenerate(self):
        '''
        Post-generate call
        '''
        AbstractXsdCodegen.doPostGenerate(self)

        FileUtils.delete(XsdCodegen.XML_PARAMS_TMP_FILE)
        FileUtils.delete(XsdCodegen.SCHEMA_TMP_FILE)

        # compile generated sources so the changes will be visible
        # to the consuming code that already loaded this module
        py_compile.compile(self.path)
