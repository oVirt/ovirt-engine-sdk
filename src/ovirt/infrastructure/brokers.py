

########################################
############ GENERATED CODE ############
########################################

'''
Generated at: 2011-11-09 16:50:02.913103

@author: mpastern@redhat.com
'''

from ovirt.xml import params
from ovirt.utils.urlhelper import UrlHelper
from ovirt.utils.filterhelper import FilterHelper
from ovirt.utils.parsehelper import ParseHelper
from ovirt.utils.searchhelper import SearchHelper
from ovirt.infrastructure.common import Base


class Capabilities(Base):
    def __init__(self):
        """Constructor."""

    def get(self, name='*', **kwargs):
        url = '/api/capabilities'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_capabilities()
        return Capabilities(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/capabilities'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_capabilities()
        return ParseHelper.toCollection(Capabilities,
                                        FilterHelper.filter(result, kwargs))

class Cluster(params.Cluster, Base):
    def __init__(self, cluster):
        self.networks = []
        self.networks = ClusterNetworks(cluster)
        self.permissions = []
        self.permissions = ClusterPermissions(cluster)

        self.superclass = cluster

    def __new__(cls, cluster):
        if cluster is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/clusters/{cluster:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Cluster:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Cluster:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/clusters/{cluster:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{cluster:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Cluster(result)

class ClusterNetwork(params.Network, Base):
    def __init__(self, Cluster, network):
        self.parentclass = Cluster
        self.superclass  =  network

    def __new__(cls, Cluster, network):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(Cluster, network)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/clusters/{cluster:id}/networks/{network:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Cluster:id}' : self.parentclass.get_id(),
                                                                         '{Network:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Cluster:id}' : self.parentclass.get_id(),
                                                                         '{Network:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/clusters/{cluster:id}/networks/{network:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{Cluster:id}' : self.parentclass.get_id(),
                                                                     '{network:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return ClusterNetwork(self.parentclass, result)

class ClusterNetworks(Base):
 
    def __init__(self, Cluster):
        self.parentclass = Cluster

    def add(self, Network):

        url = '/api/clusters/{cluster:id}/networks'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{Cluster:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Network))

        return ClusterNetwork(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/clusters/{cluster:id}/networks'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Cluster:id}': self.parentclass.get_id()})).get_clusternetwork()

        return ClusterNetwork(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/clusters/{cluster:id}/networks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Cluster:id}': self.parentclass.get_id()})).get_clusternetwork()

        return ParseHelper.toSubCollection(ClusterNetwork,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class ClusterPermission(params.Permission, Base):
    def __init__(self, Cluster, permission):
        self.parentclass = Cluster
        self.superclass  =  permission

    def __new__(cls, Cluster, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(Cluster, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/clusters/{cluster:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Cluster:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Cluster:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class ClusterPermissions(Base):
 
    def __init__(self, Cluster):
        self.parentclass = Cluster

    def add(self, Permission):

        url = '/api/clusters/{cluster:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{Cluster:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Permission))

        return ClusterPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/clusters/{cluster:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Cluster:id}': self.parentclass.get_id()})).get_clusterpermission()

        return ClusterPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/clusters/{cluster:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Cluster:id}': self.parentclass.get_id()})).get_clusterpermission()

        return ParseHelper.toSubCollection(ClusterPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Clusters(Base):
    def __init__(self):
        """Constructor."""

    def add(self, Cluster):
        url = '/api/clusters'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(Cluster))
        return Cluster(result)

    def get(self, name='*', **kwargs):
        url = '/api/clusters'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_cluster()
        return Cluster(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/clusters'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_cluster()
        return ParseHelper.toCollection(Cluster,
                                        FilterHelper.filter(result, kwargs))

class DataCenter(params.DataCenter, Base):
    def __init__(self, datacenter):
        self.storagedomains = []
        self.storagedomains = DataCenterStorageDomains(datacenter)
        self.permissions = []
        self.permissions = DataCenterPermissions(datacenter)

        self.superclass = datacenter

    def __new__(cls, datacenter):
        if datacenter is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/datacenters/{datacenter:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{DataCenter:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{DataCenter:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/datacenters/{datacenter:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{datacenter:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return DataCenter(result)

class DataCenterPermission(params.Permission, Base):
    def __init__(self, DataCenter, permission):
        self.parentclass = DataCenter
        self.superclass  =  permission

    def __new__(cls, DataCenter, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(DataCenter, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/datacenters/{datacenter:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{DataCenter:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{DataCenter:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class DataCenterPermissions(Base):
 
    def __init__(self, DataCenter):
        self.parentclass = DataCenter

    def add(self, Permission):

        url = '/api/datacenters/{datacenter:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{DataCenter:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Permission))

        return DataCenterPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/datacenters/{datacenter:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{DataCenter:id}': self.parentclass.get_id()})).get_datacenterpermission()

        return DataCenterPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/datacenters/{datacenter:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{DataCenter:id}': self.parentclass.get_id()})).get_datacenterpermission()

        return ParseHelper.toSubCollection(DataCenterPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DataCenterStorageDomain(params.StorageDomain, Base):
    def __init__(self, DataCenter, storagedomain):
        self.parentclass = DataCenter
        self.superclass  =  storagedomain

    def __new__(cls, DataCenter, storagedomain):
        if storagedomain is None: return None
        obj = object.__new__(cls)
        obj.__init__(DataCenter, storagedomain)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{DataCenter:id}' : self.parentclass.get_id(),
                                                                         '{StorageDomain:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{DataCenter:id}' : self.parentclass.get_id(),
                                                                         '{StorageDomain:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def activate(self):
        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/activate'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{DataCenter:id}' : self.parentclass.get_id(),
                                                                     '{StorageDomain:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

    def deactivate(self):
        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/deactivate'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{DataCenter:id}' : self.parentclass.get_id(),
                                                                     '{StorageDomain:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class DataCenterStorageDomains(Base):
 
    def __init__(self, DataCenter):
        self.parentclass = DataCenter

    def add(self, StorageDomain):

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{DataCenter:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(StorageDomain))

        return DataCenterStorageDomain(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{DataCenter:id}': self.parentclass.get_id()})).get_datacenterstoragedomain()

        return DataCenterStorageDomain(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{DataCenter:id}': self.parentclass.get_id()})).get_datacenterstoragedomain()

        return ParseHelper.toSubCollection(DataCenterStorageDomain,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DataCenters(Base):
    def __init__(self):
        """Constructor."""

    def add(self, DataCenter):
        url = '/api/datacenters'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(DataCenter))
        return DataCenter(result)

    def get(self, name='*', **kwargs):
        url = '/api/datacenters'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_data_center()
        return DataCenter(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/datacenters'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_data_center()
        return ParseHelper.toCollection(DataCenter,
                                        FilterHelper.filter(result, kwargs))

class Domain(params.Domain, Base):
    def __init__(self, domain):
        self.users = []
        self.users = DomainUsers(domain)
        self.groups = []
        self.groups = DomainGroups(domain)

        self.superclass = domain

    def __new__(cls, domain):
        if domain is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain)
        return obj

class DomainGroup(params.Group, Base):
    def __init__(self, Domain, group):
        self.parentclass = Domain
        self.superclass  =  group

    def __new__(cls, Domain, group):
        if group is None: return None
        obj = object.__new__(cls)
        obj.__init__(Domain, group)
        return obj

class DomainGroups(Base):
 
    def __init__(self, Domain):
        self.parentclass = Domain

    def get(self, name='None', **kwargs):

        url = '/api/domains/{domain:id}/groups'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Domain:id}': self.parentclass.get_id()})).get_domaingroup()

        return DomainGroup(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/domains/{domain:id}/groups'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Domain:id}': self.parentclass.get_id()})).get_domaingroup()

        return ParseHelper.toSubCollection(DomainGroup,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DomainUser(params.User, Base):
    def __init__(self, Domain, user):
        self.parentclass = Domain
        self.superclass  =  user

    def __new__(cls, Domain, user):
        if user is None: return None
        obj = object.__new__(cls)
        obj.__init__(Domain, user)
        return obj

class DomainUsers(Base):
 
    def __init__(self, Domain):
        self.parentclass = Domain

    def get(self, name='None', **kwargs):

        url = '/api/domains/{domain:id}/users'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Domain:id}': self.parentclass.get_id()})).get_domainuser()

        return DomainUser(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/domains/{domain:id}/users'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Domain:id}': self.parentclass.get_id()})).get_domainuser()

        return ParseHelper.toSubCollection(DomainUser,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Domains(Base):
    def __init__(self):
        """Constructor."""

    def get(self, name='*', **kwargs):
        url = '/api/domains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_domain()
        return Domain(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/domains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_domain()
        return ParseHelper.toCollection(Domain,
                                        FilterHelper.filter(result, kwargs))

class Event(params.Event, Base):
    def __init__(self, event):
        #SUB_COLLECTIONS
        self.superclass = event

    def __new__(cls, event):
        if event is None: return None
        obj = object.__new__(cls)
        obj.__init__(event)
        return obj

class Events(Base):
    def __init__(self):
        """Constructor."""

    def get(self, name='*', **kwargs):
        url = '/api/events'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_event()
        return Event(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/events'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_event()
        return ParseHelper.toCollection(Event,
                                        FilterHelper.filter(result, kwargs))

class Group(params.Group, Base):
    def __init__(self, group):
        self.permissions = []
        self.permissions = GroupPermissions(group)
        self.roles = []
        self.roles = GroupRoles(group)
        self.tags = []
        self.tags = GroupTags(group)

        self.superclass = group

    def __new__(cls, group):
        if group is None: return None
        obj = object.__new__(cls)
        obj.__init__(group)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/groups/{group:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Group:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Group:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class GroupPermission(params.Permission, Base):
    def __init__(self, Group, permission):
        self.parentclass = Group
        self.superclass  =  permission

    def __new__(cls, Group, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(Group, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/groups/{group:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Group:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Group:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class GroupPermissions(Base):
 
    def __init__(self, Group):
        self.parentclass = Group

    def add(self, Permission):

        url = '/api/groups/{group:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{Group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Permission))

        return GroupPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/groups/{group:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Group:id}': self.parentclass.get_id()})).get_grouppermission()

        return GroupPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/groups/{group:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Group:id}': self.parentclass.get_id()})).get_grouppermission()

        return ParseHelper.toSubCollection(GroupPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupRole(params.Role, Base):
    def __init__(self, Group, role):
        self.parentclass = Group
        self.superclass  =  role

    def __new__(cls, Group, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(Group, role)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/groups/{group:id}/roles/{role:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Group:id}' : self.parentclass.get_id(),
                                                                         '{Role:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Group:id}' : self.parentclass.get_id(),
                                                                         '{Role:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class GroupRoles(Base):
 
    def __init__(self, Group):
        self.parentclass = Group

    def add(self, Role):

        url = '/api/groups/{group:id}/roles'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{Group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Role))

        return GroupRole(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/groups/{group:id}/roles'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Group:id}': self.parentclass.get_id()})).get_grouprole()

        return GroupRole(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/groups/{group:id}/roles'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Group:id}': self.parentclass.get_id()})).get_grouprole()

        return ParseHelper.toSubCollection(GroupRole,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupTag(params.Tag, Base):
    def __init__(self, Group, tag):
        self.parentclass = Group
        self.superclass  =  tag

    def __new__(cls, Group, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(Group, tag)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/groups/{group:id}/tags/{tag:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Group:id}' : self.parentclass.get_id(),
                                                                         '{Tag:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Group:id}' : self.parentclass.get_id(),
                                                                         '{Tag:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class GroupTags(Base):
 
    def __init__(self, Group):
        self.parentclass = Group

    def add(self, Tag):

        url = '/api/groups/{group:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{Group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Tag))

        return GroupTag(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/groups/{group:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Group:id}': self.parentclass.get_id()})).get_grouptag()

        return GroupTag(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/groups/{group:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Group:id}': self.parentclass.get_id()})).get_grouptag()

        return ParseHelper.toSubCollection(GroupTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Groups(Base):
    def __init__(self):
        """Constructor."""

    def add(self, Group):
        url = '/api/groups'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(Group))
        return Group(result)

    def get(self, name='*', **kwargs):
        url = '/api/groups'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_group()
        return Group(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/groups'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_group()
        return ParseHelper.toCollection(Group,
                                        FilterHelper.filter(result, kwargs))

class GroupsRolePermit(params.Permit, Base):
    def __init__(self, GroupsRole, permit):
        self.parentclass = GroupsRole
        self.superclass  =  permit

    def __new__(cls, GroupsRole, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(GroupsRole, permit)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/groups/{group:id}/roles/{role:id}/permits/{permit:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{GroupsRole:id}' : self.parentclass.get_id(),
                                                                         '{Permit:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{GroupsRole:id}' : self.parentclass.get_id(),
                                                                         '{Permit:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class Host(params.Host, Base):
    def __init__(self, host):
        self.nics = []
        self.nics = HostNics(host)
        self.permissions = []
        self.permissions = HostPermissions(host)
        self.statistics = []
        self.statistics = HostStatistics(host)
        self.tags = []
        self.tags = HostTags(host)

        self.superclass = host

    def __new__(cls, host):
        if host is None: return None
        obj = object.__new__(cls)
        obj.__init__(host)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/hosts/{host:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def install(self):
        url = '/api/hosts/{host:id}/install'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def fence(self):
        url = '/api/hosts/{host:id}/fence'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def activate(self):
        url = '/api/hosts/{host:id}/activate'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def deactivate(self):
        url = '/api/hosts/{host:id}/deactivate'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def approve(self):
        url = '/api/hosts/{host:id}/approve'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def iscsilogin(self):
        url = '/api/hosts/{host:id}/iscsilogin'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def iscsidiscover(self):
        url = '/api/hosts/{host:id}/iscsidiscover'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def commitnetconfig(self):
        url = '/api/hosts/{host:id}/commitnetconfig'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def Storage(self):
        url = '/api/hosts/{host:id}/storage'

        action = params.Action()
        result = self._getProxy().request(method='GET',
                                          url=UrlHelper.replace(url, {'{Host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def update(self):
        url = '/api/hosts/{host:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Host(result)

class HostNIC(params.HostNIC, Base):
    def __init__(self, Host, nic):
        self.parentclass = Host
        self.superclass  =  nic

    def __new__(cls, Host, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(Host, nic)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/hosts/{host:id}/nics/{nic:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Host:id}' : self.parentclass.get_id(),
                                                                         '{Nic:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Host:id}' : self.parentclass.get_id(),
                                                                         '{Nic:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def detach(self):
        url = '/api/hosts/{host:id}/nics/{nic:id}/detach'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Host:id}' : self.parentclass.get_id(),
                                                                     '{Nic:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

    def attach(self):
        url = '/api/hosts/{host:id}/nics/{nic:id}/attach'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Host:id}' : self.parentclass.get_id(),
                                                                     '{Nic:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

    def update(self):
        url = '/api/hosts/{host:id}/nics/{nic:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{Host:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return HostNIC(self.parentclass, result)

class HostNics(Base):
 
    def __init__(self, Host):
        self.parentclass = Host

    def add(self, Nic):

        url = '/api/hosts/{host:id}/nics'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Nic))

        return HostNIC(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/hosts/{host:id}/nics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()})).get_host_nic()

        return HostNIC(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/nics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()})).get_host_nic()

        return ParseHelper.toSubCollection(HostNIC,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostPermission(params.Permission, Base):
    def __init__(self, Host, permission):
        self.parentclass = Host
        self.superclass  =  permission

    def __new__(cls, Host, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(Host, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/hosts/{host:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Host:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Host:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class HostPermissions(Base):
 
    def __init__(self, Host):
        self.parentclass = Host

    def add(self, Permission):

        url = '/api/hosts/{host:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Permission))

        return HostPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/hosts/{host:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()})).get_hostpermission()

        return HostPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()})).get_hostpermission()

        return ParseHelper.toSubCollection(HostPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostStatistic(params.Statistic, Base):
    def __init__(self, Host, statistic):
        self.parentclass = Host
        self.superclass  =  statistic

    def __new__(cls, Host, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(Host, statistic)
        return obj

class HostStatistics(Base):
 
    def __init__(self, Host):
        self.parentclass = Host

    def get(self, name='None', **kwargs):

        url = '/api/hosts/{host:id}/statistics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()})).get_hoststatistic()

        return HostStatistic(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/statistics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()})).get_hoststatistic()

        return ParseHelper.toSubCollection(HostStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostStorage(params.HostStorage, Base):
    def __init__(self, Host, storage):
        self.parentclass = Host
        self.superclass  =  storage

    def __new__(cls, Host, storage):
        if storage is None: return None
        obj = object.__new__(cls)
        obj.__init__(Host, storage)
        return obj

class HostTag(params.Tag, Base):
    def __init__(self, Host, tag):
        self.parentclass = Host
        self.superclass  =  tag

    def __new__(cls, Host, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(Host, tag)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/hosts/{host:id}/tags/{tag:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Host:id}' : self.parentclass.get_id(),
                                                                         '{Tag:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Host:id}' : self.parentclass.get_id(),
                                                                         '{Tag:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class HostTags(Base):
 
    def __init__(self, Host):
        self.parentclass = Host

    def add(self, Tag):

        url = '/api/hosts/{host:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Tag))

        return HostTag(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/hosts/{host:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()})).get_hosttag()

        return HostTag(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Host:id}': self.parentclass.get_id()})).get_hosttag()

        return ParseHelper.toSubCollection(HostTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Hosts(Base):
    def __init__(self):
        """Constructor."""

    def add(self, Host):
        url = '/api/hosts'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(Host))
        return Host(result)

    def get(self, name='*', **kwargs):
        url = '/api/hosts'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_host()
        return Host(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/hosts'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_host()
        return ParseHelper.toCollection(Host,
                                        FilterHelper.filter(result, kwargs))

class HostsNicStatistic(params.Statistic, Base):
    def __init__(self, HostsNic, statistic):
        self.parentclass = HostsNic
        self.superclass  =  statistic

    def __new__(cls, HostsNic, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(HostsNic, statistic)
        return obj

class Network(params.Network, Base):
    def __init__(self, network):
        #SUB_COLLECTIONS
        self.superclass = network

    def __new__(cls, network):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(network)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/networks/{network:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Network:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Network:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/networks/{network:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{network:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Network(result)

class Networks(Base):
    def __init__(self):
        """Constructor."""

    def add(self, Network):
        url = '/api/networks'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(Network))
        return Network(result)

    def get(self, name='*', **kwargs):
        url = '/api/networks'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_network()
        return Network(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/networks'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_network()
        return ParseHelper.toCollection(Network,
                                        FilterHelper.filter(result, kwargs))

class Role(params.Role, Base):
    def __init__(self, role):
        self.permits = []
        self.permits = RolePermits(role)

        self.superclass = role

    def __new__(cls, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(role)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/roles/{role:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Role:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Role:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class RolePermit(params.Permit, Base):
    def __init__(self, Role, permit):
        self.parentclass = Role
        self.superclass  =  permit

    def __new__(cls, Role, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(Role, permit)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/roles/{role:id}/permits/{permit:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Role:id}' : self.parentclass.get_id(),
                                                                         '{Permit:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Role:id}' : self.parentclass.get_id(),
                                                                         '{Permit:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class RolePermits(Base):
 
    def __init__(self, Role):
        self.parentclass = Role

    def add(self, Permit):

        url = '/api/roles/{role:id}/permits'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{Role:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Permit))

        return RolePermit(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/roles/{role:id}/permits'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Role:id}': self.parentclass.get_id()})).get_rolepermit()

        return RolePermit(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/roles/{role:id}/permits'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Role:id}': self.parentclass.get_id()})).get_rolepermit()

        return ParseHelper.toSubCollection(RolePermit,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Roles(Base):
    def __init__(self):
        """Constructor."""

    def add(self, Role):
        url = '/api/roles'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(Role))
        return Role(result)

    def get(self, name='*', **kwargs):
        url = '/api/roles'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_role()
        return Role(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/roles'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_role()
        return ParseHelper.toCollection(Role,
                                        FilterHelper.filter(result, kwargs))

class StorageDomain(params.StorageDomain, Base):
    def __init__(self, storagedomain):
        self.files = []
        self.files = StorageDomainFiles(storagedomain)
        self.templates = []
        self.templates = StorageDomainTemplates(storagedomain)
        self.vms = []
        self.vms = StorageDomainVMs(storagedomain)
        self.permissions = []
        self.permissions = StorageDomainPermissions(storagedomain)

        self.superclass = storagedomain

    def __new__(cls, storagedomain):
        if storagedomain is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/storagedomains/{storagedomain:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/storagedomains/{storagedomain:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{storagedomain:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return StorageDomain(result)

class StorageDomainFile(params.File, Base):
    def __init__(self, StorageDomain, file):
        self.parentclass = StorageDomain
        self.superclass  =  file

    def __new__(cls, StorageDomain, file):
        if file is None: return None
        obj = object.__new__(cls)
        obj.__init__(StorageDomain, file)
        return obj

class StorageDomainFiles(Base):
 
    def __init__(self, StorageDomain):
        self.parentclass = StorageDomain

    def get(self, name='None', **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/files'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.parentclass.get_id()})).get_storagedomainfile()

        return StorageDomainFile(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/files'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.parentclass.get_id()})).get_storagedomainfile()

        return ParseHelper.toSubCollection(StorageDomainFile,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomainPermission(params.Permission, Base):
    def __init__(self, StorageDomain, permission):
        self.parentclass = StorageDomain
        self.superclass  =  permission

    def __new__(cls, StorageDomain, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(StorageDomain, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/storagedomains/{storagedomain:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{StorageDomain:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{StorageDomain:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class StorageDomainPermissions(Base):
 
    def __init__(self, StorageDomain):
        self.parentclass = StorageDomain

    def add(self, Permission):

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Permission))

        return StorageDomainPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.parentclass.get_id()})).get_storagedomainpermission()

        return StorageDomainPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.parentclass.get_id()})).get_storagedomainpermission()

        return ParseHelper.toSubCollection(StorageDomainPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomainTemplate(params.Template, Base):
    def __init__(self, StorageDomain, template):
        self.parentclass = StorageDomain
        self.superclass  =  template

    def __new__(cls, StorageDomain, template):
        if template is None: return None
        obj = object.__new__(cls)
        obj.__init__(StorageDomain, template)
        return obj

    def import_StorageDomain(self):
        url = '/api/storagedomains/{storagedomain:id}/templates/{template:id}/import'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{StorageDomain:id}' : self.parentclass.get_id(),
                                                                     '{Template:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class StorageDomainTemplates(Base):
 
    def __init__(self, StorageDomain):
        self.parentclass = StorageDomain

    def get(self, name='None', **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/templates'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.parentclass.get_id()})).get_storagedomaintemplate()

        return StorageDomainTemplate(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/templates'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.parentclass.get_id()})).get_storagedomaintemplate()

        return ParseHelper.toSubCollection(StorageDomainTemplate,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomainVM(params.VM, Base):
    def __init__(self, StorageDomain, vm):
        self.parentclass = StorageDomain
        self.superclass  =  vm

    def __new__(cls, StorageDomain, vm):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(StorageDomain, vm)
        return obj

    def import_StorageDomain(self):
        url = '/api/storagedomains/{storagedomain:id}/vms/{vm:id}/import'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{StorageDomain:id}' : self.parentclass.get_id(),
                                                                     '{VM:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class StorageDomainVMs(Base):
 
    def __init__(self, StorageDomain):
        self.parentclass = StorageDomain

    def get(self, name='None', **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/vms'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.parentclass.get_id()})).get_storagedomainvm()

        return StorageDomainVM(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/vms'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{StorageDomain:id}': self.parentclass.get_id()})).get_storagedomainvm()

        return ParseHelper.toSubCollection(StorageDomainVM,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomains(Base):
    def __init__(self):
        """Constructor."""

    def add(self, StorageDomain):
        url = '/api/storagedomains'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(StorageDomain))
        return StorageDomain(result)

    def get(self, name='*', **kwargs):
        url = '/api/storagedomains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_storage_domain()
        return StorageDomain(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/storagedomains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_storage_domain()
        return ParseHelper.toCollection(StorageDomain,
                                        FilterHelper.filter(result, kwargs))

class Tag(params.Tag, Base):
    def __init__(self, tag):
        #SUB_COLLECTIONS
        self.superclass = tag

    def __new__(cls, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(tag)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/tags/{tag:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Tag:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Tag:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/tags/{tag:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{tag:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Tag(result)

class Tags(Base):
    def __init__(self):
        """Constructor."""

    def add(self, Tag):
        url = '/api/tags'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(Tag))
        return Tag(result)

    def get(self, name='*', **kwargs):
        url = '/api/tags'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_tag()
        return Tag(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/tags'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_tag()
        return ParseHelper.toCollection(Tag,
                                        FilterHelper.filter(result, kwargs))

class Template(params.Template, Base):
    def __init__(self, template):
        self.nics = []
        self.nics = TemplateNics(template)
        self.cdroms = []
        self.cdroms = TemplateCdRoms(template)
        self.disks = []
        self.disks = TemplateDisks(template)
        self.permissions = []
        self.permissions = TemplatePermissions(template)

        self.superclass = template

    def __new__(cls, template):
        if template is None: return None
        obj = object.__new__(cls)
        obj.__init__(template)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/templates/{template:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Template:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Template:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def export(self):
        url = '/api/templates/{template:id}/export'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{Template:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def update(self):
        url = '/api/templates/{template:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{template:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Template(result)

class TemplateCdRom(params.CdRom, Base):
    def __init__(self, Template, cdrom):
        self.parentclass = Template
        self.superclass  =  cdrom

    def __new__(cls, Template, cdrom):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(Template, cdrom)
        return obj

class TemplateCdRoms(Base):
 
    def __init__(self, Template):
        self.parentclass = Template

    def get(self, name='None', **kwargs):

        url = '/api/templates/{template:id}/cdroms'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Template:id}': self.parentclass.get_id()})).get_templatecdrom()

        return TemplateCdRom(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/cdroms'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Template:id}': self.parentclass.get_id()})).get_templatecdrom()

        return ParseHelper.toSubCollection(TemplateCdRom,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplateDisk(params.Disk, Base):
    def __init__(self, Template, disk):
        self.parentclass = Template
        self.superclass  =  disk

    def __new__(cls, Template, disk):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(Template, disk)
        return obj

class TemplateDisks(Base):
 
    def __init__(self, Template):
        self.parentclass = Template

    def get(self, name='None', **kwargs):

        url = '/api/templates/{template:id}/disks'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Template:id}': self.parentclass.get_id()})).get_templatedisk()

        return TemplateDisk(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/disks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Template:id}': self.parentclass.get_id()})).get_templatedisk()

        return ParseHelper.toSubCollection(TemplateDisk,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplateNic(params.NIC, Base):
    def __init__(self, Template, nic):
        self.parentclass = Template
        self.superclass  =  nic

    def __new__(cls, Template, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(Template, nic)
        return obj

class TemplateNics(Base):
 
    def __init__(self, Template):
        self.parentclass = Template

    def get(self, name='None', **kwargs):

        url = '/api/templates/{template:id}/nics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Template:id}': self.parentclass.get_id()})).get_templatenic()

        return TemplateNic(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/nics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Template:id}': self.parentclass.get_id()})).get_templatenic()

        return ParseHelper.toSubCollection(TemplateNic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplatePermission(params.Permission, Base):
    def __init__(self, Template, permission):
        self.parentclass = Template
        self.superclass  =  permission

    def __new__(cls, Template, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(Template, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/templates/{template:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Template:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{Template:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class TemplatePermissions(Base):
 
    def __init__(self, Template):
        self.parentclass = Template

    def add(self, Permission):

        url = '/api/templates/{template:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{Template:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Permission))

        return TemplatePermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/templates/{template:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Template:id}': self.parentclass.get_id()})).get_templatepermission()

        return TemplatePermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{Template:id}': self.parentclass.get_id()})).get_templatepermission()

        return ParseHelper.toSubCollection(TemplatePermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Templates(Base):
    def __init__(self):
        """Constructor."""

    def add(self, Template):
        url = '/api/templates'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(Template))
        return Template(result)

    def get(self, name='*', **kwargs):
        url = '/api/templates'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_template()
        return Template(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/templates'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_template()
        return ParseHelper.toCollection(Template,
                                        FilterHelper.filter(result, kwargs))

class User(params.User, Base):
    def __init__(self, user):
        self.permissions = []
        self.permissions = UserPermissions(user)
        self.roles = []
        self.roles = UserRoles(user)
        self.tags = []
        self.tags = UserTags(user)

        self.superclass = user

    def __new__(cls, user):
        if user is None: return None
        obj = object.__new__(cls)
        obj.__init__(user)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/users/{user:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{User:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{User:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class UserPermission(params.Permission, Base):
    def __init__(self, User, permission):
        self.parentclass = User
        self.superclass  =  permission

    def __new__(cls, User, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(User, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/users/{user:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{User:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{User:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class UserPermissions(Base):
 
    def __init__(self, User):
        self.parentclass = User

    def add(self, Permission):

        url = '/api/users/{user:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{User:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Permission))

        return UserPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/users/{user:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{User:id}': self.parentclass.get_id()})).get_userpermission()

        return UserPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/users/{user:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{User:id}': self.parentclass.get_id()})).get_userpermission()

        return ParseHelper.toSubCollection(UserPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UserRole(params.Role, Base):
    def __init__(self, User, role):
        self.parentclass = User
        self.superclass  =  role

    def __new__(cls, User, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(User, role)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/users/{user:id}/roles/{role:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{User:id}' : self.parentclass.get_id(),
                                                                         '{Role:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{User:id}' : self.parentclass.get_id(),
                                                                         '{Role:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class UserRoles(Base):
 
    def __init__(self, User):
        self.parentclass = User

    def add(self, Role):

        url = '/api/users/{user:id}/roles'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{User:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Role))

        return UserRole(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/users/{user:id}/roles'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{User:id}': self.parentclass.get_id()})).get_userrole()

        return UserRole(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/users/{user:id}/roles'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{User:id}': self.parentclass.get_id()})).get_userrole()

        return ParseHelper.toSubCollection(UserRole,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UserTag(params.Tag, Base):
    def __init__(self, User, tag):
        self.parentclass = User
        self.superclass  =  tag

    def __new__(cls, User, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(User, tag)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/users/{user:id}/tags/{tag:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{User:id}' : self.parentclass.get_id(),
                                                                         '{Tag:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{User:id}' : self.parentclass.get_id(),
                                                                         '{Tag:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class UserTags(Base):
 
    def __init__(self, User):
        self.parentclass = User

    def add(self, Tag):

        url = '/api/users/{user:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{User:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Tag))

        return UserTag(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/users/{user:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{User:id}': self.parentclass.get_id()})).get_usertag()

        return UserTag(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/users/{user:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{User:id}': self.parentclass.get_id()})).get_usertag()

        return ParseHelper.toSubCollection(UserTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Users(Base):
    def __init__(self):
        """Constructor."""

    def add(self, User):
        url = '/api/users'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(User))
        return User(result)

    def get(self, name='*', **kwargs):
        url = '/api/users'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_user()
        return User(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/users'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_user()
        return ParseHelper.toCollection(User,
                                        FilterHelper.filter(result, kwargs))

class UsersRolePermit(params.Permit, Base):
    def __init__(self, UsersRole, permit):
        self.parentclass = UsersRole
        self.superclass  =  permit

    def __new__(cls, UsersRole, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(UsersRole, permit)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/users/{user:id}/roles/{role:id}/permits/{permit:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{UsersRole:id}' : self.parentclass.get_id(),
                                                                         '{Permit:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{UsersRole:id}' : self.parentclass.get_id(),
                                                                         '{Permit:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class VM(params.VM, Base):
    def __init__(self, vm):
        self.cdroms = []
        self.cdroms = VMCdRoms(vm)
        self.statistics = []
        self.statistics = VMStatistics(vm)
        self.tags = []
        self.tags = VMTags(vm)
        self.nics = []
        self.nics = VMNics(vm)
        self.disks = []
        self.disks = VMDisks(vm)
        self.snapshots = []
        self.snapshots = VMSnapshots(vm)
        self.permissions = []
        self.permissions = VMPermissions(vm)

        self.superclass = vm

    def __new__(cls, vm):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def shutdown(self):
        url = '/api/vms/{vm:id}/shutdown'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def start(self):
        url = '/api/vms/{vm:id}/start'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def stop(self):
        url = '/api/vms/{vm:id}/stop'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def suspend(self):
        url = '/api/vms/{vm:id}/suspend'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def detach(self):
        url = '/api/vms/{vm:id}/detach'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def export(self):
        url = '/api/vms/{vm:id}/export'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def move(self):
        url = '/api/vms/{vm:id}/move'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def Ticket(self):
        url = '/api/vms/{vm:id}/ticket'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def migrate(self):
        url = '/api/vms/{vm:id}/migrate'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{VM:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def update(self):
        url = '/api/vms/{vm:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return VM(result)

class VMCdRom(params.CdRom, Base):
    def __init__(self, VM, cdrom):
        self.parentclass = VM
        self.superclass  =  cdrom

    def __new__(cls, VM, cdrom):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(VM, cdrom)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/cdroms/{cdrom:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{CdRom:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{CdRom:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/vms/{vm:id}/cdroms/{cdrom:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                     '{cdrom:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return VMCdRom(self.parentclass, result)

class VMCdRoms(Base):
 
    def __init__(self, VM):
        self.parentclass = VM

    def add(self, CdRom):

        url = '/api/vms/{vm:id}/cdroms'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(CdRom))

        return VMCdRom(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/cdroms'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmcdrom()

        return VMCdRom(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/cdroms'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmcdrom()

        return ParseHelper.toSubCollection(VMCdRom,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMDisk(params.Disk, Base):
    def __init__(self, VM, disk):
        self.parentclass = VM
        self.superclass  =  disk

    def __new__(cls, VM, disk):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(VM, disk)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/disks/{disk:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{Disk:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{Disk:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/vms/{vm:id}/disks/{disk:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                     '{disk:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return VMDisk(self.parentclass, result)

class VMDisks(Base):
 
    def __init__(self, VM):
        self.parentclass = VM

    def add(self, Disk):

        url = '/api/vms/{vm:id}/disks'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Disk))

        return VMDisk(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/disks'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmdisk()

        return VMDisk(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/disks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmdisk()

        return ParseHelper.toSubCollection(VMDisk,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMNic(params.NIC, Base):
    def __init__(self, VM, nic):
        self.parentclass = VM
        self.superclass  =  nic

    def __new__(cls, VM, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(VM, nic)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/nics/{nic:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{Nic:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{Nic:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/vms/{vm:id}/nics/{nic:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return VMNic(self.parentclass, result)

class VMNics(Base):
 
    def __init__(self, VM):
        self.parentclass = VM

    def add(self, Nic):

        url = '/api/vms/{vm:id}/nics'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Nic))

        return VMNic(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/nics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmnic()

        return VMNic(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/nics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmnic()

        return ParseHelper.toSubCollection(VMNic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMPermission(params.Permission, Base):
    def __init__(self, VM, permission):
        self.parentclass = VM
        self.superclass  =  permission

    def __new__(cls, VM, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(VM, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class VMPermissions(Base):
 
    def __init__(self, VM):
        self.parentclass = VM

    def add(self, Permission):

        url = '/api/vms/{vm:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Permission))

        return VMPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmpermission()

        return VMPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmpermission()

        return ParseHelper.toSubCollection(VMPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMSnapshot(params.Snapshot, Base):
    def __init__(self, VM, snapshot):
        self.parentclass = VM
        self.superclass  =  snapshot

    def __new__(cls, VM, snapshot):
        if snapshot is None: return None
        obj = object.__new__(cls)
        obj.__init__(VM, snapshot)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{Snapshot:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{Snapshot:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def restore(self):
        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}/restore'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                     '{Snapshot:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class VMSnapshots(Base):
 
    def __init__(self, VM):
        self.parentclass = VM

    def add(self, Snapshot):

        url = '/api/vms/{vm:id}/snapshots'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Snapshot))

        return VMSnapshot(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/snapshots'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmsnapshot()

        return VMSnapshot(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/snapshots'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmsnapshot()

        return ParseHelper.toSubCollection(VMSnapshot,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMStatistic(params.Statistic, Base):
    def __init__(self, VM, statistic):
        self.parentclass = VM
        self.superclass  =  statistic

    def __new__(cls, VM, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(VM, statistic)
        return obj

class VMStatistics(Base):
 
    def __init__(self, VM):
        self.parentclass = VM

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/statistics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmstatistic()

        return VMStatistic(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/statistics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmstatistic()

        return ParseHelper.toSubCollection(VMStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMTag(params.Tag, Base):
    def __init__(self, VM, tag):
        self.parentclass = VM
        self.superclass  =  tag

    def __new__(cls, VM, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(VM, tag)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/tags/{tag:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{Tag:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VM:id}' : self.parentclass.get_id(),
                                                                         '{Tag:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class VMTags(Base):
 
    def __init__(self, VM):
        self.parentclass = VM

    def add(self, Tag):

        url = '/api/vms/{vm:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Tag))

        return VMTag(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmtag()

        return VMTag(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VM:id}': self.parentclass.get_id()})).get_vmtag()

        return ParseHelper.toSubCollection(VMTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMs(Base):
    def __init__(self):
        """Constructor."""

    def add(self, VM):
        url = '/api/vms'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(VM))
        return VM(result)

    def get(self, name='*', **kwargs):
        url = '/api/vms'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_vm()
        return VM(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/vms'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_vm()
        return ParseHelper.toCollection(VM,
                                        FilterHelper.filter(result, kwargs))

class VmPool(params.VmPool, Base):
    def __init__(self, vmpool):
        self.permissions = []
        self.permissions = VmPoolPermissions(vmpool)

        self.superclass = vmpool

    def __new__(cls, vmpool):
        if vmpool is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmpool)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vmpools/{vmpool:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VmPool:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VmPool:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/vmpools/{vmpool:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vmpool:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return VmPool(result)

class VmPoolPermission(params.Permission, Base):
    def __init__(self, VmPool, permission):
        self.parentclass = VmPool
        self.superclass  =  permission

    def __new__(cls, VmPool, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(VmPool, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vmpools/{vmpool:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VmPool:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{VmPool:id}' : self.parentclass.get_id(),
                                                                         '{Permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class VmPoolPermissions(Base):
 
    def __init__(self, VmPool):
        self.parentclass = VmPool

    def add(self, Permission):

        url = '/api/vmpools/{vmpool:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{VmPool:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(Permission))

        return VmPoolPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vmpools/{vmpool:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VmPool:id}': self.parentclass.get_id()})).get_vmpoolpermission()

        return VmPoolPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vmpools/{vmpool:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{VmPool:id}': self.parentclass.get_id()})).get_vmpoolpermission()

        return ParseHelper.toSubCollection(VmPoolPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VmPools(Base):
    def __init__(self):
        """Constructor."""

    def add(self, VmPool):
        url = '/api/vmpools'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(VmPool))
        return VmPool(result)

    def get(self, name='*', **kwargs):
        url = '/api/vmpools'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_vmpool()
        return VmPool(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/vmpools'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_vmpool()
        return ParseHelper.toCollection(VmPool,
                                        FilterHelper.filter(result, kwargs))

