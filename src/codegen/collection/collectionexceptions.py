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


#============================================================
#=======================COLLECTION RESOURCE==================
#============================================================

from codegen.doc.documentation import Documentation
from codegen.templates.collectionlistcapabilitiestemplate import CollectionListCapabilitiesTemplate
from codegen.templates.collectiongetcapabilitiestemplate import CollectionGetCapabilitiesTemplate
from codegen.templates.collectiongetdiskstemplate import CollectionGetDisksTemplate

collectionlistcapabilitiestemplate = CollectionListCapabilitiesTemplate()
collectiongetcapabilitiestemplate = CollectionGetCapabilitiesTemplate()
collectiongetdiskstemplate = CollectionGetDisksTemplate()

class CollectionExceptions(object):

    @staticmethod
    def list():
        return collectionlistcapabilitiestemplate.generate()

    @staticmethod
    def get(url, link, prms_str, method_params, url_params, headers_method_params_str,
            headers_map_params_str, collection_get_template_values):

        # Capabilities resource has unique structure which is not
        # fully comply with RESTful collection pattern, but preserved
        # in sake of backward compatibility
        if url == '/api/capabilities':
            return collectiongetcapabilitiestemplate\
                   .generate()

        if url == '/api/disks':
            collection_get_template_values['docs'] = \
                    Documentation.document(link, {
                              'alias: string (the alias of the entity)': False,
                              'id   : string (the id of the entity)'  : False
                              }
                   )

            collection_get_template_values['headers_method_params_str'] = \
                headers_method_params_str

            collection_get_template_values['headers_map_params_str'] = \
                headers_map_params_str

            return collectiongetdiskstemplate.generate(collection_get_template_values)
