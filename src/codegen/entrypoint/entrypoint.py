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
        "'''Generated at: " + str(datetime.datetime.now()) + "'''\n\n" + \
        "import types\n" + \
        "from ovirtsdk.infrastructure.errors import UnsecuredConnectionAttemptError\n" + \
        "from ovirtsdk.infrastructure import contextmanager\n" + \
        "from ovirtsdk.infrastructure.connectionspool import ConnectionsPool\n" + \
        "from ovirtsdk.infrastructure.proxy import Proxy\n" + \
        "from ovirtsdk.infrastructure.contextmanager import Mode\n"

        return entry_point_imports_template


    @staticmethod
    def instanceMethods(exclude=['actions', 'href', 'link', 'extensiontype_', 'creation_status', 'id', 'name', 'description'],
                        static_methods=['special_objects', 'product_info']):

        static_methods_template = "\n" + \
"""
    def get_%(attr)s(self):
        entry_point = contextmanager.get('entry_point')
        if entry_point:
            return entry_point.%(attr)s
        return None
"""
        dinamic_methods_template = "\n" + \
"""
    def get_%(attr)s(self):
        proxy = contextmanager.get('proxy')
        filter_header = contextmanager.get('filter')

        return proxy.request(method='GET',
                             url='/api').%(attr)s
"""

        methods_template = "\n" + \
"""
    def disconnect(self):
        ''' terminates server connection/s '''

        proxy = contextmanager.get('proxy')
        persistent_auth = contextmanager.get('persistent_auth')
        filter_header = contextmanager.get('filter')

        # If persistent authentication is enabled then we need to
        # send a last request as a hint to the server to close the
        # session:        
        if proxy and persistent_auth:
            try:
                proxy.request(method='GET',
                              url='/api',
                              last=True)
            except Exception:
                pass

        # Clear context
        contextmanager._clear(force=True)

    def test(self, throw_exception=False):
        ''' test server connectivity '''

        proxy = contextmanager.get('proxy')
        filter_header = contextmanager.get('filter')

        if proxy:
            try :
                proxy.request(method='GET',
                              url='/api')
            except Exception, e:
                if throw_exception: raise e
                else: return False
            return True
        return False

    def set_filter(self, filter):
        contextmanager.add('filter', filter)
"""
        from ovirtsdk.infrastructure import contextmanager
        entry_point_resource = contextmanager.get('proxy').request('GET', '/api')
        for attr in entry_point_resource.__dict__.keys():
            if attr not in exclude:
                if attr in static_methods:
                    methods_template += \
                        static_methods_template % {'attr':attr}
                else:
                    methods_template += \
                        dinamic_methods_template % {'attr':attr}

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
"""class API():
    def __init__(self, url, username, password, key_file=None, cert_file=None, ca_file=None, port=None, timeout=None, persistent_auth=True, insecure=False, filter=False, debug=False):

        \"""
        @param url: server url (format "http/s://server[:port]/api")
        @param username: user (format user@domain)
        @param password: password
        [@param key_file: client PEM key_file for ssl enabled connection]
        [@param cert_file: client PEM cert_file for ssl enabled connection]
        [@param ca_file: server ca_file for ssl enabled connection]
        [@param port: port to use (if not specified in url)]
        [@param timeout: request timeout]
        [@param persistent_auth: enable persistent authentication (format True|False)]
        [@param insecure: signals to not demand site trustworthiness for ssl enabled connection (format True|False)]
        [@param filter: signals if user permission based filtering should be turned on/off (format True|False)]
        [@param debug: debug (format True|False)]
        \"""

        # Create the connection pool:
        pool = ConnectionsPool(
            url=url,
            username=username,
            password=password,
            key_file=key_file,
            cert_file=cert_file,
            ca_file=ca_file,
            port=port,
            strict=False,
            timeout=timeout,
            insecure=insecure,
            debug=debug
        )

        # Create the proxy:
        proxy = Proxy(pool, persistent_auth)

        # Store filter to the context:
        contextmanager.add('filter', filter)

        # Get entry point
        entry_point = proxy.request(method='GET',
                                    url='/api')

        # If server returns no response for the root resource, this is sign
        # that used http protocol against SSL secured site
        if type(entry_point) == types.StringType and entry_point == '':
            raise UnsecuredConnectionAttemptError

        # Store entry point to the context
        contextmanager.add('entry_point', entry_point, Mode.R)

        # Store proxy to the context:
        contextmanager.add('proxy', proxy, Mode.R)

        # We need to remember if persistent auth is enabled:
        contextmanager.add('persistent_auth',
                           persistent_auth,
                           Mode.R)

"""

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
