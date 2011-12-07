

########################################
############ GENERATED CODE ############
########################################

'''
Generated at: 2011-12-07 12:52:52.924845

@author: mpastern@redhat.com
'''

from ovirtsdk.xml import params
from ovirtsdk.utils.urlhelper import UrlHelper
from ovirtsdk.utils.filterhelper import FilterHelper
from ovirtsdk.utils.parsehelper import ParseHelper
from ovirtsdk.utils.searchhelper import SearchHelper
from ovirtsdk.infrastructure.common import Base


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
        self.networks = ClusterNetworks(cluster)
        self.permissions = ClusterPermissions(cluster)

        self.superclass = cluster

    def __new__(cls, cluster):
        if cluster is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster)
        return obj

    def delete(self):
        url = '/api/clusters/{cluster:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def update(self):
        url = '/api/clusters/{cluster:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{cluster:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Cluster(result)

class ClusterNetwork(params.Network, Base):
    def __init__(self, cluster, network):
        self.parentclass = cluster
        self.superclass  =  network

    def __new__(cls, cluster, network):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, network)
        return obj

    def delete(self):
        url = '/api/clusters/{cluster:id}/networks/{network:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                   '{network:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def update(self):
        url = '/api/clusters/{cluster:id}/networks/{network:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                     '{network:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return ClusterNetwork(self.parentclass, result)

class ClusterNetworks(Base):
 
    def __init__(self, cluster):
        self.parentclass = cluster

    def add(self, network):

        url = '/api/clusters/{cluster:id}/networks'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(network))

        return ClusterNetwork(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/clusters/{cluster:id}/networks'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()})).get_network()

        return ClusterNetwork(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/clusters/{cluster:id}/networks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()})).get_network()

        return ParseHelper.toSubCollection(ClusterNetwork,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class ClusterPermission(params.Permission, Base):
    def __init__(self, cluster, permission):
        self.parentclass = cluster
        self.superclass  =  permission

    def __new__(cls, cluster, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, permission)
        return obj

    def delete(self):
        url = '/api/clusters/{cluster:id}/permissions/{permission:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                   '{permission:id}': self.get_id()}),
                                       headers={'Content-type':None})

class ClusterPermissions(Base):
 
    def __init__(self, cluster):
        self.parentclass = cluster

    def add(self, permission):

        url = '/api/clusters/{cluster:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return ClusterPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/clusters/{cluster:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()})).get_permission()

        return ClusterPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/clusters/{cluster:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()})).get_permission()

        return ParseHelper.toSubCollection(ClusterPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Clusters(Base):
    def __init__(self):
        """Constructor."""

    def add(self, cluster):
        url = '/api/clusters'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(cluster))
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
        self.storagedomains = DataCenterStorageDomains(datacenter)
        self.permissions = DataCenterPermissions(datacenter)

        self.superclass = datacenter

    def __new__(cls, datacenter):
        if datacenter is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter)
        return obj

    def delete(self):
        url = '/api/datacenters/{datacenter:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{datacenter:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def update(self):
        url = '/api/datacenters/{datacenter:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{datacenter:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return DataCenter(result)

class DataCenterPermission(params.Permission, Base):
    def __init__(self, datacenter, permission):
        self.parentclass = datacenter
        self.superclass  =  permission

    def __new__(cls, datacenter, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, permission)
        return obj

    def delete(self):
        url = '/api/datacenters/{datacenter:id}/permissions/{permission:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                   '{permission:id}': self.get_id()}),
                                       headers={'Content-type':None})

class DataCenterPermissions(Base):
 
    def __init__(self, datacenter):
        self.parentclass = datacenter

    def add(self, permission):

        url = '/api/datacenters/{datacenter:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return DataCenterPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/datacenters/{datacenter:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()})).get_permission()

        return DataCenterPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/datacenters/{datacenter:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()})).get_permission()

        return ParseHelper.toSubCollection(DataCenterPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DataCenterStorageDomain(params.StorageDomain, Base):
    def __init__(self, datacenter, storagedomain):
        self.parentclass = datacenter
        self.superclass  =  storagedomain

    def __new__(cls, datacenter, storagedomain):
        if storagedomain is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, storagedomain)
        return obj

    def delete(self):
        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                   '{storagedomain:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def activate(self, action=params.Action()):
        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/activate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                     '{storagedomain:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

    def deactivate(self, action=params.Action()):
        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/deactivate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                     '{storagedomain:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class DataCenterStorageDomains(Base):
 
    def __init__(self, datacenter):
        self.parentclass = datacenter

    def add(self, storagedomain):

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(storagedomain))

        return DataCenterStorageDomain(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()})).get_storage_domain()

        return DataCenterStorageDomain(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()})).get_storage_domain()

        return ParseHelper.toSubCollection(DataCenterStorageDomain,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DataCenters(Base):
    def __init__(self):
        """Constructor."""

    def add(self, datacenter):
        url = '/api/datacenters'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(datacenter))
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
        self.users = DomainUsers(domain)
        self.groups = DomainGroups(domain)

        self.superclass = domain

    def __new__(cls, domain):
        if domain is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain)
        return obj

class DomainGroup(params.Group, Base):
    def __init__(self, domain, group):
        self.parentclass = domain
        self.superclass  =  group

    def __new__(cls, domain, group):
        if group is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain, group)
        return obj

class DomainGroups(Base):
 
    def __init__(self, domain):
        self.parentclass = domain

    def get(self, name=None, **kwargs):

        url = '/api/domains/{domain:id}/groups'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()})).get_group()

        return DomainGroup(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/domains/{domain:id}/groups'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()})).get_group()

        return ParseHelper.toSubCollection(DomainGroup,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DomainUser(params.User, Base):
    def __init__(self, domain, user):
        self.parentclass = domain
        self.superclass  =  user

    def __new__(cls, domain, user):
        if user is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain, user)
        return obj

class DomainUsers(Base):
 
    def __init__(self, domain):
        self.parentclass = domain

    def get(self, name=None, **kwargs):

        url = '/api/domains/{domain:id}/users'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()})).get_user()

        return DomainUser(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/domains/{domain:id}/users'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()})).get_user()

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
        self.permissions = GroupPermissions(group)
        self.roles = GroupRoles(group)
        self.tags = GroupTags(group)

        self.superclass = group

    def __new__(cls, group):
        if group is None: return None
        obj = object.__new__(cls)
        obj.__init__(group)
        return obj

    def delete(self):
        url = '/api/groups/{group:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}': self.get_id()}),
                                       headers={'Content-type':None})

class GroupPermission(params.Permission, Base):
    def __init__(self, group, permission):
        self.parentclass = group
        self.superclass  =  permission

    def __new__(cls, group, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, permission)
        return obj

    def delete(self):
        url = '/api/groups/{group:id}/permissions/{permission:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.get_id(),
                                                                   '{permission:id}': self.get_id()}),
                                       headers={'Content-type':None})

class GroupPermissions(Base):
 
    def __init__(self, group):
        self.parentclass = group

    def add(self, permission):

        url = '/api/groups/{group:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return GroupPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/groups/{group:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_permission()

        return GroupPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/groups/{group:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_permission()

        return ParseHelper.toSubCollection(GroupPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupRole(params.Role, Base):
    def __init__(self, group, role):
        self.parentclass = group
        self.superclass  =  role

    def __new__(cls, group, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, role)
        return obj

    def delete(self):
        url = '/api/groups/{group:id}/roles/{role:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.get_id(),
                                                                   '{role:id}': self.get_id()}),
                                       headers={'Content-type':None})

class GroupRoles(Base):
 
    def __init__(self, group):
        self.parentclass = group

    def add(self, role):

        url = '/api/groups/{group:id}/roles'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(role))

        return GroupRole(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/groups/{group:id}/roles'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_role()

        return GroupRole(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/groups/{group:id}/roles'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_role()

        return ParseHelper.toSubCollection(GroupRole,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupTag(params.Tag, Base):
    def __init__(self, group, tag):
        self.parentclass = group
        self.superclass  =  tag

    def __new__(cls, group, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, tag)
        return obj

    def delete(self):
        url = '/api/groups/{group:id}/tags/{tag:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.get_id(),
                                                                   '{tag:id}': self.get_id()}),
                                       headers={'Content-type':None})

class GroupTags(Base):
 
    def __init__(self, group):
        self.parentclass = group

    def add(self, tag):

        url = '/api/groups/{group:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag))

        return GroupTag(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/groups/{group:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_tag()

        return GroupTag(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/groups/{group:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_tag()

        return ParseHelper.toSubCollection(GroupTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Groups(Base):
    def __init__(self):
        """Constructor."""

    def add(self, group):
        url = '/api/groups'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(group))
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
    def __init__(self, groupsrole, permit):
        self.parentclass = groupsrole
        self.superclass  =  permit

    def __new__(cls, groupsrole, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(groupsrole, permit)
        return obj

    def delete(self):
        url = '/api/groups/{group:id}/roles/{role:id}/permits/{permit:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{groupsrole:id}' : self.parentclass.get_id(),
                                                                   '{permit:id}': self.get_id()}),
                                       headers={'Content-type':None})

class Host(params.Host, Base):
    def __init__(self, host):
        self.nics = HostNics(host)
        self.permissions = HostPermissions(host)
        self.statistics = HostStatistics(host)
        self.tags = HostTags(host)

        self.superclass = host

    def __new__(cls, host):
        if host is None: return None
        obj = object.__new__(cls)
        obj.__init__(host)
        return obj

    def delete(self):
        url = '/api/hosts/{host:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def install(self, action=params.Action()):
        url = '/api/hosts/{host:id}/install'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def fence(self, action=params.Action()):
        url = '/api/hosts/{host:id}/fence'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def activate(self, action=params.Action()):
        url = '/api/hosts/{host:id}/activate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def deactivate(self, action=params.Action()):
        url = '/api/hosts/{host:id}/deactivate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def approve(self, action=params.Action()):
        url = '/api/hosts/{host:id}/approve'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def iscsilogin(self, action=params.Action()):
        url = '/api/hosts/{host:id}/iscsilogin'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def iscsidiscover(self, action=params.Action()):
        url = '/api/hosts/{host:id}/iscsidiscover'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def commitnetconfig(self, action=params.Action()):
        url = '/api/hosts/{host:id}/commitnetconfig'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def update(self):
        url = '/api/hosts/{host:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Host(result)

class HostNIC(params.HostNIC, Base):
    def __init__(self, host, nic):
        self.parentclass = host
        self.superclass  =  nic

    def __new__(cls, host, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, nic)
        return obj

    def delete(self):
        url = '/api/hosts/{host:id}/nics/{nic:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                   '{nic:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def detach(self, action=params.Action()):
        url = '/api/hosts/{host:id}/nics/{nic:id}/detach'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

    def attach(self, action=params.Action()):
        url = '/api/hosts/{host:id}/nics/{nic:id}/attach'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

    def update(self):
        url = '/api/hosts/{host:id}/nics/{nic:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return HostNIC(self.parentclass, result)

class HostNics(Base):
 
    def __init__(self, host):
        self.parentclass = host

    def add(self, hostnic):

        url = '/api/hosts/{host:id}/nics'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(hostnic))

        return HostNIC(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/hosts/{host:id}/nics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_host_nic()

        return HostNIC(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/nics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_host_nic()

        return ParseHelper.toSubCollection(HostNIC,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostPermission(params.Permission, Base):
    def __init__(self, host, permission):
        self.parentclass = host
        self.superclass  =  permission

    def __new__(cls, host, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, permission)
        return obj

    def delete(self):
        url = '/api/hosts/{host:id}/permissions/{permission:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                   '{permission:id}': self.get_id()}),
                                       headers={'Content-type':None})

class HostPermissions(Base):
 
    def __init__(self, host):
        self.parentclass = host

    def add(self, permission):

        url = '/api/hosts/{host:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return HostPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/hosts/{host:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_permission()

        return HostPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_permission()

        return ParseHelper.toSubCollection(HostPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostStatistic(params.Statistic, Base):
    def __init__(self, host, statistic):
        self.parentclass = host
        self.superclass  =  statistic

    def __new__(cls, host, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, statistic)
        return obj

class HostStatistics(Base):
 
    def __init__(self, host):
        self.parentclass = host

    def get(self, name=None, **kwargs):

        url = '/api/hosts/{host:id}/statistics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_statistic()

        return HostStatistic(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/statistics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_statistic()

        return ParseHelper.toSubCollection(HostStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostStorage(params.HostStorage, Base):
    def __init__(self, host, storage):
        self.parentclass = host
        self.superclass  =  storage

    def __new__(cls, host, storage):
        if storage is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, storage)
        return obj

class HostTag(params.Tag, Base):
    def __init__(self, host, tag):
        self.parentclass = host
        self.superclass  =  tag

    def __new__(cls, host, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, tag)
        return obj

    def delete(self):
        url = '/api/hosts/{host:id}/tags/{tag:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                   '{tag:id}': self.get_id()}),
                                       headers={'Content-type':None})

class HostTags(Base):
 
    def __init__(self, host):
        self.parentclass = host

    def add(self, tag):

        url = '/api/hosts/{host:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag))

        return HostTag(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/hosts/{host:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_tag()

        return HostTag(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_tag()

        return ParseHelper.toSubCollection(HostTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Hosts(Base):
    def __init__(self):
        """Constructor."""

    def add(self, host):
        url = '/api/hosts'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(host))
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
    def __init__(self, hostsnic, statistic):
        self.parentclass = hostsnic
        self.superclass  =  statistic

    def __new__(cls, hostsnic, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(hostsnic, statistic)
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

    def delete(self):
        url = '/api/networks/{network:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{network:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def update(self):
        url = '/api/networks/{network:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{network:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Network(result)

class Networks(Base):
    def __init__(self):
        """Constructor."""

    def add(self, network):
        url = '/api/networks'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(network))
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
        self.permits = RolePermits(role)

        self.superclass = role

    def __new__(cls, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(role)
        return obj

    def delete(self):
        url = '/api/roles/{role:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{role:id}': self.get_id()}),
                                       headers={'Content-type':None})

class RolePermit(params.Permit, Base):
    def __init__(self, role, permit):
        self.parentclass = role
        self.superclass  =  permit

    def __new__(cls, role, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(role, permit)
        return obj

    def delete(self):
        url = '/api/roles/{role:id}/permits/{permit:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{role:id}' : self.parentclass.get_id(),
                                                                   '{permit:id}': self.get_id()}),
                                       headers={'Content-type':None})

class RolePermits(Base):
 
    def __init__(self, role):
        self.parentclass = role

    def add(self, permit):

        url = '/api/roles/{role:id}/permits'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{role:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permit))

        return RolePermit(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/roles/{role:id}/permits'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{role:id}': self.parentclass.get_id()})).get_permit()

        return RolePermit(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/roles/{role:id}/permits'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{role:id}': self.parentclass.get_id()})).get_permit()

        return ParseHelper.toSubCollection(RolePermit,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Roles(Base):
    def __init__(self):
        """Constructor."""

    def add(self, role):
        url = '/api/roles'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(role))
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
        self.files = StorageDomainFiles(storagedomain)
        self.templates = StorageDomainTemplates(storagedomain)
        self.vms = StorageDomainVMs(storagedomain)
        self.permissions = StorageDomainPermissions(storagedomain)

        self.superclass = storagedomain

    def __new__(cls, storagedomain):
        if storagedomain is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain)
        return obj

    def delete(self, storagedomain):
        url = '/api/storagedomains/{storagedomain:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{storagedomain:id}': self.get_id()}),
                                       body=ParseHelper.toXml(storagedomain))

    def update(self):
        url = '/api/storagedomains/{storagedomain:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{storagedomain:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return StorageDomain(result)

class StorageDomainFile(params.File, Base):
    def __init__(self, storagedomain, file):
        self.parentclass = storagedomain
        self.superclass  =  file

    def __new__(cls, storagedomain, file):
        if file is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, file)
        return obj

class StorageDomainFiles(Base):
 
    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def get(self, name=None, **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/files'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_file()

        return StorageDomainFile(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/files'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_file()

        return ParseHelper.toSubCollection(StorageDomainFile,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomainPermission(params.Permission, Base):
    def __init__(self, storagedomain, permission):
        self.parentclass = storagedomain
        self.superclass  =  permission

    def __new__(cls, storagedomain, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, permission)
        return obj

    def delete(self):
        url = '/api/storagedomains/{storagedomain:id}/permissions/{permission:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{storagedomain:id}' : self.parentclass.get_id(),
                                                                   '{permission:id}': self.get_id()}),
                                       headers={'Content-type':None})

class StorageDomainPermissions(Base):
 
    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def add(self, permission):

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return StorageDomainPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_permission()

        return StorageDomainPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_permission()

        return ParseHelper.toSubCollection(StorageDomainPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomainTemplate(params.Template, Base):
    def __init__(self, storagedomain, template):
        self.parentclass = storagedomain
        self.superclass  =  template

    def __new__(cls, storagedomain, template):
        if template is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, template)
        return obj

    def import_template(self, action=params.Action()):
        url = '/api/storagedomains/{storagedomain:id}/templates/{template:id}/import'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{storagedomain:id}' : self.parentclass.get_id(),
                                                                     '{template:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class StorageDomainTemplates(Base):
 
    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def get(self, name=None, **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/templates'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_template()

        return StorageDomainTemplate(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/templates'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_template()

        return ParseHelper.toSubCollection(StorageDomainTemplate,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomainVM(params.VM, Base):
    def __init__(self, storagedomain, vm):
        self.parentclass = storagedomain
        self.superclass  =  vm

    def __new__(cls, storagedomain, vm):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, vm)
        return obj

    def import_vm(self, action=params.Action()):
        url = '/api/storagedomains/{storagedomain:id}/vms/{vm:id}/import'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{storagedomain:id}' : self.parentclass.get_id(),
                                                                     '{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class StorageDomainVMs(Base):
 
    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def get(self, name=None, **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/vms'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_vm()

        return StorageDomainVM(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/vms'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_vm()

        return ParseHelper.toSubCollection(StorageDomainVM,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomains(Base):
    def __init__(self):
        """Constructor."""

    def add(self, storagedomain):
        url = '/api/storagedomains'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(storagedomain))
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

    def delete(self):
        url = '/api/tags/{tag:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{tag:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def update(self):
        url = '/api/tags/{tag:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{tag:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Tag(result)

class Tags(Base):
    def __init__(self):
        """Constructor."""

    def add(self, tag):
        url = '/api/tags'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(tag))
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
        self.nics = TemplateNics(template)
        self.cdroms = TemplateCdRoms(template)
        self.disks = TemplateDisks(template)
        self.permissions = TemplatePermissions(template)

        self.superclass = template

    def __new__(cls, template):
        if template is None: return None
        obj = object.__new__(cls)
        obj.__init__(template)
        return obj

    def delete(self):
        url = '/api/templates/{template:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{template:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def export(self, action=params.Action()):
        url = '/api/templates/{template:id}/export'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{template:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def update(self):
        url = '/api/templates/{template:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{template:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Template(result)

class TemplateCdRom(params.CdRom, Base):
    def __init__(self, template, cdrom):
        self.parentclass = template
        self.superclass  =  cdrom

    def __new__(cls, template, cdrom):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, cdrom)
        return obj

class TemplateCdRoms(Base):
 
    def __init__(self, template):
        self.parentclass = template

    def get(self, name=None, **kwargs):

        url = '/api/templates/{template:id}/cdroms'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_cdrom()

        return TemplateCdRom(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/cdroms'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_cdrom()

        return ParseHelper.toSubCollection(TemplateCdRom,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplateDisk(params.Disk, Base):
    def __init__(self, template, disk):
        self.parentclass = template
        self.superclass  =  disk

    def __new__(cls, template, disk):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, disk)
        return obj

class TemplateDisks(Base):
 
    def __init__(self, template):
        self.parentclass = template

    def get(self, name=None, **kwargs):

        url = '/api/templates/{template:id}/disks'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_disk()

        return TemplateDisk(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/disks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_disk()

        return ParseHelper.toSubCollection(TemplateDisk,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplateNic(params.NIC, Base):
    def __init__(self, template, nic):
        self.parentclass = template
        self.superclass  =  nic

    def __new__(cls, template, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, nic)
        return obj

class TemplateNics(Base):
 
    def __init__(self, template):
        self.parentclass = template

    def get(self, name=None, **kwargs):

        url = '/api/templates/{template:id}/nics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_nic()

        return TemplateNic(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/nics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_nic()

        return ParseHelper.toSubCollection(TemplateNic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplatePermission(params.Permission, Base):
    def __init__(self, template, permission):
        self.parentclass = template
        self.superclass  =  permission

    def __new__(cls, template, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, permission)
        return obj

    def delete(self):
        url = '/api/templates/{template:id}/permissions/{permission:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{template:id}' : self.parentclass.get_id(),
                                                                   '{permission:id}': self.get_id()}),
                                       headers={'Content-type':None})

class TemplatePermissions(Base):
 
    def __init__(self, template):
        self.parentclass = template

    def add(self, permission):

        url = '/api/templates/{template:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return TemplatePermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/templates/{template:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_permission()

        return TemplatePermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_permission()

        return ParseHelper.toSubCollection(TemplatePermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Templates(Base):
    def __init__(self):
        """Constructor."""

    def add(self, template):
        url = '/api/templates'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(template))
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
        self.permissions = UserPermissions(user)
        self.roles = UserRoles(user)
        self.tags = UserTags(user)

        self.superclass = user

    def __new__(cls, user):
        if user is None: return None
        obj = object.__new__(cls)
        obj.__init__(user)
        return obj

    def delete(self):
        url = '/api/users/{user:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}': self.get_id()}),
                                       headers={'Content-type':None})

class UserPermission(params.Permission, Base):
    def __init__(self, user, permission):
        self.parentclass = user
        self.superclass  =  permission

    def __new__(cls, user, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, permission)
        return obj

    def delete(self):
        url = '/api/users/{user:id}/permissions/{permission:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.get_id(),
                                                                   '{permission:id}': self.get_id()}),
                                       headers={'Content-type':None})

class UserPermissions(Base):
 
    def __init__(self, user):
        self.parentclass = user

    def add(self, permission):

        url = '/api/users/{user:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return UserPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/users/{user:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_permission()

        return UserPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/users/{user:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_permission()

        return ParseHelper.toSubCollection(UserPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UserRole(params.Role, Base):
    def __init__(self, user, role):
        self.parentclass = user
        self.superclass  =  role

    def __new__(cls, user, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, role)
        return obj

    def delete(self):
        url = '/api/users/{user:id}/roles/{role:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.get_id(),
                                                                   '{role:id}': self.get_id()}),
                                       headers={'Content-type':None})

class UserRoles(Base):
 
    def __init__(self, user):
        self.parentclass = user

    def add(self, role):

        url = '/api/users/{user:id}/roles'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(role))

        return UserRole(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/users/{user:id}/roles'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_role()

        return UserRole(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/users/{user:id}/roles'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_role()

        return ParseHelper.toSubCollection(UserRole,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UserTag(params.Tag, Base):
    def __init__(self, user, tag):
        self.parentclass = user
        self.superclass  =  tag

    def __new__(cls, user, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, tag)
        return obj

    def delete(self):
        url = '/api/users/{user:id}/tags/{tag:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.get_id(),
                                                                   '{tag:id}': self.get_id()}),
                                       headers={'Content-type':None})

class UserTags(Base):
 
    def __init__(self, user):
        self.parentclass = user

    def add(self, tag):

        url = '/api/users/{user:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag))

        return UserTag(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/users/{user:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_tag()

        return UserTag(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/users/{user:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_tag()

        return ParseHelper.toSubCollection(UserTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Users(Base):
    def __init__(self):
        """Constructor."""

    def add(self, user):
        url = '/api/users'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(user))
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
    def __init__(self, usersrole, permit):
        self.parentclass = usersrole
        self.superclass  =  permit

    def __new__(cls, usersrole, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(usersrole, permit)
        return obj

    def delete(self):
        url = '/api/users/{user:id}/roles/{role:id}/permits/{permit:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{usersrole:id}' : self.parentclass.get_id(),
                                                                   '{permit:id}': self.get_id()}),
                                       headers={'Content-type':None})

class VM(params.VM, Base):
    def __init__(self, vm):
        self.cdroms = VMCdRoms(vm)
        self.statistics = VMStatistics(vm)
        self.tags = VMTags(vm)
        self.nics = VMNics(vm)
        self.disks = VMDisks(vm)
        self.snapshots = VMSnapshots(vm)
        self.permissions = VMPermissions(vm)

        self.superclass = vm

    def __new__(cls, vm):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm)
        return obj

    def delete(self):
        url = '/api/vms/{vm:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def shutdown(self, action=params.Action()):
        url = '/api/vms/{vm:id}/shutdown'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def start(self, action=params.Action()):
        url = '/api/vms/{vm:id}/start'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def stop(self, action=params.Action()):
        url = '/api/vms/{vm:id}/stop'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def suspend(self, action=params.Action()):
        url = '/api/vms/{vm:id}/suspend'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def detach(self, action=params.Action()):
        url = '/api/vms/{vm:id}/detach'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def export(self, action=params.Action()):
        url = '/api/vms/{vm:id}/export'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def move(self, action=params.Action()):
        url = '/api/vms/{vm:id}/move'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def ticket(self, action=params.Action()):
        url = '/api/vms/{vm:id}/ticket'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def migrate(self, action=params.Action()):
        url = '/api/vms/{vm:id}/migrate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def update(self):
        url = '/api/vms/{vm:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return VM(result)

class VMCdRom(params.CdRom, Base):
    def __init__(self, vm, cdrom):
        self.parentclass = vm
        self.superclass  =  cdrom

    def __new__(cls, vm, cdrom):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, cdrom)
        return obj

    def delete(self):
        url = '/api/vms/{vm:id}/cdroms/{cdrom:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                   '{cdrom:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def update(self):
        url = '/api/vms/{vm:id}/cdroms/{cdrom:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{cdrom:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return VMCdRom(self.parentclass, result)

class VMCdRoms(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, cdrom):

        url = '/api/vms/{vm:id}/cdroms'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(cdrom))

        return VMCdRom(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/vms/{vm:id}/cdroms'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_cdrom()

        return VMCdRom(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/cdroms'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_cdrom()

        return ParseHelper.toSubCollection(VMCdRom,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMDisk(params.Disk, Base):
    def __init__(self, vm, disk):
        self.parentclass = vm
        self.superclass  =  disk

    def __new__(cls, vm, disk):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, disk)
        return obj

    def delete(self):
        url = '/api/vms/{vm:id}/disks/{disk:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                   '{disk:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def update(self):
        url = '/api/vms/{vm:id}/disks/{disk:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{disk:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return VMDisk(self.parentclass, result)

class VMDisks(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, disk):

        url = '/api/vms/{vm:id}/disks'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(disk))

        return VMDisk(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/vms/{vm:id}/disks'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_disk()

        return VMDisk(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/disks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_disk()

        return ParseHelper.toSubCollection(VMDisk,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMNic(params.NIC, Base):
    def __init__(self, vm, nic):
        self.parentclass = vm
        self.superclass  =  nic

    def __new__(cls, vm, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, nic)
        return obj

    def delete(self):
        url = '/api/vms/{vm:id}/nics/{nic:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                   '{nic:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def update(self):
        url = '/api/vms/{vm:id}/nics/{nic:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return VMNic(self.parentclass, result)

class VMNics(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, nic):

        url = '/api/vms/{vm:id}/nics'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(nic))

        return VMNic(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/vms/{vm:id}/nics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_nic()

        return VMNic(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/nics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_nic()

        return ParseHelper.toSubCollection(VMNic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMPermission(params.Permission, Base):
    def __init__(self, vm, permission):
        self.parentclass = vm
        self.superclass  =  permission

    def __new__(cls, vm, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, permission)
        return obj

    def delete(self):
        url = '/api/vms/{vm:id}/permissions/{permission:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                   '{permission:id}': self.get_id()}),
                                       headers={'Content-type':None})

class VMPermissions(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, permission):

        url = '/api/vms/{vm:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return VMPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/vms/{vm:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_permission()

        return VMPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_permission()

        return ParseHelper.toSubCollection(VMPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMSnapshot(params.Snapshot, Base):
    def __init__(self, vm, snapshot):
        self.parentclass = vm
        self.superclass  =  snapshot

    def __new__(cls, vm, snapshot):
        if snapshot is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, snapshot)
        return obj

    def delete(self):
        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                   '{snapshot:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def restore(self, action=params.Action()):
        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}/restore'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{snapshot:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class VMSnapshots(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, snapshot):

        url = '/api/vms/{vm:id}/snapshots'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(snapshot))

        return VMSnapshot(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/vms/{vm:id}/snapshots'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_snapshot()

        return VMSnapshot(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/snapshots'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_snapshot()

        return ParseHelper.toSubCollection(VMSnapshot,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMStatistic(params.Statistic, Base):
    def __init__(self, vm, statistic):
        self.parentclass = vm
        self.superclass  =  statistic

    def __new__(cls, vm, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, statistic)
        return obj

class VMStatistics(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def get(self, name=None, **kwargs):

        url = '/api/vms/{vm:id}/statistics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_statistic()

        return VMStatistic(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/statistics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_statistic()

        return ParseHelper.toSubCollection(VMStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMTag(params.Tag, Base):
    def __init__(self, vm, tag):
        self.parentclass = vm
        self.superclass  =  tag

    def __new__(cls, vm, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, tag)
        return obj

    def delete(self):
        url = '/api/vms/{vm:id}/tags/{tag:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                   '{tag:id}': self.get_id()}),
                                       headers={'Content-type':None})

class VMTags(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, tag):

        url = '/api/vms/{vm:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag))

        return VMTag(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/vms/{vm:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_tag()

        return VMTag(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_tag()

        return ParseHelper.toSubCollection(VMTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMs(Base):
    def __init__(self):
        """Constructor."""

    def add(self, vm):
        url = '/api/vms'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(vm))
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
        self.permissions = VmPoolPermissions(vmpool)

        self.superclass = vmpool

    def __new__(cls, vmpool):
        if vmpool is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmpool)
        return obj

    def delete(self):
        url = '/api/vmpools/{vmpool:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{vmpool:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def update(self):
        url = '/api/vmpools/{vmpool:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vmpool:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return VmPool(result)

class VmPoolPermission(params.Permission, Base):
    def __init__(self, vmpool, permission):
        self.parentclass = vmpool
        self.superclass  =  permission

    def __new__(cls, vmpool, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmpool, permission)
        return obj

    def delete(self):
        url = '/api/vmpools/{vmpool:id}/permissions/{permission:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{vmpool:id}' : self.parentclass.get_id(),
                                                                   '{permission:id}': self.get_id()}),
                                       headers={'Content-type':None})

class VmPoolPermissions(Base):
 
    def __init__(self, vmpool):
        self.parentclass = vmpool

    def add(self, permission):

        url = '/api/vmpools/{vmpool:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vmpool:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return VmPoolPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        url = '/api/vmpools/{vmpool:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vmpool:id}': self.parentclass.get_id()})).get_permission()

        return VmPoolPermission(self.parentclass,
                                          FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vmpools/{vmpool:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vmpool:id}': self.parentclass.get_id()})).get_permission()

        return ParseHelper.toSubCollection(VmPoolPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VmPools(Base):
    def __init__(self):
        """Constructor."""

    def add(self, vmpool):
        url = '/api/vmpools'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(vmpool))
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

