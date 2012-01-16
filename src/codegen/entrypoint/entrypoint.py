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

class EntryPoint(object):

    @staticmethod
    def entryPointImports():
        entry_point_imports_template = \
        "#\n" + \
        "# Copyright (c) 2010 Red Hat, Inc.\n" + \
        "#\n" + \
        "# Licensed under the Apache License, Version 2.0 (the \"License\");\n" + \
        "# you may not use this file except in compliance with the License.\n" + \
        "# You may obtain a copy of the License at\n" + \
        "#\n" + \
        "#           http://www.apache.org/licenses/LICENSE-2.0\n" + \
        "#\n" + \
        "# Unless required by applicable law or agreed to in writing, software\n" + \
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n" + \
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n" + \
        "# See the License for the specific language governing permissions and\n" + \
        "# limitations under the License.\n" + \
        "#\n" + \
        "\n\n########################################\n" + \
        "############ GENERATED CODE ############\n" + \
        "########################################\n\n" + \
        "'''\nGenerated at: " + str(datetime.datetime.now()) + "\n\n" + \
        "@author: mpastern@redhat.com\n'''\n\n" + \
        "from ovirtsdk.infrastructure import contextmanager\n" + \
        "from ovirtsdk.infrastructure.connectionspool import ConnectionsPool\n" + \
        "from ovirtsdk.infrastructure.proxy import Proxy\n" + \
        "from ovirtsdk.infrastructure.contextmanager import Mode\n"

        return entry_point_imports_template


    @staticmethod
    def instanceMethods():
        methods_template = "\n" + \
        "    def disconnect(self):\n" + \
        "        ''' terminates server connection/s '''\n" + \
        "        contextmanager._remove('proxy', force=True)\n" + \
        "\n" + \
        "    def test(self):\n" + \
        "        ''' test server connectivity '''\n" + \
        "        proxy = contextmanager.get('proxy')\n" + \
        "        if proxy:\n" + \
        "            proxy.request(method='GET', url='/api')\n" + \
        "            return True\n" + \
        "        return False\n"

        return methods_template

    @staticmethod
    def entryPointCustomImports(types=[]):
        entry_point_custom_imports_template = "from ovirtsdk.infrastructure.brokers import % s\n"

        imports = ''
        for item in types:
            imports += entry_point_custom_imports_template % item

        return imports + ('\n\n')

    @staticmethod
    def entryPoint(types=[], rootCollections=''):
        api_template = EntryPoint.entryPointImports() + \
        EntryPoint.entryPointCustomImports(types) + \
        "class API():\n" + \
        "    #TODO: - read .ini configuration\n\n" + \
        "    def __init__(self, url, username, password, key_file=None, cert_file=None, port=None, timeout=None):\n" + \
        "        contextmanager.add('proxy',\n" + \
        "                           Proxy(ConnectionsPool(url=url,\n" + \
        "                                                 username=username,\n" + \
        "                                                 password=password,\n" + \
        "                                                 key_file=key_file,\n" + \
        "                                                 cert_file=cert_file,\n" + \
        "                                                 port=port,\n" + \
        "                                                 strict=False,\n" + \
        "                                                 timeout=timeout)),\n" + \
        "                           Mode.R)\n\n"

        return (api_template + rootCollections + EntryPoint.instanceMethods())

    @staticmethod
    def collection(name, item={}):
        entrypoint_template = '        self.%s = %s()\n'
        if item.has_key('root_collection') and item['root_collection'] == True:
            if  item.has_key('name'):
                coll_name = item['name']
            else:
                coll_name = name
            return entrypoint_template % (coll_name.lower(), coll_name)
        return None
