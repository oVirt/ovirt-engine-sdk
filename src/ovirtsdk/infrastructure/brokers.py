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
Generated at: 2012-08-05 11:02:40.693705

@author: mpastern@redhat.com
'''

from ovirtsdk.xml import params
from ovirtsdk.utils.urlhelper import UrlHelper
from ovirtsdk.utils.filterhelper import FilterHelper
from ovirtsdk.utils.parsehelper import ParseHelper
from ovirtsdk.utils.searchhelper import SearchHelper
from ovirtsdk.infrastructure.common import Base
from ovirtsdk.infrastructure.errors import RequestError


class Capabilities(Base):
    def __init__(self):
        """Constructor."""


    def get(self, id=None, **kwargs):
        '''
        [@param id: string (the id of the entity)]
        [@param **kwargs: dict (property based filtering)]

        @return VersionCaps:
        '''

        url = '/api/capabilities'

        if id or (kwargs and kwargs.has_key('id') and kwargs['id'] <> None):
            try :
                return VersionCaps(self._getProxy().get(url=UrlHelper.append(url,
                                                                             id if id
                                                                                else kwargs['id'])))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=url).version
            return VersionCaps(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return [VersionCaps]:
        '''

        url='/api/capabilities'

        result = self._getProxy().get(url=url).version
        return ParseHelper.toCollection(VersionCaps,
                                        FilterHelper.filter(result, kwargs))
class Cluster(params.Cluster, Base):
    def __init__(self, cluster):
        self.superclass = cluster

        self.glustervolumes = ClusterGlusterVolumes(self)
        self.networks = ClusterNetworks(self)
        self.permissions = ClusterPermissions(self)

    def __new__(cls, cluster):
        if cluster is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/clusters/{cluster:id}',
                                {'{cluster:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def update(self, correlation_id=None):
        '''
        [@param cluster.name: string]
        [@param cluster.description: string]
        [@param cluster.cpu.id: string]
        [@param cluster.version.major: int]
        [@param cluster.version.minor: int]
        [@param cluster.memory_policy.overcommit.percent: double]
        [@param cluster.memory_policy.transparent_hugepages.enabled: boolean]
        [@param cluster.scheduling_policy.policy: string]
        [@param cluster.scheduling_policy.thresholds.low: int]
        [@param cluster.scheduling_policy.thresholds.high: int]
        [@param cluster.scheduling_policy.thresholds.duration: int]
        [@param cluster.error_handling.on_error: string]
        [@param cluster.virt_service: boolean]
        [@param cluster.gluster_service: boolean]
        [@param correlation_id: any string]

        @return Cluster:
        '''

        url = '/api/clusters/{cluster:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{cluster:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return Cluster(result)

class ClusterGlusterVolume(params.GlusterVolume, Base):
    def __init__(self, cluster, glustervolume):
        self.parentclass = cluster
        self.superclass  =  glustervolume

        self.bricks = ClusterGlusterVolumeBricks(self)

    def __new__(cls, cluster, glustervolume):
        if glustervolume is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, glustervolume)
        return obj

    def delete(self):
        '''
        @return None:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                   '{glustervolume:id}': self.get_id()}),
                                       headers={'Content-type':None})

    def start(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.force: boolean]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/start'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                     '{glustervolume:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

    def stop(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.force: boolean]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/stop'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                     '{glustervolume:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

    def setOption(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.option.name: string
        @param action.option.value: string
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/setOption'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                     '{glustervolume:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

    def rebalance(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.fix_layout: boolean]
        [@param action.force: boolean]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/rebalance'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                     '{glustervolume:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

    def resetOption(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.option.name: string
        @param action.force: boolean
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/resetOption'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                     '{glustervolume:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

    def resetAllOptions(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/resetAllOptions'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                     '{glustervolume:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

class ClusterGlusterVolumeBrick(params.GlusterBrick, Base):
    def __init__(self, clusterglustervolume, brick):
        self.parentclass = clusterglustervolume
        self.superclass  =  brick

        #SUB_COLLECTIONS
    def __new__(cls, clusterglustervolume, brick):
        if brick is None: return None
        obj = object.__new__(cls)
        obj.__init__(clusterglustervolume, brick)
        return obj

    def delete(self):
        '''
        @return None:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.parentclass.get_id(),
                                                                   '{glustervolume:id}': self.parentclass.get_id(),
                                                                   '{brick:id}': self.get_id()}),
                                       headers={'Content-type':None})

class ClusterGlusterVolumeBricks(Base):

    def __init__(self, clusterglustervolume):
        self.parentclass = clusterglustervolume

    def add(self, glusterbricks, expect=None, correlation_id=None):

        '''
        @type GlusterBricks:

        @param bricks.brick: collection
        {
          @ivar brick.server_id: string
          @ivar brick.brick_dir: string
        }
        [@param bricks.brick: collection]
        {
          [@ivar brick.replica_count: unsignedShort]
          [@ivar brick.stripe_count: unsignedShort]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return GlusterBricks:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.parentclass.get_id(),
                                                                  '{glustervolume:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(glusterbricks),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return ClusterGlusterVolumeBrick(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return GlusterBricks:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.parentclass.get_id(),
                                                                                           '{glustervolume:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return ClusterGlusterVolumeBrick(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.parentclass.get_id(),
                                                                      '{glustervolume:id}': self.parentclass.get_id()}),
                                          headers={}).get_brick()

            return ClusterGlusterVolumeBrick(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return GlusterBricks:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.parentclass.get_id(),
                                                                  '{glustervolume:id}': self.parentclass.get_id()})).get_brick()

        return ParseHelper.toSubCollection(ClusterGlusterVolumeBrick,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class ClusterGlusterVolumes(Base):

    def __init__(self, cluster):
        self.parentclass = cluster

    def add(self, glustervolume, expect=None, correlation_id=None):

        '''
        @type GlusterVolume:

        @param gluster_volume.name: string
        @param gluster_volume.volume_type: string
        @param gluster_volume.bricks.brick: collection
        {
          @ivar brick.server_id: string
          @ivar brick.brick_dir: string
        }
        [@param gluster_volume.transport_types: collection]
        {
          [@ivar transport_type: string]
        }
        [@param gluster_volume.replica_count: unsignedShort]
        [@param gluster_volume.stripe_count: unsignedShort]
        [@param gluster_volume.access_protocols: collection]
        {
          [@ivar access_protocol: string]
        }
        [@param gluster_volume.access_control_list: collection]
        {
          [@ivar ip: string]
        }
        [@param gluster_volume.options.option: collection]
        {
          [@ivar option.name: string]
          [@ivar option.value: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return GlusterVolume:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(glustervolume),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return ClusterGlusterVolume(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return GlusterVolumes:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return ClusterGlusterVolume(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                          headers={}).get_gluster_volume()

            return ClusterGlusterVolume(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]

        @return GlusterVolumes:
        '''

        url = '/api/clusters/{cluster:id}/glustervolumes'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{cluster:id}': self.parentclass.get_id()}),
                                                                   qargs={'search:query':query,'case_sensitive:matrix':case_sensitive}),
                                      headers={}).get_gluster_volume()
        return ParseHelper.toSubCollection(ClusterGlusterVolume,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class ClusterNetwork(params.Network, Base):
    def __init__(self, cluster, network):
        self.parentclass = cluster
        self.superclass  =  network

        #SUB_COLLECTIONS
    def __new__(cls, cluster, network):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, network)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/clusters/{cluster:id}/networks/{network:id}',
                                {'{cluster:id}' : self.parentclass.get_id(),
                                 '{network:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def update(self, correlation_id=None):
        '''
        [@param network.display: boolean]
        [@param network.usages.usage: collection]
        {
          [@ivar usage: string]
        }
        [@param correlation_id: any string]

        @return Network:
        '''

        url = '/api/clusters/{cluster:id}/networks/{network:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                     '{network:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})

        return ClusterNetwork(self.parentclass, result)

class ClusterNetworks(Base):

    def __init__(self, cluster):
        self.parentclass = cluster

    def add(self, network, expect=None, correlation_id=None):

        '''
        @type Network:

        @param network.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Network:
        '''

        url = '/api/clusters/{cluster:id}/networks'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(network),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return ClusterNetwork(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Networks:
        '''

        url = '/api/clusters/{cluster:id}/networks'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return ClusterNetwork(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                          headers={}).get_network()

            return ClusterNetwork(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Networks:
        '''

        url = '/api/clusters/{cluster:id}/networks'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{cluster:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_network()
        return ParseHelper.toSubCollection(ClusterNetwork,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class ClusterPermission(params.Permission, Base):
    def __init__(self, cluster, permission):
        self.parentclass = cluster
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, cluster, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, permission)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/clusters/{cluster:id}/permissions/{permission:id}',
                                {'{cluster:id}' : self.parentclass.get_id(),
                                 '{permission:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class ClusterPermissions(Base):

    def __init__(self, cluster):
        self.parentclass = cluster

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.role.id: string
          @param permission.group.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/api/clusters/{cluster:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return ClusterPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/api/clusters/{cluster:id}/permissions'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return ClusterPermission(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                          headers={}).get_permission()

            return ClusterPermission(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/api/clusters/{cluster:id}/permissions'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{cluster:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permission()
        return ParseHelper.toSubCollection(ClusterPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Clusters(Base):
    def __init__(self):
        """Constructor."""

    def add(self, cluster, expect=None, correlation_id=None):
        '''
        @type Cluster:

        @param cluster.data_center.id|name: string
        @param cluster.name: string
        @param cluster.version.major: int
        @param cluster.version.minor: int
        @param cluster.cpu.id: string
        [@param cluster.description: string]
        [@param cluster.memory_policy.overcommit.percent: double]
        [@param cluster.memory_policy.transparent_hugepages.enabled: boolean]
        [@param cluster.scheduling_policy.policy: string]
        [@param cluster.scheduling_policy.thresholds.low: int]
        [@param cluster.scheduling_policy.thresholds.high: int]
        [@param cluster.scheduling_policy.thresholds.duration: int]
        [@param cluster.error_handling.on_error: string]
        [@param cluster.virt_service: boolean]
        [@param cluster.gluster_service: boolean]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Cluster:
        '''

        url = '/api/clusters'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(cluster),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})
        return Cluster(result)

    def get(self, name='name', filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]
        [@param filter: true|false]

        @return Clusters:
        '''

        url = '/api/clusters'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return Cluster(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={"Filter":filter}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={"Filter":filter}).get_cluster()
            return Cluster(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param filter: true|false]

        @return Clusters:
        '''

        url='/api/clusters'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={"Filter":filter}).get_cluster()
        return ParseHelper.toCollection(Cluster,
                                        FilterHelper.filter(result, kwargs))

class DataCenter(params.DataCenter, Base):
    def __init__(self, datacenter):
        self.superclass = datacenter

        self.storagedomains = DataCenterStorageDomains(self)
        self.quotas = DataCenterQuotas(self)
        self.permissions = DataCenterPermissions(self)

    def __new__(cls, datacenter):
        if datacenter is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter)
        return obj

    def delete(self, action=params.Action(), async=None, correlation_id=None):
        '''
        @type Action:

        [@param action.force: boolean]
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/datacenters/{datacenter:id}',
                                {'{datacenter:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       body=ParseHelper.toXml(action),
                                       headers={"Correlation-Id":correlation_id})

    def update(self, correlation_id=None):
        '''
        [@param datacenter.name: string]
        [@param datacenter.storage_type: string]
        [@param datacenter.version.major: int]
        [@param datacenter.version.minor: int]
        [@param datacenter.description: string]
        [@param datacenter.storage_format: string]
        [@param correlation_id: any string]

        @return DataCenter:
        '''

        url = '/api/datacenters/{datacenter:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{datacenter:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return DataCenter(result)

class DataCenterPermission(params.Permission, Base):
    def __init__(self, datacenter, permission):
        self.parentclass = datacenter
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, datacenter, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, permission)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/datacenters/{datacenter:id}/permissions/{permission:id}',
                                {'{datacenter:id}' : self.parentclass.get_id(),
                                 '{permission:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class DataCenterPermissions(Base):

    def __init__(self, datacenter):
        self.parentclass = datacenter

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.role.id: string
          @param permission.group.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/api/datacenters/{datacenter:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return DataCenterPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/api/datacenters/{datacenter:id}/permissions'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return DataCenterPermission(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                          headers={}).get_permission()

            return DataCenterPermission(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Permissions:
        '''

        url = '/api/datacenters/{datacenter:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()})).get_permission()

        return ParseHelper.toSubCollection(DataCenterPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DataCenterQuota(params.Quota, Base):
    def __init__(self, datacenter, quota):
        self.parentclass = datacenter
        self.superclass  =  quota

        #SUB_COLLECTIONS
    def __new__(cls, datacenter, quota):
        if quota is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, quota)
        return obj

    def delete(self):
        '''
        @return None:
        '''

        url = '/api/datacenters/{datacenter:id}/quotas/{quota:id}'

        return self._getProxy().delete(url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                   '{quota:id}': self.get_id()}),
                                       headers={'Content-type':None})

class DataCenterQuotas(Base):

    def __init__(self, datacenter):
        self.parentclass = datacenter

    def add(self, quota):

        '''
        @type Quota:


        @return Quota:
        '''

        url = '/api/datacenters/{datacenter:id}/quotas'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(quota),
                                      headers={})

        return DataCenterQuota(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Quotas:
        '''

        url = '/api/datacenters/{datacenter:id}/quotas'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return DataCenterQuota(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                          headers={}).get_quota()

            return DataCenterQuota(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Quotas:
        '''

        url = '/api/datacenters/{datacenter:id}/quotas'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()})).get_quota()

        return ParseHelper.toSubCollection(DataCenterQuota,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DataCenterStorageDomain(params.StorageDomain, Base):
    def __init__(self, datacenter, storagedomain):
        self.parentclass = datacenter
        self.superclass  =  storagedomain

        #SUB_COLLECTIONS
    def __new__(cls, datacenter, storagedomain):
        if storagedomain is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, storagedomain)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}',
                                {'{datacenter:id}' : self.parentclass.get_id(),
                                 '{storagedomain:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def activate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/activate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                     '{storagedomain:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

    def deactivate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/deactivate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                     '{storagedomain:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

class DataCenterStorageDomains(Base):

    def __init__(self, datacenter):
        self.parentclass = datacenter

    def add(self, storagedomain, expect=None, correlation_id=None):

        '''
        @type StorageDomain:

        @param storagedomain.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return StorageDomain:
        '''

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(storagedomain),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return DataCenterStorageDomain(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return StorageDomains:
        '''

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return DataCenterStorageDomain(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                          headers={}).get_storage_domain()

            return DataCenterStorageDomain(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return StorageDomains:
        '''

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{datacenter:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_storage_domain()
        return ParseHelper.toSubCollection(DataCenterStorageDomain,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DataCenters(Base):
    def __init__(self):
        """Constructor."""

    def add(self, datacenter, expect=None, correlation_id=None):
        '''
        @type DataCenter:

        @param datacenter.name: string
        @param datacenter.storage_type: string
        @param datacenter.version.major: int
        @param datacenter.version.minor: int
        [@param datacenter.description: string]
        [@param datacenter.storage_format: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return DataCenter:
        '''

        url = '/api/datacenters'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(datacenter),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})
        return DataCenter(result)

    def get(self, name='name', filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]
        [@param filter: true|false]

        @return DataCenters:
        '''

        url = '/api/datacenters'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return DataCenter(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={"Filter":filter}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={"Filter":filter}).get_data_center()
            return DataCenter(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param filter: true|false]

        @return DataCenters:
        '''

        url='/api/datacenters'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={"Filter":filter}).get_data_center()
        return ParseHelper.toCollection(DataCenter,
                                        FilterHelper.filter(result, kwargs))

class Disk(params.Disk, Base):
    def __init__(self, disk):
        self.superclass = disk

        self.statistics = DiskStatistics(self)

    def __new__(cls, disk):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk)
        return obj

    def update(self, correlation_id=None):
        '''
        [@param size: int]
        [@param provisioned_size: int]
        [@param disk.interface: string]
        [@param disk.format: string]
        [@param disk.sparse: boolean]
        [@param disk.bootable: boolean]
        [@param disk.shareable: boolean]
        [@param disk.propagate_errors: boolean]
        [@param disk.wipe_after_delete: boolean]
        [@param correlation_id: any string]

        @return Disk:
        '''

        url = '/api/disks/{disk:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{disk:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return Disk(result)

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/disks/{disk:id}',
                                {'{disk:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class DiskStatistic(params.Statistic, Base):
    def __init__(self, disk, statistic):
        self.parentclass = disk
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, disk, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk, statistic)
        return obj

class DiskStatistics(Base):

    def __init__(self, disk):
        self.parentclass = disk

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/api/disks/{disk:id}/statistics'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{disk:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return DiskStatistic(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{disk:id}': self.parentclass.get_id()}),
                                          headers={}).get_statistic()

            return DiskStatistic(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Statistics:
        '''

        url = '/api/disks/{disk:id}/statistics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{disk:id}': self.parentclass.get_id()})).get_statistic()

        return ParseHelper.toSubCollection(DiskStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Disks(Base):
    def __init__(self):
        """Constructor."""

    def add(self, disk, expect=None, correlation_id=None):
        '''
        @type Disk:

        @param provisioned_size: int
        @param disk.interface: string
        @param disk.format: string
        [@param disk.size: int]
        [@param disk.sparse: boolean]
        [@param disk.bootable: boolean]
        [@param disk.shareable: boolean]
        [@param disk.propagate_errors: boolean]
        [@param disk.wipe_after_delete: boolean]
        [@param disk.storage_domains.storage_domain: collection]
        {
          [@ivar storage_domain.id|name: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Disk:
        '''

        url = '/api/disks'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(disk),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})
        return Disk(result)

    def get(self, name='name', **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]

        @return Disks:
        '''

        url = '/api/disks'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return Disk(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={}).get_disk()
            return Disk(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Disks:
        '''

        url='/api/disks'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={}).get_disk()
        return ParseHelper.toCollection(Disk,
                                        FilterHelper.filter(result, kwargs))

class Domain(params.Domain, Base):
    def __init__(self, domain):
        self.superclass = domain

        self.users = DomainUsers(self)
        self.groups = DomainGroups(self)

    def __new__(cls, domain):
        if domain is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain)
        return obj

class DomainGroup(params.Group, Base):
    def __init__(self, domain, group):
        self.parentclass = domain
        self.superclass  =  group

        #SUB_COLLECTIONS
    def __new__(cls, domain, group):
        if group is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain, group)
        return obj

class DomainGroups(Base):

    def __init__(self, domain):
        self.parentclass = domain

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Groups:
        '''

        url = '/api/domains/{domain:id}/groups'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return DomainGroup(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()}),
                                          headers={}).get_group()

            return DomainGroup(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Groups:
        '''

        url = '/api/domains/{domain:id}/groups'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{domain:id}': self.parentclass.get_id()}),
                                                                   qargs={'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={}).get_group()
        return ParseHelper.toSubCollection(DomainGroup,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DomainUser(params.User, Base):
    def __init__(self, domain, user):
        self.parentclass = domain
        self.superclass  =  user

        #SUB_COLLECTIONS
    def __new__(cls, domain, user):
        if user is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain, user)
        return obj

class DomainUsers(Base):

    def __init__(self, domain):
        self.parentclass = domain

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Users:
        '''

        url = '/api/domains/{domain:id}/users'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return DomainUser(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()}),
                                          headers={}).get_user()

            return DomainUser(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Users:
        '''

        url = '/api/domains/{domain:id}/users'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{domain:id}': self.parentclass.get_id()}),
                                                                   qargs={'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={}).get_user()
        return ParseHelper.toSubCollection(DomainUser,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Domains(Base):
    def __init__(self):
        """Constructor."""

    def get(self, name='*', **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param name: string (the name of the entity)]

        @return Domains:
        '''

        url = '/api/domains'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return Domain(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']), headers={}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=url,
                                          headers={}).get_domain()
            if name != '*': kwargs['name']=name
            return Domain(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return Domains:
        '''

        url='/api/domains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'max:matrix':max}),
                                      headers={}).get_domain()
        return ParseHelper.toCollection(Domain,
                                        FilterHelper.filter(result, kwargs))

class Event(params.Event, Base):
    def __init__(self, event):
        self.superclass = event

        #SUB_COLLECTIONS
    def __new__(cls, event):
        if event is None: return None
        obj = object.__new__(cls)
        obj.__init__(event)
        return obj

class Events(Base):
    def __init__(self):
        """Constructor."""

    def get(self, name='name', **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]

        @return Events:
        '''

        url = '/api/events'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return Event(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={}).get_event()
            return Event(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, from_event_id=None, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param from_event_id: string (event_id)]
        [@param max: int (max results)]

        @return Events:
        '''

        url='/api/events'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'from:matrix':from_event_id,'max:matrix':max}),
                                      headers={}).get_event()
        return ParseHelper.toCollection(Event,
                                        FilterHelper.filter(result, kwargs))

class Group(params.Group, Base):
    def __init__(self, group):
        self.superclass = group

        self.permissions = GroupPermissions(self)
        self.roles = GroupRoles(self)
        self.tags = GroupTags(self)

    def __new__(cls, group):
        if group is None: return None
        obj = object.__new__(cls)
        obj.__init__(group)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/groups/{group:id}',
                                {'{group:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class GroupPermission(params.Permission, Base):
    def __init__(self, group, permission):
        self.parentclass = group
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, group, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, permission)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/groups/{group:id}/permissions/{permission:id}',
                                {'{group:id}' : self.parentclass.get_id(),
                                 '{permission:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class GroupPermissions(Base):

    def __init__(self, group):
        self.parentclass = group

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.role.id: string
          @param permission.data_center.id: string
        Overload 2:
          @param permission.role.id: string
          @param permission.cluster.id: string
        Overload 3:
          @param permission.role.id: string
          @param permission.host.id: string
        Overload 4:
          @param permission.role.id: string
          @param permission.storage_domain.id: string
        Overload 5:
          @param permission.role.id: string
          @param permission.vm.id: string
        Overload 6:
          @param permission.role.id: string
          @param permission.vmpool.id: string
        Overload 7:
          @param permission.role.id: string
          @param permission.template.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/api/groups/{group:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return GroupPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/api/groups/{group:id}/permissions'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return GroupPermission(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                          headers={}).get_permission()

            return GroupPermission(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/api/groups/{group:id}/permissions'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{group:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permission()
        return ParseHelper.toSubCollection(GroupPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupRole(params.Role, Base):
    def __init__(self, group, role):
        self.parentclass = group
        self.superclass  =  role

        self.permits = GroupRolePermits(self)

    def __new__(cls, group, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, role)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/groups/{group:id}/roles/{role:id}',
                                {'{group:id}' : self.parentclass.get_id(),
                                 '{role:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class GroupRolePermit(params.Permit, Base):
    def __init__(self, grouprole, permit):
        self.parentclass = grouprole
        self.superclass  =  permit

        #SUB_COLLECTIONS
    def __new__(cls, grouprole, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(grouprole, permit)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/groups/{group:id}/roles/{role:id}/permits/{permit:id}',
                                {'{group:id}' : self.parentclass.parentclass.get_id(),
                                 '{role:id}': self.parentclass.get_id(),
                                 '{permit:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class GroupRolePermits(Base):

    def __init__(self, grouprole):
        self.parentclass = grouprole

    def add(self, permit, expect=None, correlation_id=None):

        '''
        @type Permit:

        @param permit.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permit:
        '''

        url = '/api/groups/{group:id}/roles/{role:id}/permits'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.parentclass.get_id(),
                                                                  '{role:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permit),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return GroupRolePermit(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permits:
        '''

        url = '/api/groups/{group:id}/roles/{role:id}/permits'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{group:id}' : self.parentclass.parentclass.get_id(),
                                                                                           '{role:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return GroupRolePermit(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.parentclass.get_id(),
                                                                      '{role:id}': self.parentclass.get_id()}),
                                          headers={}).get_permit()

            return GroupRolePermit(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permits:
        '''

        url = '/api/groups/{group:id}/roles/{role:id}/permits'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{group:id}' : self.parentclass.parentclass.get_id(),
                                                                                               '{role:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permit()
        return ParseHelper.toSubCollection(GroupRolePermit,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupRoles(Base):

    def __init__(self, group):
        self.parentclass = group

    def add(self, role, expect=None, correlation_id=None):

        '''
        @type Role:

        @param role.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Role:
        '''

        url = '/api/groups/{group:id}/roles'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(role),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return GroupRole(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Roles:
        '''

        url = '/api/groups/{group:id}/roles'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return GroupRole(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                          headers={}).get_role()

            return GroupRole(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Roles:
        '''

        url = '/api/groups/{group:id}/roles'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{group:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_role()
        return ParseHelper.toSubCollection(GroupRole,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupTag(params.Tag, Base):
    def __init__(self, group, tag):
        self.parentclass = group
        self.superclass  =  tag

        #SUB_COLLECTIONS
    def __new__(cls, group, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, tag)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/groups/{group:id}/tags/{tag:id}',
                                {'{group:id}' : self.parentclass.get_id(),
                                 '{tag:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class GroupTags(Base):

    def __init__(self, group):
        self.parentclass = group

    def add(self, tag, expect=None, correlation_id=None):

        '''
        @type Tag:

        @param tag.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/api/groups/{group:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return GroupTag(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/api/groups/{group:id}/tags'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return GroupTag(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                          headers={}).get_tag()

            return GroupTag(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Tags:
        '''

        url = '/api/groups/{group:id}/tags'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{group:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_tag()
        return ParseHelper.toSubCollection(GroupTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Groups(Base):
    def __init__(self):
        """Constructor."""

    def add(self, group, correlation_id=None):
        '''
        @type Group:

        @param group.name: string
        [@param correlation_id: any string]

        @return Group:
        '''

        url = '/api/groups'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(group),
                                      headers={"Correlation-Id":correlation_id})
        return Group(result)

    def get(self, name='name', **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]

        @return Groups:
        '''

        url = '/api/groups'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return Group(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={}).get_group()
            return Group(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Groups:
        '''

        url='/api/groups'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={}).get_group()
        return ParseHelper.toCollection(Group,
                                        FilterHelper.filter(result, kwargs))

class Host(params.Host, Base):
    def __init__(self, host):
        self.superclass = host

        self.nics = HostNics(self)
        self.permissions = HostPermissions(self)
        self.storage = HostStorage(self)
        self.statistics = HostStatistics(self)
        self.tags = HostTags(self)

    def __new__(cls, host):
        if host is None: return None
        obj = object.__new__(cls)
        obj.__init__(host)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/hosts/{host:id}',
                                {'{host:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def fence(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/hosts/{host:id}/fence'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def install(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/hosts/{host:id}/install'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def activate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/hosts/{host:id}/activate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def deactivate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/hosts/{host:id}/deactivate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def approve(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.cluster.id|name: string]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/hosts/{host:id}/approve'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def iscsilogin(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.iscsi.address: string
        @param action.iscsi.target: string
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/hosts/{host:id}/iscsilogin'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def iscsidiscover(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.iscsi.address: string
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/hosts/{host:id}/iscsidiscover'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def commitnetconfig(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/hosts/{host:id}/commitnetconfig'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def update(self, correlation_id=None):
        '''
        [@param host.name: string]
        [@param host.address: string]
        [@param host.root_password: string]
        [@param host.cluster.id: string]
        [@param host.port: int]
        [@param host.storage_manager.priority: int]
        [@param host.power_management.type: string]
        [@param host.power_management.enabled: boolean]
        [@param host.power_management.address: string]
        [@param host.power_management.user_name: string]
        [@param host.power_management.password: string]
        [@param host.power_management.options.option: collection]
        {
          [@ivar option.name: string]
          [@ivar option.value: string]
        }
        [@param correlation_id: any string]

        @return Host:
        '''

        url = '/api/hosts/{host:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return Host(result)

class HostNIC(params.HostNIC, Base):
    def __init__(self, host, nic):
        self.parentclass = host
        self.superclass  =  nic

        self.statistics = HostNicStatistics(self)

    def __new__(cls, host, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, nic)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/hosts/{host:id}/nics/{nic:id}',
                                {'{host:id}' : self.parentclass.get_id(),
                                 '{nic:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def attach(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.network.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/hosts/{host:id}/nics/{nic:id}/attach'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

    def detach(self, action=params.Action()):
        '''
        @type Action:


        @return Response:
        '''

        url = '/api/hosts/{host:id}/nics/{nic:id}/detach'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={})

        return result

    def update(self, correlation_id=None):
        '''
        [@param hostnic.bonding.slaves.host_nic: collection]
        {
          [@ivar host_nic.id|name: string]
        }
        [@param hostnic.network.id|name: string]
        [@param hostnic.name: string]
        [@param hostnic.bonding.options.option: collection]
        {
          [@ivar option.name: string]
          [@ivar option.value: string]
          [@ivar type: string]
        }
        [@param hostnic.ip.gateway: string]
        [@param hostnic.boot_protocol: string]
        [@param hostnic.mac: string]
        [@param hostnic.ip.address: string]
        [@param hostnic.ip.netmask: string]
        [@param hostnic.ip.mtu: int]
        [@param correlation_id: any string]

        @return HostNIC:
        '''

        url = '/api/hosts/{host:id}/nics/{nic:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})

        return HostNIC(self.parentclass, result)

class HostNicStatistic(params.Statistic, Base):
    def __init__(self, hostnic, statistic):
        self.parentclass = hostnic
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, hostnic, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(hostnic, statistic)
        return obj

class HostNicStatistics(Base):

    def __init__(self, hostnic):
        self.parentclass = hostnic

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/api/hosts/{host:id}/nics/{nic:id}/statistics'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{host:id}' : self.parentclass.parentclass.get_id(),
                                                                                           '{nic:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return HostNicStatistic(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.parentclass.get_id(),
                                                                      '{nic:id}': self.parentclass.get_id()}),
                                          headers={}).get_statistic()

            return HostNicStatistic(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Statistics:
        '''

        url = '/api/hosts/{host:id}/nics/{nic:id}/statistics'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{host:id}' : self.parentclass.parentclass.get_id(),
                                                                                               '{nic:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_statistic()
        return ParseHelper.toSubCollection(HostNicStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostNics(Base):

    def __init__(self, host):
        self.parentclass = host

    def add(self, hostnic, expect=None, correlation_id=None):

        '''
        @type HostNIC:

        @param hostnic.network.id|name: string
        @param hostnic.name: string
        [@param hostnic.bonding.slaves.host_nic: collection]
        {
          [@ivar host_nic.id|name: string]
        }
        [@param hostnic.bonding.options.option: collection]
        {
          [@ivar option.name: string]
          [@ivar option.value: string]
          [@ivar type: string]
        }
        [@param hostnic.ip.gateway: string]
        [@param hostnic.boot_protocol: string]
        [@param hostnic.mac: string]
        [@param hostnic.ip.address: string]
        [@param hostnic.ip.netmask: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return HostNIC:
        '''

        url = '/api/hosts/{host:id}/nics'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(hostnic),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return HostNIC(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return HostNics:
        '''

        url = '/api/hosts/{host:id}/nics'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return HostNIC(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                          headers={}).get_host_nic()

            return HostNIC(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return HostNics:
        '''

        url = '/api/hosts/{host:id}/nics'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{host:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_host_nic()
        return ParseHelper.toSubCollection(HostNIC,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

    def setupnetworks(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.host_nics.host_nic: collection]
        {
          [@ivar host_nic.network.id|name: string]
          [@ivar host_nic.name: string]
          [@ivar host_nic.ip.gateway: string]
          [@ivar host_nic.boot_protocol: string]
          [@ivar host_nic.mac: string]
          [@ivar host_nic.ip.address: string]
          [@ivar host_nic.ip.netmask: string]
          [@ivar host_nic.bonding.options.option: collection]
          {
            [@param option.name: string]
            [@param option.value: string]
            [@param option.type: string]
          }
          [@ivar bonding.slaves.host_nic: collection]
          {
            [@param host_nic.name|id: string]
          }
          [@ivar host_nic.override_configuration: boolean]
        }
        [@param action.checkConnectivity: boolean]
        [@param action.connectivityTimeout: int]
        [@param action.force: boolean]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/hosts/{host:id}/nics/setupnetworks'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

class HostPermission(params.Permission, Base):
    def __init__(self, host, permission):
        self.parentclass = host
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, host, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, permission)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/hosts/{host:id}/permissions/{permission:id}',
                                {'{host:id}' : self.parentclass.get_id(),
                                 '{permission:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class HostPermissions(Base):

    def __init__(self, host):
        self.parentclass = host

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.role.id: string
          @param permission.group.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/api/hosts/{host:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return HostPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/api/hosts/{host:id}/permissions'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return HostPermission(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                          headers={}).get_permission()

            return HostPermission(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/api/hosts/{host:id}/permissions'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{host:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permission()
        return ParseHelper.toSubCollection(HostPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostStatistic(params.Statistic, Base):
    def __init__(self, host, statistic):
        self.parentclass = host
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, host, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, statistic)
        return obj

class HostStatistics(Base):

    def __init__(self, host):
        self.parentclass = host

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/api/hosts/{host:id}/statistics'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return HostStatistic(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                          headers={}).get_statistic()

            return HostStatistic(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Statistics:
        '''

        url = '/api/hosts/{host:id}/statistics'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{host:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_statistic()
        return ParseHelper.toSubCollection(HostStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostStorage(Base):

    def __init__(self, host):
        self.parentclass = host

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return HostStorage:
        '''

        url = '/api/hosts/{host:id}/storage'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return HostStorage(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                          headers={}).get_storage()

            return HostStorage(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return HostStorage:
        '''

        url = '/api/hosts/{host:id}/storage'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{host:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_storage()
        return ParseHelper.toSubCollection(HostStorage,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostTag(params.Tag, Base):
    def __init__(self, host, tag):
        self.parentclass = host
        self.superclass  =  tag

        #SUB_COLLECTIONS
    def __new__(cls, host, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, tag)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/hosts/{host:id}/tags/{tag:id}',
                                {'{host:id}' : self.parentclass.get_id(),
                                 '{tag:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class HostTags(Base):

    def __init__(self, host):
        self.parentclass = host

    def add(self, tag):

        '''
        @type Tag:


        @return Tag:
        '''

        url = '/api/hosts/{host:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag),
                                      headers={})

        return HostTag(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/api/hosts/{host:id}/tags'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return HostTag(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                          headers={}).get_tag()

            return HostTag(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Tags:
        '''

        url = '/api/hosts/{host:id}/tags'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{host:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_tag()
        return ParseHelper.toSubCollection(HostTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Hosts(Base):
    def __init__(self):
        """Constructor."""

    def add(self, host, expect=None, correlation_id=None):
        '''
        @type Host:

        @param host.name: string
        @param host.address: string
        @param host.root_password: string
        @param host.cluster.id: string
        [@param host.port: int]
        [@param host.storage_manager.priority: int]
        [@param host.power_management.type: string]
        [@param host.power_management.enabled: boolean]
        [@param host.power_management.address: string]
        [@param host.power_management.user_name: string]
        [@param host.power_management.password: string]
        [@param host.power_management.options.option: collection]
        {
          [@ivar option.name: string]
          [@ivar option.value: string]
        }
        [@param host.reboot_after_installation: boolean]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Host:
        '''

        url = '/api/hosts'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(host),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})
        return Host(result)

    def get(self, name='name', filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]
        [@param filter: true|false]

        @return Hosts:
        '''

        url = '/api/hosts'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return Host(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={"Filter":filter}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={"Filter":filter}).get_host()
            return Host(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param filter: true|false]

        @return Hosts:
        '''

        url='/api/hosts'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={"Filter":filter}).get_host()
        return ParseHelper.toCollection(Host,
                                        FilterHelper.filter(result, kwargs))

class Network(params.Network, Base):
    def __init__(self, network):
        self.superclass = network

        #SUB_COLLECTIONS
    def __new__(cls, network):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(network)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/networks/{network:id}',
                                {'{network:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def update(self, correlation_id=None):
        '''
        [@param network.name: string]
        [@param network.description: string]
        [@param network.vlan.id: string]
        [@param network.ip.address: string]
        [@param network.ip.gateway: string]
        [@param network.ip.netmask: string]
        [@param network.display: boolean]
        [@param network.stp: boolean]
        [@param network.mtu: int]
        [@param correlation_id: any string]

        @return Network:
        '''

        url = '/api/networks/{network:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{network:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return Network(result)

class Networks(Base):
    def __init__(self):
        """Constructor."""

    def add(self, network, expect=None, correlation_id=None):
        '''
        @type Network:

        @param network.data_center.id|name: string
        @param network.name: string
        [@param network.description: string]
        [@param network.vlan.id: string]
        [@param network.ip.address: string]
        [@param network.ip.gateway: string]
        [@param network.ip.netmask: string]
        [@param network.display: boolean]
        [@param network.stp: boolean]
        [@param network.mtu: int]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Network:
        '''

        url = '/api/networks'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(network),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})
        return Network(result)

    def get(self, name='*', **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param name: string (the name of the entity)]

        @return Networks:
        '''

        url = '/api/networks'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return Network(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']), headers={}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=url,
                                          headers={}).get_network()
            if name != '*': kwargs['name']=name
            return Network(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return Networks:
        '''

        url='/api/networks'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'max:matrix':max}),
                                      headers={}).get_network()
        return ParseHelper.toCollection(Network,
                                        FilterHelper.filter(result, kwargs))

class Role(params.Role, Base):
    def __init__(self, role):
        self.superclass = role

        self.permits = RolePermits(self)

    def __new__(cls, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(role)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/roles/{role:id}',
                                {'{role:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def update(self, correlation_id=None):
        '''
        [@param role.permits.permit: collection]
        {
          [@ivar permit.id: string]
        }
        [@param role.description: string]
        [@param correlation_id: any string]

        @return Role:
        '''

        url = '/api/roles/{role:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{role:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return Role(result)

class RolePermit(params.Permit, Base):
    def __init__(self, role, permit):
        self.parentclass = role
        self.superclass  =  permit

        #SUB_COLLECTIONS
    def __new__(cls, role, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(role, permit)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/roles/{role:id}/permits/{permit:id}',
                                {'{role:id}' : self.parentclass.get_id(),
                                 '{permit:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class RolePermits(Base):

    def __init__(self, role):
        self.parentclass = role

    def add(self, permit, expect=None, correlation_id=None):

        '''
        @type Permit:

        @param permit.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permit:
        '''

        url = '/api/roles/{role:id}/permits'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{role:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permit),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return RolePermit(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permits:
        '''

        url = '/api/roles/{role:id}/permits'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{role:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return RolePermit(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{role:id}': self.parentclass.get_id()}),
                                          headers={}).get_permit()

            return RolePermit(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permits:
        '''

        url = '/api/roles/{role:id}/permits'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{role:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permit()
        return ParseHelper.toSubCollection(RolePermit,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Roles(Base):
    def __init__(self):
        """Constructor."""

    def add(self, role, expect=None, correlation_id=None):
        '''
        @type Role:

        @param role.name: string
        @param role.permits.permit: collection
        {
          @ivar permit.id: string
        }
        [@param role.description: string]
        [@param role.administrative: boolean]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Role:
        '''

        url = '/api/roles'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(role),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})
        return Role(result)

    def get(self, name='*', **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param name: string (the name of the entity)]

        @return Roles:
        '''

        url = '/api/roles'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return Role(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']), headers={}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=url,
                                          headers={}).get_role()
            if name != '*': kwargs['name']=name
            return Role(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return Roles:
        '''

        url='/api/roles'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'max:matrix':max}),
                                      headers={}).get_role()
        return ParseHelper.toCollection(Role,
                                        FilterHelper.filter(result, kwargs))

class StorageDomain(params.StorageDomain, Base):
    def __init__(self, storagedomain):
        self.superclass = storagedomain

        self.files = StorageDomainFiles(self)
        self.templates = StorageDomainTemplates(self)
        self.vms = StorageDomainVMs(self)
        self.permissions = StorageDomainPermissions(self)

    def __new__(cls, storagedomain):
        if storagedomain is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain)
        return obj

    def delete(self, storagedomain=params.StorageDomain(), async=None, correlation_id=None):
        '''
        @type StorageDomain:

        @param storagedomain.host.id|name: string
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/storagedomains/{storagedomain:id}',
                                {'{storagedomain:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       body=ParseHelper.toXml(storagedomain),
                                       headers={"Correlation-Id":correlation_id})

    def update(self, correlation_id=None):
        '''
        [@param storagedomain.name: string]
        [@param correlation_id: any string]

        @return StorageDomain:
        '''

        url = '/api/storagedomains/{storagedomain:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{storagedomain:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return StorageDomain(result)

class StorageDomainFile(params.File, Base):
    def __init__(self, storagedomain, file):
        self.parentclass = storagedomain
        self.superclass  =  file

        #SUB_COLLECTIONS
    def __new__(cls, storagedomain, file):
        if file is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, file)
        return obj

class StorageDomainFiles(Base):

    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Files:
        '''

        url = '/api/storagedomains/{storagedomain:id}/files'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return StorageDomainFile(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                          headers={}).get_file()

            return StorageDomainFile(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Files:
        '''

        url = '/api/storagedomains/{storagedomain:id}/files'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{storagedomain:id}': self.parentclass.get_id()}),
                                                                   qargs={'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={}).get_file()
        return ParseHelper.toSubCollection(StorageDomainFile,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomainPermission(params.Permission, Base):
    def __init__(self, storagedomain, permission):
        self.parentclass = storagedomain
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, storagedomain, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, permission)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/storagedomains/{storagedomain:id}/permissions/{permission:id}',
                                {'{storagedomain:id}' : self.parentclass.get_id(),
                                 '{permission:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class StorageDomainPermissions(Base):

    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.role.id: string
          @param permission.group.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return StorageDomainPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return StorageDomainPermission(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                          headers={}).get_permission()

            return StorageDomainPermission(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{storagedomain:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permission()
        return ParseHelper.toSubCollection(StorageDomainPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomainTemplate(params.Template, Base):
    def __init__(self, storagedomain, template):
        self.parentclass = storagedomain
        self.superclass  =  template

        #SUB_COLLECTIONS
    def __new__(cls, storagedomain, template):
        if template is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, template)
        return obj

    def import_template(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.cluster.id|name: string
        [@param action.storage_domain.id|name: string]
        [@param action.clone: boolen]
        [@param action.template.name: string]
        [@param action.vm.disks.disk: collection]
        {
          [@ivar disk.id: string]
        }
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/storagedomains/{storagedomain:id}/templates/{template:id}/import'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{storagedomain:id}' : self.parentclass.get_id(),
                                                                     '{template:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

class StorageDomainTemplates(Base):

    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Templates:
        '''

        url = '/api/storagedomains/{storagedomain:id}/templates'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return StorageDomainTemplate(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                          headers={}).get_template()

            return StorageDomainTemplate(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Templates:
        '''

        url = '/api/storagedomains/{storagedomain:id}/templates'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{storagedomain:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_template()
        return ParseHelper.toSubCollection(StorageDomainTemplate,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomainVM(params.VM, Base):
    def __init__(self, storagedomain, vm):
        self.parentclass = storagedomain
        self.superclass  =  vm

        #SUB_COLLECTIONS
    def __new__(cls, storagedomain, vm):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, vm)
        return obj

    def import_vm(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.cluster.id|name: string
        [@param action.storage_domain.id|name: string]
        [@param action.vm.snapshots.collapse_snapshots: boolean]
        [@param action.clone: boolen]
        [@param action.vm.name: string]
        [@param action.vm.disks.disk: collection]
        {
          [@ivar disk.id: string]
        }
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/storagedomains/{storagedomain:id}/vms/{vm:id}/import'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{storagedomain:id}' : self.parentclass.get_id(),
                                                                     '{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})

        return result

class StorageDomainVMs(Base):

    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return VMs:
        '''

        url = '/api/storagedomains/{storagedomain:id}/vms'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return StorageDomainVM(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                          headers={}).get_vm()

            return StorageDomainVM(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return VMs:
        '''

        url = '/api/storagedomains/{storagedomain:id}/vms'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{storagedomain:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_vm()
        return ParseHelper.toSubCollection(StorageDomainVM,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StorageDomains(Base):
    def __init__(self):
        """Constructor."""

    def add(self, storagedomain, expect=None, correlation_id=None):
        '''
        @type StorageDomain:

        Overload 1:
          @param storagedomain.host.id|name: string
          @param storagedomain.type: string
          @param storagedomain.storage.type: string
          @param storagedomain.format: boolean
          @param storagedomain.storage.address: string
          @param storagedomain.storage.logical_unit: collection
          {
            @ivar logical_unit.address: string
            @ivar logical_unit.port: int
            @ivar logical_unit.target: string
            @ivar logical_unit.username: string
            @ivar logical_unit.password: string
            @ivar logical_unit.serial: string
            @ivar logical_unit.vendor_id: string
            @ivar logical_unit.product_id: string
            @ivar logical_unit.lun_mapping: int
            @ivar logical_unit.portal: string
            @ivar logical_unit.paths: int
            @ivar logical_unit.id: string
          }
          [@param storagedomain.name: string]
          [@param storagedomain.storage.override_luns: boolean]
        Overload 2:
          @param storagedomain.host.id|name: string
          @param storagedomain.type: string
          @param storagedomain.storage.type: string
          @param storagedomain.format: boolean
          @param storagedomain.storage.address: string
          @param storagedomain.storage.path: string
          [@param storagedomain.name: string]
        Overload 3:
          @param storagedomain.host.id|name: string
          @param storagedomain.type: string
          @param storagedomain.storage.type: string
          @param storagedomain.format: boolean
          @param storagedomain.storage.path: string
          [@param storagedomain.name: string]
        Overload 4:
          @param storagedomain.host.id|name: string
          @param storagedomain.type: string
          @param storagedomain.storage.type: string
          @param storagedomain.format: boolean
          @param storagedomain.storage.path: string
          @param storagedomain.storage.vfs_type: string
          [@param storagedomain.name: string]
          [@param storagedomain.storage.address: string]
          [@param storagedomain.storage.mount_options: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return StorageDomain:
        '''

        url = '/api/storagedomains'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(storagedomain),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})
        return StorageDomain(result)

    def get(self, name='name', filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]
        [@param filter: true|false]

        @return StorageDomains:
        '''

        url = '/api/storagedomains'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return StorageDomain(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={"Filter":filter}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={"Filter":filter}).get_storage_domain()
            return StorageDomain(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param filter: true|false]

        @return StorageDomains:
        '''

        url='/api/storagedomains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={"Filter":filter}).get_storage_domain()
        return ParseHelper.toCollection(StorageDomain,
                                        FilterHelper.filter(result, kwargs))

class Tag(params.Tag, Base):
    def __init__(self, tag):
        self.superclass = tag

        #SUB_COLLECTIONS
    def __new__(cls, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(tag)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/tags/{tag:id}',
                                {'{tag:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def update(self, correlation_id=None):
        '''
        [@param tag.name: string]
        [@param tag.description: string]
        [@param tag.parent.name: string]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/api/tags/{tag:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{tag:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return Tag(result)

class Tags(Base):
    def __init__(self):
        """Constructor."""

    def add(self, tag, correlation_id=None):
        '''
        @type Tag:

        @param tag.name: string
        [@param tag.description: string]
        [@param tag.parent.name: string]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/api/tags'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(tag),
                                      headers={"Correlation-Id":correlation_id})
        return Tag(result)

    def get(self, name='*', **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/api/tags'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return Tag(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']), headers={}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=url,
                                          headers={}).get_tag()
            if name != '*': kwargs['name']=name
            return Tag(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return Tags:
        '''

        url='/api/tags'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'max:matrix':max}),
                                      headers={}).get_tag()
        return ParseHelper.toCollection(Tag,
                                        FilterHelper.filter(result, kwargs))

class Template(params.Template, Base):
    def __init__(self, template):
        self.superclass = template

        self.nics = TemplateNics(self)
        self.cdroms = TemplateCdRoms(self)
        self.disks = TemplateDisks(self)
        self.permissions = TemplatePermissions(self)

    def __new__(cls, template):
        if template is None: return None
        obj = object.__new__(cls)
        obj.__init__(template)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/templates/{template:id}',
                                {'{template:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def export(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.storage_domain.id|name: string
        [@param action.async: boolean]
        [@param action.exclusive: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/templates/{template:id}/export'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{template:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def update(self, correlation_id=None):
        '''
        [@param template.name: string]
        [@param template.memory: long]
        [@param template.cpu.topology.cores: int]
        [@param template.high_availability.enabled: boolean]
        [@param template.os.cmdline: string]
        [@param template.origin: string]
        [@param template.high_availability.priority: int]
        [@param template.timezone: string]
        [@param template.domain.name: string]
        [@param template.type: string]
        [@param template.stateless: boolean]
        [@param template.placement_policy.affinity: string]
        [@param template.description: string]
        [@param template.custom_properties.custom_property: collection]
        {
          [@ivar custom_property.name: string]
          [@ivar custom_property.value: string]
        }
        [@param template.os.type: string]
        [@param template.os.boot: collection]
        {
          [@ivar boot.dev: string]
        }
        [@param template.cpu.topology.sockets: int]
        [@param template.os.kernel: string]
        [@param template.display.type: string]
        [@param template.display.monitors: int]
        [@param template.display.allow_reconnect: boolean]
        [@param template.os.initRd: string]
        [@param template.usb.enabled: boolean]
        [@param template.usb.type: string]
        [@param correlation_id: any string]

        @return Template:
        '''

        url = '/api/templates/{template:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{template:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return Template(result)

class TemplateCdRom(params.CdRom, Base):
    def __init__(self, template, cdrom):
        self.parentclass = template
        self.superclass  =  cdrom

        #SUB_COLLECTIONS
    def __new__(cls, template, cdrom):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, cdrom)
        return obj

class TemplateCdRoms(Base):

    def __init__(self, template):
        self.parentclass = template

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return CdRoms:
        '''

        url = '/api/templates/{template:id}/cdroms'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return TemplateCdRom(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                          headers={}).get_cdrom()

            return TemplateCdRom(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return CdRoms:
        '''

        url = '/api/templates/{template:id}/cdroms'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{template:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_cdrom()
        return ParseHelper.toSubCollection(TemplateCdRom,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplateDisk(params.Disk, Base):
    def __init__(self, template, disk):
        self.parentclass = template
        self.superclass  =  disk

        #SUB_COLLECTIONS
    def __new__(cls, template, disk):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, disk)
        return obj

    def delete(self, action, async=None, correlation_id=None):
        '''
        @type Action:

        [@param action.storage_domain.id: string]
        [@param action.force: boolean]
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/templates/{template:id}/disks/{disk:id}',
                                {'{template:id}' : self.parentclass.get_id(),
                                 '{disk:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       body=ParseHelper.toXml(action),
                                       headers={"Correlation-Id":correlation_id})

class TemplateDisks(Base):

    def __init__(self, template):
        self.parentclass = template

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Disks:
        '''

        url = '/api/templates/{template:id}/disks'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return TemplateDisk(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                          headers={}).get_disk()

            return TemplateDisk(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Disks:
        '''

        url = '/api/templates/{template:id}/disks'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{template:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_disk()
        return ParseHelper.toSubCollection(TemplateDisk,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplateNic(params.NIC, Base):
    def __init__(self, template, nic):
        self.parentclass = template
        self.superclass  =  nic

        #SUB_COLLECTIONS
    def __new__(cls, template, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, nic)
        return obj

class TemplateNics(Base):

    def __init__(self, template):
        self.parentclass = template

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Nics:
        '''

        url = '/api/templates/{template:id}/nics'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return TemplateNic(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                          headers={}).get_nic()

            return TemplateNic(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Nics:
        '''

        url = '/api/templates/{template:id}/nics'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{template:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_nic()
        return ParseHelper.toSubCollection(TemplateNic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplatePermission(params.Permission, Base):
    def __init__(self, template, permission):
        self.parentclass = template
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, template, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, permission)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/templates/{template:id}/permissions/{permission:id}',
                                {'{template:id}' : self.parentclass.get_id(),
                                 '{permission:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class TemplatePermissions(Base):

    def __init__(self, template):
        self.parentclass = template

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.role.id: string
          @param permission.group.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/api/templates/{template:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return TemplatePermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/api/templates/{template:id}/permissions'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return TemplatePermission(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                          headers={}).get_permission()

            return TemplatePermission(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/api/templates/{template:id}/permissions'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{template:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permission()
        return ParseHelper.toSubCollection(TemplatePermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Templates(Base):
    def __init__(self):
        """Constructor."""

    def add(self, template, expect=None, correlation_id=None):
        '''
        @type Template:

        @param template.vm.id|name: string
        @param template.name: string
        [@param template.memory: long]
        [@param template.cpu.topology.cores: int]
        [@param template.high_availability.enabled: boolean]
        [@param template.os.cmdline: string]
        [@param template.origin: string]
        [@param template.high_availability.priority: int]
        [@param template.timezone: string]
        [@param template.domain.name: string]
        [@param template.type: string]
        [@param template.stateless: boolean]
        [@param template.placement_policy.affinity: string]
        [@param template.description: string]
        [@param template.custom_properties.custom_property: collection]
        {
          [@ivar custom_property.name: string]
          [@ivar custom_property.value: string]
        }
        [@param template.os.type: string]
        [@param template.os.boot: collection]
        {
          [@ivar boot.dev: string]
        }
        [@param template.cpu.topology.sockets: int]
        [@param template.os.kernel: string]
        [@param template.display.type: string]
        [@param template.display.monitors: int]
        [@param template.display.allow_reconnect: boolean]
        [@param template.os.initRd: string]
        [@param template.usb.enabled: boolean]
        [@param template.usb.type: string]
        [@param template.vm.disks.disk: collection]
        {
          [@ivar disk.id: string]
          [@ivar storage_domains.storage_domain: collection]
          {
            [@param storage_domain.id: string]
          }
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Template:
        '''

        url = '/api/templates'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(template),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})
        return Template(result)

    def get(self, name='name', filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]
        [@param filter: true|false]

        @return Templates:
        '''

        url = '/api/templates'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return Template(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={"Filter":filter}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={"Filter":filter}).get_template()
            return Template(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param filter: true|false]

        @return Templates:
        '''

        url='/api/templates'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={"Filter":filter}).get_template()
        return ParseHelper.toCollection(Template,
                                        FilterHelper.filter(result, kwargs))

class User(params.User, Base):
    def __init__(self, user):
        self.superclass = user

        self.permissions = UserPermissions(self)
        self.roles = UserRoles(self)
        self.tags = UserTags(self)

    def __new__(cls, user):
        if user is None: return None
        obj = object.__new__(cls)
        obj.__init__(user)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/users/{user:id}',
                                {'{user:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class UserPermission(params.Permission, Base):
    def __init__(self, user, permission):
        self.parentclass = user
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, user, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, permission)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/users/{user:id}/permissions/{permission:id}',
                                {'{user:id}' : self.parentclass.get_id(),
                                 '{permission:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class UserPermissions(Base):

    def __init__(self, user):
        self.parentclass = user

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.role.id: string
          @param permission.data_center.id: string
        Overload 2:
          @param permission.role.id: string
          @param permission.cluster.id: string
        Overload 3:
          @param permission.role.id: string
          @param permission.host.id: string
        Overload 4:
          @param permission.role.id: string
          @param permission.storage_domain.id: string
        Overload 5:
          @param permission.role.id: string
          @param permission.vm.id: string
        Overload 6:
          @param permission.role.id: string
          @param permission.vmpool.id: string
        Overload 7:
          @param permission.role.id: string
          @param permission.template.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/api/users/{user:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return UserPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/api/users/{user:id}/permissions'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return UserPermission(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                          headers={}).get_permission()

            return UserPermission(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/api/users/{user:id}/permissions'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{user:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permission()
        return ParseHelper.toSubCollection(UserPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UserRole(params.Role, Base):
    def __init__(self, user, role):
        self.parentclass = user
        self.superclass  =  role

        self.permits = UserRolePermits(self)

    def __new__(cls, user, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, role)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/users/{user:id}/roles/{role:id}',
                                {'{user:id}' : self.parentclass.get_id(),
                                 '{role:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class UserRolePermit(params.Permit, Base):
    def __init__(self, userrole, permit):
        self.parentclass = userrole
        self.superclass  =  permit

        #SUB_COLLECTIONS
    def __new__(cls, userrole, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(userrole, permit)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/users/{user:id}/roles/{role:id}/permits/{permit:id}',
                                {'{user:id}' : self.parentclass.parentclass.get_id(),
                                 '{role:id}': self.parentclass.get_id(),
                                 '{permit:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class UserRolePermits(Base):

    def __init__(self, userrole):
        self.parentclass = userrole

    def add(self, permit, expect=None, correlation_id=None):

        '''
        @type Permit:

        @param permit.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permit:
        '''

        url = '/api/users/{user:id}/roles/{role:id}/permits'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.parentclass.get_id(),
                                                                  '{role:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permit),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return UserRolePermit(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permits:
        '''

        url = '/api/users/{user:id}/roles/{role:id}/permits'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{user:id}' : self.parentclass.parentclass.get_id(),
                                                                                           '{role:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return UserRolePermit(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.parentclass.get_id(),
                                                                      '{role:id}': self.parentclass.get_id()}),
                                          headers={}).get_permit()

            return UserRolePermit(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permits:
        '''

        url = '/api/users/{user:id}/roles/{role:id}/permits'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{user:id}' : self.parentclass.parentclass.get_id(),
                                                                                               '{role:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permit()
        return ParseHelper.toSubCollection(UserRolePermit,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UserRoles(Base):

    def __init__(self, user):
        self.parentclass = user

    def add(self, role, expect=None, correlation_id=None):

        '''
        @type Role:

        @param role.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Role:
        '''

        url = '/api/users/{user:id}/roles'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(role),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return UserRole(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Roles:
        '''

        url = '/api/users/{user:id}/roles'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return UserRole(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                          headers={}).get_role()

            return UserRole(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Roles:
        '''

        url = '/api/users/{user:id}/roles'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{user:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_role()
        return ParseHelper.toSubCollection(UserRole,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UserTag(params.Tag, Base):
    def __init__(self, user, tag):
        self.parentclass = user
        self.superclass  =  tag

        #SUB_COLLECTIONS
    def __new__(cls, user, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, tag)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/users/{user:id}/tags/{tag:id}',
                                {'{user:id}' : self.parentclass.get_id(),
                                 '{tag:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class UserTags(Base):

    def __init__(self, user):
        self.parentclass = user

    def add(self, tag, expect=None, correlation_id=None):

        '''
        @type Tag:

        @param tag.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/api/users/{user:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return UserTag(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/api/users/{user:id}/tags'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return UserTag(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                          headers={}).get_tag()

            return UserTag(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Tags:
        '''

        url = '/api/users/{user:id}/tags'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{user:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_tag()
        return ParseHelper.toSubCollection(UserTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Users(Base):
    def __init__(self):
        """Constructor."""

    def add(self, user, expect=None, correlation_id=None):
        '''
        @type User:

        @param user.user_name: string
        @param user.domain.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return User:
        '''

        url = '/api/users'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(user),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})
        return User(result)

    def get(self, name='name', **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]

        @return Users:
        '''

        url = '/api/users'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return User(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={}).get_user()
            return User(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Users:
        '''

        url='/api/users'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={}).get_user()
        return ParseHelper.toCollection(User,
                                        FilterHelper.filter(result, kwargs))

class VM(params.VM, Base):
    def __init__(self, vm):
        self.superclass = vm

        self.cdroms = VMCdRoms(self)
        self.statistics = VMStatistics(self)
        self.tags = VMTags(self)
        self.nics = VMNics(self)
        self.disks = VMDisks(self)
        self.snapshots = VMSnapshots(self)
        self.permissions = VMPermissions(self)

    def __new__(cls, vm):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm)
        return obj

    def delete(self, action=params.Action(), async=None, correlation_id=None):
        '''
        @type Action:

        [@param action.force: boolean]
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/vms/{vm:id}',
                                {'{vm:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       body=ParseHelper.toXml(action),
                                       headers={"Correlation-Id":correlation_id})

    def shutdown(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/vms/{vm:id}/shutdown'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def start(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.vm.os.initRd: string]
        [@param action.vm.domain.name: string]
        [@param action.vm.placement_policy.host.id|name: string]
        [@param action.vm.placement_policy.affinity: string]
        [@param action.async: boolean]
        [@param action.vm.os.kernel: string]
        [@param action.grace_period.expiry: long]
        [@param action.vm.display.type: string]
        [@param action.vm.stateless: boolean]
        [@param action.vm.os.cmdline: string]
        [@param action.vm.domain.user.username: string]
        [@param action.pause: boolean]
        [@param action.vm.os.boot: collection]
        {
          [@ivar boot.dev: string]
        }
        [@param action.vm.domain.user.password: string]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/vms/{vm:id}/start'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def stop(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/vms/{vm:id}/stop'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def suspend(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/vms/{vm:id}/suspend'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def export(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.exclusive: boolean]
        [@param action.discard_snapshots: boolean]
        [@param action.storage_domain.id|name: string]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/vms/{vm:id}/export'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def detach(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/vms/{vm:id}/detach'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def move(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.storage_domain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/vms/{vm:id}/move'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def ticket(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/vms/{vm:id}/ticket'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def migrate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.host.id|name: string]
        [@param action.async: boolean]
        [@param action.force: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Response:
        '''

        url = '/api/vms/{vm:id}/migrate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={"Correlation-Id":correlation_id})
        return result

    def cancelmigration(self, action=params.Action()):
        '''
        @type Action:


        @return Response:
        '''

        url = '/api/vms/{vm:id}/cancelmigration'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={})
        return result

    def update(self, correlation_id=None):
        '''
        [@param vm.name: string]
        [@param vm.cluster.id|name: string]
        [@param vm.timezone: string]
        [@param vm.os.boot: collection]
        {
          [@ivar boot.dev: string]
        }
        [@param vm.custom_properties.custom_property: collection]
        {
          [@ivar custom_property.name: string]
          [@ivar custom_property.value: string]
        }
        [@param vm.os.type: string]
        [@param vm.usb.enabled: boolean]
        [@param vm.usb.type: string]
        [@param vm.type: string]
        [@param vm.os.initRd: string]
        [@param vm.display.monitors: int]
        [@param vm.display.type: string]
        [@param vm.display.allow_reconnect: boolean]
        [@param vm.os.cmdline: string]
        [@param vm.cpu.topology.cores: int]
        [@param vm.memory: long]
        [@param vm.high_availability.priority: int]
        [@param vm.high_availability.enabled: boolean]
        [@param vm.domain.name: string]
        [@param vm.description: string]
        [@param vm.stateless: boolean]
        [@param vm.cpu.topology.sockets: int]
        [@param vm.placement_policy.affinity: string]
        [@param vm.placement_policy.host.id|name: string]
        [@param vm.origin: string]
        [@param vm.os.kernel: string]
        [@param vm.payloads.payload: collection]
        {
          [@ivar payload.type: string]
          [@ivar payload.file.name: string]
          [@ivar payload.file.content: string]
        }
        [@param vm.cpu.cpu_tune.vcpu_pin: collection]
        {
          [@ivar vcpu_pin.vcpu: int]
          [@ivar vcpu_pin.cpu_set: string]
        }
        [@param correlation_id: any string]

        @return VM:
        '''

        url = '/api/vms/{vm:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return VM(result)

class VMCdRom(params.CdRom, Base):
    def __init__(self, vm, cdrom):
        self.parentclass = vm
        self.superclass  =  cdrom

        #SUB_COLLECTIONS
    def __new__(cls, vm, cdrom):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, cdrom)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/vms/{vm:id}/cdroms/{cdrom:id}',
                                {'{vm:id}' : self.parentclass.get_id(),
                                 '{cdrom:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def update(self, correlation_id=None):
        '''
        [@param cdrom.file.id: string]
        [@param correlation_id: any string]

        @return CdRom:
        '''

        url = '/api/vms/{vm:id}/cdroms/{cdrom:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{cdrom:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})

        return VMCdRom(self.parentclass, result)

class VMCdRoms(Base):

    def __init__(self, vm):
        self.parentclass = vm

    def add(self, cdrom, expect=None, correlation_id=None):

        '''
        @type CdRom:

        @param cdrom.file.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return CdRom:
        '''

        url = '/api/vms/{vm:id}/cdroms'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(cdrom),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return VMCdRom(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return CdRoms:
        '''

        url = '/api/vms/{vm:id}/cdroms'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMCdRom(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                          headers={}).get_cdrom()

            return VMCdRom(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return CdRoms:
        '''

        url = '/api/vms/{vm:id}/cdroms'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{vm:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_cdrom()
        return ParseHelper.toSubCollection(VMCdRom,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMDisk(params.Disk, Base):
    def __init__(self, vm, disk):
        self.parentclass = vm
        self.superclass  =  disk

        self.statistics = VMDiskStatistics(self)

    def __new__(cls, vm, disk):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, disk)
        return obj

    def delete(self, action, async=None, correlation_id=None):
        '''
        @type Action:

        @param action.detach: boolean
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/vms/{vm:id}/disks/{disk:id}',
                                {'{vm:id}' : self.parentclass.get_id(),
                                 '{disk:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       body=ParseHelper.toXml(action),
                                       headers={"Correlation-Id":correlation_id})

    def activate(self, action=params.Action()):
        '''
        @type Action:


        @return Response:
        '''

        url = '/api/vms/{vm:id}/disks/{disk:id}/activate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{disk:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={})

        return result

    def deactivate(self, action=params.Action()):
        '''
        @type Action:


        @return Response:
        '''

        url = '/api/vms/{vm:id}/disks/{disk:id}/deactivate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{disk:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={})

        return result

    def update(self, correlation_id=None):
        '''
        [@param size: int]
        [@param provisioned_size: int]
        [@param disk.interface: string]
        [@param disk.format: string]
        [@param disk.sparse: boolean]
        [@param disk.bootable: boolean]
        [@param disk.shareable: boolean]
        [@param disk.propagate_errors: boolean]
        [@param disk.wipe_after_delete: boolean]
        [@param correlation_id: any string]

        @return Disk:
        '''

        url = '/api/vms/{vm:id}/disks/{disk:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{disk:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})

        return VMDisk(self.parentclass, result)

class VMDiskStatistic(params.Statistic, Base):
    def __init__(self, vmdisk, statistic):
        self.parentclass = vmdisk
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, vmdisk, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmdisk, statistic)
        return obj

class VMDiskStatistics(Base):

    def __init__(self, vmdisk):
        self.parentclass = vmdisk

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/api/vms/{vm:id}/disks/{disk:id}/statistics'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                                           '{disk:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMDiskStatistic(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                      '{disk:id}': self.parentclass.get_id()}),
                                          headers={}).get_statistic()

            return VMDiskStatistic(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Statistics:
        '''

        url = '/api/vms/{vm:id}/disks/{disk:id}/statistics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                  '{disk:id}': self.parentclass.get_id()})).get_statistic()

        return ParseHelper.toSubCollection(VMDiskStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMDisks(Base):

    def __init__(self, vm):
        self.parentclass = vm

    def add(self, disk, expect=None, correlation_id=None):

        '''
        @type Disk:

        Overload 1:
          @param provisioned_size: int
          @param disk.interface: string
          @param disk.format: string
          [@param disk.size: int]
          [@param disk.sparse: boolean]
          [@param disk.bootable: boolean]
          [@param disk.shareable: boolean]
          [@param disk.propagate_errors: boolean]
          [@param disk.wipe_after_delete: boolean]
          [@param disk.storage_domains.storage_domain: collection]
          {
            [@ivar storage_domain.id|name: string]
          }
        Overload 2:
          @param disk.id: string
          [@param disk.active: boolean]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Disk:
        '''

        url = '/api/vms/{vm:id}/disks'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(disk),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return VMDisk(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Disks:
        '''

        url = '/api/vms/{vm:id}/disks'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMDisk(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                          headers={}).get_disk()

            return VMDisk(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Disks:
        '''

        url = '/api/vms/{vm:id}/disks'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{vm:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_disk()
        return ParseHelper.toSubCollection(VMDisk,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMNic(params.NIC, Base):
    def __init__(self, vm, nic):
        self.parentclass = vm
        self.superclass  =  nic

        self.statistics = VMNicStatistics(self)

    def __new__(cls, vm, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, nic)
        return obj

    def update(self, correlation_id=None):
        '''
        [@param nic.network.id|name: string]
        [@param nic.name: string]
        [@param nic.mac.address: string]
        [@param nic.interface: string]
        [@param nic.port_mirroring.networks.network: collection]
        {
          [@ivar network.id: string]
        }
        [@param correlation_id: any string]

        @return NIC:
        '''

        url = '/api/vms/{vm:id}/nics/{nic:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})

        return VMNic(self.parentclass, result)

    def activate(self, action=params.Action()):
        '''
        @type Action:


        @return Response:
        '''

        url = '/api/vms/{vm:id}/nics/{nic:id}/activate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={})

        return result

    def deactivate(self, action=params.Action()):
        '''
        @type Action:


        @return Response:
        '''

        url = '/api/vms/{vm:id}/nics/{nic:id}/deactivate'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={})

        return result

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/vms/{vm:id}/nics/{nic:id}',
                                {'{vm:id}' : self.parentclass.get_id(),
                                 '{nic:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class VMNicStatistic(params.Statistic, Base):
    def __init__(self, vmnic, statistic):
        self.parentclass = vmnic
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, vmnic, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmnic, statistic)
        return obj

class VMNicStatistics(Base):

    def __init__(self, vmnic):
        self.parentclass = vmnic

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/api/vms/{vm:id}/nics/{nic:id}/statistics'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                                           '{nic:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMNicStatistic(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                      '{nic:id}': self.parentclass.get_id()}),
                                          headers={}).get_statistic()

            return VMNicStatistic(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Statistics:
        '''

        url = '/api/vms/{vm:id}/nics/{nic:id}/statistics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                  '{nic:id}': self.parentclass.get_id()})).get_statistic()

        return ParseHelper.toSubCollection(VMNicStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMNics(Base):

    def __init__(self, vm):
        self.parentclass = vm

    def add(self, nic, expect=None, correlation_id=None):

        '''
        @type NIC:

        @param nic.network.id|name: string
        @param nic.name: string
        [@param nic.mac.address: string]
        [@param nic.interface: string]
        [@param nic.port_mirroring.networks.network: collection]
        {
          [@ivar network.id: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return NIC:
        '''

        url = '/api/vms/{vm:id}/nics'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(nic),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return VMNic(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Nics:
        '''

        url = '/api/vms/{vm:id}/nics'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMNic(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                          headers={}).get_nic()

            return VMNic(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Nics:
        '''

        url = '/api/vms/{vm:id}/nics'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{vm:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_nic()
        return ParseHelper.toSubCollection(VMNic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMPermission(params.Permission, Base):
    def __init__(self, vm, permission):
        self.parentclass = vm
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, vm, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, permission)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/vms/{vm:id}/permissions/{permission:id}',
                                {'{vm:id}' : self.parentclass.get_id(),
                                 '{permission:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class VMPermissions(Base):

    def __init__(self, vm):
        self.parentclass = vm

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.role.id: string
          @param permission.group.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/api/vms/{vm:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return VMPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/api/vms/{vm:id}/permissions'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMPermission(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                          headers={}).get_permission()

            return VMPermission(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/api/vms/{vm:id}/permissions'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{vm:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permission()
        return ParseHelper.toSubCollection(VMPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMSnapshot(params.Snapshot, Base):
    def __init__(self, vm, snapshot):
        self.parentclass = vm
        self.superclass  =  snapshot

        self.nics = VMSnapshotNics(self)
        self.cdroms = VMSnapshotCdroms(self)
        self.disks = VMSnapshotDisks(self)

    def __new__(cls, vm, snapshot):
        if snapshot is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, snapshot)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/vms/{vm:id}/snapshots/{snapshot:id}',
                                {'{vm:id}' : self.parentclass.get_id(),
                                 '{snapshot:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def restore(self, action=params.Action()):
        '''
        @type Action:


        @return Response:
        '''

        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}/restore'

        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{snapshot:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action),
                                          headers={})

        return result

class VMSnapshotCdrom(params.CdRom, Base):
    def __init__(self, vmsnapshot, cdrom):
        self.parentclass = vmsnapshot
        self.superclass  =  cdrom

        #SUB_COLLECTIONS
    def __new__(cls, vmsnapshot, cdrom):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmsnapshot, cdrom)
        return obj

class VMSnapshotCdroms(Base):

    def __init__(self, vmsnapshot):
        self.parentclass = vmsnapshot

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return CdRoms:
        '''

        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}/cdroms'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                                           '{snapshot:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMSnapshotCdrom(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                      '{snapshot:id}': self.parentclass.get_id()}),
                                          headers={}).get_cdrom()

            return VMSnapshotCdrom(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return CdRoms:
        '''

        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}/cdroms'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                  '{snapshot:id}': self.parentclass.get_id()})).get_cdrom()

        return ParseHelper.toSubCollection(VMSnapshotCdrom,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMSnapshotDisk(params.Disk, Base):
    def __init__(self, vmsnapshot, disk):
        self.parentclass = vmsnapshot
        self.superclass  =  disk

        #SUB_COLLECTIONS
    def __new__(cls, vmsnapshot, disk):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmsnapshot, disk)
        return obj

class VMSnapshotDisks(Base):

    def __init__(self, vmsnapshot):
        self.parentclass = vmsnapshot

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Disks:
        '''

        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}/disks'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                                           '{snapshot:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMSnapshotDisk(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                      '{snapshot:id}': self.parentclass.get_id()}),
                                          headers={}).get_disk()

            return VMSnapshotDisk(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Disks:
        '''

        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}/disks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                  '{snapshot:id}': self.parentclass.get_id()})).get_disk()

        return ParseHelper.toSubCollection(VMSnapshotDisk,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMSnapshotNic(params.NIC, Base):
    def __init__(self, vmsnapshot, nic):
        self.parentclass = vmsnapshot
        self.superclass  =  nic

        #SUB_COLLECTIONS
    def __new__(cls, vmsnapshot, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmsnapshot, nic)
        return obj

class VMSnapshotNics(Base):

    def __init__(self, vmsnapshot):
        self.parentclass = vmsnapshot

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Nics:
        '''

        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}/nics'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                                           '{snapshot:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMSnapshotNic(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                      '{snapshot:id}': self.parentclass.get_id()}),
                                          headers={}).get_nic()

            return VMSnapshotNic(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Nics:
        '''

        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}/nics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.parentclass.get_id(),
                                                                  '{snapshot:id}': self.parentclass.get_id()})).get_nic()

        return ParseHelper.toSubCollection(VMSnapshotNic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMSnapshots(Base):

    def __init__(self, vm):
        self.parentclass = vm

    def add(self, snapshot, expect=None, correlation_id=None):

        '''
        @type Snapshot:

        @param snapshot.description: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Snapshot:
        '''

        url = '/api/vms/{vm:id}/snapshots'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(snapshot),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return VMSnapshot(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Snapshots:
        '''

        url = '/api/vms/{vm:id}/snapshots'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMSnapshot(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                          headers={}).get_snapshot()

            return VMSnapshot(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Snapshots:
        '''

        url = '/api/vms/{vm:id}/snapshots'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{vm:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_snapshot()
        return ParseHelper.toSubCollection(VMSnapshot,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMStatistic(params.Statistic, Base):
    def __init__(self, vm, statistic):
        self.parentclass = vm
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, vm, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, statistic)
        return obj

class VMStatistics(Base):

    def __init__(self, vm):
        self.parentclass = vm

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/api/vms/{vm:id}/statistics'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMStatistic(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                          headers={}).get_statistic()

            return VMStatistic(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Statistics:
        '''

        url = '/api/vms/{vm:id}/statistics'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{vm:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_statistic()
        return ParseHelper.toSubCollection(VMStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMTag(params.Tag, Base):
    def __init__(self, vm, tag):
        self.parentclass = vm
        self.superclass  =  tag

        #SUB_COLLECTIONS
    def __new__(cls, vm, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, tag)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/vms/{vm:id}/tags/{tag:id}',
                                {'{vm:id}' : self.parentclass.get_id(),
                                 '{tag:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class VMTags(Base):

    def __init__(self, vm):
        self.parentclass = vm

    def add(self, tag, expect=None, correlation_id=None):

        '''
        @type Tag:

        @param tag.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/api/vms/{vm:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return VMTag(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/api/vms/{vm:id}/tags'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VMTag(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                          headers={}).get_tag()

            return VMTag(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Tags:
        '''

        url = '/api/vms/{vm:id}/tags'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{vm:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_tag()
        return ParseHelper.toSubCollection(VMTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VMs(Base):
    def __init__(self):
        """Constructor."""

    def add(self, vm, correlation_id=None, expect=None):
        '''
        @type VM:

        @param vm.name: string
        @param vm.template.id|name: string
        @param vm.cluster.id|name: string
        [@param vm.quota.id: string]
        [@param vm.timezone: string]
        [@param vm.os.boot: collection]
        {
          [@ivar boot.dev: string]
        }
        [@param vm.custom_properties.custom_property: collection]
        {
          [@ivar custom_property.name: string]
          [@ivar custom_property.value: string]
        }
        [@param vm.os.type: string]
        [@param vm.usb.enabled: boolean]
        [@param vm.usb.type: string]
        [@param vm.type: string]
        [@param vm.os.initRd: string]
        [@param vm.display.monitors: int]
        [@param vm.display.type: string]
        [@param vm.display.allow_reconnect: boolean]
        [@param vm.os.cmdline: string]
        [@param vm.cpu.topology.cores: int]
        [@param vm.memory: long]
        [@param vm.high_availability.priority: int]
        [@param vm.high_availability.enabled: boolean]
        [@param vm.domain.name: string]
        [@param vm.description: string]
        [@param vm.stateless: boolean]
        [@param vm.cpu.topology.sockets: int]
        [@param vm.placement_policy.affinity: string]
        [@param vm.placement_policy.host.id|name: string]
        [@param vm.origin: string]
        [@param vm.os.kernel: string]
        [@param vm.disks.clone: boolean]
        [@param vm.payloads.payload: collection]
        {
          [@ivar payload.type: string]
          [@ivar payload.file.name: string]
          [@ivar payload.file.content: string]
        }
        [@param correlation_id: any string]
        [@param expect: 201-created]

        @return VM:
        '''

        url = '/api/vms'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(vm),
                                      headers={"Correlation-Id":correlation_id, "Expect":expect})
        return VM(result)

    def get(self, name='name', filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]
        [@param filter: true|false]

        @return VMs:
        '''

        url = '/api/vms'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return VM(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={"Filter":filter}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={"Filter":filter}).get_vm()
            return VM(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param filter: true|false]

        @return VMs:
        '''

        url='/api/vms'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={"Filter":filter}).get_vm()
        return ParseHelper.toCollection(VM,
                                        FilterHelper.filter(result, kwargs))

class VersionCaps(params.VersionCaps, Base):
    def __init__(self, versioncaps):
        self.superclass = versioncaps

        #SUB_COLLECTIONS
    def __new__(cls, versioncaps):
        if versioncaps is None: return None
        obj = object.__new__(cls)
        obj.__init__(versioncaps)
        return obj

class VmPool(params.VmPool, Base):
    def __init__(self, vmpool):
        self.superclass = vmpool

        self.permissions = VmPoolPermissions(self)

    def __new__(cls, vmpool):
        if vmpool is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmpool)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/vmpools/{vmpool:id}',
                                {'{vmpool:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

    def update(self, correlation_id=None):
        '''
        [@param vmpool.cluster.id|name: string]
        [@param vmpool.template.id|name: string]
        [@param vmpool.name: string]
        [@param correlation_id: any string]

        @return VmPool:
        '''

        url = '/api/vmpools/{vmpool:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vmpool:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass),
                                         headers={"Correlation-Id":correlation_id})
        return VmPool(result)

class VmPoolPermission(params.Permission, Base):
    def __init__(self, vmpool, permission):
        self.parentclass = vmpool
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, vmpool, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmpool, permission)
        return obj

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace('/api/vmpools/{vmpool:id}/permissions/{permission:id}',
                                {'{vmpool:id}' : self.parentclass.get_id(),
                                 '{permission:id}': self.get_id()})

        return self._getProxy().delete(url=SearchHelper.appendQuery(url, {'async:matrix':async}),
                                       headers={"Correlation-Id":correlation_id,"Content-type":None})

class VmPoolPermissions(Base):

    def __init__(self, vmpool):
        self.parentclass = vmpool

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.role.id: string
          @param permission.group.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/api/vmpools/{vmpool:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vmpool:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})

        return VmPoolPermission(self.parentclass, result)

    def get(self, name=None, **kwargs):

        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/api/vmpools/{vmpool:id}/permissions'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                result = self._getProxy().get(url=UrlHelper.append(UrlHelper.replace(url, {'{vmpool:id}': self.parentclass.get_id()}),
                                                                   kwargs['id']),
                                              headers={})
                return VmPoolPermission(self.parentclass, result)
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            if(name is not None): kwargs['name']=name
            result = self._getProxy().get(url=UrlHelper.replace(url, {'{vmpool:id}': self.parentclass.get_id()}),
                                          headers={}).get_permission()

            return VmPoolPermission(self.parentclass, FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/api/vmpools/{vmpool:id}/permissions'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url=UrlHelper.replace(url=url,
                                                                                         args={'{vmpool:id}': self.parentclass.get_id()}),
                                                                   qargs={'max:matrix':max}),
                                      headers={}).get_permission()
        return ParseHelper.toSubCollection(VmPoolPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VmPools(Base):
    def __init__(self):
        """Constructor."""

    def add(self, vmpool, expect=None, correlation_id=None):
        '''
        @type VmPool:

        @param vmpool.cluster.id|name: string
        @param vmpool.template.id|name: string
        @param vmpool.name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return VmPool:
        '''

        url = '/api/vmpools'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(vmpool),
                                      headers={"Expect":expect, "Correlation-Id":correlation_id})
        return VmPool(result)

    def get(self, name='name', filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param name: string (string the name of the entity)]
        [@param filter: true|false]

        @return VmPools:
        '''

        url = '/api/vmpools'

        if kwargs and kwargs.has_key('id') and kwargs['id'] <> None:
            try :
                return VmPool(self._getProxy().get(url=UrlHelper.append(url, kwargs['id']),
                                                              headers={"Filter":filter}))
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        else:
            result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search':'name='+name}),
                                          headers={"Filter":filter}).get_vmpool()
            return VmPool(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, case_sensitive=True, max=None, filter=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param filter: true|false]

        @return VmPools:
        '''

        url='/api/vmpools'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
                                      headers={"Filter":filter}).get_vmpool()
        return ParseHelper.toCollection(VmPool,
                                        FilterHelper.filter(result, kwargs))

