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

class CollectionExceptions(object):

    @staticmethod
    def get(url, link, prms_str, method_params, url_params, headers_method_params_str,
            headers_map_params_str, collection_get_template_values):

        #Capabilities resource has unique structure which is not
        #fully comply with RESTful collection pattern, but preserved
        #in sake of backward compatibility
        if url == '/api/capabilities':
            return \
"""
    def get(self, id=None, **kwargs):
        '''
        [@param id: string (the id of the entity)]
        [@param **kwargs: dict (property based filtering)]

        @return VersionCaps:
        '''

        url = '/api/capabilities'

        if id:
            try :
                return VersionCaps(self.__getProxy().get(url=UrlHelper.append(url, id)),
                                   self.context)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif kwargs:
            result = self.__getProxy().get(url=url).version
            return VersionCaps(FilterHelper.getItem(FilterHelper.filter(result, kwargs)),
                               self.context)
        else:
            raise MissingParametersError(['id', 'kwargs'])
"""

        if url == '/api/disks':
            return \
            ("    def get(self, alias=None, " + headers_method_params_str + "id=None):\n" + \
             Documentation.document(link, {'alias: string (the alias of the entity)': False,
                                           'id   : string (the id of the entity)'  : False}) +
            "        url = '%(url)s'\n\n" + \

            "        if id:\n" +
            "            try :\n" + \
            "                return %(resource_type)s(self.__getProxy().get(url=UrlHelper.append(url, id),\n"
            "                                                               headers=" + headers_map_params_str + "),\n" + \
            "                                         self.context)\n" +
            "            except RequestError, err:\n" + \
            "                if err.status and err.status == 404:\n" + \
            "                    return None\n" + \
            "                raise err\n" + \
            "        elif alias:\n" +
            "            result = self.__getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':'alias='+alias}),\n"
            "                                           headers=" + headers_map_params_str + ").get_%(resource_name_lc)s()\n" + \
            "            return %(resource_type)s(FilterHelper.getItem(result),\n" + \
            "                                     self.context)\n" + \
            "        else:\n" + \
            "            raise MissingParametersError(['id', 'alias'])\n\n") % collection_get_template_values
