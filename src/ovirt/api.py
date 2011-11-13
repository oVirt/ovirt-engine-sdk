

########################################
############ GENERATED CODE ############
########################################

'''
Generated at: 2011-11-13 11:43:21.083445

@author: mpastern@redhat.com
'''

from ovirt.infrastructure import contextmanager
from ovirt.infrastructure.connectionspool import ConnectionsPool
from ovirt.infrastructure.proxy import Proxy
from ovirt.infrastructure.contextmanager import Mode
from ovirt.infrastructure.brokers import Capabilities
from ovirt.infrastructure.brokers import Clusters
from ovirt.infrastructure.brokers import DataCenters
from ovirt.infrastructure.brokers import Domains
from ovirt.infrastructure.brokers import Events
from ovirt.infrastructure.brokers import Groups
from ovirt.infrastructure.brokers import Hosts
from ovirt.infrastructure.brokers import Networks
from ovirt.infrastructure.brokers import Roles
from ovirt.infrastructure.brokers import StorageDomains
from ovirt.infrastructure.brokers import Tags
from ovirt.infrastructure.brokers import Templates
from ovirt.infrastructure.brokers import Users
from ovirt.infrastructure.brokers import VMs
from ovirt.infrastructure.brokers import VmPools


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
