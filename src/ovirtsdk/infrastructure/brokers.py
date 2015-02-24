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

'''Generated at: 2015-02-24 15:32:06.000878'''


from ovirtsdk.xml import params
from ovirtsdk.utils.urlhelper import UrlHelper
from ovirtsdk.utils.filterhelper import FilterHelper
from ovirtsdk.utils.parsehelper import ParseHelper
from ovirtsdk.utils.searchhelper import SearchHelper
from ovirtsdk.infrastructure.common import Base
from ovirtsdk.infrastructure.context import context
from ovirtsdk.infrastructure.errors import MissingParametersError
from ovirtsdk.infrastructure.errors import DisconnectedError
from ovirtsdk.infrastructure.errors import RequestError


class Bookmark(params.Bookmark, Base):
    def __init__(self, bookmark, context):
        Base.__init__(self, context)
        self.superclass = bookmark

        #SUB_COLLECTIONS
    def __new__(cls, bookmark, context):
        if bookmark is None: return None
        obj = object.__new__(cls)
        obj.__init__(bookmark, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/bookmarks/{bookmark:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{bookmark:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def update(self):
        '''
        @return Bookmark:
        '''

        url = '/bookmarks/{bookmark:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{bookmark:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={}
        )

        return Bookmark(result, self.context)

class Bookmarks(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, bookmark):
        '''
        @type Bookmark:

        @param bookmark.name: string
        @param bookmark.value: string

        @return Bookmark:
        '''

        url = '/bookmarks'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(bookmark),
           headers={}
        )

        return Bookmark(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Bookmarks:
        '''

        url = '/bookmarks'

        if id:
            try :
                return Bookmark(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_bookmark()

            return Bookmark(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]

        @return Bookmarks:
        '''

        url='/bookmarks'

        result = self.__getProxy().get(
            url=url
        ).get_bookmark()

        return ParseHelper.toCollection(
            Bookmark,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )
class Capabilities(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError


    def get(self, id=None, **kwargs):
        '''
        [@param id: string (the id of the entity)]
        [@param **kwargs: dict (property based filtering)]

        @return VersionCaps:
        '''

        url = '/capabilities'

        if id:
            try :
                return VersionCaps(
                    self.__getProxy().get(url=UrlHelper.append(url, id)),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif kwargs:
            result = self.__getProxy().get(url=url).version

            return VersionCaps(
                FilterHelper.getItem(FilterHelper.filter(result, kwargs)),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'kwargs'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return [VersionCaps]:
        '''

        url='/capabilities'

        result = self.__getProxy().get(url=url).version

        return ParseHelper.toCollection(
            VersionCaps,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )
class Capability(params.VersionCaps, Base):
    def __init__(self, versioncaps, context):
        Base.__init__(self, context)
        self.superclass = versioncaps

        #SUB_COLLECTIONS
    def __new__(cls, versioncaps, context):
        if versioncaps is None: return None
        obj = object.__new__(cls)
        obj.__init__(versioncaps, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class Cluster(params.Cluster, Base):
    def __init__(self, cluster, context):
        Base.__init__(self, context)
        self.superclass = cluster

        self.affinitygroups = ClusterAffinitygroups(self, context)
        self.cpuprofiles = ClusterCpuprofiles(self, context)
        self.glusterhooks = ClusterGlusterhooks(self, context)
        self.glustervolumes = ClusterGlustervolumes(self, context)
        self.networks = ClusterNetworks(self, context)
        self.permissions = ClusterPermissions(self, context)

    def __new__(cls, cluster, context):
        if cluster is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/clusters/{cluster:id}',
            {
                '{cluster:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param cluster.name: string]
        [@param cluster.description: string]
        [@param cluster.comment: string]
        [@param cluster.data_center.id: string]
        [@param cluster.cpu.id: string]
        [@param cluster.version.major: int]
        [@param cluster.version.minor: int]
        [@param cluster.memory_policy.overcommit.percent: double]
        [@param cluster.memory_policy.transparent_hugepages.enabled: boolean]
        [@param cluster.scheduling_policy.policy: string]
        [@param cluster.scheduling_policy.thresholds.low: int]
        [@param cluster.scheduling_policy.thresholds.high: int]
        [@param cluster.scheduling_policy.thresholds.duration: int]
        [@param cluster.scheduling_policy.id: string]
        [@param cluster.scheduling_policy.properties.property: collection]
        {
          [@ivar property.name: string]
          [@ivar property.value: string]
        }
        [@param cluster.error_handling.on_error: string]
        [@param cluster.virt_service: boolean]
        [@param cluster.gluster_service: boolean]
        [@param cluster.threads_as_cores: boolean]
        [@param cluster.tunnel_migration: boolean]
        [@param cluster.ballooning_enabled: boolean]
        [@param cluster.cpu.architecture: string]
        [@param cluster.display.proxy: string]
        [@param cluster.ksm.enabled: boolean]
        [@param cluster.fencing_policy.enabled: boolean]
        [@param cluster.fencing_policy.skip_if_sd_active.enabled: boolean]
        [@param cluster.fencing_policy.skip_if_connectivity_broken.enabled: boolean]
        [@param cluster.fencing_policy.skip_if_connectivity_broken.threshold: int]
        [@param correlation_id: any string]

        @return Cluster:
        '''

        url = '/clusters/{cluster:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Cluster(result, self.context)

class ClusterAffinitygroup(params.AffinityGroup, Base):
    def __init__(self, cluster, affinitygroup, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  affinitygroup

        self.vms = ClusterAffinitygroupVms(self, context)

    def __new__(cls, cluster, affinitygroup, context):
        if affinitygroup is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, affinitygroup, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{affinitygroup:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def update(self):
        '''
        [@param affinitygroup.name: string]
        [@param affinitygroup.positive: boolean]
        [@param affinitygroup.enforcing: boolean]

        @return AffinityGroup:
        '''

        url = '/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}'
        url = UrlHelper.replace(
            url,
            {
                '{cluster:id}': self.parentclass.get_id(),
                '{affinitygroup:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={}
        )

        return ClusterAffinitygroup(
            self.parentclass,
            result,
            self.context
        )

class ClusterAffinitygroupVm(params.VM, Base):
    def __init__(self, affinitygroup, vm, context):
        Base.__init__(self, context)
        self.parentclass = affinitygroup
        self.superclass  =  vm

        #SUB_COLLECTIONS
    def __new__(cls, affinitygroup, vm, context):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(affinitygroup, vm, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}/vms/{vm:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{affinitygroup:id}': self.parentclass.get_id(),
                    '{vm:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class ClusterAffinitygroupVms(Base):

    def __init__(self, affinitygroup , context):
        Base.__init__(self, context)
        self.parentclass = affinitygroup

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, vm, expect=None):

        '''
        @type VM:

        @param vm.id|name: string
        [@param expect: 201-created]

        @return VM:
        '''

        url = '/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}/vms'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{affinitygroup:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(vm),
            headers={"Expect":expect}
        )

        return ClusterAffinitygroupVm(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return VMs:
        '''

        url = '/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}/vms'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cluster:id}': self.parentclass.parentclass.get_id(),
                                '{affinitygroup:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ClusterAffinitygroupVm(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cluster:id}': self.parentclass.parentclass.get_id(),
                        '{affinitygroup:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_vm()

            return ClusterAffinitygroupVm(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return VMs:
        '''

        url = '/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}/vms'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{cluster:id}': self.parentclass.parentclass.get_id(),
                        '{affinitygroup:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_vm()

        return ParseHelper.toSubCollection(
            ClusterAffinitygroupVm,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ClusterAffinitygroups(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, affinitygroup, expect=None):

        '''
        @type AffinityGroup:

        @param affinitygroup.name: string
        @param affinitygroup.positive: boolean
        @param affinitygroup.enforcing: boolean
        [@param expect: 201-created]

        @return AffinityGroup:
        '''

        url = '/clusters/{cluster:id}/affinitygroups'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(affinitygroup),
            headers={"Expect":expect}
        )

        return ClusterAffinitygroup(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return AffinityGroups:
        '''

        url = '/clusters/{cluster:id}/affinitygroups'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ClusterAffinitygroup(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_affinity_group()

            return ClusterAffinitygroup(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return AffinityGroups:
        '''

        url = '/clusters/{cluster:id}/affinitygroups'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_affinity_group()

        return ParseHelper.toSubCollection(
            ClusterAffinitygroup,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ClusterCpuprofile(params.CpuProfile, Base):
    def __init__(self, cluster, cpuprofile, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  cpuprofile

        #SUB_COLLECTIONS
    def __new__(cls, cluster, cpuprofile, context):
        if cpuprofile is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, cpuprofile, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/clusters/{cluster:id}/cpuprofiles/{cpuprofile:id}',
            {
                '{cluster:id}': self.parentclass.get_id(),
                '{cpuprofile:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class ClusterCpuprofiles(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, cpuprofile, expect=None, correlation_id=None):

        '''
        @type CpuProfile:

        @param cpuprofile.name: string
        [@param cpuprofile.description: string]
        [@param cpuprofile.qos.id: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return CpuProfile:
        '''

        url = '/clusters/{cluster:id}/cpuprofiles'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(cpuprofile),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return ClusterCpuprofile(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return CpuProfiles:
        '''

        url = '/clusters/{cluster:id}/cpuprofiles'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ClusterCpuprofile(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_cpu_profile()

            return ClusterCpuprofile(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return CpuProfiles:
        '''

        url = '/clusters/{cluster:id}/cpuprofiles'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_cpu_profile()

        return ParseHelper.toSubCollection(
            ClusterCpuprofile,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ClusterGlusterhook(params.GlusterHook, Base):
    def __init__(self, cluster, glusterhook, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  glusterhook

        #SUB_COLLECTIONS
    def __new__(cls, cluster, glusterhook, context):
        if glusterhook is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, glusterhook, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/clusters/{cluster:id}/glusterhooks/{glusterhook:id}',
            {
                '{cluster:id}': self.parentclass.get_id(),
                '{glusterhook:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def disable(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glusterhooks/{glusterhook:id}/disable'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glusterhook:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def enable(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glusterhooks/{glusterhook:id}/enable'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glusterhook:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def resolve(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.resolution_type: string
        [@param action.host.id|name: string]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glusterhooks/{glusterhook:id}/resolve'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glusterhook:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class ClusterGlusterhooks(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return GlusterHooks:
        '''

        url = '/clusters/{cluster:id}/glusterhooks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ClusterGlusterhook(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_gluster_hook()

            return ClusterGlusterhook(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return GlusterHooks:
        '''

        url = '/clusters/{cluster:id}/glusterhooks'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                }
            )
        ).get_gluster_hook()

        return ParseHelper.toSubCollection(
            ClusterGlusterhook,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ClusterGlustervolume(params.GlusterVolume, Base):
    def __init__(self, cluster, glustervolume, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  glustervolume

        self.bricks = ClusterGlustervolumeBricks(self, context)
        self.statistics = ClusterGlustervolumeStatistics(self, context)

    def __new__(cls, cluster, glustervolume, context):
        if glustervolume is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, glustervolume, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def activate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.bricks: collection
        {
          @ivar brick.name: string
        }
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/activate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def migrate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.bricks: collection
        {
          @ivar brick.name: string
        }
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/migrate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def stopmigrate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.bricks: collection
        {
          @ivar brick.name: string
        }
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/stopmigrate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def rebalance(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.fix_layout: boolean]
        [@param action.force: boolean]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/rebalance'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def resetalloptions(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/resetalloptions'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def resetoption(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.option.name: string
        @param action.force: boolean
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/resetoption'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def setoption(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.option.name: string
        @param action.option.value: string
        @param action.async: boolean
        @param action.grace_period.expiry: long
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/setoption'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def start(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.force: boolean]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/start'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def startprofile(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/startprofile'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def stop(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.force: boolean]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/stop'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def stopprofile(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/stopprofile'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def stoprebalance(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/stoprebalance'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class ClusterGlustervolumeBrick(params.GlusterBrick, Base):
    def __init__(self, glustervolume, glusterbrick, context):
        Base.__init__(self, context)
        self.parentclass = glustervolume
        self.superclass  =  glusterbrick

        self.statistics = ClusterGlustervolumeBrickStatistics(self, context)

    def __new__(cls, glustervolume, glusterbrick, context):
        if glusterbrick is None: return None
        obj = object.__new__(cls)
        obj.__init__(glustervolume, glusterbrick, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{glustervolume:id}': self.parentclass.get_id(),
                    '{brick:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def replace(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.brick.server_id: string
        @param action.brick.brick_dir: string
        [@param action.force: boolean]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}/replace'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{glustervolume:id}': self.parentclass.get_id(),
                    '{brick:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class ClusterGlustervolumeBrickStatistic(params.Statistic, Base):
    def __init__(self, glusterbrick, statistic, context):
        Base.__init__(self, context)
        self.parentclass = glusterbrick
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, glusterbrick, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(glusterbrick, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class ClusterGlustervolumeBrickStatistics(Base):

    def __init__(self, glusterbrick , context):
        Base.__init__(self, context)
        self.parentclass = glusterbrick

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cluster:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{glustervolume:id}': self.parentclass.parentclass.get_id(),
                                '{brick:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ClusterGlustervolumeBrickStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cluster:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{glustervolume:id}': self.parentclass.parentclass.get_id(),
                        '{brick:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return ClusterGlustervolumeBrickStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Statistics:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}/statistics'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{cluster:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{glustervolume:id}': self.parentclass.parentclass.get_id(),
                        '{brick:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_statistic()

        return ParseHelper.toSubCollection(
            ClusterGlustervolumeBrickStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ClusterGlustervolumeBricks(Base):

    def __init__(self, glustervolume , context):
        Base.__init__(self, context)
        self.parentclass = glustervolume

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, brick, expect=None, correlation_id=None):

        '''
        @type GlusterBricks:

        @param brick: collection
        {
          @ivar brick.server_id: string
          @ivar brick.brick_dir: string
        }
        [@param replica_count: unsignedShort]
        [@param stripe_count: unsignedShort]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return GlusterBricks:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{glustervolume:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(brick),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return ClusterGlustervolumeBrick(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, all_content=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]
        [@param all_content: true|false]

        @return GlusterBricks:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cluster:id}': self.parentclass.parentclass.get_id(),
                                '{glustervolume:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={"All-Content":all_content}
                )

                return ClusterGlustervolumeBrick(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cluster:id}': self.parentclass.parentclass.get_id(),
                        '{glustervolume:id}': self.parentclass.get_id(),
                    }
                ),
                headers={"All-Content":all_content}
            ).get_brick()

            return ClusterGlustervolumeBrick(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, all_content=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param all_content: true|false]

        @return GlusterBricks:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{cluster:id}': self.parentclass.parentclass.get_id(),
                        '{glustervolume:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={}
            ),
            headers={"All-Content":all_content}
        ).get_brick()

        return ParseHelper.toSubCollection(
            ClusterGlustervolumeBrick,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ClusterGlustervolumeStatistic(params.Statistic, Base):
    def __init__(self, glustervolume, statistic, context):
        Base.__init__(self, context)
        self.parentclass = glustervolume
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, glustervolume, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(glustervolume, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class ClusterGlustervolumeStatistics(Base):

    def __init__(self, glustervolume , context):
        Base.__init__(self, context)
        self.parentclass = glustervolume

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cluster:id}': self.parentclass.parentclass.get_id(),
                                '{glustervolume:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ClusterGlustervolumeStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cluster:id}': self.parentclass.parentclass.get_id(),
                        '{glustervolume:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return ClusterGlustervolumeStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Statistics:
        '''

        url = '/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/statistics'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{glustervolume:id}': self.parentclass.get_id(),
                }
            )
        ).get_statistic()

        return ParseHelper.toSubCollection(
            ClusterGlustervolumeStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ClusterGlustervolumes(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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
        [@param gluster_volume.options.option: collection]
        {
          [@ivar option.name: string]
          [@ivar option.value: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return GlusterVolume:
        '''

        url = '/clusters/{cluster:id}/glustervolumes'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(glustervolume),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return ClusterGlustervolume(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return GlusterVolumes:
        '''

        url = '/clusters/{cluster:id}/glustervolumes'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ClusterGlustervolume(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_gluster_volume()

            return ClusterGlustervolume(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]

        @return GlusterVolumes:
        '''

        url = '/clusters/{cluster:id}/glustervolumes'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'search:query':query,'case_sensitive:matrix':case_sensitive}
            ),
            headers={}
        ).get_gluster_volume()

        return ParseHelper.toSubCollection(
            ClusterGlustervolume,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ClusterNetwork(params.Network, Base):
    def __init__(self, cluster, network, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  network

        #SUB_COLLECTIONS
    def __new__(cls, cluster, network, context):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, network, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/clusters/{cluster:id}/networks/{network:id}',
            {
                '{cluster:id}': self.parentclass.get_id(),
                '{network:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

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

        url = '/clusters/{cluster:id}/networks/{network:id}'
        url = UrlHelper.replace(
            url,
            {
                '{cluster:id}': self.parentclass.get_id(),
                '{network:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return ClusterNetwork(
            self.parentclass,
            result,
            self.context
        )

class ClusterNetworks(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, network, expect=None, correlation_id=None):

        '''
        @type Network:

        @param network.id|name: string
        [@param network.usages.usage: collection]
        {
          [@ivar usage: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Network:
        '''

        url = '/clusters/{cluster:id}/networks'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(network),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return ClusterNetwork(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Networks:
        '''

        url = '/clusters/{cluster:id}/networks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ClusterNetwork(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_network()

            return ClusterNetwork(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Networks:
        '''

        url = '/clusters/{cluster:id}/networks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_network()

        return ParseHelper.toSubCollection(
            ClusterNetwork,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ClusterPermission(params.Permission, Base):
    def __init__(self, cluster, permission, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, cluster, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/clusters/{cluster:id}/permissions/{permission:id}',
            {
                '{cluster:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class ClusterPermissions(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/clusters/{cluster:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{cluster:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return ClusterPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/clusters/{cluster:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ClusterPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return ClusterPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/clusters/{cluster:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            ClusterPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Clusters(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, cluster, expect=None, correlation_id=None):
        '''
        @type Cluster:

        @param cluster.data_center.id|name: string
        @param cluster.name: string
        @param cluster.version.major: int
        @param cluster.version.minor: int
        @param cluster.cpu.id: string
        [@param cluster.description: string]
        [@param cluster.comment: string]
        [@param cluster.memory_policy.overcommit.percent: double]
        [@param cluster.memory_policy.transparent_hugepages.enabled: boolean]
        [@param cluster.scheduling_policy.policy: string]
        [@param cluster.scheduling_policy.thresholds.low: int]
        [@param cluster.scheduling_policy.thresholds.high: int]
        [@param cluster.scheduling_policy.thresholds.duration: int]
        [@param cluster.scheduling_policy.id: string]
        [@param cluster.scheduling_policy.properties.property: collection]
        {
          [@ivar property.name: string]
          [@ivar property.value: string]
        }
        [@param cluster.error_handling.on_error: string]
        [@param cluster.virt_service: boolean]
        [@param cluster.gluster_service: boolean]
        [@param cluster.threads_as_cores: boolean]
        [@param cluster.tunnel_migration: boolean]
        [@param cluster.trusted_service: boolean]
        [@param cluster.ha_reservation: boolean]
        [@param cluster.ballooning_enabled: boolean]
        [@param cluster.cpu.architecture: string]
        [@param cluster.display.proxy: string]
        [@param cluster.ksm.enabled: boolean]
        [@param cluster.fencing_policy.enabled: boolean]
        [@param cluster.fencing_policy.skip_if_sd_active.enabled: boolean]
        [@param cluster.fencing_policy.skip_if_connectivity_broken.enabled: boolean]
        [@param cluster.fencing_policy.skip_if_connectivity_broken.threshold: int]
        [@param cluster.management_network.id|name: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Cluster:
        '''

        url = '/clusters'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(cluster),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Cluster(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Clusters:
        '''

        url = '/clusters'

        if id:
            try :
                return Cluster(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={}
            ).get_cluster()

            return Cluster(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Clusters:
        '''

        url='/clusters'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={}
        ).get_cluster()

        return ParseHelper.toCollection(
            Cluster,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Cpuprofile(params.CpuProfile, Base):
    def __init__(self, cpuprofile, context):
        Base.__init__(self, context)
        self.superclass = cpuprofile

        self.permissions = CpuprofilePermissions(self, context)

    def __new__(cls, cpuprofile, context):
        if cpuprofile is None: return None
        obj = object.__new__(cls)
        obj.__init__(cpuprofile, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/cpuprofiles/{cpuprofile:id}',
            {
                '{cpuprofile:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param cpuprofile.name: string]
        [@param cpuprofile.description: string]
        [@param cpuprofile.qos.id: string]
        [@param correlation_id: any string]

        @return CpuProfile:
        '''

        url = '/cpuprofiles/{cpuprofile:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{cpuprofile:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Cpuprofile(result, self.context)

class CpuprofilePermission(params.Permission, Base):
    def __init__(self, cpuprofile, permission, context):
        Base.__init__(self, context)
        self.parentclass = cpuprofile
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, cpuprofile, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(cpuprofile, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/cpuprofiles/{cpuprofile:id}/permissions/{permission:id}',
            {
                '{cpuprofile:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class CpuprofilePermissions(Base):

    def __init__(self, cpuprofile , context):
        Base.__init__(self, context)
        self.parentclass = cpuprofile

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.group.id: string
          @param permission.role.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/cpuprofiles/{cpuprofile:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{cpuprofile:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return CpuprofilePermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/cpuprofiles/{cpuprofile:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{cpuprofile:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return CpuprofilePermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{cpuprofile:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return CpuprofilePermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/cpuprofiles/{cpuprofile:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{cpuprofile:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            CpuprofilePermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Cpuprofiles(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, cpuprofile, expect=None, correlation_id=None):
        '''
        @type CpuProfile:

        @param cpuprofile.cluster.id: string
        @param cpuprofile.name: string
        [@param cpuprofile.description: string]
        [@param cpuprofile.qos.id: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return CpuProfile:
        '''

        url = '/cpuprofiles'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(cpuprofile),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Cpuprofile(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return CpuProfiles:
        '''

        url = '/cpuprofiles'

        if id:
            try :
                return Cpuprofile(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_cpu_profile()

            return Cpuprofile(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return CpuProfiles:
        '''

        url='/cpuprofiles'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_cpu_profile()

        return ParseHelper.toCollection(
            Cpuprofile,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Datacenter(params.DataCenter, Base):
    def __init__(self, datacenter, context):
        Base.__init__(self, context)
        self.superclass = datacenter

        self.clusters = DatacenterClusters(self, context)
        self.iscsibonds = DatacenterIscsibonds(self, context)
        self.networks = DatacenterNetworks(self, context)
        self.permissions = DatacenterPermissions(self, context)
        self.qoss = DatacenterQoss(self, context)
        self.quotas = DatacenterQuotas(self, context)
        self.storagedomains = DatacenterStoragedomains(self, context)

    def __new__(cls, datacenter, context):
        if datacenter is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, action=params.Action(), async=None, correlation_id=None):
        '''
        @type Action:

        [@param action.force: boolean]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/datacenters/{datacenter:id}',
            {
                '{datacenter:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

    def update(self, correlation_id=None):
        '''
        [@param datacenter.name: string]
        [@param datacenter.description: string]
        [@param datacenter.comment: string]
        [@param datacenter.storage_type: string]
        [@param datacenter.local: boolean]
        [@param datacenter.version.major: int]
        [@param datacenter.version.minor: int]
        [@param datacenter.storage_format: string]
        [@param datacenter.mac_pool.id: string]
        [@param correlation_id: any string]

        @return DataCenter:
        '''

        url = '/datacenters/{datacenter:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Datacenter(result, self.context)

class DatacenterCluster(params.Cluster, Base):
    def __init__(self, datacenter, cluster, context):
        Base.__init__(self, context)
        self.parentclass = datacenter
        self.superclass  =  cluster

        self.affinitygroups = DatacenterClusterAffinitygroups(self, context)
        self.cpuprofiles = DatacenterClusterCpuprofiles(self, context)
        self.glusterhooks = DatacenterClusterGlusterhooks(self, context)
        self.glustervolumes = DatacenterClusterGlustervolumes(self, context)
        self.networks = DatacenterClusterNetworks(self, context)
        self.permissions = DatacenterClusterPermissions(self, context)

    def __new__(cls, datacenter, cluster, context):
        if cluster is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, cluster, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/datacenters/{datacenter:id}/clusters/{cluster:id}',
            {
                '{datacenter:id}': self.parentclass.get_id(),
                '{cluster:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

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
        [@param cluster.scheduling_policy.id: string]
        [@param cluster.scheduling_policy.properties.property: collection]
        {
          [@ivar property.name: string]
          [@ivar property.value: string]
        }
        [@param cluster.error_handling.on_error: string]
        [@param cluster.virt_service: boolean]
        [@param cluster.gluster_service: boolean]
        [@param cluster.threads_as_cores: boolean]
        [@param cluster.tunnel_migration: boolean]
        [@param cluster.trusted_service: boolean]
        [@param cluster.ha_reservation: boolean]
        [@param cluster.ballooning_enabled: boolean]
        [@param cluster.cpu.architecture: string]
        [@param cluster.display.proxy: string]
        [@param cluster.ksm.enabled: boolean]
        [@param correlation_id: any string]

        @return Cluster:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}'
        url = UrlHelper.replace(
            url,
            {
                '{datacenter:id}': self.parentclass.get_id(),
                '{cluster:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return DatacenterCluster(
            self.parentclass,
            result,
            self.context
        )

class DatacenterClusterAffinitygroup(params.AffinityGroup, Base):
    def __init__(self, cluster, affinitygroup, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  affinitygroup

        self.vms = DatacenterClusterAffinitygroupVms(self, context)

    def __new__(cls, cluster, affinitygroup, context):
        if affinitygroup is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, affinitygroup, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{affinitygroup:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def update(self):
        '''
        @return AffinityGroup:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}'
        url = UrlHelper.replace(
            url,
            {
                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                '{cluster:id}': self.parentclass.get_id(),
                '{affinitygroup:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={}
        )

        return DatacenterClusterAffinitygroup(
            self.parentclass,
            result,
            self.context
        )

class DatacenterClusterAffinitygroupVm(params.VM, Base):
    def __init__(self, affinitygroup, vm, context):
        Base.__init__(self, context)
        self.parentclass = affinitygroup
        self.superclass  =  vm

        #SUB_COLLECTIONS
    def __new__(cls, affinitygroup, vm, context):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(affinitygroup, vm, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}/vms/{vm:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{affinitygroup:id}': self.parentclass.get_id(),
                    '{vm:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DatacenterClusterAffinitygroupVms(Base):

    def __init__(self, affinitygroup , context):
        Base.__init__(self, context)
        self.parentclass = affinitygroup

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, vm):

        '''
        @type VM:


        @return VM:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}/vms'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{affinitygroup:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(vm),
            headers={}
        )

        return DatacenterClusterAffinitygroupVm(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return VMs:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}/vms'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{cluster:id}': self.parentclass.parentclass.get_id(),
                                '{affinitygroup:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterClusterAffinitygroupVm(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.parentclass.get_id(),
                        '{affinitygroup:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_vm()

            return DatacenterClusterAffinitygroupVm(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return VMs:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/affinitygroups/{affinitygroup:id}/vms'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{affinitygroup:id}': self.parentclass.get_id(),
                }
            )
        ).get_vm()

        return ParseHelper.toSubCollection(
            DatacenterClusterAffinitygroupVm,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterClusterAffinitygroups(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, affinitygroup):

        '''
        @type AffinityGroup:


        @return AffinityGroup:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/affinitygroups'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(affinitygroup),
            headers={}
        )

        return DatacenterClusterAffinitygroup(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return AffinityGroups:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/affinitygroups'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterClusterAffinitygroup(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_affinity_group()

            return DatacenterClusterAffinitygroup(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return AffinityGroups:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/affinitygroups'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                }
            )
        ).get_affinity_group()

        return ParseHelper.toSubCollection(
            DatacenterClusterAffinitygroup,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterClusterCpuprofile(params.CpuProfile, Base):
    def __init__(self, cluster, cpuprofile, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  cpuprofile

        #SUB_COLLECTIONS
    def __new__(cls, cluster, cpuprofile, context):
        if cpuprofile is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, cpuprofile, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/cpuprofiles/{cpuprofile:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{cpuprofile:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DatacenterClusterCpuprofiles(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, cpuprofile):

        '''
        @type CpuProfile:


        @return CpuProfile:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/cpuprofiles'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(cpuprofile),
            headers={}
        )

        return DatacenterClusterCpuprofile(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return CpuProfiles:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/cpuprofiles'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterClusterCpuprofile(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_cpu_profile()

            return DatacenterClusterCpuprofile(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return CpuProfiles:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/cpuprofiles'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                }
            )
        ).get_cpu_profile()

        return ParseHelper.toSubCollection(
            DatacenterClusterCpuprofile,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterClusterGlusterhook(params.GlusterHook, Base):
    def __init__(self, cluster, glusterhook, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  glusterhook

        #SUB_COLLECTIONS
    def __new__(cls, cluster, glusterhook, context):
        if glusterhook is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, glusterhook, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glusterhooks/{glusterhook:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glusterhook:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def disable(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glusterhooks/{glusterhook:id}/disable'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glusterhook:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def enable(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glusterhooks/{glusterhook:id}/enable'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glusterhook:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def resolve(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glusterhooks/{glusterhook:id}/resolve'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glusterhook:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

class DatacenterClusterGlusterhooks(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return GlusterHooks:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glusterhooks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterClusterGlusterhook(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_gluster_hook()

            return DatacenterClusterGlusterhook(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return GlusterHooks:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glusterhooks'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                }
            )
        ).get_gluster_hook()

        return ParseHelper.toSubCollection(
            DatacenterClusterGlusterhook,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterClusterGlustervolume(params.GlusterVolume, Base):
    def __init__(self, cluster, glustervolume, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  glustervolume

        self.bricks = DatacenterClusterGlustervolumeBricks(self, context)
        self.statistics = DatacenterClusterGlustervolumeStatistics(self, context)

    def __new__(cls, cluster, glustervolume, context):
        if glustervolume is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, glustervolume, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def activate(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/activate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def migrate(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/migrate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def stopmigrate(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/stopmigrate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def rebalance(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/rebalance'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def resetalloptions(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/resetalloptions'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def resetoption(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/resetoption'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def setoption(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/setoption'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def start(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/start'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def startprofile(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/startprofile'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def stop(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/stop'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def stopprofile(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/stopprofile'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def stoprebalance(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/stoprebalance'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                    '{glustervolume:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

class DatacenterClusterGlustervolumeBrick(params.GlusterBrick, Base):
    def __init__(self, glustervolume, glusterbrick, context):
        Base.__init__(self, context)
        self.parentclass = glustervolume
        self.superclass  =  glusterbrick

        self.statistics = DatacenterClusterGlustervolumeBrickStatistics(self, context)

    def __new__(cls, glustervolume, glusterbrick, context):
        if glusterbrick is None: return None
        obj = object.__new__(cls)
        obj.__init__(glustervolume, glusterbrick, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{glustervolume:id}': self.parentclass.get_id(),
                    '{brick:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def replace(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}/replace'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{glustervolume:id}': self.parentclass.get_id(),
                    '{brick:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

class DatacenterClusterGlustervolumeBrickStatistic(params.Statistic, Base):
    def __init__(self, glusterbrick, statistic, context):
        Base.__init__(self, context)
        self.parentclass = glusterbrick
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, glusterbrick, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(glusterbrick, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class DatacenterClusterGlustervolumeBrickStatistics(Base):

    def __init__(self, glusterbrick , context):
        Base.__init__(self, context)
        self.parentclass = glusterbrick

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.parentclass.get_id(),
                                '{cluster:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{glustervolume:id}': self.parentclass.parentclass.get_id(),
                                '{brick:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterClusterGlustervolumeBrickStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{glustervolume:id}': self.parentclass.parentclass.get_id(),
                        '{brick:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return DatacenterClusterGlustervolumeBrickStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Statistics:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks/{brick:id}/statistics'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{glustervolume:id}': self.parentclass.parentclass.get_id(),
                    '{brick:id}': self.parentclass.get_id(),
                }
            )
        ).get_statistic()

        return ParseHelper.toSubCollection(
            DatacenterClusterGlustervolumeBrickStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterClusterGlustervolumeBricks(Base):

    def __init__(self, glustervolume , context):
        Base.__init__(self, context)
        self.parentclass = glustervolume

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, brick):

        '''
        @type GlusterBricks:


        @return GlusterBricks:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{glustervolume:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(brick),
            headers={}
        )

        return DatacenterClusterGlustervolumeBrick(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return GlusterBricks:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{cluster:id}': self.parentclass.parentclass.get_id(),
                                '{glustervolume:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterClusterGlustervolumeBrick(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.parentclass.get_id(),
                        '{glustervolume:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_brick()

            return DatacenterClusterGlustervolumeBrick(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return GlusterBricks:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/bricks'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{glustervolume:id}': self.parentclass.get_id(),
                }
            )
        ).get_brick()

        return ParseHelper.toSubCollection(
            DatacenterClusterGlustervolumeBrick,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterClusterGlustervolumeStatistic(params.Statistic, Base):
    def __init__(self, glustervolume, statistic, context):
        Base.__init__(self, context)
        self.parentclass = glustervolume
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, glustervolume, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(glustervolume, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class DatacenterClusterGlustervolumeStatistics(Base):

    def __init__(self, glustervolume , context):
        Base.__init__(self, context)
        self.parentclass = glustervolume

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{cluster:id}': self.parentclass.parentclass.get_id(),
                                '{glustervolume:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterClusterGlustervolumeStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.parentclass.get_id(),
                        '{glustervolume:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return DatacenterClusterGlustervolumeStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Statistics:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes/{glustervolume:id}/statistics'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.parentclass.get_id(),
                    '{glustervolume:id}': self.parentclass.get_id(),
                }
            )
        ).get_statistic()

        return ParseHelper.toSubCollection(
            DatacenterClusterGlustervolumeStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterClusterGlustervolumes(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, glustervolume):

        '''
        @type GlusterVolume:


        @return GlusterVolume:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(glustervolume),
            headers={}
        )

        return DatacenterClusterGlustervolume(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return GlusterVolumes:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterClusterGlustervolume(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_gluster_volume()

            return DatacenterClusterGlustervolume(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return GlusterVolumes:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/glustervolumes'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                }
            )
        ).get_gluster_volume()

        return ParseHelper.toSubCollection(
            DatacenterClusterGlustervolume,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterClusterNetwork(params.Network, Base):
    def __init__(self, cluster, network, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  network

        #SUB_COLLECTIONS
    def __new__(cls, cluster, network, context):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, network, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/datacenters/{datacenter:id}/clusters/{cluster:id}/networks/{network:id}',
            {
                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                '{cluster:id}': self.parentclass.get_id(),
                '{network:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

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

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/networks/{network:id}'
        url = UrlHelper.replace(
            url,
            {
                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                '{cluster:id}': self.parentclass.get_id(),
                '{network:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return DatacenterClusterNetwork(
            self.parentclass,
            result,
            self.context
        )

class DatacenterClusterNetworks(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, network, expect=None, correlation_id=None):

        '''
        @type Network:

        @param network.id|name: string
        [@param network.usages.usage: collection]
        {
          [@ivar usage: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Network:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/networks'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(network),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return DatacenterClusterNetwork(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Networks:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/networks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterClusterNetwork(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_network()

            return DatacenterClusterNetwork(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Networks:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/networks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_network()

        return ParseHelper.toSubCollection(
            DatacenterClusterNetwork,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterClusterPermission(params.Permission, Base):
    def __init__(self, cluster, permission, context):
        Base.__init__(self, context)
        self.parentclass = cluster
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, cluster, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/datacenters/{datacenter:id}/clusters/{cluster:id}/permissions/{permission:id}',
            {
                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                '{cluster:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class DatacenterClusterPermissions(Base):

    def __init__(self, cluster , context):
        Base.__init__(self, context)
        self.parentclass = cluster

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{cluster:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return DatacenterClusterPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{cluster:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterClusterPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return DatacenterClusterPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/clusters/{cluster:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{cluster:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            DatacenterClusterPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterClusters(Base):

    def __init__(self, datacenter , context):
        Base.__init__(self, context)
        self.parentclass = datacenter

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, cluster, expect=None, correlation_id=None):

        '''
        @type Cluster:

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
        [@param cluster.scheduling_policy.id: string]
        [@param cluster.scheduling_policy.properties.property: collection]
        {
          [@ivar property.name: string]
          [@ivar property.value: string]
        }
        [@param cluster.error_handling.on_error: string]
        [@param cluster.virt_service: boolean]
        [@param cluster.gluster_service: boolean]
        [@param cluster.threads_as_cores: boolean]
        [@param cluster.tunnel_migration: boolean]
        [@param cluster.ballooning_enabled: boolean]
        [@param cluster.cpu.architecture: string]
        [@param cluster.display.proxy: string]
        [@param cluster.ksm.enabled: boolean]
        [@param cluster.management_network.id|name: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Cluster:
        '''

        url = '/datacenters/{datacenter:id}/clusters'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(cluster),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return DatacenterCluster(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Clusters:
        '''

        url = '/datacenters/{datacenter:id}/clusters'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterCluster(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_cluster()

            return DatacenterCluster(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Clusters:
        '''

        url = '/datacenters/{datacenter:id}/clusters'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_cluster()

        return ParseHelper.toSubCollection(
            DatacenterCluster,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterIscsibond(params.IscsiBond, Base):
    def __init__(self, datacenter, iscsibond, context):
        Base.__init__(self, context)
        self.parentclass = datacenter
        self.superclass  =  iscsibond

        self.networks = DatacenterIscsibondNetworks(self, context)
        self.storageconnections = DatacenterIscsibondStorageconnections(self, context)

    def __new__(cls, datacenter, iscsibond, context):
        if iscsibond is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, iscsibond, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                    '{iscsibond:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def update(self, expect=None):
        '''
        [@param expect: 201-created]

        @return IscsiBond:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}'
        url = UrlHelper.replace(
            url,
            {
                '{datacenter:id}': self.parentclass.get_id(),
                '{iscsibond:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Expect":expect}
        )

        return DatacenterIscsibond(
            self.parentclass,
            result,
            self.context
        )

class DatacenterIscsibondNetwork(params.Network, Base):
    def __init__(self, iscsibond, network, context):
        Base.__init__(self, context)
        self.parentclass = iscsibond
        self.superclass  =  network

        self.labels = DatacenterIscsibondNetworkLabels(self, context)
        self.permissions = DatacenterIscsibondNetworkPermissions(self, context)
        self.vnicprofiles = DatacenterIscsibondNetworkVnicprofiles(self, context)

    def __new__(cls, iscsibond, network, context):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(iscsibond, network, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.get_id(),
                    '{network:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def update(self):
        '''
        @return Network:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}'
        url = UrlHelper.replace(
            url,
            {
                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                '{iscsibond:id}': self.parentclass.get_id(),
                '{network:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={}
        )

        return DatacenterIscsibondNetwork(
            self.parentclass,
            result,
            self.context
        )

class DatacenterIscsibondNetworkLabel(params.Label, Base):
    def __init__(self, network, label, context):
        Base.__init__(self, context)
        self.parentclass = network
        self.superclass  =  label

        #SUB_COLLECTIONS
    def __new__(cls, network, label, context):
        if label is None: return None
        obj = object.__new__(cls)
        obj.__init__(network, label, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/labels/{label:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                    '{label:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DatacenterIscsibondNetworkLabels(Base):

    def __init__(self, network , context):
        Base.__init__(self, context)
        self.parentclass = network

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, label):

        '''
        @type Label:


        @return Label:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/labels'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(label),
            headers={}
        )

        return DatacenterIscsibondNetworkLabel(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Labels:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/labels'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                                '{network:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterIscsibondNetworkLabel(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_label()

            return DatacenterIscsibondNetworkLabel(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Labels:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/labels'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            )
        ).get_label()

        return ParseHelper.toSubCollection(
            DatacenterIscsibondNetworkLabel,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterIscsibondNetworkPermission(params.Permission, Base):
    def __init__(self, network, permission, context):
        Base.__init__(self, context)
        self.parentclass = network
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, network, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(network, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/permissions/{permission:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                    '{permission:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DatacenterIscsibondNetworkPermissions(Base):

    def __init__(self, network , context):
        Base.__init__(self, context)
        self.parentclass = network

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission):

        '''
        @type Permission:


        @return Permission:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={}
        )

        return DatacenterIscsibondNetworkPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                                '{network:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterIscsibondNetworkPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return DatacenterIscsibondNetworkPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/permissions'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            )
        ).get_permission()

        return ParseHelper.toSubCollection(
            DatacenterIscsibondNetworkPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterIscsibondNetworkVnicprofile(params.VnicProfile, Base):
    def __init__(self, network, vnicprofile, context):
        Base.__init__(self, context)
        self.parentclass = network
        self.superclass  =  vnicprofile

        self.permissions = DatacenterIscsibondNetworkVnicprofilePermissions(self, context)

    def __new__(cls, network, vnicprofile, context):
        if vnicprofile is None: return None
        obj = object.__new__(cls)
        obj.__init__(network, vnicprofile, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/vnicprofiles/{vnicprofile:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                    '{vnicprofile:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DatacenterIscsibondNetworkVnicprofilePermission(params.Permission, Base):
    def __init__(self, vnicprofile, permission, context):
        Base.__init__(self, context)
        self.parentclass = vnicprofile
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, vnicprofile, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vnicprofile, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions/{permission:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.parentclass.get_id(),
                    '{vnicprofile:id}': self.parentclass.get_id(),
                    '{permission:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DatacenterIscsibondNetworkVnicprofilePermissions(Base):

    def __init__(self, vnicprofile , context):
        Base.__init__(self, context)
        self.parentclass = vnicprofile

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission):

        '''
        @type Permission:


        @return Permission:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.parentclass.get_id(),
                    '{vnicprofile:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={}
        )

        return DatacenterIscsibondNetworkVnicprofilePermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.parentclass.get_id(),
                                '{iscsibond:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{network:id}': self.parentclass.parentclass.get_id(),
                                '{vnicprofile:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterIscsibondNetworkVnicprofilePermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.parentclass.get_id(),
                        '{iscsibond:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{network:id}': self.parentclass.parentclass.get_id(),
                        '{vnicprofile:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return DatacenterIscsibondNetworkVnicprofilePermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.parentclass.get_id(),
                    '{vnicprofile:id}': self.parentclass.get_id(),
                }
            )
        ).get_permission()

        return ParseHelper.toSubCollection(
            DatacenterIscsibondNetworkVnicprofilePermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterIscsibondNetworkVnicprofiles(Base):

    def __init__(self, network , context):
        Base.__init__(self, context)
        self.parentclass = network

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, vnicprofile):

        '''
        @type VnicProfile:


        @return VnicProfile:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/vnicprofiles'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(vnicprofile),
            headers={}
        )

        return DatacenterIscsibondNetworkVnicprofile(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return VnicProfiles:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/vnicprofiles'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                                '{network:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterIscsibondNetworkVnicprofile(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_vnic_profile()

            return DatacenterIscsibondNetworkVnicprofile(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return VnicProfiles:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks/{network:id}/vnicprofiles'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            )
        ).get_vnic_profile()

        return ParseHelper.toSubCollection(
            DatacenterIscsibondNetworkVnicprofile,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterIscsibondNetworks(Base):

    def __init__(self, iscsibond , context):
        Base.__init__(self, context)
        self.parentclass = iscsibond

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, network):

        '''
        @type Network:


        @return Network:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(network),
            headers={}
        )

        return DatacenterIscsibondNetwork(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Networks:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{iscsibond:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterIscsibondNetwork(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{iscsibond:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_network()

            return DatacenterIscsibondNetwork(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Networks:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/networks'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.get_id(),
                }
            )
        ).get_network()

        return ParseHelper.toSubCollection(
            DatacenterIscsibondNetwork,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterIscsibondStorageconnection(params.StorageConnection, Base):
    def __init__(self, iscsibond, storageconnection, context):
        Base.__init__(self, context)
        self.parentclass = iscsibond
        self.superclass  =  storageconnection

        #SUB_COLLECTIONS
    def __new__(cls, iscsibond, storageconnection, context):
        if storageconnection is None: return None
        obj = object.__new__(cls)
        obj.__init__(iscsibond, storageconnection, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/storageconnections/{storageconnection:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.get_id(),
                    '{storageconnection:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def delete(self, action):
        '''
        @type Action:


        @return None:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/storageconnections/{storageconnection:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(url,
{
                                                                   '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                                                   '{iscsibond:id}': self.parentclass.get_id(),
                                                                   '{storageconnection:id}': self.get_id(),
                                                               }),
            body=ParseHelper.toXml(action)
        )

    def update(self):
        '''
        @return StorageConnection:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/storageconnections/{storageconnection:id}'
        url = UrlHelper.replace(
            url,
            {
                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                '{iscsibond:id}': self.parentclass.get_id(),
                '{storageconnection:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={}
        )

        return DatacenterIscsibondStorageconnection(
            self.parentclass,
            result,
            self.context
        )

class DatacenterIscsibondStorageconnections(Base):

    def __init__(self, iscsibond , context):
        Base.__init__(self, context)
        self.parentclass = iscsibond

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, storageconnection):

        '''
        @type StorageConnection:


        @return StorageConnection:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/storageconnections'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(storageconnection),
            headers={}
        )

        return DatacenterIscsibondStorageconnection(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return StorageConnections:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/storageconnections'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{iscsibond:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterIscsibondStorageconnection(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{iscsibond:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_storage_connection()

            return DatacenterIscsibondStorageconnection(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return StorageConnections:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds/{iscsibond:id}/storageconnections'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{iscsibond:id}': self.parentclass.get_id(),
                }
            )
        ).get_storage_connection()

        return ParseHelper.toSubCollection(
            DatacenterIscsibondStorageconnection,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterIscsibonds(Base):

    def __init__(self, datacenter , context):
        Base.__init__(self, context)
        self.parentclass = datacenter

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, iscsibond, expect=None):

        '''
        @type IscsiBond:

        @param iscsibond.name: string
        [@param expect: 201-created]

        @return IscsiBond:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(iscsibond),
            headers={"Expect":expect}
        )

        return DatacenterIscsibond(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return IscsiBonds:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterIscsibond(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_iscsi_bond()

            return DatacenterIscsibond(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return IscsiBonds:
        '''

        url = '/datacenters/{datacenter:id}/iscsibonds'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                }
            )
        ).get_iscsi_bond()

        return ParseHelper.toSubCollection(
            DatacenterIscsibond,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterNetwork(params.Network, Base):
    def __init__(self, datacenter, network, context):
        Base.__init__(self, context)
        self.parentclass = datacenter
        self.superclass  =  network

        self.labels = DatacenterNetworkLabels(self, context)
        self.permissions = DatacenterNetworkPermissions(self, context)
        self.vnicprofiles = DatacenterNetworkVnicprofiles(self, context)

    def __new__(cls, datacenter, network, context):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, network, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/datacenters/{datacenter:id}/networks/{network:id}',
            {
                '{datacenter:id}': self.parentclass.get_id(),
                '{network:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

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

        url = '/datacenters/{datacenter:id}/networks/{network:id}'
        url = UrlHelper.replace(
            url,
            {
                '{datacenter:id}': self.parentclass.get_id(),
                '{network:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return DatacenterNetwork(
            self.parentclass,
            result,
            self.context
        )

class DatacenterNetworkLabel(params.Label, Base):
    def __init__(self, network, label, context):
        Base.__init__(self, context)
        self.parentclass = network
        self.superclass  =  label

        #SUB_COLLECTIONS
    def __new__(cls, network, label, context):
        if label is None: return None
        obj = object.__new__(cls)
        obj.__init__(network, label, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/datacenters/{datacenter:id}/networks/{network:id}/labels/{label:id}',
            {
                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                '{network:id}': self.parentclass.get_id(),
                '{label:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class DatacenterNetworkLabels(Base):

    def __init__(self, network , context):
        Base.__init__(self, context)
        self.parentclass = network

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, label, expect=None, correlation_id=None):

        '''
        @type Label:

        @param label.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Label:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/labels'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(label),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return DatacenterNetworkLabel(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Labels:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/labels'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{network:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterNetworkLabel(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_label()

            return DatacenterNetworkLabel(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Labels:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/labels'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            )
        ).get_label()

        return ParseHelper.toSubCollection(
            DatacenterNetworkLabel,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterNetworkPermission(params.Permission, Base):
    def __init__(self, network, permission, context):
        Base.__init__(self, context)
        self.parentclass = network
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, network, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(network, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/permissions/{permission:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                    '{permission:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DatacenterNetworkPermissions(Base):

    def __init__(self, network , context):
        Base.__init__(self, context)
        self.parentclass = network

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission):

        '''
        @type Permission:


        @return Permission:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={}
        )

        return DatacenterNetworkPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{network:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterNetworkPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return DatacenterNetworkPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/permissions'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            )
        ).get_permission()

        return ParseHelper.toSubCollection(
            DatacenterNetworkPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterNetworkVnicprofile(params.VnicProfile, Base):
    def __init__(self, network, vnicprofile, context):
        Base.__init__(self, context)
        self.parentclass = network
        self.superclass  =  vnicprofile

        self.permissions = DatacenterNetworkVnicprofilePermissions(self, context)

    def __new__(cls, network, vnicprofile, context):
        if vnicprofile is None: return None
        obj = object.__new__(cls)
        obj.__init__(network, vnicprofile, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/vnicprofiles/{vnicprofile:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                    '{vnicprofile:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DatacenterNetworkVnicprofilePermission(params.Permission, Base):
    def __init__(self, vnicprofile, permission, context):
        Base.__init__(self, context)
        self.parentclass = vnicprofile
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, vnicprofile, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vnicprofile, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions/{permission:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.parentclass.get_id(),
                    '{vnicprofile:id}': self.parentclass.get_id(),
                    '{permission:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DatacenterNetworkVnicprofilePermissions(Base):

    def __init__(self, vnicprofile , context):
        Base.__init__(self, context)
        self.parentclass = vnicprofile

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission):

        '''
        @type Permission:


        @return Permission:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.parentclass.get_id(),
                    '{vnicprofile:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={}
        )

        return DatacenterNetworkVnicprofilePermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{network:id}': self.parentclass.parentclass.get_id(),
                                '{vnicprofile:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterNetworkVnicprofilePermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{network:id}': self.parentclass.parentclass.get_id(),
                        '{vnicprofile:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return DatacenterNetworkVnicprofilePermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.parentclass.get_id(),
                    '{vnicprofile:id}': self.parentclass.get_id(),
                }
            )
        ).get_permission()

        return ParseHelper.toSubCollection(
            DatacenterNetworkVnicprofilePermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterNetworkVnicprofiles(Base):

    def __init__(self, network , context):
        Base.__init__(self, context)
        self.parentclass = network

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, vnicprofile):

        '''
        @type VnicProfile:


        @return VnicProfile:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/vnicprofiles'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(vnicprofile),
            headers={}
        )

        return DatacenterNetworkVnicprofile(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return VnicProfiles:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/vnicprofiles'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{network:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterNetworkVnicprofile(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_vnic_profile()

            return DatacenterNetworkVnicprofile(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return VnicProfiles:
        '''

        url = '/datacenters/{datacenter:id}/networks/{network:id}/vnicprofiles'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            )
        ).get_vnic_profile()

        return ParseHelper.toSubCollection(
            DatacenterNetworkVnicprofile,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterNetworks(Base):

    def __init__(self, datacenter , context):
        Base.__init__(self, context)
        self.parentclass = datacenter

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, network, expect=None, correlation_id=None):

        '''
        @type Network:

        @param network.id|name: string
        [@param network.description: string]
        [@param network.comment: string]
        [@param network.vlan.id: string]
        [@param network.ip.address: string]
        [@param network.ip.gateway: string]
        [@param network.ip.netmask: string]
        [@param network.stp: boolean]
        [@param network.mtu: int]
        [@param network.profile_required: boolean]
        [@param network.usages.usage: collection]
        {
          [@ivar usage: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Network:
        '''

        url = '/datacenters/{datacenter:id}/networks'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(network),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return DatacenterNetwork(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Networks:
        '''

        url = '/datacenters/{datacenter:id}/networks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterNetwork(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_network()

            return DatacenterNetwork(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Networks:
        '''

        url = '/datacenters/{datacenter:id}/networks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_network()

        return ParseHelper.toSubCollection(
            DatacenterNetwork,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterPermission(params.Permission, Base):
    def __init__(self, datacenter, permission, context):
        Base.__init__(self, context)
        self.parentclass = datacenter
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, datacenter, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/datacenters/{datacenter:id}/permissions/{permission:id}',
            {
                '{datacenter:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class DatacenterPermissions(Base):

    def __init__(self, datacenter , context):
        Base.__init__(self, context)
        self.parentclass = datacenter

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/datacenters/{datacenter:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return DatacenterPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return DatacenterPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/permissions'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                }
            )
        ).get_permission()

        return ParseHelper.toSubCollection(
            DatacenterPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterQos(params.QoS, Base):
    def __init__(self, datacenter, qos, context):
        Base.__init__(self, context)
        self.parentclass = datacenter
        self.superclass  =  qos

        #SUB_COLLECTIONS
    def __new__(cls, datacenter, qos, context):
        if qos is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, qos, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/datacenters/{datacenter:id}/qoss/{qos:id}',
            {
                '{datacenter:id}': self.parentclass.get_id(),
                '{qos:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param qos.name: string]
        [@param qos.description: string]
        [@param qos.max_throughput: int]
        [@param qos.max_read_throughput: int]
        [@param qos.max_write_throughput: int]
        [@param qos.max_iops: int]
        [@param qos.max_read_iops: int]
        [@param qos.max_write_iops: int]
        [@param qos.cpu_limit: int]
        [@param qos.inbound_average: int]
        [@param qos.inbound_peak: int]
        [@param qos.inbound_burst: int]
        [@param qos.outbound_average: int]
        [@param qos.outbound_peak: int]
        [@param qos.outbound_burst: int]
        [@param correlation_id: any string]

        @return QoS:
        '''

        url = '/datacenters/{datacenter:id}/qoss/{qos:id}'
        url = UrlHelper.replace(
            url,
            {
                '{datacenter:id}': self.parentclass.get_id(),
                '{qos:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return DatacenterQos(
            self.parentclass,
            result,
            self.context
        )

class DatacenterQoss(Base):

    def __init__(self, datacenter , context):
        Base.__init__(self, context)
        self.parentclass = datacenter

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, qos, expect=None, correlation_id=None):

        '''
        @type QoS:

        @param qos.name: string
        @param qos.type: string
        [@param qos.description: string]
        [@param qos.max_throughput: int]
        [@param qos.max_read_throughput: int]
        [@param qos.max_write_throughput: int]
        [@param qos.max_iops: int]
        [@param qos.max_read_iops: int]
        [@param qos.max_write_iops: int]
        [@param qos.cpu_limit: int]
        [@param qos.inbound_average: int]
        [@param qos.inbound_peak: int]
        [@param qos.inbound_burst: int]
        [@param qos.outbound_average: int]
        [@param qos.outbound_peak: int]
        [@param qos.outbound_burst: int]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return QoS:
        '''

        url = '/datacenters/{datacenter:id}/qoss'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(qos),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return DatacenterQos(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return QoSs:
        '''

        url = '/datacenters/{datacenter:id}/qoss'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterQos(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_qos()

            return DatacenterQos(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return QoSs:
        '''

        url = '/datacenters/{datacenter:id}/qoss'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_qos()

        return ParseHelper.toSubCollection(
            DatacenterQos,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterQuota(params.Quota, Base):
    def __init__(self, datacenter, quota, context):
        Base.__init__(self, context)
        self.parentclass = datacenter
        self.superclass  =  quota

        #SUB_COLLECTIONS
    def __new__(cls, datacenter, quota, context):
        if quota is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, quota, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class DatacenterQuotas(Base):

    def __init__(self, datacenter , context):
        Base.__init__(self, context)
        self.parentclass = datacenter

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Quotas:
        '''

        url = '/datacenters/{datacenter:id}/quotas'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterQuota(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_quota()

            return DatacenterQuota(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Quotas:
        '''

        url = '/datacenters/{datacenter:id}/quotas'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                }
            )
        ).get_quota()

        return ParseHelper.toSubCollection(
            DatacenterQuota,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterStoragedomain(params.StorageDomain, Base):
    def __init__(self, datacenter, storagedomain, context):
        Base.__init__(self, context)
        self.parentclass = datacenter
        self.superclass  =  storagedomain

        self.disks = DatacenterStoragedomainDisks(self, context)

    def __new__(cls, datacenter, storagedomain, context):
        if storagedomain is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, storagedomain, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}',
            {
                '{datacenter:id}': self.parentclass.get_id(),
                '{storagedomain:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def activate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/activate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                    '{storagedomain:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def deactivate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/deactivate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                    '{storagedomain:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class DatacenterStoragedomainDisk(params.Disk, Base):
    def __init__(self, storagedomain, disk, context):
        Base.__init__(self, context)
        self.parentclass = storagedomain
        self.superclass  =  disk

        self.permissions = DatacenterStoragedomainDiskPermissions(self, context)
        self.statistics = DatacenterStoragedomainDiskStatistics(self, context)

    def __new__(cls, storagedomain, disk, context):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, disk, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks/{disk:id}',
            {
                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                '{storagedomain:id}': self.parentclass.get_id(),
                '{disk:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def copy(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks/{disk:id}/copy'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def export(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param storagedomain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks/{disk:id}/export'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def move(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks/{disk:id}/move'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

class DatacenterStoragedomainDiskPermission(params.Permission, Base):
    def __init__(self, disk, permission, context):
        Base.__init__(self, context)
        self.parentclass = disk
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, disk, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks/{disk:id}/permissions/{permission:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                    '{permission:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DatacenterStoragedomainDiskPermissions(Base):

    def __init__(self, disk , context):
        Base.__init__(self, context)
        self.parentclass = disk

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission):

        '''
        @type Permission:


        @return Permission:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks/{disk:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={}
        )

        return DatacenterStoragedomainDiskPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks/{disk:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                                '{disk:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterStoragedomainDiskPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                        '{disk:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return DatacenterStoragedomainDiskPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Permissions:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks/{disk:id}/permissions'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                }
            )
        ).get_permission()

        return ParseHelper.toSubCollection(
            DatacenterStoragedomainDiskPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterStoragedomainDiskStatistic(params.Statistic, Base):
    def __init__(self, disk, statistic, context):
        Base.__init__(self, context)
        self.parentclass = disk
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, disk, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class DatacenterStoragedomainDiskStatistics(Base):

    def __init__(self, disk , context):
        Base.__init__(self, context)
        self.parentclass = disk

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks/{disk:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                                '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                                '{disk:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterStoragedomainDiskStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                        '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                        '{disk:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return DatacenterStoragedomainDiskStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Statistics:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks/{disk:id}/statistics'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.parentclass.get_id(),
                    '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                }
            )
        ).get_statistic()

        return ParseHelper.toSubCollection(
            DatacenterStoragedomainDiskStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterStoragedomainDisks(Base):

    def __init__(self, storagedomain , context):
        Base.__init__(self, context)
        self.parentclass = storagedomain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, disk, expect=None, correlation_id=None):

        '''
        @type Disk:

        Overload 1:
          @param provisioned_size: int
          @param disk.interface: string
          @param disk.format: string
          [@param disk.alias: string]
          [@param disk.name: string]
          [@param disk.size: int]
          [@param disk.sparse: boolean]
          [@param disk.bootable: boolean]
          [@param disk.shareable: boolean]
          [@param disk.propagate_errors: boolean]
          [@param disk.wipe_after_delete: boolean]
          [@param disk.quota.id: string]
          [@param disk.disk_profile.id: string]
        Overload 2:
          @param disk.interface: string
          @param disk.format: string
          @param disk.lun_storage.type: string
          @param disk.lun_storage.logical_unit: collection
          {
            @ivar logical_unit.id: string
            @ivar logical_unit.address: string
            @ivar logical_unit.port: int
            @ivar logical_unit.target: string
          }
          [@param disk.alias: string]
          [@param disk.sparse: boolean]
          [@param disk.bootable: boolean]
          [@param disk.shareable: boolean]
          [@param disk.propagate_errors: boolean]
          [@param disk.wipe_after_delete: boolean]
          [@param disk.quota.id: string]
          [@param disk.sgio: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Disk:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.parentclass.get_id(),
                    '{storagedomain:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(disk),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return DatacenterStoragedomainDisk(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Disks:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.parentclass.get_id(),
                                '{storagedomain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterStoragedomainDisk(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_disk()

            return DatacenterStoragedomainDisk(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, unregistered=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param unregistered: boolean (true|false)]

        @return Disks:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/disks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{datacenter:id}': self.parentclass.parentclass.get_id(),
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max,'unregistered:matrix':unregistered}
            ),
            headers={}
        ).get_disk()

        return ParseHelper.toSubCollection(
            DatacenterStoragedomainDisk,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DatacenterStoragedomains(Base):

    def __init__(self, datacenter , context):
        Base.__init__(self, context)
        self.parentclass = datacenter

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, storagedomain, expect=None, correlation_id=None):

        '''
        @type StorageDomain:

        @param storagedomain.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return StorageDomain:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{datacenter:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(storagedomain),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return DatacenterStoragedomain(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return StorageDomains:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{datacenter:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DatacenterStoragedomain(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_storage_domain()

            return DatacenterStoragedomain(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return StorageDomains:
        '''

        url = '/datacenters/{datacenter:id}/storagedomains'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{datacenter:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_storage_domain()

        return ParseHelper.toSubCollection(
            DatacenterStoragedomain,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Datacenters(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, datacenter, expect=None, correlation_id=None):
        '''
        @type DataCenter:

        @param datacenter.local: boolean
        @param datacenter.name: string
        [@param datacenter.comment: string]
        [@param datacenter.description: string]
        [@param datacenter.storage_format: string]
        [@param datacenter.storage_type: string]
        [@param datacenter.version.major: int]
        [@param datacenter.version.minor: int]
        [@param datacenter.mac_pool.id: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return DataCenter:
        '''

        url = '/datacenters'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(datacenter),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Datacenter(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return DataCenters:
        '''

        url = '/datacenters'

        if id:
            try :
                return Datacenter(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={}
            ).get_data_center()

            return Datacenter(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return DataCenters:
        '''

        url='/datacenters'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={}
        ).get_data_center()

        return ParseHelper.toCollection(
            Datacenter,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Disk(params.Disk, Base):
    def __init__(self, disk, context):
        Base.__init__(self, context)
        self.superclass = disk

        self.permissions = DiskPermissions(self, context)
        self.statistics = DiskStatistics(self, context)

    def __new__(cls, disk, context):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/disks/{disk:id}',
            {
                '{disk:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def copy(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.storage_domain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/disks/{disk:id}/copy'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def export(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.storage_domain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/disks/{disk:id}/export'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def move(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.storage_domain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/disks/{disk:id}/move'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class DiskPermission(params.Permission, Base):
    def __init__(self, disk, permission, context):
        Base.__init__(self, context)
        self.parentclass = disk
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, disk, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/disks/{disk:id}/permissions/{permission:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{disk:id}': self.parentclass.get_id(),
                    '{permission:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class DiskPermissions(Base):

    def __init__(self, disk , context):
        Base.__init__(self, context)
        self.parentclass = disk

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission):

        '''
        @type Permission:


        @return Permission:
        '''

        url = '/disks/{disk:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{disk:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={}
        )

        return DiskPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/disks/{disk:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{disk:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DiskPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{disk:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return DiskPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/disks/{disk:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{disk:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            DiskPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DiskStatistic(params.Statistic, Base):
    def __init__(self, disk, statistic, context):
        Base.__init__(self, context)
        self.parentclass = disk
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, disk, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class DiskStatistics(Base):

    def __init__(self, disk , context):
        Base.__init__(self, context)
        self.parentclass = disk

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/disks/{disk:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{disk:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DiskStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{disk:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return DiskStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Statistics:
        '''

        url = '/disks/{disk:id}/statistics'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{disk:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_statistic()

        return ParseHelper.toSubCollection(
            DiskStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Diskprofile(params.DiskProfile, Base):
    def __init__(self, diskprofile, context):
        Base.__init__(self, context)
        self.superclass = diskprofile

        self.permissions = DiskprofilePermissions(self, context)

    def __new__(cls, diskprofile, context):
        if diskprofile is None: return None
        obj = object.__new__(cls)
        obj.__init__(diskprofile, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/diskprofiles/{diskprofile:id}',
            {
                '{diskprofile:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param diskprofile.name: string]
        [@param diskprofile.description: string]
        [@param diskprofile.qos.id: string]
        [@param correlation_id: any string]

        @return DiskProfile:
        '''

        url = '/diskprofiles/{diskprofile:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{diskprofile:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Diskprofile(result, self.context)

class DiskprofilePermission(params.Permission, Base):
    def __init__(self, diskprofile, permission, context):
        Base.__init__(self, context)
        self.parentclass = diskprofile
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, diskprofile, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(diskprofile, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/diskprofiles/{diskprofile:id}/permissions/{permission:id}',
            {
                '{diskprofile:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class DiskprofilePermissions(Base):

    def __init__(self, diskprofile , context):
        Base.__init__(self, context)
        self.parentclass = diskprofile

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.group.id: string
          @param permission.role.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/diskprofiles/{diskprofile:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{diskprofile:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return DiskprofilePermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/diskprofiles/{diskprofile:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{diskprofile:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DiskprofilePermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{diskprofile:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return DiskprofilePermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/diskprofiles/{diskprofile:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{diskprofile:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            DiskprofilePermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Diskprofiles(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, diskprofile, expect=None, correlation_id=None):
        '''
        @type DiskProfile:

        @param diskprofile.storagedomain.id: string
        @param diskprofile.name: string
        [@param diskprofile.description: string]
        [@param diskprofile.qos.id: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return DiskProfile:
        '''

        url = '/diskprofiles'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(diskprofile),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Diskprofile(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return DiskProfiles:
        '''

        url = '/diskprofiles'

        if id:
            try :
                return Diskprofile(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_disk_profile()

            return Diskprofile(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return DiskProfiles:
        '''

        url='/diskprofiles'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_disk_profile()

        return ParseHelper.toCollection(
            Diskprofile,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Disks(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, disk, expect=None, correlation_id=None):
        '''
        @type Disk:

        Overload 1:
          @param provisioned_size: int
          @param disk.interface: string
          @param disk.format: string
          [@param disk.alias: string]
          [@param disk.name: string]
          [@param disk.size: int]
          [@param disk.sparse: boolean]
          [@param disk.bootable: boolean]
          [@param disk.shareable: boolean]
          [@param disk.propagate_errors: boolean]
          [@param disk.wipe_after_delete: boolean]
          [@param disk.quota.id: string]
          [@param disk.disk_profile.id: string]
          [@param disk.storage_domains.storage_domain: collection]
          {
            [@ivar storage_domain.id|name: string]
          }
        Overload 2:
          @param disk.interface: string
          @param disk.lun_storage.type: string
          @param disk.lun_storage.logical_unit: collection
          {
            @ivar logical_unit.id: string
            @ivar logical_unit.address: string
            @ivar logical_unit.port: int
            @ivar logical_unit.target: string
          }
          [@param disk.alias: string]
          [@param disk.sparse: boolean]
          [@param disk.bootable: boolean]
          [@param disk.shareable: boolean]
          [@param disk.propagate_errors: boolean]
          [@param disk.wipe_after_delete: boolean]
          [@param disk.quota.id: string]
          [@param disk.sgio: string]
          [@param disk.lun_storage.host: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Disk:
        '''

        url = '/disks'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(disk),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Disk(result, self.context)

    def get(self, alias=None, id=None):
        '''
        [@param id   : string (the id of the entity)]
        [@param alias: string (the alias of the entity)]

        @return Disks:
        '''

        url = '/disks'

        if id:
            try :
                return Disk(
                    self.__getProxy().get(url=UrlHelper.append(url, id),
                    headers={}),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif alias:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'alias='+alias}),
                headers={}
            ).get_disk()

            return Disk(
                        FilterHelper.getItem(
                            FilterHelper.filter(result, {'alias':alias}),
                            query="alias=" + alias
                        ),
                        self.context
            )
        else:
            raise MissingParametersError(['id', 'alias'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Disks:
        '''

        url='/disks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={}
        ).get_disk()

        return ParseHelper.toCollection(
            Disk,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Domain(params.Domain, Base):
    def __init__(self, domain, context):
        Base.__init__(self, context)
        self.superclass = domain

        self.groups = DomainGroups(self, context)
        self.users = DomainUsers(self, context)

    def __new__(cls, domain, context):
        if domain is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class DomainGroup(params.Group, Base):
    def __init__(self, domain, group, context):
        Base.__init__(self, context)
        self.parentclass = domain
        self.superclass  =  group

        #SUB_COLLECTIONS
    def __new__(cls, domain, group, context):
        if group is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain, group, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class DomainGroups(Base):

    def __init__(self, domain , context):
        Base.__init__(self, context)
        self.parentclass = domain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Groups:
        '''

        url = '/domains/{domain:id}/groups'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{domain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DomainGroup(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{domain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_group()

            return DomainGroup(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Groups:
        '''

        url = '/domains/{domain:id}/groups'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{domain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}
            ),
            headers={}
        ).get_group()

        return ParseHelper.toSubCollection(
            DomainGroup,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class DomainUser(params.User, Base):
    def __init__(self, domain, user, context):
        Base.__init__(self, context)
        self.parentclass = domain
        self.superclass  =  user

        #SUB_COLLECTIONS
    def __new__(cls, domain, user, context):
        if user is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain, user, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class DomainUsers(Base):

    def __init__(self, domain , context):
        Base.__init__(self, context)
        self.parentclass = domain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Users:
        '''

        url = '/domains/{domain:id}/users'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{domain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return DomainUser(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{domain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_user()

            return DomainUser(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Users:
        '''

        url = '/domains/{domain:id}/users'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{domain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}
            ),
            headers={}
        ).get_user()

        return ParseHelper.toSubCollection(
            DomainUser,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Domains(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Domains:
        '''

        url = '/domains'

        if id:
            try :
                return Domain(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_domain()

            return Domain(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return Domains:
        '''

        url='/domains'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_domain()

        return ParseHelper.toCollection(
            Domain,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Event(params.Event, Base):
    def __init__(self, event, context):
        Base.__init__(self, context)
        self.superclass = event

        #SUB_COLLECTIONS
    def __new__(cls, event, context):
        if event is None: return None
        obj = object.__new__(cls)
        obj.__init__(event, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/events/{event:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{event:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class Events(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, event, expect=None, correlation_id=None):
        '''
        @type Event:

        @param event.description: string
        @param event.severity: string
        @param event.origin: string
        @param event.custom_id: int
        [@param event.flood_rate: int]
        [@param event.host.id: string]
        [@param event.user.id: string]
        [@param event.vm.id: string]
        [@param event.storage_domain.id: string]
        [@param event.template.id: string]
        [@param event.cluster.id: string]
        [@param event.data_center.id: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Event:
        '''

        url = '/events'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(event),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Event(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Events:
        '''

        url = '/events'

        if id:
            try :
                return Event(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={}
            ).get_event()

            return Event(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, from_event_id=None, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param from_event_id: string (event_id)]
        [@param max: int (max results)]

        @return Events:
        '''

        url='/events'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'from:matrix':from_event_id,'max:matrix':max}),
            headers={}
        ).get_event()

        return ParseHelper.toCollection(
            Event,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Externalhostprovider(params.ExternalHostProvider, Base):
    def __init__(self, externalhostprovider, context):
        Base.__init__(self, context)
        self.superclass = externalhostprovider

        self.certificates = ExternalhostproviderCertificates(self, context)
        self.computeresources = ExternalhostproviderComputeresources(self, context)
        self.discoveredhosts = ExternalhostproviderDiscoveredhosts(self, context)
        self.hostgroups = ExternalhostproviderHostgroups(self, context)
        self.hosts = ExternalhostproviderHosts(self, context)

    def __new__(cls, externalhostprovider, context):
        if externalhostprovider is None: return None
        obj = object.__new__(cls)
        obj.__init__(externalhostprovider, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/externalhostproviders/{externalhostprovider:id}',
            {
                '{externalhostprovider:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param external_host_provider.name: string]
        [@param external_host_provider.description: string]
        [@param external_host_provider.requires_authentication: boolean]
        [@param external_host_provider.username: string]
        [@param external_host_provider.password: string]
        [@param correlation_id: any string]

        @return ExternalHostProvider:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{externalhostprovider:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Externalhostprovider(result, self.context)

    def importcertificates(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/importcertificates'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{externalhostprovider:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def testconnectivity(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/testconnectivity'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{externalhostprovider:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class ExternalhostproviderCertificate(params.Certificate, Base):
    def __init__(self, externalhostprovider, certificate, context):
        Base.__init__(self, context)
        self.parentclass = externalhostprovider
        self.superclass  =  certificate

        #SUB_COLLECTIONS
    def __new__(cls, externalhostprovider, certificate, context):
        if certificate is None: return None
        obj = object.__new__(cls)
        obj.__init__(externalhostprovider, certificate, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class ExternalhostproviderCertificates(Base):

    def __init__(self, externalhostprovider , context):
        Base.__init__(self, context)
        self.parentclass = externalhostprovider

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Certificates:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/certificates'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{externalhostprovider:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ExternalhostproviderCertificate(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{externalhostprovider:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_certificate()

            return ExternalhostproviderCertificate(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Certificates:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/certificates'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{externalhostprovider:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_certificate()

        return ParseHelper.toSubCollection(
            ExternalhostproviderCertificate,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ExternalhostproviderComputeresource(params.ExternalComputeResource, Base):
    def __init__(self, externalhostprovider, externalcomputeresource, context):
        Base.__init__(self, context)
        self.parentclass = externalhostprovider
        self.superclass  =  externalcomputeresource

        #SUB_COLLECTIONS
    def __new__(cls, externalhostprovider, externalcomputeresource, context):
        if externalcomputeresource is None: return None
        obj = object.__new__(cls)
        obj.__init__(externalhostprovider, externalcomputeresource, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class ExternalhostproviderComputeresources(Base):

    def __init__(self, externalhostprovider , context):
        Base.__init__(self, context)
        self.parentclass = externalhostprovider

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return ExternalComputeResources:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/computeresources'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{externalhostprovider:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ExternalhostproviderComputeresource(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{externalhostprovider:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_external_compute_resource()

            return ExternalhostproviderComputeresource(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return ExternalComputeResources:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/computeresources'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{externalhostprovider:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_external_compute_resource()

        return ParseHelper.toSubCollection(
            ExternalhostproviderComputeresource,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ExternalhostproviderDiscoveredhost(params.ExternalDiscoveredHost, Base):
    def __init__(self, externalhostprovider, externaldiscoveredhost, context):
        Base.__init__(self, context)
        self.parentclass = externalhostprovider
        self.superclass  =  externaldiscoveredhost

        #SUB_COLLECTIONS
    def __new__(cls, externalhostprovider, externaldiscoveredhost, context):
        if externaldiscoveredhost is None: return None
        obj = object.__new__(cls)
        obj.__init__(externalhostprovider, externaldiscoveredhost, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class ExternalhostproviderDiscoveredhosts(Base):

    def __init__(self, externalhostprovider , context):
        Base.__init__(self, context)
        self.parentclass = externalhostprovider

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return ExternalDiscoveredHosts:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/discoveredhosts'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{externalhostprovider:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ExternalhostproviderDiscoveredhost(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{externalhostprovider:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_external_discovered_host()

            return ExternalhostproviderDiscoveredhost(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return ExternalDiscoveredHosts:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/discoveredhosts'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{externalhostprovider:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_external_discovered_host()

        return ParseHelper.toSubCollection(
            ExternalhostproviderDiscoveredhost,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ExternalhostproviderHost(params.ExternalHost, Base):
    def __init__(self, externalhostprovider, externalhost, context):
        Base.__init__(self, context)
        self.parentclass = externalhostprovider
        self.superclass  =  externalhost

        #SUB_COLLECTIONS
    def __new__(cls, externalhostprovider, externalhost, context):
        if externalhost is None: return None
        obj = object.__new__(cls)
        obj.__init__(externalhostprovider, externalhost, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class ExternalhostproviderHostgroup(params.ExternalHostGroup, Base):
    def __init__(self, externalhostprovider, externalhostgroup, context):
        Base.__init__(self, context)
        self.parentclass = externalhostprovider
        self.superclass  =  externalhostgroup

        #SUB_COLLECTIONS
    def __new__(cls, externalhostprovider, externalhostgroup, context):
        if externalhostgroup is None: return None
        obj = object.__new__(cls)
        obj.__init__(externalhostprovider, externalhostgroup, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class ExternalhostproviderHostgroups(Base):

    def __init__(self, externalhostprovider , context):
        Base.__init__(self, context)
        self.parentclass = externalhostprovider

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return ExternalHostGroups:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/hostgroups'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{externalhostprovider:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ExternalhostproviderHostgroup(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{externalhostprovider:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_external_host_group()

            return ExternalhostproviderHostgroup(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return ExternalHostGroups:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/hostgroups'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{externalhostprovider:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_external_host_group()

        return ParseHelper.toSubCollection(
            ExternalhostproviderHostgroup,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class ExternalhostproviderHosts(Base):

    def __init__(self, externalhostprovider , context):
        Base.__init__(self, context)
        self.parentclass = externalhostprovider

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return ExternalHosts:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/hosts'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{externalhostprovider:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return ExternalhostproviderHost(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{externalhostprovider:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_external_host()

            return ExternalhostproviderHost(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return ExternalHosts:
        '''

        url = '/externalhostproviders/{externalhostprovider:id}/hosts'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{externalhostprovider:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_external_host()

        return ParseHelper.toSubCollection(
            ExternalhostproviderHost,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Externalhostproviders(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, externalhostprovider, expect=None, correlation_id=None):
        '''
        @type ExternalHostProvider:

        @param external_host_provider.name: string
        [@param external_host_provider.description: string]
        [@param external_host_provider.url: string]
        [@param external_host_provider.requires_authentication: boolean]
        [@param external_host_provider.username: string]
        [@param external_host_provider.password: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return ExternalHostProvider:
        '''

        url = '/externalhostproviders'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(externalhostprovider),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Externalhostprovider(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return ExternalHostProviders:
        '''

        url = '/externalhostproviders'

        if id:
            try :
                return Externalhostprovider(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_external_host_provider()

            return Externalhostprovider(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return ExternalHostProviders:
        '''

        url='/externalhostproviders'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_external_host_provider()

        return ParseHelper.toCollection(
            Externalhostprovider,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Group(params.Group, Base):
    def __init__(self, group, context):
        Base.__init__(self, context)
        self.superclass = group

        self.permissions = GroupPermissions(self, context)
        self.roles = GroupRoles(self, context)
        self.tags = GroupTags(self, context)

    def __new__(cls, group, context):
        if group is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/groups/{group:id}',
            {
                '{group:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class GroupPermission(params.Permission, Base):
    def __init__(self, group, permission, context):
        Base.__init__(self, context)
        self.parentclass = group
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, group, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/groups/{group:id}/permissions/{permission:id}',
            {
                '{group:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class GroupPermissions(Base):

    def __init__(self, group , context):
        Base.__init__(self, context)
        self.parentclass = group

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/groups/{group:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{group:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return GroupPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/groups/{group:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{group:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return GroupPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{group:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return GroupPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/groups/{group:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{group:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            GroupPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class GroupRole(params.Role, Base):
    def __init__(self, group, role, context):
        Base.__init__(self, context)
        self.parentclass = group
        self.superclass  =  role

        self.permits = GroupRolePermits(self, context)

    def __new__(cls, group, role, context):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, role, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class GroupRolePermit(params.Permit, Base):
    def __init__(self, role, permit, context):
        Base.__init__(self, context)
        self.parentclass = role
        self.superclass  =  permit

        #SUB_COLLECTIONS
    def __new__(cls, role, permit, context):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(role, permit, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/groups/{group:id}/roles/{role:id}/permits/{permit:id}',
            {
                '{group:id}': self.parentclass.parentclass.get_id(),
                '{role:id}': self.parentclass.get_id(),
                '{permit:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class GroupRolePermits(Base):

    def __init__(self, role , context):
        Base.__init__(self, context)
        self.parentclass = role

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permit, expect=None, correlation_id=None):

        '''
        @type Permit:

        @param permit.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permit:
        '''

        url = '/groups/{group:id}/roles/{role:id}/permits'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{group:id}': self.parentclass.parentclass.get_id(),
                    '{role:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permit),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return GroupRolePermit(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permits:
        '''

        url = '/groups/{group:id}/roles/{role:id}/permits'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{group:id}': self.parentclass.parentclass.get_id(),
                                '{role:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return GroupRolePermit(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{group:id}': self.parentclass.parentclass.get_id(),
                        '{role:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permit()

            return GroupRolePermit(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permits:
        '''

        url = '/groups/{group:id}/roles/{role:id}/permits'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{group:id}': self.parentclass.parentclass.get_id(),
                        '{role:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permit()

        return ParseHelper.toSubCollection(
            GroupRolePermit,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class GroupRoles(Base):

    def __init__(self, group , context):
        Base.__init__(self, context)
        self.parentclass = group

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Roles:
        '''

        url = '/groups/{group:id}/roles'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{group:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return GroupRole(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{group:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_role()

            return GroupRole(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Roles:
        '''

        url = '/groups/{group:id}/roles'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{group:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_role()

        return ParseHelper.toSubCollection(
            GroupRole,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class GroupTag(params.Tag, Base):
    def __init__(self, group, tag, context):
        Base.__init__(self, context)
        self.parentclass = group
        self.superclass  =  tag

        #SUB_COLLECTIONS
    def __new__(cls, group, tag, context):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, tag, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/groups/{group:id}/tags/{tag:id}',
            {
                '{group:id}': self.parentclass.get_id(),
                '{tag:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class GroupTags(Base):

    def __init__(self, group , context):
        Base.__init__(self, context)
        self.parentclass = group

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, tag, expect=None, correlation_id=None):

        '''
        @type Tag:

        @param tag.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/groups/{group:id}/tags'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{group:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(tag),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return GroupTag(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/groups/{group:id}/tags'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{group:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return GroupTag(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{group:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_tag()

            return GroupTag(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Tags:
        '''

        url = '/groups/{group:id}/tags'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{group:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_tag()

        return ParseHelper.toSubCollection(
            GroupTag,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Groups(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, group, correlation_id=None):
        '''
        @type Group:

        @param group.name: string
        [@param group.namespace: string]
        [@param group.principal: string]
        [@param correlation_id: any string]

        @return Group:
        '''

        url = '/groups'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(group),
           headers={"Correlation-Id":correlation_id}
        )

        return Group(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Groups:
        '''

        url = '/groups'

        if id:
            try :
                return Group(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={}
            ).get_group()

            return Group(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Groups:
        '''

        url='/groups'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={}
        ).get_group()

        return ParseHelper.toCollection(
            Group,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Host(params.Host, Base):
    def __init__(self, host, context):
        Base.__init__(self, context)
        self.superclass = host

        self.fenceagents = HostFenceagents(self, context)
        self.hooks = HostHooks(self, context)
        self.katelloerrata = HostKatelloerrata(self, context)
        self.nics = HostNics(self, context)
        self.numanodes = HostNumanodes(self, context)
        self.permissions = HostPermissions(self, context)
        self.statistics = HostStatistics(self, context)
        self.storage = HostStorage(self, context)
        self.tags = HostTags(self, context)

    def __new__(cls, host, context):
        if host is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, action=params.Action(), async=None, correlation_id=None):
        '''
        @type Action:

        [@param action.force: boolean]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/hosts/{host:id}',
            {
                '{host:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

    def update(self, correlation_id=None):
        '''
        Overload 1:
          [@param host.name: string]
          [@param host.comment: string]
          [@param host.address: string]
          [@param host.root_password: string]
          [@param host.display.address: string]
          [@param host.cluster.id|name: string]
          [@param host.port: int]
          [@param host.spm.priority: int]
          [@param host.power_management.type: string]
          [@param host.power_management.enabled: boolean]
          [@param host.power_management.address: string]
          [@param host.power_management.username: string]
          [@param host.power_management.password: string]
          [@param host.power_management.automatic_pm_enabled: boolean]
          [@param host.power_management.options.option: collection]
          {
            [@ivar option.name: string]
            [@ivar option.value: string]
          }
          [@param host.power_management.pm_proxy: collection]
          {
            [@ivar propietary: string]
          }
          [@param host.power_management.agents.agent: collection]
          {
            [@ivar type: string]
            [@ivar address: string]
            [@ivar username: string]
            [@ivar password: string]
            [@ivar options.option: collection]
            {
              [@param option.name: string]
              [@param option.value: string]
            }
          }
          [@param host.power_management.kdump_detection: boolean]
          [@param host.external_host_provider.id: string]
        Overload 2:
          [@param host.name: string]
          [@param host.comment: string]
          [@param host.address: string]
          [@param host.ssh.port: int]
          [@param host.ssh.user.user_name: string]
          [@param host.ssh.fingerprint: string]
          [@param host.display.address: string]
          [@param host.cluster.id|name: string]
          [@param host.port: int]
          [@param host.spm.priority: int]
          [@param host.power_management.type: string]
          [@param host.power_management.automatic_pm_enabled: boolean]
          [@param host.power_management.enabled: boolean]
          [@param host.power_management.address: string]
          [@param host.power_management.username: string]
          [@param host.power_management.password: string]
          [@param host.power_management.options.option: collection]
          {
            [@ivar option.name: string]
            [@ivar option.value: string]
          }
          [@param host.power_management.pm_proxy: collection]
          {
            [@ivar propietary: string]
          }
          [@param host.power_management.agents.agent: collection]
          {
            [@ivar type: string]
            [@ivar address: string]
            [@ivar username: string]
            [@ivar password: string]
            [@ivar options.option: collection]
            {
              [@param option.name: string]
              [@param option.value: string]
            }
          }
          [@param host.power_management.kdump_detection: boolean]
        [@param correlation_id: any string]

        @return Host:
        '''

        url = '/hosts/{host:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Host(result, self.context)

    def activate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/activate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def approve(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        Overload 1:
          [@param action.cluster.id|name: string]
          [@param action.async: boolean]
          [@param action.grace_period.expiry: long]
          [@param host.root_password: string]
        Overload 2:
          [@param action.cluster.id|name: string]
          [@param action.async: boolean]
          [@param action.grace_period.expiry: long]
          [@param host.ssh.authentication_method: string]
          [@param host.ssh.user.user_name: string]
          [@param host.ssh.user.password: string]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/approve'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def commitnetconfig(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/commitnetconfig'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def deactivate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/deactivate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def fence(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.fence_type: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/fence'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def forceselectspm(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/forceselectspm'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def install(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        Overload 1:
          [@param action.root_password: string]
          [@param action.image: string]
          [@param action.host.override_iptables: boolean]
        Overload 2:
          [@param action.ssh.port: int]
          [@param action.ssh.fingerprint: string]
          [@param action.ssh.authentication_method: string]
          [@param action.ssh.user.user_name: string]
          [@param action.ssh.user.password: string]
          [@param action.image: string]
          [@param action.async: boolean]
          [@param action.grace_period.expiry: long]
          [@param action.host.override_iptables: boolean]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/install'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def iscsidiscover(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.iscsi.address: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/iscsidiscover'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def iscsilogin(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.iscsi.address: string
        @param action.iscsi.target: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/iscsilogin'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def unregisteredstoragedomainsdiscover(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.iscsi.address: string
        @param action.target: string
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/unregisteredstoragedomainsdiscover'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class HostFenceagent(params.Agent, Base):
    def __init__(self, host, agent, context):
        Base.__init__(self, context)
        self.parentclass = host
        self.superclass  =  agent

        #SUB_COLLECTIONS
    def __new__(cls, host, agent, context):
        if agent is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, agent, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/hosts/{host:id}/fenceagents/{fenceagent:id}',
            {
                '{host:id}': self.parentclass.get_id(),
                '{fenceagent:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, expect=None, correlation_id=None):
        '''
        [@param agent.address: string]
        [@param agent.order: int]
        [@param agent.type: string]
        [@param agent.username: string]
        [@param agent.password: string]
        [@param agent.port: int]
        [@param agent.options: collection]
        {
          [@ivar option.name: string]
          [@ivar option.value: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Agent:
        '''

        url = '/hosts/{host:id}/fenceagents/{fenceagent:id}'
        url = UrlHelper.replace(
            url,
            {
                '{host:id}': self.parentclass.get_id(),
                '{fenceagent:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return HostFenceagent(
            self.parentclass,
            result,
            self.context
        )

class HostFenceagents(Base):

    def __init__(self, host , context):
        Base.__init__(self, context)
        self.parentclass = host

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, agent, expect=None, correlation_id=None):

        '''
        @type Agent:

        @param agent.address: string
        @param agent.order: int
        @param agent.type: string
        @param agent.username: string
        @param agent.password: string
        [@param agent.port: int]
        [@param agent.options: collection]
        {
          [@ivar option.name: string]
          [@ivar option.value: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Agent:
        '''

        url = '/hosts/{host:id}/fenceagents'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(agent),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return HostFenceagent(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Agents:
        '''

        url = '/hosts/{host:id}/fenceagents'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostFenceagent(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_agent()

            return HostFenceagent(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Agents:
        '''

        url = '/hosts/{host:id}/fenceagents'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.get_id(),
                }
            )
        ).get_agent()

        return ParseHelper.toSubCollection(
            HostFenceagent,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class HostHook(params.Hook, Base):
    def __init__(self, host, hook, context):
        Base.__init__(self, context)
        self.parentclass = host
        self.superclass  =  hook

        #SUB_COLLECTIONS
    def __new__(cls, host, hook, context):
        if hook is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, hook, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class HostHooks(Base):

    def __init__(self, host , context):
        Base.__init__(self, context)
        self.parentclass = host

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Hooks:
        '''

        url = '/hosts/{host:id}/hooks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostHook(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_hook()

            return HostHook(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Hooks:
        '''

        url = '/hosts/{host:id}/hooks'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.get_id(),
                }
            )
        ).get_hook()

        return ParseHelper.toSubCollection(
            HostHook,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class HostKatelloerrata(Base):

    def __init__(self, host , context):
        Base.__init__(self, context)
        self.parentclass = host

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return KatelloErrata:
        '''

        url = '/hosts/{host:id}/katelloerrata'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostKatelloerrata(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_katello_erratum()

            return HostKatelloerrata(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return KatelloErrata:
        '''

        url = '/hosts/{host:id}/katelloerrata'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_katello_erratum()

        return ParseHelper.toSubCollection(
            HostKatelloerrata,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class HostNic(params.HostNIC, Base):
    def __init__(self, host, hostnic, context):
        Base.__init__(self, context)
        self.parentclass = host
        self.superclass  =  hostnic

        self.labels = HostNicLabels(self, context)
        self.statistics = HostNicStatistics(self, context)

    def __new__(cls, host, hostnic, context):
        if hostnic is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, hostnic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/hosts/{host:id}/nics/{nic:id}',
            {
                '{host:id}': self.parentclass.get_id(),
                '{nic:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, async=None, correlation_id=None):
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
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return HostNIC:
        '''

        url = '/hosts/{host:id}/nics/{nic:id}'
        url = UrlHelper.replace(
            url,
            {
                '{host:id}': self.parentclass.get_id(),
                '{nic:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {'async:matrix':async}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return HostNic(
            self.parentclass,
            result,
            self.context
        )

    def attach(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.network.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/nics/{nic:id}/attach'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.get_id(),
                    '{nic:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def detach(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/nics/{nic:id}/detach'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.get_id(),
                    '{nic:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class HostNicLabel(params.Label, Base):
    def __init__(self, hostnic, label, context):
        Base.__init__(self, context)
        self.parentclass = hostnic
        self.superclass  =  label

        #SUB_COLLECTIONS
    def __new__(cls, hostnic, label, context):
        if label is None: return None
        obj = object.__new__(cls)
        obj.__init__(hostnic, label, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/hosts/{host:id}/nics/{nic:id}/labels/{label:id}',
            {
                '{host:id}': self.parentclass.parentclass.get_id(),
                '{nic:id}': self.parentclass.get_id(),
                '{label:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class HostNicLabels(Base):

    def __init__(self, hostnic , context):
        Base.__init__(self, context)
        self.parentclass = hostnic

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, label, expect=None, correlation_id=None):

        '''
        @type Label:

        @param label.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Label:
        '''

        url = '/hosts/{host:id}/nics/{nic:id}/labels'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.parentclass.get_id(),
                    '{nic:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(label),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return HostNicLabel(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Labels:
        '''

        url = '/hosts/{host:id}/nics/{nic:id}/labels'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.parentclass.get_id(),
                                '{nic:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostNicLabel(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.parentclass.get_id(),
                        '{nic:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_label()

            return HostNicLabel(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Labels:
        '''

        url = '/hosts/{host:id}/nics/{nic:id}/labels'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.parentclass.get_id(),
                    '{nic:id}': self.parentclass.get_id(),
                }
            )
        ).get_label()

        return ParseHelper.toSubCollection(
            HostNicLabel,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class HostNicStatistic(params.Statistic, Base):
    def __init__(self, hostnic, statistic, context):
        Base.__init__(self, context)
        self.parentclass = hostnic
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, hostnic, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(hostnic, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class HostNicStatistics(Base):

    def __init__(self, hostnic , context):
        Base.__init__(self, context)
        self.parentclass = hostnic

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/hosts/{host:id}/nics/{nic:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.parentclass.get_id(),
                                '{nic:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostNicStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.parentclass.get_id(),
                        '{nic:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return HostNicStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Statistics:
        '''

        url = '/hosts/{host:id}/nics/{nic:id}/statistics'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{host:id}': self.parentclass.parentclass.get_id(),
                        '{nic:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_statistic()

        return ParseHelper.toSubCollection(
            HostNicStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class HostNics(Base):

    def __init__(self, host , context):
        Base.__init__(self, context)
        self.parentclass = host

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, hostnic, expect=None, correlation_id=None):

        '''
        @type HostNIC:

        @param hostnic.network.id|name: string
        @param hostnic.name: string
        @param hostnic.bonding.slaves.host_nic: collection
        {
          @ivar host_nic.id|name: string
        }
        [@param hostnic.bonding.options.option: collection]
        {
          [@ivar option.name: string]
          [@ivar option.value: string]
          [@ivar type: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return HostNIC:
        '''

        url = '/hosts/{host:id}/nics'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(hostnic),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return HostNic(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return HostNics:
        '''

        url = '/hosts/{host:id}/nics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostNic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_host_nic()

            return HostNic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return HostNics:
        '''

        url = '/hosts/{host:id}/nics'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_host_nic()

        return ParseHelper.toSubCollection(
            HostNic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

    def setupnetworks(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.host_nics.host_nic: collection]
        {
          [@ivar host_nic.network.id|name: string]
          [@ivar host_nic.name: string]
          [@ivar host_nic.base_interface: string]
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
          [@ivar host_nic.properties.property: collection]
          {
            [@param property.name: string]
            [@param property.value: string]
          }
          [@ivar action.async: boolean]
          [@ivar action.grace_period.expiry: long]
        }
        [@param action.checkConnectivity: boolean]
        [@param action.connectivityTimeout: int]
        [@param action.force: boolean]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/hosts/{host:id}/nics/setupnetworks'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class HostNumanode(params.NumaNode, Base):
    def __init__(self, host, numanode, context):
        Base.__init__(self, context)
        self.parentclass = host
        self.superclass  =  numanode

        self.statistics = HostNumanodeStatistics(self, context)

    def __new__(cls, host, numanode, context):
        if numanode is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, numanode, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class HostNumanodeStatistic(params.Statistic, Base):
    def __init__(self, numanode, statistic, context):
        Base.__init__(self, context)
        self.parentclass = numanode
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, numanode, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(numanode, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class HostNumanodeStatistics(Base):

    def __init__(self, numanode , context):
        Base.__init__(self, context)
        self.parentclass = numanode

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/hosts/{host:id}/numanodes/{numanode:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.parentclass.get_id(),
                                '{numanode:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostNumanodeStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.parentclass.get_id(),
                        '{numanode:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return HostNumanodeStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Statistics:
        '''

        url = '/hosts/{host:id}/numanodes/{numanode:id}/statistics'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{host:id}': self.parentclass.parentclass.get_id(),
                        '{numanode:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_statistic()

        return ParseHelper.toSubCollection(
            HostNumanodeStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class HostNumanodes(Base):

    def __init__(self, host , context):
        Base.__init__(self, context)
        self.parentclass = host

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return NumaNodes:
        '''

        url = '/hosts/{host:id}/numanodes'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostNumanode(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_host_numa_node()

            return HostNumanode(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return NumaNodes:
        '''

        url = '/hosts/{host:id}/numanodes'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_host_numa_node()

        return ParseHelper.toSubCollection(
            HostNumanode,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class HostPermission(params.Permission, Base):
    def __init__(self, host, permission, context):
        Base.__init__(self, context)
        self.parentclass = host
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, host, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/hosts/{host:id}/permissions/{permission:id}',
            {
                '{host:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class HostPermissions(Base):

    def __init__(self, host , context):
        Base.__init__(self, context)
        self.parentclass = host

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/hosts/{host:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return HostPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/hosts/{host:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return HostPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/hosts/{host:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            HostPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class HostStatistic(params.Statistic, Base):
    def __init__(self, host, statistic, context):
        Base.__init__(self, context)
        self.parentclass = host
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, host, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class HostStatistics(Base):

    def __init__(self, host , context):
        Base.__init__(self, context)
        self.parentclass = host

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/hosts/{host:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return HostStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Statistics:
        '''

        url = '/hosts/{host:id}/statistics'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_statistic()

        return ParseHelper.toSubCollection(
            HostStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class HostStorage(Base):

    def __init__(self, host , context):
        Base.__init__(self, context)
        self.parentclass = host

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return HostStorage:
        '''

        url = '/hosts/{host:id}/storage'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostStorage(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_storage()

            return HostStorage(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return HostStorage:
        '''

        url = '/hosts/{host:id}/storage'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_storage()

        return ParseHelper.toSubCollection(
            HostStorage,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class HostTag(params.Tag, Base):
    def __init__(self, host, tag, context):
        Base.__init__(self, context)
        self.parentclass = host
        self.superclass  =  tag

        #SUB_COLLECTIONS
    def __new__(cls, host, tag, context):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, tag, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/hosts/{host:id}/tags/{tag:id}',
            {
                '{host:id}': self.parentclass.get_id(),
                '{tag:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class HostTags(Base):

    def __init__(self, host , context):
        Base.__init__(self, context)
        self.parentclass = host

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, tag, expect=None, correlation_id=None):

        '''
        @type Tag:

        @param tag.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/hosts/{host:id}/tags'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{host:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(tag),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return HostTag(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/hosts/{host:id}/tags'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{host:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return HostTag(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_tag()

            return HostTag(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Tags:
        '''

        url = '/hosts/{host:id}/tags'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{host:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_tag()

        return ParseHelper.toSubCollection(
            HostTag,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Hosts(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, host, expect=None, correlation_id=None):
        '''
        @type Host:

        Overload 1:
          @param host.name: string
          @param host.address: string
          @param host.root_password: string
          @param host.cluster.id|name: string
          [@param host.comment: string]
          [@param host.port: int]
          [@param host.display.address: string]
          [@param host.spm.priority: int]
          [@param host.power_management.type: string]
          [@param host.power_management.enabled: boolean]
          [@param host.power_management.address: string]
          [@param host.power_management.username: string]
          [@param host.power_management.automatic_pm_enabled: boolean]
          [@param host.power_management.password: string]
          [@param host.power_management.options.option: collection]
          {
            [@ivar option.name: string]
            [@ivar option.value: string]
          }
          [@param host.power_management.pm_proxy: collection]
          {
            [@ivar propietary: string]
          }
          [@param host.power_management.agents.agent: collection]
          {
            [@ivar type: string]
            [@ivar address: string]
            [@ivar username: string]
            [@ivar password: string]
            [@ivar options.option: collection]
            {
              [@param option.name: string]
              [@param option.value: string]
            }
          }
          [@param host.reboot_after_installation: boolean]
          [@param host.override_iptables: boolean]
          [@param host.power_management.kdump_detection: boolean]
          [@param host.protocol: int]
        Overload 2:
          @param host.name: string
          @param host.address: string
          @param host.cluster.id|name: string
          [@param host.comment: string]
          [@param host.ssh.port: int]
          [@param host.ssh.fingerprint: string]
          [@param host.ssh.authentication_method: string]
          [@param host.ssh.user.user_name: string]
          [@param host.ssh.user.password: string]
          [@param host.port: int]
          [@param host.display.address: string]
          [@param host.spm.priority: int]
          [@param host.power_management.type: string]
          [@param host.power_management.automatic_pm_enabled: boolean]
          [@param host.power_management.enabled: boolean]
          [@param host.power_management.address: string]
          [@param host.power_management.username: string]
          [@param host.power_management.password: string]
          [@param host.power_management.options.option: collection]
          {
            [@ivar option.name: string]
            [@ivar option.value: string]
          }
          [@param host.power_management.pm_proxy: collection]
          {
            [@ivar propietary: string]
          }
          [@param host.power_management.agents.agent: collection]
          {
            [@ivar type: string]
            [@ivar address: string]
            [@ivar username: string]
            [@ivar password: string]
            [@ivar options.option: collection]
            {
              [@param option.name: string]
              [@param option.value: string]
            }
          }
          [@param host.reboot_after_installation: boolean]
          [@param host.override_iptables: boolean]
          [@param host.power_management.kdump_detection: boolean]
          [@param host.protocol: int]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Host:
        '''

        url = '/hosts'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(host),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Host(result, self.context)

    def get(self, name=None, all_content=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]
        [@param all_content: true|false]

        @return Hosts:
        '''

        url = '/hosts'

        if id:
            try :
                return Host(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={"All-Content":all_content}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={"All-Content":all_content}
            ).get_host()

            return Host(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, all_content=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param all_content: true|false]

        @return Hosts:
        '''

        url='/hosts'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={"All-Content":all_content}
        ).get_host()

        return ParseHelper.toCollection(
            Host,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Instancetype(params.InstanceType, Base):
    def __init__(self, instancetype, context):
        Base.__init__(self, context)
        self.superclass = instancetype

        self.nics = InstancetypeNics(self, context)
        self.watchdogs = InstancetypeWatchdogs(self, context)

    def __new__(cls, instancetype, context):
        if instancetype is None: return None
        obj = object.__new__(cls)
        obj.__init__(instancetype, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/instancetypes/{instancetype:id}',
            {
                '{instancetype:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self):
        '''
        @return InstanceType:
        '''

        url = '/instancetypes/{instancetype:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{instancetype:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={}
        )

        return Instancetype(result, self.context)

class InstancetypeNic(params.NIC, Base):
    def __init__(self, instancetype, nic, context):
        Base.__init__(self, context)
        self.parentclass = instancetype
        self.superclass  =  nic

        #SUB_COLLECTIONS
    def __new__(cls, instancetype, nic, context):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(instancetype, nic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/instancetypes/{instancetype:id}/nics/{nic:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{instancetype:id}': self.parentclass.get_id(),
                    '{nic:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def update(self):
        '''
        @return NIC:
        '''

        url = '/instancetypes/{instancetype:id}/nics/{nic:id}'
        url = UrlHelper.replace(
            url,
            {
                '{instancetype:id}': self.parentclass.get_id(),
                '{nic:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={}
        )

        return InstancetypeNic(
            self.parentclass,
            result,
            self.context
        )

class InstancetypeNics(Base):

    def __init__(self, instancetype , context):
        Base.__init__(self, context)
        self.parentclass = instancetype

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, nic):

        '''
        @type NIC:


        @return NIC:
        '''

        url = '/instancetypes/{instancetype:id}/nics'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{instancetype:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(nic),
            headers={}
        )

        return InstancetypeNic(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Nics:
        '''

        url = '/instancetypes/{instancetype:id}/nics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{instancetype:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return InstancetypeNic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{instancetype:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_nic()

            return InstancetypeNic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Nics:
        '''

        url = '/instancetypes/{instancetype:id}/nics'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{instancetype:id}': self.parentclass.get_id(),
                }
            )
        ).get_nic()

        return ParseHelper.toSubCollection(
            InstancetypeNic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class InstancetypeWatchdog(params.WatchDog, Base):
    def __init__(self, instancetype, watchdog, context):
        Base.__init__(self, context)
        self.parentclass = instancetype
        self.superclass  =  watchdog

        #SUB_COLLECTIONS
    def __new__(cls, instancetype, watchdog, context):
        if watchdog is None: return None
        obj = object.__new__(cls)
        obj.__init__(instancetype, watchdog, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/instancetypes/{instancetype:id}/watchdogs/{watchdog:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{instancetype:id}': self.parentclass.get_id(),
                    '{watchdog:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

    def update(self):
        '''
        @return WatchDog:
        '''

        url = '/instancetypes/{instancetype:id}/watchdogs/{watchdog:id}'
        url = UrlHelper.replace(
            url,
            {
                '{instancetype:id}': self.parentclass.get_id(),
                '{watchdog:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={}
        )

        return InstancetypeWatchdog(
            self.parentclass,
            result,
            self.context
        )

class InstancetypeWatchdogs(Base):

    def __init__(self, instancetype , context):
        Base.__init__(self, context)
        self.parentclass = instancetype

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, watchdog):

        '''
        @type WatchDog:


        @return WatchDog:
        '''

        url = '/instancetypes/{instancetype:id}/watchdogs'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{instancetype:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(watchdog),
            headers={}
        )

        return InstancetypeWatchdog(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return WatchDogs:
        '''

        url = '/instancetypes/{instancetype:id}/watchdogs'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{instancetype:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return InstancetypeWatchdog(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{instancetype:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_watchdog()

            return InstancetypeWatchdog(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return WatchDogs:
        '''

        url = '/instancetypes/{instancetype:id}/watchdogs'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{instancetype:id}': self.parentclass.get_id(),
                }
            )
        ).get_watchdog()

        return ParseHelper.toSubCollection(
            InstancetypeWatchdog,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Instancetypes(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, instancetype, expect=None, correlation_id=None):
        '''
        @type InstanceType:

        @param instance_type.name: string
        [@param instance_type.memory: long]
        [@param instance_type.cpu.topology.cores: int]
        [@param instance_type.high_availability.enabled: boolean]
        [@param instance_type.origin: string]
        [@param instance_type.high_availability.priority: int]
        [@param instance_type.console.enabled: boolean]
        [@param instance_type.description: string]
        [@param instance_type.os.boot: collection]
        {
          [@ivar boot.dev: string]
        }
        [@param instance_type.cpu.topology.sockets: int]
        [@param instance_type.cpu_shares: int]
        [@param instance_type.cpu.architecture: string]
        [@param instance_type.display.type: string]
        [@param instance_type.display.monitors: int]
        [@param instance_typeay.single_qxl_pci: boolean]
        [@param instance_type.display.smartcard_enabled: boolean]
        [@param instance_type.usb.enabled: boolean]
        [@param instance_type.usb.type: string]
        [@param instance_type.migration_downtime: int]
        [@param instance_type.virtio_scsi.enabled: boolean]
        [@param instance_type.soundcard_enabled: boolean]
        [@param instance_type.custom_emulated_machine: string]
        [@param instance_type.custom_cpu_model: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return InstanceType:
        '''

        url = '/instancetypes'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(instancetype),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Instancetype(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return InstanceTypes:
        '''

        url = '/instancetypes'

        if id:
            try :
                return Instancetype(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_instance_type()

            return Instancetype(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return InstanceTypes:
        '''

        url='/instancetypes'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_instance_type()

        return ParseHelper.toCollection(
            Instancetype,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Job(params.Job, Base):
    def __init__(self, job, context):
        Base.__init__(self, context)
        self.superclass = job

        self.steps = JobSteps(self, context)

    def __new__(cls, job, context):
        if job is None: return None
        obj = object.__new__(cls)
        obj.__init__(job, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def clear(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/jobs/{job:id}/clear'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{job:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def end(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.status.state: string
        [@param action.force: boolean]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/jobs/{job:id}/end'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{job:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class JobStep(params.Step, Base):
    def __init__(self, job, step, context):
        Base.__init__(self, context)
        self.parentclass = job
        self.superclass  =  step

        self.statistics = JobStepStatistics(self, context)

    def __new__(cls, job, step, context):
        if step is None: return None
        obj = object.__new__(cls)
        obj.__init__(job, step, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def end(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.succeeded: boolean
        [@param action.force: boolean]
        [@param action.status.state: string]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/jobs/{job:id}/steps/{step:id}/end'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{job:id}': self.parentclass.get_id(),
                    '{step:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class JobStepStatistic(params.Statistic, Base):
    def __init__(self, step, statistic, context):
        Base.__init__(self, context)
        self.parentclass = step
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, step, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(step, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class JobStepStatistics(Base):

    def __init__(self, step , context):
        Base.__init__(self, context)
        self.parentclass = step

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/jobs/{job:id}/steps/{step:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{job:id}': self.parentclass.parentclass.get_id(),
                                '{step:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return JobStepStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{job:id}': self.parentclass.parentclass.get_id(),
                        '{step:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return JobStepStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Statistics:
        '''

        url = '/jobs/{job:id}/steps/{step:id}/statistics'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{job:id}': self.parentclass.parentclass.get_id(),
                        '{step:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_statistic()

        return ParseHelper.toSubCollection(
            JobStepStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class JobSteps(Base):

    def __init__(self, job , context):
        Base.__init__(self, context)
        self.parentclass = job

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, step, expect=None, correlation_id=None):

        '''
        @type Step:

        @param step.type: string
        @param step.description: string
        [@param step.job.id: string]
        [@param step.parent_step.id: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Step:
        '''

        url = '/jobs/{job:id}/steps'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{job:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(step),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return JobStep(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Steps:
        '''

        url = '/jobs/{job:id}/steps'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{job:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return JobStep(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{job:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_step()

            return JobStep(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Steps:
        '''

        url = '/jobs/{job:id}/steps'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{job:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_step()

        return ParseHelper.toSubCollection(
            JobStep,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Jobs(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, job, expect=None, correlation_id=None):
        '''
        @type Job:

        @param job.description: string
        [@param job.auto_cleared: boolean]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Job:
        '''

        url = '/jobs'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(job),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Job(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Jobs:
        '''

        url = '/jobs'

        if id:
            try :
                return Job(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_job()

            return Job(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return Jobs:
        '''

        url='/jobs'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_job()

        return ParseHelper.toCollection(
            Job,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Katelloerrata(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return KatelloErrata:
        '''

        url = '/katelloerrata'

        if id:
            try :
                return Katelloerrata(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_katello_erratum()

            return Katelloerrata(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return KatelloErrata:
        '''

        url='/katelloerrata'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_katello_erratum()

        return ParseHelper.toCollection(
            Katelloerrata,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Macpool(params.MacPool, Base):
    def __init__(self, macpool, context):
        Base.__init__(self, context)
        self.superclass = macpool

        #SUB_COLLECTIONS
    def __new__(cls, macpool, context):
        if macpool is None: return None
        obj = object.__new__(cls)
        obj.__init__(macpool, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/macpools/{macpool:id}',
            {
                '{macpool:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param macpool.name: string]
        [@param macpool.description: string]
        [@param macpool.allow_duplicates: boolean]
        [@param macpool.default_pool: boolean]
        [@param macpool.ranges.range: collection]
        {
          [@ivar range.from: string]
          [@ivar range.to: string]
        }
        [@param correlation_id: any string]

        @return MacPool:
        '''

        url = '/macpools/{macpool:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{macpool:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Macpool(result, self.context)

class Macpools(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, macpool, expect=None, correlation_id=None):
        '''
        @type MacPool:

        @param macpool.name: string
        @param macpool.ranges.range: collection
        {
          @ivar range.from: string
          @ivar range.to: string
        }
        [@param macpool.description: string]
        [@param macpool.allow_duplicates: boolean]
        [@param macpool.default_pool: boolean]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return MacPool:
        '''

        url = '/macpools'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(macpool),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Macpool(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return MacPools:
        '''

        url = '/macpools'

        if id:
            try :
                return Macpool(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_mac_pool()

            return Macpool(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return MacPools:
        '''

        url='/macpools'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_mac_pool()

        return ParseHelper.toCollection(
            Macpool,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Network(params.Network, Base):
    def __init__(self, network, context):
        Base.__init__(self, context)
        self.superclass = network

        self.labels = NetworkLabels(self, context)
        self.permissions = NetworkPermissions(self, context)
        self.vnicprofiles = NetworkVnicprofiles(self, context)

    def __new__(cls, network, context):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(network, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/networks/{network:id}',
            {
                '{network:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param network.name: string]
        [@param network.description: string]
        [@param network.comment: string]
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

        url = '/networks/{network:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{network:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Network(result, self.context)

class NetworkLabel(params.Label, Base):
    def __init__(self, network, label, context):
        Base.__init__(self, context)
        self.parentclass = network
        self.superclass  =  label

        #SUB_COLLECTIONS
    def __new__(cls, network, label, context):
        if label is None: return None
        obj = object.__new__(cls)
        obj.__init__(network, label, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/networks/{network:id}/labels/{label:id}',
            {
                '{network:id}': self.parentclass.get_id(),
                '{label:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class NetworkLabels(Base):

    def __init__(self, network , context):
        Base.__init__(self, context)
        self.parentclass = network

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, label, expect=None, correlation_id=None):

        '''
        @type Label:

        @param label.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Label:
        '''

        url = '/networks/{network:id}/labels'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{network:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(label),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return NetworkLabel(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Labels:
        '''

        url = '/networks/{network:id}/labels'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{network:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return NetworkLabel(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_label()

            return NetworkLabel(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Labels:
        '''

        url = '/networks/{network:id}/labels'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{network:id}': self.parentclass.get_id(),
                }
            )
        ).get_label()

        return ParseHelper.toSubCollection(
            NetworkLabel,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class NetworkPermission(params.Permission, Base):
    def __init__(self, network, permission, context):
        Base.__init__(self, context)
        self.parentclass = network
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, network, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(network, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/networks/{network:id}/permissions/{permission:id}',
            {
                '{network:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class NetworkPermissions(Base):

    def __init__(self, network , context):
        Base.__init__(self, context)
        self.parentclass = network

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.group.id: string
          @param permission.role.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/networks/{network:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{network:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return NetworkPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/networks/{network:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{network:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return NetworkPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return NetworkPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/networks/{network:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            NetworkPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class NetworkVnicprofile(params.VnicProfile, Base):
    def __init__(self, network, vnicprofile, context):
        Base.__init__(self, context)
        self.parentclass = network
        self.superclass  =  vnicprofile

        self.permissions = NetworkVnicprofilePermissions(self, context)

    def __new__(cls, network, vnicprofile, context):
        if vnicprofile is None: return None
        obj = object.__new__(cls)
        obj.__init__(network, vnicprofile, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/networks/{network:id}/vnicprofiles/{vnicprofile:id}',
            {
                '{network:id}': self.parentclass.get_id(),
                '{vnicprofile:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class NetworkVnicprofilePermission(params.Permission, Base):
    def __init__(self, vnicprofile, permission, context):
        Base.__init__(self, context)
        self.parentclass = vnicprofile
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, vnicprofile, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vnicprofile, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions/{permission:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{network:id}': self.parentclass.parentclass.get_id(),
                    '{vnicprofile:id}': self.parentclass.get_id(),
                    '{permission:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class NetworkVnicprofilePermissions(Base):

    def __init__(self, vnicprofile , context):
        Base.__init__(self, context)
        self.parentclass = vnicprofile

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission):

        '''
        @type Permission:


        @return Permission:
        '''

        url = '/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{network:id}': self.parentclass.parentclass.get_id(),
                    '{vnicprofile:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={}
        )

        return NetworkVnicprofilePermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{network:id}': self.parentclass.parentclass.get_id(),
                                '{vnicprofile:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return NetworkVnicprofilePermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{network:id}': self.parentclass.parentclass.get_id(),
                        '{vnicprofile:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return NetworkVnicprofilePermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Permissions:
        '''

        url = '/networks/{network:id}/vnicprofiles/{vnicprofile:id}/permissions'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{network:id}': self.parentclass.parentclass.get_id(),
                    '{vnicprofile:id}': self.parentclass.get_id(),
                }
            )
        ).get_permission()

        return ParseHelper.toSubCollection(
            NetworkVnicprofilePermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class NetworkVnicprofiles(Base):

    def __init__(self, network , context):
        Base.__init__(self, context)
        self.parentclass = network

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, vnicprofile, expect=None, correlation_id=None):

        '''
        @type VnicProfile:

        @param vnicprofile.name: string
        [@param vnicprofile.description: string]
        [@param vnicprofile.port_mirroring: boolean]
        [@param vnicprofile.custom_properties.custom_property: collection]
        {
          [@ivar custom_property.name: string]
          [@ivar custom_property.value: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return VnicProfile:
        '''

        url = '/networks/{network:id}/vnicprofiles'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{network:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(vnicprofile),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return NetworkVnicprofile(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return VnicProfiles:
        '''

        url = '/networks/{network:id}/vnicprofiles'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{network:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return NetworkVnicprofile(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_vnic_profile()

            return NetworkVnicprofile(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return VnicProfiles:
        '''

        url = '/networks/{network:id}/vnicprofiles'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_vnic_profile()

        return ParseHelper.toSubCollection(
            NetworkVnicprofile,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Networks(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, network, expect=None, correlation_id=None):
        '''
        @type Network:

        @param network.data_center.id|name: string
        @param network.name: string
        [@param network.description: string]
        [@param network.comment: string]
        [@param network.vlan.id: string]
        [@param network.ip.address: string]
        [@param network.ip.gateway: string]
        [@param network.ip.netmask: string]
        [@param network.stp: boolean]
        [@param network.mtu: int]
        [@param network.profile_required: boolean]
        [@param network.usages.usage: collection]
        {
          [@ivar usage: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Network:
        '''

        url = '/networks'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(network),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Network(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Networks:
        '''

        url = '/networks'

        if id:
            try :
                return Network(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={}
            ).get_network()

            return Network(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Networks:
        '''

        url='/networks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={}
        ).get_network()

        return ParseHelper.toCollection(
            Network,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Openstackimageprovider(params.OpenStackImageProvider, Base):
    def __init__(self, openstackimageprovider, context):
        Base.__init__(self, context)
        self.superclass = openstackimageprovider

        self.certificates = OpenstackimageproviderCertificates(self, context)
        self.images = OpenstackimageproviderImages(self, context)

    def __new__(cls, openstackimageprovider, context):
        if openstackimageprovider is None: return None
        obj = object.__new__(cls)
        obj.__init__(openstackimageprovider, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/openstackimageproviders/{openstackimageprovider:id}',
            {
                '{openstackimageprovider:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param openstack_image_provider.name: string]
        [@param openstack_image_provider.description: string]
        [@param openstack_image_provider.requires_authentication: boolean]
        [@param openstack_image_provider.username: string]
        [@param openstack_image_provider.password: string]
        [@param openstack_image_provider.properties.property: collection]
        {
          [@ivar property.name: string]
          [@ivar property.value: string]
        }
        [@param correlation_id: any string]

        @return OpenStackImageProvider:
        '''

        url = '/openstackimageproviders/{openstackimageprovider:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{openstackimageprovider:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Openstackimageprovider(result, self.context)

    def importcertificates(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/openstackimageproviders/{openstackimageprovider:id}/importcertificates'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{openstackimageprovider:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def testconnectivity(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/openstackimageproviders/{openstackimageprovider:id}/testconnectivity'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{openstackimageprovider:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class OpenstackimageproviderCertificate(params.Certificate, Base):
    def __init__(self, openstackimageprovider, certificate, context):
        Base.__init__(self, context)
        self.parentclass = openstackimageprovider
        self.superclass  =  certificate

        #SUB_COLLECTIONS
    def __new__(cls, openstackimageprovider, certificate, context):
        if certificate is None: return None
        obj = object.__new__(cls)
        obj.__init__(openstackimageprovider, certificate, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class OpenstackimageproviderCertificates(Base):

    def __init__(self, openstackimageprovider , context):
        Base.__init__(self, context)
        self.parentclass = openstackimageprovider

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Certificates:
        '''

        url = '/openstackimageproviders/{openstackimageprovider:id}/certificates'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{openstackimageprovider:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return OpenstackimageproviderCertificate(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{openstackimageprovider:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_certificate()

            return OpenstackimageproviderCertificate(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Certificates:
        '''

        url = '/openstackimageproviders/{openstackimageprovider:id}/certificates'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{openstackimageprovider:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_certificate()

        return ParseHelper.toSubCollection(
            OpenstackimageproviderCertificate,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class OpenstackimageproviderImage(params.OpenStackImage, Base):
    def __init__(self, openstackimageprovider, openstackimage, context):
        Base.__init__(self, context)
        self.parentclass = openstackimageprovider
        self.superclass  =  openstackimage

        #SUB_COLLECTIONS
    def __new__(cls, openstackimageprovider, openstackimage, context):
        if openstackimage is None: return None
        obj = object.__new__(cls)
        obj.__init__(openstackimageprovider, openstackimage, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def import_image(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/openstackimageproviders/{openstackimageprovider:id}/images/{image:id}/import'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{openstackimageprovider:id}': self.parentclass.get_id(),
                    '{image:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

class OpenstackimageproviderImages(Base):

    def __init__(self, openstackimageprovider , context):
        Base.__init__(self, context)
        self.parentclass = openstackimageprovider

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return OpenStackImages:
        '''

        url = '/openstackimageproviders/{openstackimageprovider:id}/images'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{openstackimageprovider:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return OpenstackimageproviderImage(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{openstackimageprovider:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_openstack_image()

            return OpenstackimageproviderImage(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return OpenStackImages:
        '''

        url = '/openstackimageproviders/{openstackimageprovider:id}/images'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{openstackimageprovider:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_openstack_image()

        return ParseHelper.toSubCollection(
            OpenstackimageproviderImage,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Openstackimageproviders(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, openstackimageprovider, expect=None, correlation_id=None):
        '''
        @type OpenStackImageProvider:

        @param openstack_image_provider.name: string
        [@param openstack_image_provider.description: string]
        [@param openstack_image_provider.url: string]
        [@param openstack_image_provider.requires_authentication: boolean]
        [@param openstack_image_provider.username: string]
        [@param openstack_image_provider.password: string]
        [@param openstack_image_provider.properties.property: collection]
        {
          [@ivar property.name: string]
          [@ivar property.value: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return OpenStackImageProvider:
        '''

        url = '/openstackimageproviders'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(openstackimageprovider),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Openstackimageprovider(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return OpenStackImageProviders:
        '''

        url = '/openstackimageproviders'

        if id:
            try :
                return Openstackimageprovider(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_openstack_image_provider()

            return Openstackimageprovider(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return OpenStackImageProviders:
        '''

        url='/openstackimageproviders'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_openstack_image_provider()

        return ParseHelper.toCollection(
            Openstackimageprovider,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Openstacknetworkprovider(params.OpenStackNetworkProvider, Base):
    def __init__(self, openstacknetworkprovider, context):
        Base.__init__(self, context)
        self.superclass = openstacknetworkprovider

        self.certificates = OpenstacknetworkproviderCertificates(self, context)
        self.networks = OpenstacknetworkproviderNetworks(self, context)

    def __new__(cls, openstacknetworkprovider, context):
        if openstacknetworkprovider is None: return None
        obj = object.__new__(cls)
        obj.__init__(openstacknetworkprovider, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/openstacknetworkproviders/{openstacknetworkprovider:id}',
            {
                '{openstacknetworkprovider:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param openstack_network_provider.name: string]
        [@param openstack_network_provider.description: string]
        [@param openstack_network_provider.requires_authentication: boolean]
        [@param openstack_network_provider.username: string]
        [@param openstack_network_provider.password: string]
        [@param openstack_network_provider.properties.property: collection]
        {
          [@ivar property.name: string]
          [@ivar property.value: string]
        }
        [@param correlation_id: any string]

        @return OpenStackNetworkProvider:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{openstacknetworkprovider:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Openstacknetworkprovider(result, self.context)

    def importcertificates(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}/importcertificates'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{openstacknetworkprovider:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def testconnectivity(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}/testconnectivity'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{openstacknetworkprovider:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

class OpenstacknetworkproviderCertificate(params.Certificate, Base):
    def __init__(self, openstacknetworkprovider, certificate, context):
        Base.__init__(self, context)
        self.parentclass = openstacknetworkprovider
        self.superclass  =  certificate

        #SUB_COLLECTIONS
    def __new__(cls, openstacknetworkprovider, certificate, context):
        if certificate is None: return None
        obj = object.__new__(cls)
        obj.__init__(openstacknetworkprovider, certificate, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class OpenstacknetworkproviderCertificates(Base):

    def __init__(self, openstacknetworkprovider , context):
        Base.__init__(self, context)
        self.parentclass = openstacknetworkprovider

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Certificates:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}/certificates'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{openstacknetworkprovider:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return OpenstacknetworkproviderCertificate(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{openstacknetworkprovider:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_certificate()

            return OpenstacknetworkproviderCertificate(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Certificates:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}/certificates'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{openstacknetworkprovider:id}': self.parentclass.get_id(),
                }
            )
        ).get_certificate()

        return ParseHelper.toSubCollection(
            OpenstacknetworkproviderCertificate,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class OpenstacknetworkproviderNetwork(params.OpenStackNetwork, Base):
    def __init__(self, openstacknetworkprovider, openstacknetwork, context):
        Base.__init__(self, context)
        self.parentclass = openstacknetworkprovider
        self.superclass  =  openstacknetwork

        self.subnets = OpenstacknetworkproviderNetworkSubnets(self, context)

    def __new__(cls, openstacknetworkprovider, openstacknetwork, context):
        if openstacknetwork is None: return None
        obj = object.__new__(cls)
        obj.__init__(openstacknetworkprovider, openstacknetwork, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class OpenstacknetworkproviderNetworkSubnet(params.OpenStackSubnet, Base):
    def __init__(self, openstacknetwork, openstacksubnet, context):
        Base.__init__(self, context)
        self.parentclass = openstacknetwork
        self.superclass  =  openstacksubnet

        #SUB_COLLECTIONS
    def __new__(cls, openstacknetwork, openstacksubnet, context):
        if openstacksubnet is None: return None
        obj = object.__new__(cls)
        obj.__init__(openstacknetwork, openstacksubnet, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}/networks/{network:id}/subnets/{subnet:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{openstacknetworkprovider:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                    '{subnet:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class OpenstacknetworkproviderNetworkSubnets(Base):

    def __init__(self, openstacknetwork , context):
        Base.__init__(self, context)
        self.parentclass = openstacknetwork

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, openstacksubnet):

        '''
        @type OpenStackSubnet:


        @return OpenStackSubnet:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}/networks/{network:id}/subnets'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{openstacknetworkprovider:id}': self.parentclass.parentclass.get_id(),
                    '{network:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(openstacksubnet),
            headers={}
        )

        return OpenstacknetworkproviderNetworkSubnet(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return OpenStackSubnets:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}/networks/{network:id}/subnets'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{openstacknetworkprovider:id}': self.parentclass.parentclass.get_id(),
                                '{network:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return OpenstacknetworkproviderNetworkSubnet(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{openstacknetworkprovider:id}': self.parentclass.parentclass.get_id(),
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_openstack_subnet()

            return OpenstacknetworkproviderNetworkSubnet(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return OpenStackSubnets:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}/networks/{network:id}/subnets'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{openstacknetworkprovider:id}': self.parentclass.parentclass.get_id(),
                        '{network:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_openstack_subnet()

        return ParseHelper.toSubCollection(
            OpenstacknetworkproviderNetworkSubnet,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class OpenstacknetworkproviderNetworks(Base):

    def __init__(self, openstacknetworkprovider , context):
        Base.__init__(self, context)
        self.parentclass = openstacknetworkprovider

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return OpenStackNetworks:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}/networks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{openstacknetworkprovider:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return OpenstacknetworkproviderNetwork(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{openstacknetworkprovider:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_openstack_network()

            return OpenstacknetworkproviderNetwork(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return OpenStackNetworks:
        '''

        url = '/openstacknetworkproviders/{openstacknetworkprovider:id}/networks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{openstacknetworkprovider:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_openstack_network()

        return ParseHelper.toSubCollection(
            OpenstacknetworkproviderNetwork,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Openstacknetworkproviders(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, openstacknetworkprovider, expect=None, correlation_id=None):
        '''
        @type OpenStackNetworkProvider:

        @param openstack_network_provider.name: string
        [@param openstack_network_provider.description: string]
        [@param openstack_network_provider.url: string]
        [@param openstack_network_provider.requires_authentication: boolean]
        [@param openstack_network_provider.username: string]
        [@param openstack_network_provider.password: string]
        [@param openstack_network_provider.properties.property: collection]
        {
          [@ivar property.name: string]
          [@ivar property.value: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return OpenStackNetworkProvider:
        '''

        url = '/openstacknetworkproviders'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(openstacknetworkprovider),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Openstacknetworkprovider(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return OpenStackNetworkProviders:
        '''

        url = '/openstacknetworkproviders'

        if id:
            try :
                return Openstacknetworkprovider(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_openstack_network_provider()

            return Openstacknetworkprovider(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return OpenStackNetworkProviders:
        '''

        url='/openstacknetworkproviders'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_openstack_network_provider()

        return ParseHelper.toCollection(
            Openstacknetworkprovider,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Operatingsystem(params.OperatingSystemInfo, Base):
    def __init__(self, operatingsysteminfo, context):
        Base.__init__(self, context)
        self.superclass = operatingsysteminfo

        #SUB_COLLECTIONS
    def __new__(cls, operatingsysteminfo, context):
        if operatingsysteminfo is None: return None
        obj = object.__new__(cls)
        obj.__init__(operatingsysteminfo, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class Operatingsystems(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return OperatingSystemInfos:
        '''

        url = '/operatingsystems'

        if id:
            try :
                return Operatingsystem(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_operating_system()

            return Operatingsystem(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]

        @return OperatingSystemInfos:
        '''

        url='/operatingsystems'

        result = self.__getProxy().get(
            url=url
        ).get_operating_system()

        return ParseHelper.toCollection(
            Operatingsystem,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )
class Permission(params.Permission, Base):
    def __init__(self, permission, context):
        Base.__init__(self, context)
        self.superclass = permission

        #SUB_COLLECTIONS
    def __new__(cls, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/permissions/{permission:id}',
            {
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class Permissions(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/permissions'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(permission),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Permission(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/permissions'

        if id:
            try :
                return Permission(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_permission()

            return Permission(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url='/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_permission()

        return ParseHelper.toCollection(
            Permission,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Role(params.Role, Base):
    def __init__(self, role, context):
        Base.__init__(self, context)
        self.superclass = role

        self.permits = RolePermits(self, context)

    def __new__(cls, role, context):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(role, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/roles/{role:id}',
            {
                '{role:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

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

        url = '/roles/{role:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{role:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Role(result, self.context)

class RolePermit(params.Permit, Base):
    def __init__(self, role, permit, context):
        Base.__init__(self, context)
        self.parentclass = role
        self.superclass  =  permit

        #SUB_COLLECTIONS
    def __new__(cls, role, permit, context):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(role, permit, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/roles/{role:id}/permits/{permit:id}',
            {
                '{role:id}': self.parentclass.get_id(),
                '{permit:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class RolePermits(Base):

    def __init__(self, role , context):
        Base.__init__(self, context)
        self.parentclass = role

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permit, expect=None, correlation_id=None):

        '''
        @type Permit:

        @param permit.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permit:
        '''

        url = '/roles/{role:id}/permits'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{role:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permit),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return RolePermit(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permits:
        '''

        url = '/roles/{role:id}/permits'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{role:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return RolePermit(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{role:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permit()

            return RolePermit(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permits:
        '''

        url = '/roles/{role:id}/permits'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{role:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permit()

        return ParseHelper.toSubCollection(
            RolePermit,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Roles(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/roles'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(role),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Role(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Roles:
        '''

        url = '/roles'

        if id:
            try :
                return Role(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_role()

            return Role(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return Roles:
        '''

        url='/roles'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_role()

        return ParseHelper.toCollection(
            Role,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Schedulingpolicies(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, schedulingpolicy, expect=None, correlation_id=None):
        '''
        @type SchedulingPolicy:

        @param schedulingpolicy.name: string
        [@param schedulingpolicy.description: string]
        [@param schedulingpolicy.properties.property: collection]
        {
          [@ivar property.name: string]
          [@ivar property.value: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return SchedulingPolicy:
        '''

        url = '/schedulingpolicies'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(schedulingpolicy),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Schedulingpolicy(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return SchedulingPolicies:
        '''

        url = '/schedulingpolicies'

        if id:
            try :
                return Schedulingpolicy(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_scheduling_policy()

            return Schedulingpolicy(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return SchedulingPolicies:
        '''

        url='/schedulingpolicies'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={}
        ).get_scheduling_policy()

        return ParseHelper.toCollection(
            Schedulingpolicy,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Schedulingpolicy(params.SchedulingPolicy, Base):
    def __init__(self, schedulingpolicy, context):
        Base.__init__(self, context)
        self.superclass = schedulingpolicy

        self.balances = SchedulingpolicyBalances(self, context)
        self.filters = SchedulingpolicyFilters(self, context)
        self.weights = SchedulingpolicyWeights(self, context)

    def __new__(cls, schedulingpolicy, context):
        if schedulingpolicy is None: return None
        obj = object.__new__(cls)
        obj.__init__(schedulingpolicy, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/schedulingpolicies/{schedulingpolicy:id}',
            {
                '{schedulingpolicy:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param schedulingpolicy.name: string]
        [@param schedulingpolicy.description: string]
        [@param schedulingpolicy.properties.property: collection]
        {
          [@ivar property.name: string]
          [@ivar property.value: string]
        }
        [@param correlation_id: any string]

        @return SchedulingPolicy:
        '''

        url = '/schedulingpolicies/{schedulingpolicy:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{schedulingpolicy:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Schedulingpolicy(result, self.context)

class SchedulingpolicyBalance(params.Balance, Base):
    def __init__(self, schedulingpolicy, balance, context):
        Base.__init__(self, context)
        self.parentclass = schedulingpolicy
        self.superclass  =  balance

        #SUB_COLLECTIONS
    def __new__(cls, schedulingpolicy, balance, context):
        if balance is None: return None
        obj = object.__new__(cls)
        obj.__init__(schedulingpolicy, balance, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/schedulingpolicies/{schedulingpolicy:id}/balances/{balance:id}',
            {
                '{schedulingpolicy:id}': self.parentclass.get_id(),
                '{balance:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class SchedulingpolicyBalances(Base):

    def __init__(self, schedulingpolicy , context):
        Base.__init__(self, context)
        self.parentclass = schedulingpolicy

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, balance, expect=None, correlation_id=None):

        '''
        @type Balance:

        @param balance.scheduling_policy_unit.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Balance:
        '''

        url = '/schedulingpolicies/{schedulingpolicy:id}/balances'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{schedulingpolicy:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(balance),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return SchedulingpolicyBalance(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Balances:
        '''

        url = '/schedulingpolicies/{schedulingpolicy:id}/balances'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{schedulingpolicy:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return SchedulingpolicyBalance(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{schedulingpolicy:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_balance()

            return SchedulingpolicyBalance(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Balances:
        '''

        url = '/schedulingpolicies/{schedulingpolicy:id}/balances'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{schedulingpolicy:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'case_sensitive:matrix':case_sensitive,'max:matrix':max}
            ),
            headers={}
        ).get_balance()

        return ParseHelper.toSubCollection(
            SchedulingpolicyBalance,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class SchedulingpolicyFilter(params.Filter, Base):
    def __init__(self, schedulingpolicy, filter, context):
        Base.__init__(self, context)
        self.parentclass = schedulingpolicy
        self.superclass  =  filter

        #SUB_COLLECTIONS
    def __new__(cls, schedulingpolicy, filter, context):
        if filter is None: return None
        obj = object.__new__(cls)
        obj.__init__(schedulingpolicy, filter, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/schedulingpolicies/{schedulingpolicy:id}/filters/{filter:id}',
            {
                '{schedulingpolicy:id}': self.parentclass.get_id(),
                '{filter:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class SchedulingpolicyFilters(Base):

    def __init__(self, schedulingpolicy , context):
        Base.__init__(self, context)
        self.parentclass = schedulingpolicy

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, filter, expect=None, correlation_id=None):

        '''
        @type Filter:

        @param filter.scheduling_policy_unit.id: string
        [@param filter.scheduling_policy_unit.position: int]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Filter:
        '''

        url = '/schedulingpolicies/{schedulingpolicy:id}/filters'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{schedulingpolicy:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(filter),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return SchedulingpolicyFilter(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Filters:
        '''

        url = '/schedulingpolicies/{schedulingpolicy:id}/filters'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{schedulingpolicy:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return SchedulingpolicyFilter(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{schedulingpolicy:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_filter()

            return SchedulingpolicyFilter(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Filters:
        '''

        url = '/schedulingpolicies/{schedulingpolicy:id}/filters'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{schedulingpolicy:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'case_sensitive:matrix':case_sensitive,'max:matrix':max}
            ),
            headers={}
        ).get_filter()

        return ParseHelper.toSubCollection(
            SchedulingpolicyFilter,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class SchedulingpolicyWeight(params.Weight, Base):
    def __init__(self, schedulingpolicy, weight, context):
        Base.__init__(self, context)
        self.parentclass = schedulingpolicy
        self.superclass  =  weight

        #SUB_COLLECTIONS
    def __new__(cls, schedulingpolicy, weight, context):
        if weight is None: return None
        obj = object.__new__(cls)
        obj.__init__(schedulingpolicy, weight, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/schedulingpolicies/{schedulingpolicy:id}/weights/{weight:id}',
            {
                '{schedulingpolicy:id}': self.parentclass.get_id(),
                '{weight:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class SchedulingpolicyWeights(Base):

    def __init__(self, schedulingpolicy , context):
        Base.__init__(self, context)
        self.parentclass = schedulingpolicy

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, weight, expect=None, correlation_id=None):

        '''
        @type Weight:

        @param weight.scheduling_policy_unit.id: string
        [@param weight.scheduling_policy_unit.factor: int]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Weight:
        '''

        url = '/schedulingpolicies/{schedulingpolicy:id}/weights'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{schedulingpolicy:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(weight),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return SchedulingpolicyWeight(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Weights:
        '''

        url = '/schedulingpolicies/{schedulingpolicy:id}/weights'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{schedulingpolicy:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return SchedulingpolicyWeight(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{schedulingpolicy:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_weight()

            return SchedulingpolicyWeight(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Weights:
        '''

        url = '/schedulingpolicies/{schedulingpolicy:id}/weights'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{schedulingpolicy:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'case_sensitive:matrix':case_sensitive,'max:matrix':max}
            ),
            headers={}
        ).get_weight()

        return ParseHelper.toSubCollection(
            SchedulingpolicyWeight,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Schedulingpolicyunit(params.SchedulingPolicyUnit, Base):
    def __init__(self, schedulingpolicyunit, context):
        Base.__init__(self, context)
        self.superclass = schedulingpolicyunit

        #SUB_COLLECTIONS
    def __new__(cls, schedulingpolicyunit, context):
        if schedulingpolicyunit is None: return None
        obj = object.__new__(cls)
        obj.__init__(schedulingpolicyunit, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/schedulingpolicyunits/{schedulingpolicyunit:id}',
            {
                '{schedulingpolicyunit:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class Schedulingpolicyunits(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return SchedulingPolicyUnits:
        '''

        url = '/schedulingpolicyunits'

        if id:
            try :
                return Schedulingpolicyunit(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_scheduling_policy_unit()

            return Schedulingpolicyunit(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return SchedulingPolicyUnits:
        '''

        url='/schedulingpolicyunits'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={}
        ).get_scheduling_policy_unit()

        return ParseHelper.toCollection(
            Schedulingpolicyunit,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Storageconnection(params.StorageConnection, Base):
    def __init__(self, storageconnection, context):
        Base.__init__(self, context)
        self.superclass = storageconnection

        #SUB_COLLECTIONS
    def __new__(cls, storageconnection, context):
        if storageconnection is None: return None
        obj = object.__new__(cls)
        obj.__init__(storageconnection, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, action=params.Action(), async=None, correlation_id=None):
        '''
        @type Action:

        [@param action.host.id|name: string]
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/storageconnections/{storageconnection:id}',
            {
                '{storageconnection:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

    def update(self, correlation_id=None):
        '''
        Overload 1:
          [@param storage_connection.port: int]
          [@param storage_connection.username: string]
          [@param storage_connection.password: string]
          [@param storage_connection.iqn: string]
          [@param storage_connection.address: string]
        Overload 2:
          [@param storage_connection.nfs_timeo: string]
          [@param storage_connection.nfs_version: string]
          [@param storage_connection.nfs_retrans: string]
          [@param storage_connection.address: string]
          [@param storage_connection.path: string]
        Overload 3:
          [@param storage_connection.mount_options: string]
          [@param storage_connection.vfs_type: string]
          [@param storage_connection.address: string]
          [@param storage_connection.path: string]
        Overload 4:
          [@param storage_connection.path: string]
        [@param correlation_id: any string]

        @return StorageConnection:
        '''

        url = '/storageconnections/{storageconnection:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{storageconnection:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Storageconnection(result, self.context)

class Storageconnections(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, storageconnection, expect=None, correlation_id=None):
        '''
        @type StorageConnection:

        Overload 1:
          @param storage_connection.address: string
          @param storage_connection.type: string
          @param storage_connection.iqn: string
          @param storage_connection.port: int
          [@param storage_connection.username: string]
          [@param storage_connection.password: string]
        Overload 2:
          @param storage_connection.address: string
          @param storage_connection.type: string
          @param storage_connection.path: string
          [@param storage_connection.nfs_timeo: string]
          [@param storage_connection.nfs_version: string]
          [@param storage_connection.nfs_retrans: string]
        Overload 3:
          @param storage_connection.type: string
          @param storage_connection.path: string
          @param storage_connection.vfs_type: string
          [@param storage_connection.address: string]
          [@param storage_connection.mount_options: string]
        Overload 4:
          @param storage_connection.type: string
          @param storage_connection.path: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return StorageConnection:
        '''

        url = '/storageconnections'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(storageconnection),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Storageconnection(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return StorageConnections:
        '''

        url = '/storageconnections'

        if id:
            try :
                return Storageconnection(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_storage_connection()

            return Storageconnection(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]

        @return StorageConnections:
        '''

        url='/storageconnections'

        result = self.__getProxy().get(
            url=url
        ).get_storage_connection()

        return ParseHelper.toCollection(
            Storageconnection,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )
class Storagedomain(params.StorageDomain, Base):
    def __init__(self, storagedomain, context):
        Base.__init__(self, context)
        self.superclass = storagedomain

        self.diskprofiles = StoragedomainDiskprofiles(self, context)
        self.disks = StoragedomainDisks(self, context)
        self.disksnapshots = StoragedomainDisksnapshots(self, context)
        self.files = StoragedomainFiles(self, context)
        self.images = StoragedomainImages(self, context)
        self.permissions = StoragedomainPermissions(self, context)
        self.storageconnections = StoragedomainStorageconnections(self, context)
        self.templates = StoragedomainTemplates(self, context)
        self.vms = StoragedomainVms(self, context)

    def __new__(cls, storagedomain, context):
        if storagedomain is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, storagedomain, async=None, correlation_id=None):
        '''
        @type StorageDomain:

        @param storagedomain.host.id|name: string
        [@param storagedomain.format: boolean]
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/storagedomains/{storagedomain:id}',
            {
                '{storagedomain:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            body=ParseHelper.toXml(storagedomain),
            headers={"Correlation-Id":correlation_id}
        )

    def update(self, correlation_id=None):
        '''
        Overload 1:
          [@param storagedomain.name: string]
        Overload 2:
          @param storagedomain.host.id|name: string
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
          [@param storagedomain.comment: string]
          [@param storagedomain.storage.override_luns: boolean]
          [@param storagedomain.wipe_after_delete: boolean]
        [@param correlation_id: any string]

        @return StorageDomain:
        '''

        url = '/storagedomains/{storagedomain:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Storagedomain(result, self.context)

    def isattached(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.host.id: string
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/storagedomains/{storagedomain:id}/isattached'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class StoragedomainDisk(params.Disk, Base):
    def __init__(self, storagedomain, disk, context):
        Base.__init__(self, context)
        self.parentclass = storagedomain
        self.superclass  =  disk

        self.permissions = StoragedomainDiskPermissions(self, context)
        self.statistics = StoragedomainDiskStatistics(self, context)

    def __new__(cls, storagedomain, disk, context):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, disk, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/storagedomains/{storagedomain:id}/disks/{disk:id}',
            {
                '{storagedomain:id}': self.parentclass.get_id(),
                '{disk:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def copy(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/storagedomains/{storagedomain:id}/disks/{disk:id}/copy'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def export(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param storagedomain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/storagedomains/{storagedomain:id}/disks/{disk:id}/export'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def move(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/storagedomains/{storagedomain:id}/disks/{disk:id}/move'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

class StoragedomainDiskPermission(params.Permission, Base):
    def __init__(self, disk, permission, context):
        Base.__init__(self, context)
        self.parentclass = disk
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, disk, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/storagedomains/{storagedomain:id}/disks/{disk:id}/permissions/{permission:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                    '{permission:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class StoragedomainDiskPermissions(Base):

    def __init__(self, disk , context):
        Base.__init__(self, context)
        self.parentclass = disk

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission):

        '''
        @type Permission:


        @return Permission:
        '''

        url = '/storagedomains/{storagedomain:id}/disks/{disk:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={}
        )

        return StoragedomainDiskPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/storagedomains/{storagedomain:id}/disks/{disk:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                                '{disk:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainDiskPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                        '{disk:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return StoragedomainDiskPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Permissions:
        '''

        url = '/storagedomains/{storagedomain:id}/disks/{disk:id}/permissions'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                }
            )
        ).get_permission()

        return ParseHelper.toSubCollection(
            StoragedomainDiskPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainDiskStatistic(params.Statistic, Base):
    def __init__(self, disk, statistic, context):
        Base.__init__(self, context)
        self.parentclass = disk
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, disk, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class StoragedomainDiskStatistics(Base):

    def __init__(self, disk , context):
        Base.__init__(self, context)
        self.parentclass = disk

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/storagedomains/{storagedomain:id}/disks/{disk:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                                '{disk:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainDiskStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                        '{disk:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return StoragedomainDiskStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Statistics:
        '''

        url = '/storagedomains/{storagedomain:id}/disks/{disk:id}/statistics'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                }
            )
        ).get_statistic()

        return ParseHelper.toSubCollection(
            StoragedomainDiskStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainDiskprofile(params.DiskProfile, Base):
    def __init__(self, storagedomain, diskprofile, context):
        Base.__init__(self, context)
        self.parentclass = storagedomain
        self.superclass  =  diskprofile

        #SUB_COLLECTIONS
    def __new__(cls, storagedomain, diskprofile, context):
        if diskprofile is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, diskprofile, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/storagedomains/{storagedomain:id}/diskprofiles/{diskprofile:id}',
            {
                '{storagedomain:id}': self.parentclass.get_id(),
                '{diskprofile:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class StoragedomainDiskprofiles(Base):

    def __init__(self, storagedomain , context):
        Base.__init__(self, context)
        self.parentclass = storagedomain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, diskprofile, expect=None, correlation_id=None):

        '''
        @type DiskProfile:

        @param diskprofile.name: string
        [@param diskprofile.description: string]
        [@param diskprofile.qos.id: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return DiskProfile:
        '''

        url = '/storagedomains/{storagedomain:id}/diskprofiles'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(diskprofile),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return StoragedomainDiskprofile(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return DiskProfiles:
        '''

        url = '/storagedomains/{storagedomain:id}/diskprofiles'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainDiskprofile(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_disk_profile()

            return StoragedomainDiskprofile(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return DiskProfiles:
        '''

        url = '/storagedomains/{storagedomain:id}/diskprofiles'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_disk_profile()

        return ParseHelper.toSubCollection(
            StoragedomainDiskprofile,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainDisks(Base):

    def __init__(self, storagedomain , context):
        Base.__init__(self, context)
        self.parentclass = storagedomain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, disk, expect=None, correlation_id=None):

        '''
        @type Disk:

        Overload 1:
          @param provisioned_size: int
          @param disk.interface: string
          @param disk.format: string
          [@param disk.alias: string]
          [@param disk.name: string]
          [@param disk.size: int]
          [@param disk.sparse: boolean]
          [@param disk.bootable: boolean]
          [@param disk.shareable: boolean]
          [@param disk.propagate_errors: boolean]
          [@param disk.wipe_after_delete: boolean]
          [@param disk.quota.id: string]
          [@param disk.disk_profile.id: string]
        Overload 2:
          @param disk.interface: string
          @param disk.format: string
          @param disk.lun_storage.type: string
          @param disk.lun_storage.logical_unit: collection
          {
            @ivar logical_unit.id: string
            @ivar logical_unit.address: string
            @ivar logical_unit.port: int
            @ivar logical_unit.target: string
          }
          [@param disk.alias: string]
          [@param disk.sparse: boolean]
          [@param disk.bootable: boolean]
          [@param disk.shareable: boolean]
          [@param disk.propagate_errors: boolean]
          [@param disk.wipe_after_delete: boolean]
          [@param disk.quota.id: string]
          [@param disk.sgio: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Disk:
        '''

        url = '/storagedomains/{storagedomain:id}/disks'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(disk),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return StoragedomainDisk(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Disks:
        '''

        url = '/storagedomains/{storagedomain:id}/disks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainDisk(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_disk()

            return StoragedomainDisk(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, unregistered=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param unregistered: boolean (true|false)]

        @return Disks:
        '''

        url = '/storagedomains/{storagedomain:id}/disks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max,'unregistered:matrix':unregistered}
            ),
            headers={}
        ).get_disk()

        return ParseHelper.toSubCollection(
            StoragedomainDisk,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainDisksnapshot(params.DiskSnapshot, Base):
    def __init__(self, storagedomain, disksnapshot, context):
        Base.__init__(self, context)
        self.parentclass = storagedomain
        self.superclass  =  disksnapshot

        #SUB_COLLECTIONS
    def __new__(cls, storagedomain, disksnapshot, context):
        if disksnapshot is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, disksnapshot, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/storagedomains/{storagedomain:id}/disksnapshots/{disksnapshot:id}',
            {
                '{storagedomain:id}': self.parentclass.get_id(),
                '{disksnapshot:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class StoragedomainDisksnapshots(Base):

    def __init__(self, storagedomain , context):
        Base.__init__(self, context)
        self.parentclass = storagedomain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return DiskSnapshots:
        '''

        url = '/storagedomains/{storagedomain:id}/disksnapshots'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainDisksnapshot(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_disk_snapshot()

            return StoragedomainDisksnapshot(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return DiskSnapshots:
        '''

        url = '/storagedomains/{storagedomain:id}/disksnapshots'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_disk_snapshot()

        return ParseHelper.toSubCollection(
            StoragedomainDisksnapshot,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainFile(params.File, Base):
    def __init__(self, storagedomain, file, context):
        Base.__init__(self, context)
        self.parentclass = storagedomain
        self.superclass  =  file

        #SUB_COLLECTIONS
    def __new__(cls, storagedomain, file, context):
        if file is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, file, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class StoragedomainFiles(Base):

    def __init__(self, storagedomain , context):
        Base.__init__(self, context)
        self.parentclass = storagedomain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Files:
        '''

        url = '/storagedomains/{storagedomain:id}/files'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainFile(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_file()

            return StoragedomainFile(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Files:
        '''

        url = '/storagedomains/{storagedomain:id}/files'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}
            ),
            headers={}
        ).get_file()

        return ParseHelper.toSubCollection(
            StoragedomainFile,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainImage(params.Image, Base):
    def __init__(self, storagedomain, image, context):
        Base.__init__(self, context)
        self.parentclass = storagedomain
        self.superclass  =  image

        #SUB_COLLECTIONS
    def __new__(cls, storagedomain, image, context):
        if image is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, image, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def import_image(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/storagedomains/{storagedomain:id}/images/{image:id}/import'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{image:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

class StoragedomainImages(Base):

    def __init__(self, storagedomain , context):
        Base.__init__(self, context)
        self.parentclass = storagedomain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Images:
        '''

        url = '/storagedomains/{storagedomain:id}/images'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainImage(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_image()

            return StoragedomainImage(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Images:
        '''

        url = '/storagedomains/{storagedomain:id}/images'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_image()

        return ParseHelper.toSubCollection(
            StoragedomainImage,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainPermission(params.Permission, Base):
    def __init__(self, storagedomain, permission, context):
        Base.__init__(self, context)
        self.parentclass = storagedomain
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, storagedomain, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/storagedomains/{storagedomain:id}/permissions/{permission:id}',
            {
                '{storagedomain:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class StoragedomainPermissions(Base):

    def __init__(self, storagedomain , context):
        Base.__init__(self, context)
        self.parentclass = storagedomain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/storagedomains/{storagedomain:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return StoragedomainPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/storagedomains/{storagedomain:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return StoragedomainPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/storagedomains/{storagedomain:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            StoragedomainPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainStorageconnection(params.StorageConnection, Base):
    def __init__(self, storagedomain, storageconnection, context):
        Base.__init__(self, context)
        self.parentclass = storagedomain
        self.superclass  =  storageconnection

        #SUB_COLLECTIONS
    def __new__(cls, storagedomain, storageconnection, context):
        if storageconnection is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, storageconnection, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None):
        '''
        [@param async: boolean (true|false)]

        @return None:
        '''

        url = UrlHelper.replace(
            '/storagedomains/{storagedomain:id}/storageconnections/{storageconnection:id}',
            {
                '{storagedomain:id}': self.parentclass.get_id(),
                '{storageconnection:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Content-type":None}
        )

class StoragedomainStorageconnections(Base):

    def __init__(self, storagedomain , context):
        Base.__init__(self, context)
        self.parentclass = storagedomain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, storageconnection, expect=None, correlation_id=None):

        '''
        @type StorageConnection:

        @param storageconnection.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return StorageConnection:
        '''

        url = '/storagedomains/{storagedomain:id}/storageconnections'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(storageconnection),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return StoragedomainStorageconnection(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return StorageConnections:
        '''

        url = '/storagedomains/{storagedomain:id}/storageconnections'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainStorageconnection(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_storage_connection()

            return StoragedomainStorageconnection(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return StorageConnections:
        '''

        url = '/storagedomains/{storagedomain:id}/storageconnections'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_storage_connection()

        return ParseHelper.toSubCollection(
            StoragedomainStorageconnection,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainTemplate(params.Template, Base):
    def __init__(self, storagedomain, template, context):
        Base.__init__(self, context)
        self.parentclass = storagedomain
        self.superclass  =  template

        self.disks = StoragedomainTemplateDisks(self, context)

    def __new__(cls, storagedomain, template, context):
        if template is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, template, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/storagedomains/{storagedomain:id}/templates/{template:id}',
            {
                '{storagedomain:id}': self.parentclass.get_id(),
                '{template:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def import_template(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.cluster.id|name: string
        [@param action.storage_domain.id|name: string]
        [@param action.clone: boolen]
        [@param action.exclusive: boolen]
        [@param action.template.name: string]
        [@param action.vm.disks.disk: collection]
        {
          [@ivar disk.id: string]
        }
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/storagedomains/{storagedomain:id}/templates/{template:id}/import'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{template:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def register(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.cluster.id|name: string
        [@param action.clone: boolen]
        [@param action.exclusive: boolen]
        [@param action.template.name: string]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/storagedomains/{storagedomain:id}/templates/{template:id}/register'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{template:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class StoragedomainTemplateDisk(params.Disk, Base):
    def __init__(self, template, disk, context):
        Base.__init__(self, context)
        self.parentclass = template
        self.superclass  =  disk

        #SUB_COLLECTIONS
    def __new__(cls, template, disk, context):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, disk, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class StoragedomainTemplateDisks(Base):

    def __init__(self, template , context):
        Base.__init__(self, context)
        self.parentclass = template

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Disks:
        '''

        url = '/storagedomains/{storagedomain:id}/templates/{template:id}/disks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                                '{template:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainTemplateDisk(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_disk()

            return StoragedomainTemplateDisk(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Disks:
        '''

        url = '/storagedomains/{storagedomain:id}/templates/{template:id}/disks'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                    '{template:id}': self.parentclass.get_id(),
                }
            )
        ).get_disk()

        return ParseHelper.toSubCollection(
            StoragedomainTemplateDisk,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainTemplates(Base):

    def __init__(self, storagedomain , context):
        Base.__init__(self, context)
        self.parentclass = storagedomain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Templates:
        '''

        url = '/storagedomains/{storagedomain:id}/templates'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainTemplate(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_template()

            return StoragedomainTemplate(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, unregistered=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]
        [@param unregistered: boolean (true|false)]

        @return Templates:
        '''

        url = '/storagedomains/{storagedomain:id}/templates'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max,'unregistered:matrix':unregistered}
            ),
            headers={}
        ).get_template()

        return ParseHelper.toSubCollection(
            StoragedomainTemplate,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainVm(params.VM, Base):
    def __init__(self, storagedomain, vm, context):
        Base.__init__(self, context)
        self.parentclass = storagedomain
        self.superclass  =  vm

        self.disks = StoragedomainVmDisks(self, context)

    def __new__(cls, storagedomain, vm, context):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, vm, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/storagedomains/{storagedomain:id}/vms/{vm:id}',
            {
                '{storagedomain:id}': self.parentclass.get_id(),
                '{vm:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def import_vm(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.cluster.id|name: string
        [@param action.async: boolean]
        [@param action.storage_domain.id|name: string]
        [@param action.vm.snapshots.collapse_snapshots: boolean]
        [@param action.clone: boolen]
        [@param action.exclusive: boolen]
        [@param action.vm.name: string]
        [@param action.vm.disks.disk: collection]
        {
          [@ivar disk.id: string]
        }
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/storagedomains/{storagedomain:id}/vms/{vm:id}/import'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def register(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.cluster.id|name: string
        [@param action.clone: boolen]
        [@param action.vm.name: string]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/storagedomains/{storagedomain:id}/vms/{vm:id}/register'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.get_id(),
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class StoragedomainVmDisk(params.Disk, Base):
    def __init__(self, vm, disk, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  disk

        #SUB_COLLECTIONS
    def __new__(cls, vm, disk, context):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, disk, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class StoragedomainVmDisks(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Disks:
        '''

        url = '/storagedomains/{storagedomain:id}/vms/{vm:id}/disks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainVmDisk(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_disk()

            return StoragedomainVmDisk(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Disks:
        '''

        url = '/storagedomains/{storagedomain:id}/vms/{vm:id}/disks'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{storagedomain:id}': self.parentclass.parentclass.get_id(),
                    '{vm:id}': self.parentclass.get_id(),
                }
            )
        ).get_disk()

        return ParseHelper.toSubCollection(
            StoragedomainVmDisk,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class StoragedomainVms(Base):

    def __init__(self, storagedomain , context):
        Base.__init__(self, context)
        self.parentclass = storagedomain

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return VMs:
        '''

        url = '/storagedomains/{storagedomain:id}/vms'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{storagedomain:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return StoragedomainVm(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_vm()

            return StoragedomainVm(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, unregistered=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]
        [@param unregistered: boolean (true|false)]

        @return VMs:
        '''

        url = '/storagedomains/{storagedomain:id}/vms'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{storagedomain:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max,'unregistered:matrix':unregistered}
            ),
            headers={}
        ).get_vm()

        return ParseHelper.toSubCollection(
            StoragedomainVm,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Storagedomains(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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
          [@param storagedomain.comment: string]
          [@param storagedomain.storage.override_luns: boolean]
          [@param storagedomain.storage_format: string]
          [@param storagedomain.wipe_after_delete: boolean]
        Overload 2:
          @param storagedomain.host.id|name: string
          @param storagedomain.type: string
          @param storagedomain.storage.type: string
          @param storagedomain.import: boolean
          [@param storagedomain.storage.address: string]
          [@param storagedomain.format: boolean]
          [@param storagedomain.comment: string]
        Overload 3:
          @param storagedomain.host.id|name: string
          @param storagedomain.type: string
          @param storagedomain.storage.type: string
          @param storagedomain.format: boolean
          @param storagedomain.storage.address: string
          @param storagedomain.storage.path: string
          [@param storagedomain.name: string]
          [@param storagedomain.comment: string]
          [@param storagedomain.storage_format: string]
          [@param storagedomain.wipe_after_delete: boolean]
        Overload 4:
          @param storagedomain.host.id|name: string
          @param storagedomain.type: string
          @param storagedomain.storage.type: string
          @param storagedomain.format: boolean
          @param storagedomain.storage.path: string
          [@param storagedomain.name: string]
          [@param storagedomain.comment: string]
          [@param storagedomain.storage_format: string]
          [@param storagedomain.wipe_after_delete: boolean]
        Overload 5:
          @param storagedomain.host.id|name: string
          @param storagedomain.type: string
          @param storagedomain.storage.type: string
          @param storagedomain.format: boolean
          @param storagedomain.storage.path: string
          @param storagedomain.storage.vfs_type: string
          [@param storagedomain.name: string]
          [@param storagedomain.comment: string]
          [@param storagedomain.storage.address: string]
          [@param storagedomain.storage.mount_options: string]
          [@param storagedomain.storage_format: string]
          [@param storagedomain.wipe_after_delete: boolean]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return StorageDomain:
        '''

        url = '/storagedomains'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(storagedomain),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Storagedomain(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return StorageDomains:
        '''

        url = '/storagedomains'

        if id:
            try :
                return Storagedomain(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={}
            ).get_storage_domain()

            return Storagedomain(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return StorageDomains:
        '''

        url='/storagedomains'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={}
        ).get_storage_domain()

        return ParseHelper.toCollection(
            Storagedomain,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Tag(params.Tag, Base):
    def __init__(self, tag, context):
        Base.__init__(self, context)
        self.superclass = tag

        #SUB_COLLECTIONS
    def __new__(cls, tag, context):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(tag, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/tags/{tag:id}',
            {
                '{tag:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param tag.name: string]
        [@param tag.description: string]
        [@param tag.parent.tag.id|name: string]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/tags/{tag:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{tag:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Tag(result, self.context)

class Tags(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, tag, correlation_id=None):
        '''
        @type Tag:

        @param tag.name: string
        [@param tag.description: string]
        [@param tag.parent.tag.id|name: string]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/tags'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(tag),
           headers={"Correlation-Id":correlation_id}
        )

        return Tag(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/tags'

        if id:
            try :
                return Tag(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_tag()

            return Tag(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return Tags:
        '''

        url='/tags'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_tag()

        return ParseHelper.toCollection(
            Tag,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Template(params.Template, Base):
    def __init__(self, template, context):
        Base.__init__(self, context)
        self.superclass = template

        self.cdroms = TemplateCdroms(self, context)
        self.disks = TemplateDisks(self, context)
        self.nics = TemplateNics(self, context)
        self.permissions = TemplatePermissions(self, context)
        self.tags = TemplateTags(self, context)
        self.watchdogs = TemplateWatchdogs(self, context)

    def __new__(cls, template, context):
        if template is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/templates/{template:id}',
            {
                '{template:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

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
        [@param template.delete_protected: boolean]
        [@param template.sso.methods.method: collection]
        {
          [@ivar method.id: string]
        }
        [@param vm.rng_device.rate.bytes: int]
        [@param vm.rng_device.rate.period: int]
        [@param vm.rng_device.source: string]
        [@param template.console.enabled: boolean]
        [@param template.placement_policy.affinity: string]
        [@param template.description: string]
        [@param template.comment: string]
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
        [@param template.cpu_shares: int]
        [@param template.cpu.architecture: string]
        [@param template.os.kernel: string]
        [@param template.display.type: string]
        [@param template.display.monitors: int]
        [@param vm.display.single_qxl_pci: boolean]
        [@param template.display.allow_override: boolean]
        [@param template.display.smartcard_enabled: boolean]
        [@param vm.display.file_transfer_enabled: boolean]
        [@param vm.display.copy_paste_enabled: boolean]
        [@param template.display.keyboard_layout: string]
        [@param template.os.initRd: string]
        [@param template.usb.enabled: boolean]
        [@param template.usb.type: string]
        [@param template.tunnel_migration: boolean]
        [@param template.migration_downtime: int]
        [@param template.virtio_scsi.enabled: boolean]
        [@param template.soundcard_enabled: boolean]
        [@param template.custom_emulated_machine: string]
        [@param template.custom_cpu_model: string]
        [@param template.version.version_name: string]
        [@param template.serial_number.policy: string]
        [@param template.serial_number.value: string]
        [@param template.bios.boot_menu.enabled: boolean]
        [@param template.start_paused: boolean]
        [@param template.cpu_profile.id: string]
        [@param template.migration.auto_converge: string]
        [@param template.migration.compressed: string]
        [@param correlation_id: any string]

        @return Template:
        '''

        url = '/templates/{template:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{template:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Template(result, self.context)

    def export(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.storage_domain.id|name: string
        [@param action.async: boolean]
        [@param action.exclusive: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/templates/{template:id}/export'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{template:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class TemplateCdrom(params.CdRom, Base):
    def __init__(self, template, cdrom, context):
        Base.__init__(self, context)
        self.parentclass = template
        self.superclass  =  cdrom

        #SUB_COLLECTIONS
    def __new__(cls, template, cdrom, context):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, cdrom, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class TemplateCdroms(Base):

    def __init__(self, template , context):
        Base.__init__(self, context)
        self.parentclass = template

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return CdRoms:
        '''

        url = '/templates/{template:id}/cdroms'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{template:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return TemplateCdrom(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_cdrom()

            return TemplateCdrom(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return CdRoms:
        '''

        url = '/templates/{template:id}/cdroms'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_cdrom()

        return ParseHelper.toSubCollection(
            TemplateCdrom,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class TemplateDisk(params.Disk, Base):
    def __init__(self, template, disk, context):
        Base.__init__(self, context)
        self.parentclass = template
        self.superclass  =  disk

        #SUB_COLLECTIONS
    def __new__(cls, template, disk, context):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, disk, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, action=params.Action(), async=None, correlation_id=None):
        '''
        @type Action:

        [@param action.storage_domain.id: string]
        [@param action.force: boolean]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/templates/{template:id}/disks/{disk:id}',
            {
                '{template:id}': self.parentclass.get_id(),
                '{disk:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

    def copy(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param storagedomain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/templates/{template:id}/disks/{disk:id}/copy'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{template:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def export(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param storagedomain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/templates/{template:id}/disks/{disk:id}/export'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{template:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class TemplateDisks(Base):

    def __init__(self, template , context):
        Base.__init__(self, context)
        self.parentclass = template

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Disks:
        '''

        url = '/templates/{template:id}/disks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{template:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return TemplateDisk(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_disk()

            return TemplateDisk(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Disks:
        '''

        url = '/templates/{template:id}/disks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_disk()

        return ParseHelper.toSubCollection(
            TemplateDisk,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class TemplateNic(params.NIC, Base):
    def __init__(self, template, nic, context):
        Base.__init__(self, context)
        self.parentclass = template
        self.superclass  =  nic

        #SUB_COLLECTIONS
    def __new__(cls, template, nic, context):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, nic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/templates/{template:id}/nics/{nic:id}',
            {
                '{template:id}': self.parentclass.get_id(),
                '{nic:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        Overload 1:
          [@param nic.vnic_profile.id: string]
          [@param nic.linked: boolean]
          [@param nic.name: string]
          [@param nic.mac.address: string]
          [@param nic.interface: string]
          [@param nic.plugged: boolean]
        Overload 2:
          [@param nic.network.id|name: string]
          [@param nic.linked: boolean]
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

        url = '/templates/{template:id}/nics/{nic:id}'
        url = UrlHelper.replace(
            url,
            {
                '{template:id}': self.parentclass.get_id(),
                '{nic:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return TemplateNic(
            self.parentclass,
            result,
            self.context
        )

class TemplateNics(Base):

    def __init__(self, template , context):
        Base.__init__(self, context)
        self.parentclass = template

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, nic, expect=None, correlation_id=None):

        '''
        @type NIC:

        Overload 1:
          @param nic.name: string
          [@param nic.vnic_profile.id: string]
          [@param nic.linked: boolean]
          [@param nic.mac.address: string]
          [@param nic.interface: string]
          [@param nic.plugged: boolean]
        Overload 2:
          @param nic.name: string
          [@param nic.network.id|name: string]
          [@param nic.linked: boolean]
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

        url = '/templates/{template:id}/nics'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{template:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(nic),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return TemplateNic(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Nics:
        '''

        url = '/templates/{template:id}/nics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{template:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return TemplateNic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_nic()

            return TemplateNic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Nics:
        '''

        url = '/templates/{template:id}/nics'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_nic()

        return ParseHelper.toSubCollection(
            TemplateNic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class TemplatePermission(params.Permission, Base):
    def __init__(self, template, permission, context):
        Base.__init__(self, context)
        self.parentclass = template
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, template, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/templates/{template:id}/permissions/{permission:id}',
            {
                '{template:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class TemplatePermissions(Base):

    def __init__(self, template , context):
        Base.__init__(self, context)
        self.parentclass = template

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/templates/{template:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{template:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return TemplatePermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/templates/{template:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{template:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return TemplatePermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return TemplatePermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/templates/{template:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            TemplatePermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class TemplateTag(params.Tag, Base):
    def __init__(self, template, tag, context):
        Base.__init__(self, context)
        self.parentclass = template
        self.superclass  =  tag

        #SUB_COLLECTIONS
    def __new__(cls, template, tag, context):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, tag, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/templates/{template:id}/tags/{tag:id}',
            {
                '{template:id}': self.parentclass.get_id(),
                '{tag:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class TemplateTags(Base):

    def __init__(self, template , context):
        Base.__init__(self, context)
        self.parentclass = template

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, tag, expect=None, correlation_id=None):

        '''
        @type Tag:

        @param tag.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/templates/{template:id}/tags'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{template:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(tag),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return TemplateTag(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/templates/{template:id}/tags'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{template:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return TemplateTag(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_tag()

            return TemplateTag(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Tags:
        '''

        url = '/templates/{template:id}/tags'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_tag()

        return ParseHelper.toSubCollection(
            TemplateTag,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class TemplateWatchdog(params.WatchDog, Base):
    def __init__(self, template, watchdog, context):
        Base.__init__(self, context)
        self.parentclass = template
        self.superclass  =  watchdog

        #SUB_COLLECTIONS
    def __new__(cls, template, watchdog, context):
        if watchdog is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, watchdog, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/templates/{template:id}/watchdogs/{watchdog:id}',
            {
                '{template:id}': self.parentclass.get_id(),
                '{watchdog:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param watchdog.action: string]
        [@param watchdog.model: string]
        [@param correlation_id: any string]

        @return WatchDog:
        '''

        url = '/templates/{template:id}/watchdogs/{watchdog:id}'
        url = UrlHelper.replace(
            url,
            {
                '{template:id}': self.parentclass.get_id(),
                '{watchdog:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return TemplateWatchdog(
            self.parentclass,
            result,
            self.context
        )

class TemplateWatchdogs(Base):

    def __init__(self, template , context):
        Base.__init__(self, context)
        self.parentclass = template

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, watchdog, expect=None, correlation_id=None):

        '''
        @type WatchDog:

        @param watchdog.action: string
        @param watchdog.model: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return WatchDog:
        '''

        url = '/templates/{template:id}/watchdogs'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{template:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(watchdog),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return TemplateWatchdog(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return WatchDogs:
        '''

        url = '/templates/{template:id}/watchdogs'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{template:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return TemplateWatchdog(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_watchdog()

            return TemplateWatchdog(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return WatchDogs:
        '''

        url = '/templates/{template:id}/watchdogs'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{template:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_watchdog()

        return ParseHelper.toSubCollection(
            TemplateWatchdog,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Templates(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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
        [@param template.delete_protected: boolean]
        [@param template.sso.methods.method: collection]
        {
          [@ivar method.id: string]
        }
        [@param vm.rng_device.rate.bytes: int]
        [@param vm.rng_device.rate.period: int]
        [@param vm.rng_device.source: string]
        [@param template.console.enabled: boolean]
        [@param template.placement_policy.affinity: string]
        [@param template.description: string]
        [@param template.comment: string]
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
        [@param template.cpu_shares: int]
        [@param template.cpu.architecture: string]
        [@param template.os.kernel: string]
        [@param template.display.type: string]
        [@param template.display.monitors: int]
        [@param vm.display.single_qxl_pci: boolean]
        [@param template.display.allow_override: boolean]
        [@param template.display.smartcard_enabled: boolean]
        [@param template.display.file_transfer_enabled: boolean]
        [@param template.display.copy_paste_enabled: boolean]
        [@param template.display.keyboard_layout: string]
        [@param template.os.initRd: string]
        [@param template.usb.enabled: boolean]
        [@param template.usb.type: string]
        [@param template.tunnel_migration: boolean]
        [@param template.migration_downtime: int]
        [@param template.virtio_scsi.enabled: boolean]
        [@param template.soundcard_enabled: boolean]
        [@param template.custom_emulated_machine: string]
        [@param template.custom_cpu_model: string]
        [@param template.vm.disks.disk: collection]
        {
          [@ivar disk.id: string]
          [@ivar storage_domains.storage_domain: collection]
          {
            [@param storage_domain.id: string]
          }
        }
        [@param template.permissions.clone: boolean]
        [@param template.version.version_name: string]
        [@param template.version.base_template.id: string]
        [@param template.cpu.cpu_tune.vcpu_pin: collection]
        {
          [@ivar vcpu_pin.vcpu: int]
          [@ivar vcpu_pin.cpu_set: string]
        }
        [@param template.serial_number.policy: string]
        [@param template.serial_number.value: string]
        [@param template.bios.boot_menu.enabled: boolean]
        [@param template.cluster.id: string]
        [@param template.cluster.name: string]
        [@param template.start_paused: boolean]
        [@param template.cpu_profile.id: string]
        [@param template.migration.auto_converge: string]
        [@param template.migration.compressed: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Template:
        '''

        url = '/templates'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(template),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Template(result, self.context)

    def get(self, name=None, all_content=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]
        [@param all_content: true|false]

        @return Templates:
        '''

        url = '/templates'

        if id:
            try :
                return Template(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={"All-Content":all_content}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={"All-Content":all_content}
            ).get_template()

            return Template(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, all_content=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param all_content: true|false]

        @return Templates:
        '''

        url='/templates'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={"All-Content":all_content}
        ).get_template()

        return ParseHelper.toCollection(
            Template,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class User(params.User, Base):
    def __init__(self, user, context):
        Base.__init__(self, context)
        self.superclass = user

        self.permissions = UserPermissions(self, context)
        self.roles = UserRoles(self, context)
        self.tags = UserTags(self, context)

    def __new__(cls, user, context):
        if user is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/users/{user:id}',
            {
                '{user:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class UserPermission(params.Permission, Base):
    def __init__(self, user, permission, context):
        Base.__init__(self, context)
        self.parentclass = user
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, user, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/users/{user:id}/permissions/{permission:id}',
            {
                '{user:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class UserPermissions(Base):

    def __init__(self, user , context):
        Base.__init__(self, context)
        self.parentclass = user

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/users/{user:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{user:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return UserPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/users/{user:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{user:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return UserPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{user:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return UserPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/users/{user:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{user:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            UserPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class UserRole(params.Role, Base):
    def __init__(self, user, role, context):
        Base.__init__(self, context)
        self.parentclass = user
        self.superclass  =  role

        self.permits = UserRolePermits(self, context)

    def __new__(cls, user, role, context):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, role, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class UserRolePermit(params.Permit, Base):
    def __init__(self, role, permit, context):
        Base.__init__(self, context)
        self.parentclass = role
        self.superclass  =  permit

        #SUB_COLLECTIONS
    def __new__(cls, role, permit, context):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(role, permit, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/users/{user:id}/roles/{role:id}/permits/{permit:id}',
            {
                '{user:id}': self.parentclass.parentclass.get_id(),
                '{role:id}': self.parentclass.get_id(),
                '{permit:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class UserRolePermits(Base):

    def __init__(self, role , context):
        Base.__init__(self, context)
        self.parentclass = role

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permit, expect=None, correlation_id=None):

        '''
        @type Permit:

        @param permit.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permit:
        '''

        url = '/users/{user:id}/roles/{role:id}/permits'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{user:id}': self.parentclass.parentclass.get_id(),
                    '{role:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permit),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return UserRolePermit(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permits:
        '''

        url = '/users/{user:id}/roles/{role:id}/permits'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{user:id}': self.parentclass.parentclass.get_id(),
                                '{role:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return UserRolePermit(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{user:id}': self.parentclass.parentclass.get_id(),
                        '{role:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permit()

            return UserRolePermit(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permits:
        '''

        url = '/users/{user:id}/roles/{role:id}/permits'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{user:id}': self.parentclass.parentclass.get_id(),
                        '{role:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permit()

        return ParseHelper.toSubCollection(
            UserRolePermit,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class UserRoles(Base):

    def __init__(self, user , context):
        Base.__init__(self, context)
        self.parentclass = user

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Roles:
        '''

        url = '/users/{user:id}/roles'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{user:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return UserRole(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{user:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_role()

            return UserRole(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Roles:
        '''

        url = '/users/{user:id}/roles'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{user:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_role()

        return ParseHelper.toSubCollection(
            UserRole,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class UserTag(params.Tag, Base):
    def __init__(self, user, tag, context):
        Base.__init__(self, context)
        self.parentclass = user
        self.superclass  =  tag

        #SUB_COLLECTIONS
    def __new__(cls, user, tag, context):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, tag, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/users/{user:id}/tags/{tag:id}',
            {
                '{user:id}': self.parentclass.get_id(),
                '{tag:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class UserTags(Base):

    def __init__(self, user , context):
        Base.__init__(self, context)
        self.parentclass = user

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, tag, expect=None, correlation_id=None):

        '''
        @type Tag:

        @param tag.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/users/{user:id}/tags'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{user:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(tag),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return UserTag(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/users/{user:id}/tags'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{user:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return UserTag(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{user:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_tag()

            return UserTag(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Tags:
        '''

        url = '/users/{user:id}/tags'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{user:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_tag()

        return ParseHelper.toSubCollection(
            UserTag,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Users(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, user, expect=None, correlation_id=None):
        '''
        @type User:

        @param user.user_name: string
        @param user.domain.id|name: string
        [@param user.namespace: string]
        [@param user.principal: string]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return User:
        '''

        url = '/users'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(user),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return User(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Users:
        '''

        url = '/users'

        if id:
            try :
                return User(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={}
            ).get_user()

            return User(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return Users:
        '''

        url='/users'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={}
        ).get_user()

        return ParseHelper.toCollection(
            User,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Vm(params.VM, Base):
    def __init__(self, vm, context):
        Base.__init__(self, context)
        self.superclass = vm

        self.applications = VmApplications(self, context)
        self.cdroms = VmCdroms(self, context)
        self.disks = VmDisks(self, context)
        self.nics = VmNics(self, context)
        self.numanodes = VmNumanodes(self, context)
        self.permissions = VmPermissions(self, context)
        self.reporteddevices = VmReporteddevices(self, context)
        self.sessions = VmSessions(self, context)
        self.snapshots = VmSnapshots(self, context)
        self.statistics = VmStatistics(self, context)
        self.tags = VmTags(self, context)
        self.watchdogs = VmWatchdogs(self, context)

    def __new__(cls, vm, context):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, action=params.Action(), async=None, correlation_id=None):
        '''
        @type Action:

        [@param action.force: boolean]
        [@param action.vm.disks.detach_only: boolean]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vms/{vm:id}',
            {
                '{vm:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

    def update(self, correlation_id=None):
        '''
        [@param vm.instance_type.id|name: string]
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
        [@param vm.display.single_qxl_pci: boolean]
        [@param vm.display.type: string]
        [@param vm.display.allow_override: boolean]
        [@param vm.display.smartcard_enabled: boolean]
        [@param vm.display.file_transfer_enabled: boolean]
        [@param vm.display.copy_paste_enabled: boolean]
        [@param vm.display.keyboard_layout: string]
        [@param vm.os.cmdline: string]
        [@param vm.cpu.mode: string]
        [@param vm.cpu.architecture: string]
        [@param vm.cpu.topology.cores: int]
        [@param vm.cpu_shares: int]
        [@param vm.memory: long]
        [@param vm.memory_policy.guaranteed: long]
        [@param vm.memory_policy.ballooning: boolean]
        [@param vm.high_availability.priority: int]
        [@param vm.high_availability.enabled: boolean]
        [@param vm.domain.name: string]
        [@param vm.description: string]
        [@param vm.comment: string]
        [@param vm.stateless: boolean]
        [@param vm.delete_protected: boolean]
        [@param vm.sso.methods.method: collection]
        {
          [@ivar method.id: string]
        }
        [@param vm.rng_device.rate.bytes: int]
        [@param vm.rng_device.rate.period: int]
        [@param vm.rng_device.source: string]
        [@param vm.console.enabled: boolean]
        [@param vm.cpu.topology.sockets: int]
        [@param vm.placement_policy.affinity: string]
        [@param vm.placement_policy.host.id|name: string]
        [@param vm.origin: string]
        [@param vm.os.kernel: string]
        [@param vm.tunnel_migration: boolean]
        [@param vm.migration_downtime: int]
        [@param vm.virtio_scsi.enabled: boolean]
        [@param vm.soundcard_enabled: boolean]
        [@param vm.custom_emulated_machine: string]
        [@param vm.custom_cpu_model: string]
        [@param vm.use_latest_template_version: boolean]
        [@param vm.payloads.payload: collection]
        {
          [@ivar payload.type: string]
          [@ivar payload.volume_id: string]
          [@ivar payload.files.file: collection]
          {
            [@param file.name: string]
            [@param file.content: string]
          }
        }
        [@param vm.cpu.cpu_tune.vcpu_pin: collection]
        {
          [@ivar vcpu_pin.vcpu: int]
          [@ivar vcpu_pin.cpu_set: string]
        }
        [@param vm.serial_number.policy: string]
        [@param vm.serial_number.value: string]
        [@param vm.bios.boot_menu.enabled: boolean]
        [@param vm.numa_tune_mode: string]
        [@param vm.start_paused: boolean]
        [@param vm.cpu_profile.id: string]
        [@param vm.migration.auto_converge: string]
        [@param vm.migration.compressed: string]
        [@param correlation_id: any string]

        @return VM:
        '''

        url = '/vms/{vm:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Vm(result, self.context)

    def cancelmigration(self, action=params.Action()):
        '''
        @type Action:


        @return Action:
        '''

        url = '/vms/{vm:id}/cancelmigration'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={}
        )

        return result

    def clone(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.vm.name: string
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/clone'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def commit_snapshot(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/commit_snapshot'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def detach(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/detach'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

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

        @return Action:
        '''

        url = '/vms/{vm:id}/export'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def logon(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/logon'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def maintenance(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.maintenance_enabled: boolean
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/maintenance'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def migrate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.host.id|name: string]
        [@param action.async: boolean]
        [@param action.force: boolean]
        [@param action.grace_period.expiry: long]
        [@param action.cluster.id: string]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/migrate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def move(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.storage_domain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/move'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def preview_snapshot(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param action.snapshot.id: string
        [@param action.restore_memory: boolean]
        [@param action.disks.disk: collection]
        {
          [@ivar disk.id: string]
          [@ivar disk.image_id: string]
          [@ivar disk.snapshot.id: string]
        }
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/preview_snapshot'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def reboot(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/reboot'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def shutdown(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/shutdown'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

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
        [@param action.vm.initialization.cloud_init.host.address: string]
        [@param action.vm.custom_emulated_machine: string]
        [@param action.vm.custom_cpu_model: string]
        [@param action.vm.initialization.cloud_init.network_configuration.nics.nic: collection]
        {
          [@ivar nic.name: string]
          [@ivar nic.boot_protocol: string]
          [@ivar nic.network.address.ip: string]
          [@ivar nic.network.address.netmask: string]
          [@ivar nic.network.address.gateway: string]
          [@ivar nic.onboot: boolean]
        }
        [@param action.vm.initialization.cloud_init.network_configuration.dns.servers.host: collection]
        {
          [@ivar host.address: string]
        }
        [@param action.vm.initialization.cloud_init.network_configuration.dns.search_domains.host: collection]
        {
          [@ivar host.address: string]
        }
        [@param action.vm.initialization.cloud_init.authorized_keys.authorized_key: collection]
        {
          [@ivar authorized_key.key: string]
          [@ivar authorized_key.user.name: string]
        }
        [@param action.vm.initialization.cloud_init.regenerate_ssh_keys: boolean]
        [@param action.vm.initialization.cloud_init.timezone: string]
        [@param action.vm.initialization.cloud_init.users.user: collection]
        {
          [@ivar user.password: string]
          [@ivar user.name: string]
        }
        [@param action.vm.initialization.cloud_init.payload_files.payload_file: collection]
        {
          [@ivar payload_file.name: string]
          [@ivar payload_file.content: string]
          [@ivar payload_file.type: string]
        }
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/start'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def stop(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/stop'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def suspend(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/suspend'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def ticket(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.ticket.value: string]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/ticket'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def undo_snapshot(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/undo_snapshot'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class VmApplication(params.Application, Base):
    def __init__(self, vm, application, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  application

        #SUB_COLLECTIONS
    def __new__(cls, vm, application, context):
        if application is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, application, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class VmApplications(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Applications:
        '''

        url = '/vms/{vm:id}/applications'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmApplication(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_application()

            return VmApplication(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Applications:
        '''

        url = '/vms/{vm:id}/applications'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            )
        ).get_application()

        return ParseHelper.toSubCollection(
            VmApplication,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmCdrom(params.CdRom, Base):
    def __init__(self, vm, cdrom, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  cdrom

        #SUB_COLLECTIONS
    def __new__(cls, vm, cdrom, context):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, cdrom, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vms/{vm:id}/cdroms/{cdrom:id}',
            {
                '{vm:id}': self.parentclass.get_id(),
                '{cdrom:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, async=None, current=None, correlation_id=None):
        '''
        [@param cdrom.file.id: string]
        [@param async: boolean (true|false)]
        [@param current: boolean (true|false)]
        [@param correlation_id: any string]

        @return CdRom:
        '''

        url = '/vms/{vm:id}/cdroms/{cdrom:id}'
        url = UrlHelper.replace(
            url,
            {
                '{vm:id}': self.parentclass.get_id(),
                '{cdrom:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {'async:matrix':async,'current:matrix':current}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return VmCdrom(
            self.parentclass,
            result,
            self.context
        )

class VmCdroms(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, cdrom, expect=None, correlation_id=None):

        '''
        @type CdRom:

        @param cdrom.file.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return CdRom:
        '''

        url = '/vms/{vm:id}/cdroms'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(cdrom),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return VmCdrom(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return CdRoms:
        '''

        url = '/vms/{vm:id}/cdroms'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmCdrom(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_cdrom()

            return VmCdrom(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, current=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]
        [@param current: boolean (true|false)]

        @return CdRoms:
        '''

        url = '/vms/{vm:id}/cdroms'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max,'current:matrix':current}
            ),
            headers={}
        ).get_cdrom()

        return ParseHelper.toSubCollection(
            VmCdrom,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmDisk(params.Disk, Base):
    def __init__(self, vm, disk, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  disk

        self.permissions = VmDiskPermissions(self, context)
        self.statistics = VmDiskStatistics(self, context)

    def __new__(cls, vm, disk, context):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, disk, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, action=params.Action(), async=None, correlation_id=None):
        '''
        @type Action:

        @param action.detach: boolean
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vms/{vm:id}/disks/{disk:id}',
            {
                '{vm:id}': self.parentclass.get_id(),
                '{disk:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

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
        [@param disk.quota.id: string]
        [@param disk.disk_profile.id: string]
        [@param disk.sgio: string]
        [@param disk.read_only: boolean]
        [@param description: update the size, boot flag and other parameters of the disk attached to the virtual machine]
        [@param correlation_id: any string]

        @return Disk:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}'
        url = UrlHelper.replace(
            url,
            {
                '{vm:id}': self.parentclass.get_id(),
                '{disk:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return VmDisk(
            self.parentclass,
            result,
            self.context
        )

    def activate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}/activate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def deactivate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}/deactivate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def export(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param storagedomain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}/export'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def move(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        @param storagedomain.id|name: string
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}/move'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                    '{disk:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class VmDiskPermission(params.Permission, Base):
    def __init__(self, disk, permission, context):
        Base.__init__(self, context)
        self.parentclass = disk
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, disk, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self):
        '''
        @return None:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}/permissions/{permission:id}'

        return self.__getProxy().delete(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                    '{permission:id}': self.get_id(),
                }
            ),
            headers={'Content-type':None}
        )

class VmDiskPermissions(Base):

    def __init__(self, disk , context):
        Base.__init__(self, context)
        self.parentclass = disk

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission):

        '''
        @type Permission:


        @return Permission:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={}
        )

        return VmDiskPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.parentclass.get_id(),
                                '{disk:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmDiskPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.parentclass.get_id(),
                        '{disk:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return VmDiskPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Permissions:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}/permissions'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                }
            )
        ).get_permission()

        return ParseHelper.toSubCollection(
            VmDiskPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmDiskStatistic(params.Statistic, Base):
    def __init__(self, disk, statistic, context):
        Base.__init__(self, context)
        self.parentclass = disk
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, disk, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(disk, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class VmDiskStatistics(Base):

    def __init__(self, disk , context):
        Base.__init__(self, context)
        self.parentclass = disk

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.parentclass.get_id(),
                                '{disk:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmDiskStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.parentclass.get_id(),
                        '{disk:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return VmDiskStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Statistics:
        '''

        url = '/vms/{vm:id}/disks/{disk:id}/statistics'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.parentclass.get_id(),
                    '{disk:id}': self.parentclass.get_id(),
                }
            )
        ).get_statistic()

        return ParseHelper.toSubCollection(
            VmDiskStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmDisks(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, disk, expect=None, correlation_id=None):

        '''
        @type Disk:

        Overload 1:
          @param provisioned_size: int
          @param disk.interface: string
          @param disk.format: string
          [@param disk.alias: string]
          [@param disk.name: string]
          [@param disk.size: int]
          [@param disk.sparse: boolean]
          [@param disk.bootable: boolean]
          [@param disk.shareable: boolean]
          [@param disk.propagate_errors: boolean]
          [@param disk.wipe_after_delete: boolean]
          [@param disk.quota.id: string]
          [@param disk.disk_profile.id: string]
          [@param disk.storage_domains.storage_domain: collection]
          {
            [@ivar storage_domain.id|name: string]
          }
        Overload 2:
          @param disk.interface: string
          @param disk.lun_storage.type: string
          @param disk.lun_storage.logical_unit: collection
          {
            @ivar logical_unit.id: string
            @ivar logical_unit.address: string
            @ivar logical_unit.port: int
            @ivar logical_unit.target: string
          }
          [@param disk.alias: string]
          [@param disk.sparse: boolean]
          [@param disk.bootable: boolean]
          [@param disk.shareable: boolean]
          [@param disk.propagate_errors: boolean]
          [@param disk.wipe_after_delete: boolean]
          [@param disk.quota.id: string]
          [@param disk.sgio: string]
          [@param disk.lun_storage.host: string]
        Overload 3:
          @param disk.id: string
          [@param disk.active: boolean]
          [@param disk.read_only: boolean]
        Overload 4:
          @param disk.id: string
          @param disk.snapshot.id: string
          [@param disk.active: boolean]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Disk:
        '''

        url = '/vms/{vm:id}/disks'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(disk),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return VmDisk(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Disks:
        '''

        url = '/vms/{vm:id}/disks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmDisk(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_disk()

            return VmDisk(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Disks:
        '''

        url = '/vms/{vm:id}/disks'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_disk()

        return ParseHelper.toSubCollection(
            VmDisk,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmNic(params.NIC, Base):
    def __init__(self, vm, nic, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  nic

        self.reporteddevices = VmNicReporteddevices(self, context)
        self.statistics = VmNicStatistics(self, context)

    def __new__(cls, vm, nic, context):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, nic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vms/{vm:id}/nics/{nic:id}',
            {
                '{vm:id}': self.parentclass.get_id(),
                '{nic:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        Overload 1:
          [@param nic.vnic_profile.id: string]
          [@param nic.linked: boolean]
          [@param nic.name: string]
          [@param nic.mac.address: string]
          [@param nic.interface: string]
          [@param nic.plugged: boolean]
        Overload 2:
          [@param nic.network.id|name: string]
          [@param nic.linked: boolean]
          [@param nic.name: string]
          [@param nic.mac.address: string]
          [@param nic.interface: string]
          [@param nic.port_mirroring.networks.network: collection]
          {
            [@ivar network.id: string]
          }
          [@param nic.plugged: boolean]
        [@param correlation_id: any string]

        @return NIC:
        '''

        url = '/vms/{vm:id}/nics/{nic:id}'
        url = UrlHelper.replace(
            url,
            {
                '{vm:id}': self.parentclass.get_id(),
                '{nic:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return VmNic(
            self.parentclass,
            result,
            self.context
        )

    def activate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/nics/{nic:id}/activate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                    '{nic:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

    def deactivate(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/nics/{nic:id}/deactivate'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                    '{nic:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class VmNicReporteddevice(params.ReportedDevice, Base):
    def __init__(self, nic, reporteddevice, context):
        Base.__init__(self, context)
        self.parentclass = nic
        self.superclass  =  reporteddevice

        #SUB_COLLECTIONS
    def __new__(cls, nic, reporteddevice, context):
        if reporteddevice is None: return None
        obj = object.__new__(cls)
        obj.__init__(nic, reporteddevice, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class VmNicReporteddevices(Base):

    def __init__(self, nic , context):
        Base.__init__(self, context)
        self.parentclass = nic

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return ReportedDevices:
        '''

        url = '/vms/{vm:id}/nics/{nic:id}/reporteddevices'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.parentclass.get_id(),
                                '{nic:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmNicReporteddevice(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.parentclass.get_id(),
                        '{nic:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_reported_device()

            return VmNicReporteddevice(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return ReportedDevices:
        '''

        url = '/vms/{vm:id}/nics/{nic:id}/reporteddevices'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.parentclass.get_id(),
                    '{nic:id}': self.parentclass.get_id(),
                }
            )
        ).get_reported_device()

        return ParseHelper.toSubCollection(
            VmNicReporteddevice,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmNicStatistic(params.Statistic, Base):
    def __init__(self, nic, statistic, context):
        Base.__init__(self, context)
        self.parentclass = nic
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, nic, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(nic, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class VmNicStatistics(Base):

    def __init__(self, nic , context):
        Base.__init__(self, context)
        self.parentclass = nic

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/vms/{vm:id}/nics/{nic:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.parentclass.get_id(),
                                '{nic:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmNicStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.parentclass.get_id(),
                        '{nic:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return VmNicStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Statistics:
        '''

        url = '/vms/{vm:id}/nics/{nic:id}/statistics'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.parentclass.get_id(),
                    '{nic:id}': self.parentclass.get_id(),
                }
            )
        ).get_statistic()

        return ParseHelper.toSubCollection(
            VmNicStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmNics(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, nic, expect=None, correlation_id=None):

        '''
        @type NIC:

        Overload 1:
          @param nic.name: string
          [@param nic.vnic_profile.id: string]
          [@param nic.linked: boolean]
          [@param nic.mac.address: string]
          [@param nic.interface: string]
          [@param nic.plugged: boolean]
        Overload 2:
          @param nic.name: string
          [@param nic.network.id|name: string]
          [@param nic.linked: boolean]
          [@param nic.mac.address: string]
          [@param nic.interface: string]
          [@param nic.port_mirroring.networks.network: collection]
          {
            [@ivar network.id: string]
          }
          [@param nic.plugged: boolean]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return NIC:
        '''

        url = '/vms/{vm:id}/nics'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(nic),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return VmNic(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, all_content=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]
        [@param all_content: true|false]

        @return Nics:
        '''

        url = '/vms/{vm:id}/nics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={"All-Content":all_content}
                )

                return VmNic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={"All-Content":all_content}
            ).get_nic()

            return VmNic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, all_content=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]
        [@param all_content: true|false]

        @return Nics:
        '''

        url = '/vms/{vm:id}/nics'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={"All-Content":all_content}
        ).get_nic()

        return ParseHelper.toSubCollection(
            VmNic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmNumanode(params.VirtualNumaNode, Base):
    def __init__(self, vm, virtualnumanode, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  virtualnumanode

        #SUB_COLLECTIONS
    def __new__(cls, vm, virtualnumanode, context):
        if virtualnumanode is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, virtualnumanode, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vms/{vm:id}/numanodes/{numanode:id}',
            {
                '{vm:id}': self.parentclass.get_id(),
                '{numanode:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, async=None, correlation_id=None):
        '''
        [@param vm_numa_node.index: int]
        [@param vm_numa_node.memory: string]
        [@param vm_numa_node.cpu.cores.core: collection]
        {
          [@ivar core.index: int]
        }
        [@param vm_numa_node.numa_node_pins.numa_node_pin: collection]
        {
          [@ivar numa_node_pin.index: int]
        }
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return VirtualNumaNode:
        '''

        url = '/vms/{vm:id}/numanodes/{numanode:id}'
        url = UrlHelper.replace(
            url,
            {
                '{vm:id}': self.parentclass.get_id(),
                '{numanode:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {'async:matrix':async}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return VmNumanode(
            self.parentclass,
            result,
            self.context
        )

class VmNumanodes(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, vmnumanode, expect=None, correlation_id=None):

        '''
        @type VirtualNumaNode:

        @param vm_numa_node.index: int
        @param vm_numa_node.memory: string
        @param vm_numa_node.cpu.cores.core: collection
        {
          @ivar core.index: int
        }
        [@param vm_numa_node.numa_node_pins.numa_node_pin: collection]
        {
          [@ivar numa_node_pin.index: int]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return VirtualNumaNode:
        '''

        url = '/vms/{vm:id}/numanodes'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(vmnumanode),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return VmNumanode(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return VirtualNumaNodes:
        '''

        url = '/vms/{vm:id}/numanodes'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmNumanode(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_vm_numa_node()

            return VmNumanode(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return VirtualNumaNodes:
        '''

        url = '/vms/{vm:id}/numanodes'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_vm_numa_node()

        return ParseHelper.toSubCollection(
            VmNumanode,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmPermission(params.Permission, Base):
    def __init__(self, vm, permission, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, vm, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vms/{vm:id}/permissions/{permission:id}',
            {
                '{vm:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class VmPermissions(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/vms/{vm:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return VmPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/vms/{vm:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return VmPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/vms/{vm:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            VmPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmReporteddevice(params.ReportedDevice, Base):
    def __init__(self, vm, reporteddevice, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  reporteddevice

        #SUB_COLLECTIONS
    def __new__(cls, vm, reporteddevice, context):
        if reporteddevice is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, reporteddevice, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class VmReporteddevices(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return ReportedDevices:
        '''

        url = '/vms/{vm:id}/reporteddevices'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmReporteddevice(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_reported_device()

            return VmReporteddevice(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return ReportedDevices:
        '''

        url = '/vms/{vm:id}/reporteddevices'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            )
        ).get_reported_device()

        return ParseHelper.toSubCollection(
            VmReporteddevice,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmSession(params.Session, Base):
    def __init__(self, vm, session, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  session

        #SUB_COLLECTIONS
    def __new__(cls, vm, session, context):
        if session is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, session, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class VmSessions(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Sessions:
        '''

        url = '/vms/{vm:id}/sessions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmSession(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_session()

            return VmSession(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Sessions:
        '''

        url = '/vms/{vm:id}/sessions'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            )
        ).get_session()

        return ParseHelper.toSubCollection(
            VmSession,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmSnapshot(params.Snapshot, Base):
    def __init__(self, vm, snapshot, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  snapshot

        self.cdroms = VmSnapshotCdroms(self, context)
        self.disks = VmSnapshotDisks(self, context)
        self.nics = VmSnapshotNics(self, context)

    def __new__(cls, vm, snapshot, context):
        if snapshot is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, snapshot, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vms/{vm:id}/snapshots/{snapshot:id}',
            {
                '{vm:id}': self.parentclass.get_id(),
                '{snapshot:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def restore(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.restore_memory: boolean]
        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param action.disks.disk: collection]
        {
          [@ivar disk.id: string]
          [@ivar disk.image_id: string]
        }
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vms/{vm:id}/snapshots/{snapshot:id}/restore'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                    '{snapshot:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class VmSnapshotCdrom(params.CdRom, Base):
    def __init__(self, snapshot, cdrom, context):
        Base.__init__(self, context)
        self.parentclass = snapshot
        self.superclass  =  cdrom

        #SUB_COLLECTIONS
    def __new__(cls, snapshot, cdrom, context):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(snapshot, cdrom, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class VmSnapshotCdroms(Base):

    def __init__(self, snapshot , context):
        Base.__init__(self, context)
        self.parentclass = snapshot

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return CdRoms:
        '''

        url = '/vms/{vm:id}/snapshots/{snapshot:id}/cdroms'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.parentclass.get_id(),
                                '{snapshot:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmSnapshotCdrom(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.parentclass.get_id(),
                        '{snapshot:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_cdrom()

            return VmSnapshotCdrom(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return CdRoms:
        '''

        url = '/vms/{vm:id}/snapshots/{snapshot:id}/cdroms'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.parentclass.get_id(),
                    '{snapshot:id}': self.parentclass.get_id(),
                }
            )
        ).get_cdrom()

        return ParseHelper.toSubCollection(
            VmSnapshotCdrom,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmSnapshotDisk(params.Disk, Base):
    def __init__(self, snapshot, disk, context):
        Base.__init__(self, context)
        self.parentclass = snapshot
        self.superclass  =  disk

        #SUB_COLLECTIONS
    def __new__(cls, snapshot, disk, context):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(snapshot, disk, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vms/{vm:id}/snapshots/{snapshot:id}/disks/{disk:id}',
            {
                '{vm:id}': self.parentclass.parentclass.get_id(),
                '{snapshot:id}': self.parentclass.get_id(),
                '{disk:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class VmSnapshotDisks(Base):

    def __init__(self, snapshot , context):
        Base.__init__(self, context)
        self.parentclass = snapshot

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Disks:
        '''

        url = '/vms/{vm:id}/snapshots/{snapshot:id}/disks'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.parentclass.get_id(),
                                '{snapshot:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmSnapshotDisk(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.parentclass.get_id(),
                        '{snapshot:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_disk()

            return VmSnapshotDisk(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Disks:
        '''

        url = '/vms/{vm:id}/snapshots/{snapshot:id}/disks'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.parentclass.get_id(),
                    '{snapshot:id}': self.parentclass.get_id(),
                }
            )
        ).get_disk()

        return ParseHelper.toSubCollection(
            VmSnapshotDisk,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmSnapshotNic(params.NIC, Base):
    def __init__(self, snapshot, nic, context):
        Base.__init__(self, context)
        self.parentclass = snapshot
        self.superclass  =  nic

        #SUB_COLLECTIONS
    def __new__(cls, snapshot, nic, context):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(snapshot, nic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class VmSnapshotNics(Base):

    def __init__(self, snapshot , context):
        Base.__init__(self, context)
        self.parentclass = snapshot

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Nics:
        '''

        url = '/vms/{vm:id}/snapshots/{snapshot:id}/nics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.parentclass.get_id(),
                                '{snapshot:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmSnapshotNic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.parentclass.get_id(),
                        '{snapshot:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_nic()

            return VmSnapshotNic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]

        @return Nics:
        '''

        url = '/vms/{vm:id}/snapshots/{snapshot:id}/nics'

        result = self.__getProxy().get(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.parentclass.get_id(),
                    '{snapshot:id}': self.parentclass.get_id(),
                }
            )
        ).get_nic()

        return ParseHelper.toSubCollection(
            VmSnapshotNic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmSnapshots(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, snapshot, expect=None, correlation_id=None):

        '''
        @type Snapshot:

        @param snapshot.description: string
        [@param snapshot.persist_memorystate: boolean]
        [@param snapshot.disks.disk: collection]
        {
          [@ivar disk.id: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Snapshot:
        '''

        url = '/vms/{vm:id}/snapshots'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(snapshot),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return VmSnapshot(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, all_content=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]
        [@param all_content: true|false]

        @return Snapshots:
        '''

        url = '/vms/{vm:id}/snapshots'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={"All-Content":all_content}
                )

                return VmSnapshot(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={"All-Content":all_content}
            ).get_snapshot()

            return VmSnapshot(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, all_content=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]
        [@param all_content: true|false]

        @return Snapshots:
        '''

        url = '/vms/{vm:id}/snapshots'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={"All-Content":all_content}
        ).get_snapshot()

        return ParseHelper.toSubCollection(
            VmSnapshot,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmStatistic(params.Statistic, Base):
    def __init__(self, vm, statistic, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  statistic

        #SUB_COLLECTIONS
    def __new__(cls, vm, statistic, context):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, statistic, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

class VmStatistics(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Statistics:
        '''

        url = '/vms/{vm:id}/statistics'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmStatistic(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_statistic()

            return VmStatistic(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Statistics:
        '''

        url = '/vms/{vm:id}/statistics'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_statistic()

        return ParseHelper.toSubCollection(
            VmStatistic,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmTag(params.Tag, Base):
    def __init__(self, vm, tag, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  tag

        #SUB_COLLECTIONS
    def __new__(cls, vm, tag, context):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, tag, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vms/{vm:id}/tags/{tag:id}',
            {
                '{vm:id}': self.parentclass.get_id(),
                '{tag:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class VmTags(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, tag, expect=None, correlation_id=None):

        '''
        @type Tag:

        @param tag.id|name: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Tag:
        '''

        url = '/vms/{vm:id}/tags'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(tag),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return VmTag(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Tags:
        '''

        url = '/vms/{vm:id}/tags'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmTag(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_tag()

            return VmTag(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Tags:
        '''

        url = '/vms/{vm:id}/tags'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_tag()

        return ParseHelper.toSubCollection(
            VmTag,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class VmWatchdog(params.WatchDog, Base):
    def __init__(self, vm, watchdog, context):
        Base.__init__(self, context)
        self.parentclass = vm
        self.superclass  =  watchdog

        #SUB_COLLECTIONS
    def __new__(cls, vm, watchdog, context):
        if watchdog is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, watchdog, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vms/{vm:id}/watchdogs/{watchdog:id}',
            {
                '{vm:id}': self.parentclass.get_id(),
                '{watchdog:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param watchdog.action: string]
        [@param watchdog.model: string]
        [@param correlation_id: any string]

        @return WatchDog:
        '''

        url = '/vms/{vm:id}/watchdogs/{watchdog:id}'
        url = UrlHelper.replace(
            url,
            {
                '{vm:id}': self.parentclass.get_id(),
                '{watchdog:id}': self.get_id(),
            }
        )

        result = self.__getProxy().update(
            url=SearchHelper.appendQuery(url, {}),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return VmWatchdog(
            self.parentclass,
            result,
            self.context
        )

class VmWatchdogs(Base):

    def __init__(self, vm , context):
        Base.__init__(self, context)
        self.parentclass = vm

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, watchdog, expect=None, correlation_id=None):

        '''
        @type WatchDog:

        @param watchdog.action: string
        @param watchdog.model: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return WatchDog:
        '''

        url = '/vms/{vm:id}/watchdogs'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vm:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(watchdog),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return VmWatchdog(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return WatchDogs:
        '''

        url = '/vms/{vm:id}/watchdogs'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vm:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmWatchdog(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_watchdog()

            return VmWatchdog(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return WatchDogs:
        '''

        url = '/vms/{vm:id}/watchdogs'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vm:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_watchdog()

        return ParseHelper.toSubCollection(
            VmWatchdog,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Vmpool(params.VmPool, Base):
    def __init__(self, vmpool, context):
        Base.__init__(self, context)
        self.superclass = vmpool

        self.permissions = VmpoolPermissions(self, context)

    def __new__(cls, vmpool, context):
        if vmpool is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmpool, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vmpools/{vmpool:id}',
            {
                '{vmpool:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param vmpool.cluster.id|name: string]
        [@param vmpool.template.id|name: string]
        [@param vmpool.name: string]
        [@param vmpool.comment: string]
        [@param vmpool.size: int]
        [@param vmpool.max_user_vms: int]
        [@param vmpool.display.proxy: string]
        [@param vmpool.description: string]
        [@param correlation_id: any string]

        @return VmPool:
        '''

        url = '/vmpools/{vmpool:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{vmpool:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Vmpool(result, self.context)

    def allocatevm(self, action=params.Action(), correlation_id=None):
        '''
        @type Action:

        [@param action.async: boolean]
        [@param action.grace_period.expiry: long]
        [@param correlation_id: any string]

        @return Action:
        '''

        url = '/vmpools/{vmpool:id}/allocatevm'

        result = self.__getProxy().request(
            method='POST',
            url=UrlHelper.replace(
                url,
                {
                    '{vmpool:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(action),
            headers={"Correlation-Id":correlation_id}
        )

        return result

class VmpoolPermission(params.Permission, Base):
    def __init__(self, vmpool, permission, context):
        Base.__init__(self, context)
        self.parentclass = vmpool
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, vmpool, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmpool, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vmpools/{vmpool:id}/permissions/{permission:id}',
            {
                '{vmpool:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class VmpoolPermissions(Base):

    def __init__(self, vmpool , context):
        Base.__init__(self, context)
        self.parentclass = vmpool

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

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

        url = '/vmpools/{vmpool:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vmpool:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return VmpoolPermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/vmpools/{vmpool:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vmpool:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VmpoolPermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vmpool:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return VmpoolPermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/vmpools/{vmpool:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vmpool:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            VmpoolPermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Vmpools(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, vmpool, expect=None, correlation_id=None):
        '''
        @type VmPool:

        @param vmpool.cluster.id|name: string
        @param vmpool.template.id|name: string
        @param vmpool.name: string
        [@param vmpool.comment: string]
        [@param vmpool.size: int]
        [@param vmpool.max_user_vms: int]
        [@param vmpool.display.proxy: string]
        [@param vmpool.description: string]
        [@param vmpool.soundcard_enabled: boolean]
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return VmPool:
        '''

        url = '/vmpools'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(vmpool),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Vmpool(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return VmPools:
        '''

        url = '/vmpools'

        if id:
            try :
                return Vmpool(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={}
            ).get_vmpool()

            return Vmpool(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]

        @return VmPools:
        '''

        url='/vmpools'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={}
        ).get_vmpool()

        return ParseHelper.toCollection(
            Vmpool,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Vms(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, vm, correlation_id=None, expect=None):
        '''
        @type VM:

        Overload 1:
          @param vm.name: string
          @param vm.template.id|name: string
          @param vm.cluster.id|name: string
          [@param vm.instance_type.id|name: string]
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
          [@param vm.display.single_qxl_pci: boolean]
          [@param vm.display.type: string]
          [@param vm.display.allow_override: boolean]
          [@param vm.display.smartcard_enabled: boolean]
          [@param vm.display.file_transfer_enabled: boolean]
          [@param vm.display.copy_paste_enabled: boolean]
          [@param vm.display.keyboard_layout: string]
          [@param vm.os.cmdline: string]
          [@param vm.cpu.topology.cores: int]
          [@param vm.cpu.architecture: string]
          [@param vm.memory: long]
          [@param vm.memory_policy.guaranteed: long]
          [@param vm.memory_policy.ballooning: boolean]
          [@param vm.high_availability.priority: int]
          [@param vm.high_availability.enabled: boolean]
          [@param vm.domain.name: string]
          [@param vm.description: string]
          [@param vm.comment: string]
          [@param vm.stateless: boolean]
          [@param vm.permissions.clone: boolean]
          [@param vm.delete_protected: boolean]
          [@param vm.sso.methods.method: collection]
          {
            [@ivar method.id: string]
          }
          [@param vm.rng_device.rate.bytes: int]
          [@param vm.rng_device.rate.period: int]
          [@param vm.rng_device.source: string]
          [@param vm.console.enabled: boolean]
          [@param vm.cpu.mode: string]
          [@param vm.cpu.topology.sockets: int]
          [@param vm.cpu_shares: int]
          [@param vm.placement_policy.affinity: string]
          [@param vm.placement_policy.host.id|name: string]
          [@param vm.origin: string]
          [@param vm.os.kernel: string]
          [@param vm.disks.clone: boolean]
          [@param vm.disks.disk: collection]
          {
            [@ivar disk.id: string]
            [@ivar storage_domains.storage_domain: collection]
            {
              [@param storage_domain.id: string]
            }
          }
          [@param vm.tunnel_migration: boolean]
          [@param vm.migration_downtime: int]
          [@param vm.virtio_scsi.enabled: boolean]
          [@param vm.soundcard_enabled: boolean]
          [@param vm.custom_emulated_machine: string]
          [@param vm.custom_cpu_model: string]
          [@param vm.payloads.payload: collection]
          {
            [@ivar payload.type: string]
            [@ivar payload.volume_id: string]
            [@ivar payload.files.file: collection]
            {
              [@param file.name: string]
              [@param file.content: string]
            }
          }
          [@param vm.initialization.configuration.type: string]
          [@param vm.initialization.configuration.data: string]
          [@param vm.cpu.cpu_tune.vcpu_pin: collection]
          {
            [@ivar vcpu_pin.vcpu: int]
            [@ivar vcpu_pin.cpu_set: string]
          }
          [@param vm.use_latest_template_version: boolean]
          [@param vm.serial_number.policy: string]
          [@param vm.serial_number.value: string]
          [@param vm.bios.boot_menu.enabled: boolean]
          [@param vm.numa_tune_mode: string]
          [@param vm.start_paused: boolean]
          [@param vm.cpu_profile.id: string]
          [@param vm.migration.auto_converge: string]
          [@param vm.migration.compressed: string]
        Overload 2:
          @param vm.name: string
          @param vm.template.id|name: string
          @param vm.cluster.id|name: string
          @param vm.snapshots.snapshot: collection
          {
            @ivar snapshot.id: string
          }
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
          [@param vm.display.single_qxl_pci: boolean]
          [@param vm.display.type: string]
          [@param vm.display.allow_override: boolean]
          [@param vm.display.smartcard_enabled: boolean]
          [@param vm.display.file_transfer_enabled: boolean]
          [@param vm.display.copy_paste_enabled: boolean]
          [@param vm.display.keyboard_layout: string]
          [@param vm.os.cmdline: string]
          [@param vm.cpu.topology.cores: int]
          [@param vm.cpu_shares: int]
          [@param vm.cpu.architecture: string]
          [@param vm.memory: long]
          [@param vm.memory_policy.guaranteed: long]
          [@param vm.memory_policy.ballooning: boolean]
          [@param vm.high_availability.priority: int]
          [@param vm.high_availability.enabled: boolean]
          [@param vm.domain.name: string]
          [@param vm.description: string]
          [@param vm.comment: string]
          [@param vm.stateless: boolean]
          [@param vm.delete_protected: boolean]
          [@param vm.sso.methods.method: collection]
          {
            [@ivar method.id: string]
          }
          [@param vm.rng_device.rate.bytes: int]
          [@param vm.rng_device.rate.period: int]
          [@param vm.rng_device.source: string]
          [@param vm.console.enabled: boolean]
          [@param vm.cpu.topology.sockets: int]
          [@param vm.placement_policy.affinity: string]
          [@param vm.placement_policy.host.id|name: string]
          [@param vm.origin: string]
          [@param vm.os.kernel: string]
          [@param vm.tunnel_migration: boolean]
          [@param vm.migration_downtime: int]
          [@param vm.virtio_scsi.enabled: boolean]
          [@param vm.soundcard_enabled: boolean]
          [@param vm.custom_emulated_machine: string]
          [@param vm.custom_cpu_model: string]
          [@param vm.payloads.payload: collection]
          {
            [@ivar payload.type: string]
            [@ivar payload.volume_id: string]
            [@ivar payload.files.file: collection]
            {
              [@param file.name: string]
              [@param file.content: string]
            }
          }
          [@param vm.cpu.cpu_tune.vcpu_pin: collection]
          {
            [@ivar vcpu_pin.vcpu: int]
            [@ivar vcpu_pin.cpu_set: string]
          }
          [@param vm.serial_number.policy: string]
          [@param vm.serial_number.value: string]
          [@param vm.bios.boot_menu.enabled: boolean]
          [@param vm.numa_tune_mode: string]
          [@param vm.start_paused: boolean]
          [@param vm.cpu_profile.id: string]
          [@param vm.migration.auto_converge: string]
          [@param vm.migration.compressed: string]
        Overload 3:
          @param vm.initialization.configuration.type: string
          @param vm.initialization.configuration.data: string
          [@param vm.name: string]
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
          [@param vm.display.allow_override: boolean]
          [@param vm.display.smartcard_enabled: boolean]
          [@param vm.display.file_transfer_enabled: boolean]
          [@param vm.display.copy_paste_enabled: boolean]
          [@param vm.display.keyboard_layout: string]
          [@param vm.os.cmdline: string]
          [@param vm.cpu.topology.cores: int]
          [@param vm.memory: long]
          [@param vm.memory_policy.guaranteed: long]
          [@param vm.memory_policy.ballooning: boolean]
          [@param vm.high_availability.priority: int]
          [@param vm.high_availability.enabled: boolean]
          [@param vm.domain.name: string]
          [@param vm.description: string]
          [@param vm.comment: string]
          [@param vm.stateless: boolean]
          [@param vm.permissions.clone: boolean]
          [@param vm.delete_protected: boolean]
          [@param vm.sso.methods.method: collection]
          {
            [@ivar method.id: string]
          }
          [@param vm.rng_device.rate.bytes: int]
          [@param vm.rng_device.rate.period: int]
          [@param vm.rng_device.source: string]
          [@param vm.cpu.mode: string]
          [@param vm.cpu.topology.sockets: int]
          [@param vm.placement_policy.affinity: string]
          [@param vm.placement_policy.host.id|name: string]
          [@param vm.origin: string]
          [@param vm.os.kernel: string]
          [@param vm.disks.clone: boolean]
          [@param vm.disks.disk: collection]
          {
            [@ivar disk.id: string]
            [@ivar storage_domains.storage_domain: collection]
            {
              [@param storage_domain.id: string]
            }
          }
          [@param vm.tunnel_migration: boolean]
          [@param vm.migration_downtime: int]
          [@param vm.virtio_scsi.enabled: boolean]
          [@param vm.payloads.payload: collection]
          {
            [@ivar payload.type: string]
            [@ivar payload.volume_id: string]
            [@ivar payload.files.file: collection]
            {
              [@param file.name: string]
              [@param file.content: string]
            }
          }
          [@param vm.initialization.configuration.type: string]
          [@param vm.initialization.configuration.data: string]
          [@param vm.initialization.regenerate_ids: boolean]
          [@param vm.cpu.cpu_tune.vcpu_pin: collection]
          {
            [@ivar vcpu_pin.vcpu: int]
            [@ivar vcpu_pin.cpu_set: string]
          }
          [@param vm.serial_number.policy: string]
          [@param vm.serial_number.value: string]
          [@param vm.bios.boot_menu.enabled: boolean]
          [@param vm.numa_tune_mode: string]
          [@param vm.start_paused: boolean]
          [@param vm.cpu_profile.id: string]
          [@param vm.migration.auto_converge: string]
          [@param vm.migration.compressed: string]
        [@param correlation_id: any string]
        [@param expect: 201-created]

        @return VM:
        '''

        url = '/vms'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(vm),
           headers={"Correlation-Id":correlation_id, "Expect":expect}
        )

        return Vm(result, self.context)

    def get(self, name=None, all_content=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]
        [@param all_content: true|false]

        @return VMs:
        '''

        url = '/vms'

        if id:
            try :
                return Vm(
                    self.__getProxy().get(
                        url=UrlHelper.append(url, id),
                        headers={"All-Content":all_content}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=SearchHelper.appendQuery(url, {'search:query':'name='+name}),
                headers={"All-Content":all_content}
            ).get_vm()

            return Vm(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, query=None, case_sensitive=True, max=None, all_content=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param query: string (oVirt engine search dialect query)]
        [@param case_sensitive: boolean (true|false)]
        [@param max: int (max results)]
        [@param all_content: true|false]

        @return VMs:
        '''

        url='/vms'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'search:query':query,'case_sensitive:matrix':case_sensitive,'max:matrix':max}),
            headers={"All-Content":all_content}
        ).get_vm()

        return ParseHelper.toCollection(
            Vm,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

class Vnicprofile(params.VnicProfile, Base):
    def __init__(self, vnicprofile, context):
        Base.__init__(self, context)
        self.superclass = vnicprofile

        self.permissions = VnicprofilePermissions(self, context)

    def __new__(cls, vnicprofile, context):
        if vnicprofile is None: return None
        obj = object.__new__(cls)
        obj.__init__(vnicprofile, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vnicprofiles/{vnicprofile:id}',
            {
                '{vnicprofile:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

    def update(self, correlation_id=None):
        '''
        [@param vnicprofile.name: string]
        [@param vnicprofile.description: string]
        [@param vnicprofile.port_mirroring: boolean]
        [@param vnicprofile.custom_properties.custom_property: collection]
        {
          [@ivar custom_property.name: string]
          [@ivar custom_property.value: string]
        }
        [@param correlation_id: any string]

        @return VnicProfile:
        '''

        url = '/vnicprofiles/{vnicprofile:id}'

        result = self.__getProxy().update(
            url=UrlHelper.replace(
                url,
                {
                    '{vnicprofile:id}': self.get_id(),
                }
            ),
            body=ParseHelper.toXml(self.superclass),
            headers={"Correlation-Id":correlation_id}
        )

        return Vnicprofile(result, self.context)

class VnicprofilePermission(params.Permission, Base):
    def __init__(self, vnicprofile, permission, context):
        Base.__init__(self, context)
        self.parentclass = vnicprofile
        self.superclass  =  permission

        #SUB_COLLECTIONS
    def __new__(cls, vnicprofile, permission, context):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vnicprofile, permission, context)
        return obj

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def delete(self, async=None, correlation_id=None):
        '''
        [@param async: boolean (true|false)]
        [@param correlation_id: any string]

        @return None:
        '''

        url = UrlHelper.replace(
            '/vnicprofiles/{vnicprofile:id}/permissions/{permission:id}',
            {
                '{vnicprofile:id}': self.parentclass.get_id(),
                '{permission:id}': self.get_id(),
            }
        )

        return self.__getProxy().delete(
            url=SearchHelper.appendQuery(
                url,
                {'async:matrix':async}
            ),
            headers={"Correlation-Id":correlation_id,"Content-type":None}
        )

class VnicprofilePermissions(Base):

    def __init__(self, vnicprofile , context):
        Base.__init__(self, context)
        self.parentclass = vnicprofile

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, permission, expect=None, correlation_id=None):

        '''
        @type Permission:

        Overload 1:
          @param permission.user.id: string
          @param permission.role.id: string
        Overload 2:
          @param permission.group.id: string
          @param permission.role.id: string
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return Permission:
        '''

        url = '/vnicprofiles/{vnicprofile:id}/permissions'

        result = self.__getProxy().add(
            url=UrlHelper.replace(
                url,
                {
                    '{vnicprofile:id}': self.parentclass.get_id(),
                }
            ),
            body=ParseHelper.toXml(permission),
            headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return VnicprofilePermission(
            self.parentclass,
            result,
            self.context
        )

    def get(self, name=None, id=None):

        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return Permissions:
        '''

        url = '/vnicprofiles/{vnicprofile:id}/permissions'

        if id:
            try :
                result = self.__getProxy().get(
                    url=UrlHelper.append(
                        UrlHelper.replace(
                            url,
                            {
                                '{vnicprofile:id}': self.parentclass.get_id(),
                            }
                        ),
                        id
                    ),
                    headers={}
                )

                return VnicprofilePermission(
                    self.parentclass,
                    result,
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                url=UrlHelper.replace(
                    url,
                    {
                        '{vnicprofile:id}': self.parentclass.get_id(),
                    }
                ),
                headers={}
            ).get_permission()

            return VnicprofilePermission(
                self.parentclass,
                FilterHelper.getItem(
                    FilterHelper.filter(
                        result,
                        {'name':name}
                    ),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])

    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)"]
        [@param max: int (max results)]

        @return Permissions:
        '''

        url = '/vnicprofiles/{vnicprofile:id}/permissions'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(
                url=UrlHelper.replace(
                    url=url,
                    args={
                        '{vnicprofile:id}': self.parentclass.get_id(),
                    }
                ),
                qargs={'max:matrix':max}
            ),
            headers={}
        ).get_permission()

        return ParseHelper.toSubCollection(
            VnicprofilePermission,
            self.parentclass,
            FilterHelper.filter(
                result,
                kwargs
            ),
            context=self.context
        )

class Vnicprofiles(Base):
    def __init__(self, context):
        Base.__init__(self, context)

    def __getProxy(self):
        proxy = context.manager[self.context].get('proxy')
        if proxy:
            return proxy
        #This may happen only if sdk was explicitly disconnected
        #using .disconnect() method, but resource instance ref. is
        #still available at client's code.
        raise DisconnectedError

    def add(self, vnicprofile, expect=None, correlation_id=None):
        '''
        @type VnicProfile:

        @param vnicprofile.network.id: string
        @param vnicprofile.name: string
        [@param vnicprofile.description: string]
        [@param vnicprofile.port_mirroring: boolean]
        [@param vnicprofile.custom_properties.custom_property: collection]
        {
          [@ivar custom_property.name: string]
          [@ivar custom_property.value: string]
        }
        [@param expect: 201-created]
        [@param correlation_id: any string]

        @return VnicProfile:
        '''

        url = '/vnicprofiles'

        result = self.__getProxy().add(
           url=url,
           body=ParseHelper.toXml(vnicprofile),
           headers={"Expect":expect, "Correlation-Id":correlation_id}
        )

        return Vnicprofile(result, self.context)

    def get(self, name=None, id=None):
        '''
        [@param id  : string (the id of the entity)]
        [@param name: string (the name of the entity)]

        @return VnicProfiles:
        '''

        url = '/vnicprofiles'

        if id:
            try :
                return Vnicprofile(
                    self.__getProxy().get(
                                url=UrlHelper.append(url, id),
                                headers={}
                    ),
                    self.context
                )
            except RequestError, err:
                if err.status and err.status == 404:
                    return None
                raise err
        elif name:
            result = self.__getProxy().get(
                    url=url,
                    headers={}
            ).get_vnic_profile()

            return Vnicprofile(
                FilterHelper.getItem(
                    FilterHelper.filter(result, {'name':name}),
                    query="name=" + name
                ),
                self.context
            )
        else:
            raise MissingParametersError(['id', 'name'])


    def list(self, max=None, **kwargs):
        '''
        [@param **kwargs: dict (property based filtering)]
        [@param max: int (max results)]

        @return VnicProfiles:
        '''

        url='/vnicprofiles'

        result = self.__getProxy().get(
            url=SearchHelper.appendQuery(url, {'max:matrix':max}),
            headers={}
        ).get_vnic_profile()

        return ParseHelper.toCollection(
            Vnicprofile,
            FilterHelper.filter(result, kwargs),
            context=self.context
        )

