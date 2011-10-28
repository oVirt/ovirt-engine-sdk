'''
Created on Oct 5, 2011

@author: mpastern
'''
from ovirt.infrastructure import contextmanager
from ovirt.infrastructure.connectionspool import ConnectionsPool
from ovirt.infrastructure.proxy import Proxy
from ovirt.infrastructure.contextmanager import Mode
from ovirt.infrastructure.brokers import VMs


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
        
############ GENERATED CODE FROM HERE############

        #TODO: add here generated root collections
        self.vms = VMs()