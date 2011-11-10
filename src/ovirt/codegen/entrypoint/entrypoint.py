'''
Created on Nov 8, 2011

@author: mpastern
'''
import datetime

class EntryPoint(object):
    
    @staticmethod
    def entryPointImports():
        entry_point_imports_template = \
        "\n\n########################################\n"+\
        "############ GENERATED CODE ############\n"+\
        "########################################\n\n"+\
        "'''\nGenerated at: "+ str(datetime.datetime.now())+"\n\n"+\
        "@author: mpastern@redhat.com\n'''\n\n" +\
        "from ovirt.infrastructure import contextmanager\n"+\
        "from ovirt.infrastructure.connectionspool import ConnectionsPool\n"+\
        "from ovirt.infrastructure.proxy import Proxy\n"+\
        "from ovirt.infrastructure.contextmanager import Mode\n"
        
        return entry_point_imports_template

    @staticmethod
    def entryPointCustomImports(types=[]):
        entry_point_custom_imports_template = "from ovirt.infrastructure.brokers import %s\n"
        
        imports = ''
        for item in types:
            imports += entry_point_custom_imports_template % item
            
        return imports + ('\n\n')

    @staticmethod
    def entryPoint(types=[], rootCollections=''):
        api_template = EntryPoint.entryPointImports()+\
        EntryPoint.entryPointCustomImports(types)+\
        "class API():\n"+\
        "    #TODO: - read .ini configuration\n\n"+\
        "    def __init__(self, url, username, password, key_file=None, cert_file=None, port=None, strict=None, timeout=60):\n"+\
        "        contextmanager.add('proxy',\n"+\
        "                           Proxy(ConnectionsPool(url=url,\n"+\
        "                                                 username=username,\n"+\
        "                                                 password=password,\n"+\
        "                                                 key_file=key_file,\n"+\
        "                                                 cert_file=cert_file,\n"+\
        "                                                 port=port,\n"+\
        "                                                 strict=strict,\n"+\
        "                                                 timeout=timeout)),\n"+\
        "                           Mode.R)\n\n"
        
        return (api_template + rootCollections)
    
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
        