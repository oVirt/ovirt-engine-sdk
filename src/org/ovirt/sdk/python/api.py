'''
Created on Oct 5, 2011

@author: mpastern
'''

from org.ovirt.sdk.python.infrastructure.connectionspool import ConnectionsPool
from org.ovirt.sdk.python.infrastructure.brokers import VMs
from org.ovirt.sdk.python.infrastructure.proxy import Proxy
from org.ovirt.sdk.python.infrastructure import contextmanager
from org.ovirt.sdk.python.infrastructure.contextmanager import Mode


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