

########################################
############ GENERATED CODE ############
########################################

'''
Generated at: 2011-11-23 16:14:52.640702

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

    def __init__(self, url, username, password, key_file=None, cert_file=None, port=None, strict=None, timeout=60):
        contextmanager.add('proxy',
                           Proxy(ConnectionsPool(url=url,
                                                 username=username,
                                                 password=password,
                                                 key_file=key_file,
                                                 cert_file=cert_file,
                                                 port=port,
                                                 strict=strict,
                                                 timeout=timeout)),
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
