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
        "import types\n\n" + \
        "from ovirtsdk.infrastructure.errors import UnsecuredConnectionAttemptError\n" + \
        "from ovirtsdk.infrastructure.connectionspool import ConnectionsPool\n" + \
        "from ovirtsdk.infrastructure.errors import DisconnectedError\n" + \
        "from ovirtsdk.infrastructure.errors import ImmutableError\n" + \
        "from ovirtsdk.infrastructure.context import context\n" + \
        "from ovirtsdk.infrastructure.proxy import Proxy\n\n" + \
        "from ovirtsdk.infrastructure.cache import Mode\n"

        return entry_point_imports_template


    @staticmethod
    def instanceMethods(api, exclude=['actions', 'href', 'link', 'extensiontype_', 'creation_status', 'id', 'name', 'description'],
                        static_methods=['special_objects', 'product_info']):

        static_methods_template = "\n" + \
"""
    def get_%(attr)s(self):
        entry_point = context.manager[self.id].get('entry_point')
        if entry_point:
            return entry_point.%(attr)s
        raise DisconnectedError"""

        dinamic_methods_template = "\n" + \
"""
    def get_%(attr)s(self):
        proxy = context.manager[self.id].get('proxy')
        if proxy:
            return proxy.request(method='GET',
                                 url='/api').%(attr)s
        raise DisconnectedError"""

        methods_template = "\n" + \
"""
    @property
    def id(self):
        return self.__id

    def __setattr__(self, name, value):
        if name in ['__id', 'id']:
            raise ImmutableError(name)
        else:
            super(API, self).__setattr__(name, value)

    def disconnect(self):
        ''' terminates server connection/s '''

        proxy = context.manager[self.id].get('proxy')
        persistent_auth = context.manager[self.id].get('persistent_auth')

        # If persistent authentication is enabled then we need to
        # send a last request as a hint to the server to close the
        # session:
        if proxy:
            if persistent_auth:
                try:
                    proxy.request(method='GET',
                                  url='/api',
                                  last=True)
                except Exception:
                    pass
        else:
            raise DisconnectedError

        # Clear context
        context.manager[self.id].clear(force=True)

    def test(self, throw_exception=False):
        ''' test server connectivity '''

        proxy = context.manager[self.id].get('proxy')
        if proxy:
            try :
                proxy.request(method='GET',
                              url='/api')
            except Exception, e:
                if throw_exception: raise e
                return False
            return True
        raise DisconnectedError

    def set_filter(self, filter):
        ''' enables user permission based filtering '''
        if type(filter) == types.BooleanType:
            context.manager[self.id].add('filter', filter)
        else:
            raise TypeError(filter)"""

        entry_point_resource = context.manager[api.id].get('proxy').request('GET', '/api')
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
    def entryPoint(api, types=[], rootCollections=''):
        api_template = EntryPoint.entryPointImports() + \
        EntryPoint.entryPointCustomImports(types) + \
"""class API(object):
    def __init__(self, url, username, password, key_file=None, cert_file=None,
                 ca_file=None, port=None, timeout=None, persistent_auth=True, 
                 insecure=False, filter=False, debug=False):

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
        [@param insecure: signals to not demand site trustworthiness for ssl enabled 
                connection (format True|False)]
        [@param filter: signals if user permission based filtering should be turned
                on/off (format True|False)]
        [@param debug: debug (format True|False)]

        @raise NoCertificatesError: raised when CA certificate is not provided for SSL
               site (can be disabled using 'insecure=True' argument).
        @raise UnsecuredConnectionAttemptError: raised when HTTP protocol is used in 
               url against server running HTTPS.
        @raise ImmutableError: raised on sdk < 3.2 when sdk initiation attempt occurred 
               while sdk instance already exist under the same domain.
        @raise DisconnectedError: raised when sdk usage attempt occurred after it was
               explicitly disconnected.
        @raise MissingParametersError: raised when get() method invoked without id or
               name been specified.
        @raise ConnectionError: raised when any kind of communication error occurred.
        @raise RequestError: raised when any kind of oVirt server error occurred.
        \"""

        # The instance id
        self.__id = id(self)

        # Create the connection pool:
        pool = ConnectionsPool(
            url=url,
            username=username,
            password=password,
            context=self.id,
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
        context.manager[self.id].add('filter', filter)

        # Get entry point
        entry_point = proxy.request(method='GET',
                                    url='/api')

        # If server returns no response for the root resource, this is sign
        # that used http protocol against SSL secured site
        if type(entry_point) == types.StringType and entry_point == '':
            raise UnsecuredConnectionAttemptError

        # Store entry point to the context
        context.manager[self.id].add('entry_point', entry_point, Mode.R)

        # Store proxy to the context:
        context.manager[self.id].add('proxy', proxy, Mode.R)

        # We need to remember if persistent auth is enabled:
        context.manager[self.id].add('persistent_auth',
                                     persistent_auth,
                                     Mode.R)

"""

        return (api_template + rootCollections + EntryPoint.instanceMethods(api))

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
