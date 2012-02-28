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

'''
Generated at: 2012-02-28 13:08:28.528442

@author: mpastern@redhat.com
'''

from ovirtsdk.infrastructure import contextmanager
from ovirtsdk.infrastructure.connectionspool import ConnectionsPool
from ovirtsdk.infrastructure.proxy import Proxy
from ovirtsdk.infrastructure.contextmanager import Mode
from ovirtsdk.infrastructure.brokers import Capabilities
from ovirtsdk.infrastructure.brokers import Clusters
from ovirtsdk.infrastructure.brokers import DataCenters
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
    #TODO: - read .ini configuration

    def __init__(self, url, username, password, key_file=None, cert_file=None, port=None, timeout=None, debug=False):
        contextmanager.add('proxy',
                           Proxy(ConnectionsPool(url=url,
                                                 username=username,
                                                 password=password,
                                                 key_file=key_file,
                                                 cert_file=cert_file,
                                                 port=port,
                                                 strict=False,
                                                 timeout=timeout,
                                                 debug=debug)),
                           Mode.R)

        self.capabilities = Capabilities()
        self.clusters = Clusters()
        self.datacenters = DataCenters()
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
        contextmanager._remove('proxy', force=True)

    def test(self, throw_exception=False):
        ''' test server connectivity '''
        proxy = contextmanager.get('proxy')
        if proxy:
            try :
                proxy.request(method='GET', url='/api')
            except Exception, e:
                if throw_exception: raise e
                else: return False
            return True
        return False

    def get_product_info(self):
        if self.test():
            proxy = contextmanager.get('proxy')
            return proxy.request(method='GET', url='/api').product_info
