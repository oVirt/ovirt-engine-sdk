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


import datetime
from ovirtsdk.infrastructure.context import context
from codegen.templates.entrypointmethodstemplate import EntryPointMethodsTemplate
from codegen.templates.entrypointheadtemplate import EntryPointHeadTemplate
from codegen.templates.entrypointstaticmethodtemplate import EntryPointStaticMethodTemplate
from codegen.templates.entrypointdyinamicmethodtemplate import EntryPointDyinamicMethodTemplate
from codegen.templates.entrypointtemplate import EntryPointTemplate

entrypointheadtemplate = EntryPointHeadTemplate()
entrypointmethodstemplate = EntryPointMethodsTemplate()
entrypointstaticmethodtemplate = EntryPointStaticMethodTemplate()
entrypointdyinamicmethodtemplate = EntryPointDyinamicMethodTemplate()
entrypointtemplate = EntryPointTemplate()

class EntryPoint(object):

    @staticmethod
    def entryPointImports():

        entry_point_values = {}
        entry_point_values['timestamp'] = \
            "'''Generated at: " + str(datetime.datetime.now()) + "'''"

        return entrypointheadtemplate\
               .generate(entry_point_values)


    @staticmethod
    def instanceMethods(api,
                        exclude=['actions',
                                 'href',
                                 'link',
                                 'extensiontype_',
                                 'creation_status',
                                 'id',
                                 'name',
                                 'description'
                         ],
                        static_methods=['special_objects',
                                        'product_info',
                                        'comment'
                        ]):

        static_methods_template = entrypointstaticmethodtemplate

        dinamic_methods_template = entrypointdyinamicmethodtemplate

        methods_template = entrypointmethodstemplate.generate()

        entry_point_resource = context.manager[api.id]\
                               .get('proxy').request('GET', '/api')

        for attr in entry_point_resource.__dict__.keys():
            if attr not in exclude:
                if attr in static_methods:
                    methods_template += \
                        static_methods_template.generate({'attr':attr})
                else:
                    methods_template += \
                        dinamic_methods_template.generate({'attr':attr})

        return methods_template

    @staticmethod
    def entryPointCustomImports(types=[]):

        entry_point_custom_imports_template = \
            "from ovirtsdk.infrastructure.brokers import % s\n"

        imports = ''
        for item in types:
            imports += entry_point_custom_imports_template % item

        return imports + ('\n\n')

    @staticmethod
    def entryPoint(api, types=[], rootCollections=''):

        api_template = EntryPoint.entryPointImports() + \
                       EntryPoint.entryPointCustomImports(types) + \
                       entrypointtemplate.generate()

        return (
            api_template +
            rootCollections +
            EntryPoint.instanceMethods(api)
            )

    @staticmethod
    def collection(name, item={}):

        entrypoint_template = '        self.%s = %s(self.id)\n'

        if item.has_key('root_collection') and item['root_collection'] == True:
            if  item.has_key('name'):
                coll_name = item['name']
            else:
                coll_name = name
            return entrypoint_template % (coll_name.lower(), coll_name)
        return None
