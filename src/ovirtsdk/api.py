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


########################################
############ GENERATED CODE ############
########################################

'''Generated at: 2012-09-20 10:34:54.692539'''

import types
from ovirtsdk.infrastructure.errors import UnsecuredConnectionAttemptError
from ovirtsdk.infrastructure import contextmanager
from ovirtsdk.infrastructure.connectionspool import ConnectionsPool
from ovirtsdk.infrastructure.proxy import Proxy
from ovirtsdk.infrastructure.contextmanager import Mode
from ovirtsdk.infrastructure.brokers import Capabilities
from ovirtsdk.infrastructure.brokers import Clusters
from ovirtsdk.infrastructure.brokers import DataCenters
from ovirtsdk.infrastructure.brokers import Disks
from ovirtsdk.infrastructure.brokers import Domains
from ovirtsdk.infrastructure.brokers import Events
from ovirtsdk.infrastructure.brokers import Groups
from ovirtsdk.infrastructure.brokers import Hosts
from ovirtsdk.infrastructure.brokers import Networks
from ovirtsdk.infrastructure.brokers import Roles
from ovirtsdk.infrastructure.brokers import StorageDomains
from ovirtsdk.infrastructure.brokers import Tags
from ovirtsdk.infrastructure.brokers import Templates
from ovirtsdk.infrastructure.brokers import Users
from ovirtsdk.infrastructure.brokers import VMs
from ovirtsdk.infrastructure.brokers import VmPools


class API():
    def __init__(self, url, username, password, key_file=None, cert_file=None, ca_file=None, port=None, timeout=None, persistent_auth=True, insecure=False, filter=False, debug=False):

        """
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
        """

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

        self.capabilities = Capabilities()
        self.clusters = Clusters()
        self.datacenters = DataCenters()
        self.disks = Disks()
        self.domains = Domains()
        self.events = Events()
        self.groups = Groups()
        self.hosts = Hosts()
        self.networks = Networks()
        self.roles = Roles()
        self.storagedomains = StorageDomains()
        self.tags = Tags()
        self.templates = Templates()
        self.users = Users()
        self.vms = VMs()
        self.vmpools = VmPools()


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


    def get_special_objects(self):
        entry_point = contextmanager.get('entry_point')
        if entry_point:
            return entry_point.special_objects
        return None


    def get_summary(self):
        proxy = contextmanager.get('proxy')
        filter_header = contextmanager.get('filter')

        return proxy.request(method='GET',
                             url='/api').summary


    def get_time(self):
        proxy = contextmanager.get('proxy')
        filter_header = contextmanager.get('filter')

        return proxy.request(method='GET',
                             url='/api').time


    def get_product_info(self):
        entry_point = contextmanager.get('entry_point')
        if entry_point:
            return entry_point.product_info
        return None
