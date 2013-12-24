#
# Copyright (c) 2012 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from codegen.rsdl.abstractrsdlcodegen import AbstractRsdlCodegen
from codegen.entrypoint.entrypoint import EntryPoint
from codegen.utils.typeutil import TypeUtil
from ovirtsdk.infrastructure.context import context
from ovirtsdk.utils.reflectionhelper import ReflectionHelper
from ovirtsdk.xml import params
from ovirtsdk.utils.parsehelper import ParseHelper
from codegen.collection.collection import Collection
from codegen.utils.fileutils import FileUtils
from codegen.utils.stringutils import StringUtils
from codegen.resource.resource import Resource
from codegen.subresource.subresource import SubResource
from codegen.subcollection.subcollection import SubCollection
from codegen.imprt.imprt import Import

class RsdlCodegen(AbstractRsdlCodegen):
    '''
    Providing RSDL codegen capabilities
    '''

    BROKERS_FILE = '../ovirtsdk/infrastructure/brokers.py'
    ENTRY_POINT_FILE = '../ovirtsdk/api.py'
    KNOWN_ACTIONS = ['get', 'add', 'delete', 'update']

    # TODO:should be fixed on server side
    COLLECTION_TO_ENTITY_EXCEPTIONS = [
           'Capabilities',
           'Storage',
           'VersionCaps'
    ]

    # TODO:should be fixed on server side (naming inconsistency)
    NAMING_ENTITY_EXCEPTIONS = {
            'host_storage':'storage'
    }

    # names that should not be used as method/s names
    PRESERVED_NAMES = [
           'import', 'from'
    ]

    # cache known python2xml bindings types
    KNOWN_WRAPPER_TYPES = ReflectionHelper.getClassNames(params)

    def __init__(self, api):
        '''
        @param path: codegen path
        '''
        AbstractRsdlCodegen.__init__(self, RsdlCodegen.BROKERS_FILE)

        self.__api = api
        self.context = self.__api.id

    def doGenerate(self, path):
        '''
        Generates the code
        
        @param path: path to generate the code at
        '''
        AbstractRsdlCodegen.doGenerate(self, path)

        collectionsHolder = {}
        usedRels = []

        for link in context.manager[self.context].get('proxy') \
                                                 .request('GET', '/api?rsdl') \
                                                 .links.link:

            response_type = None
            body_type = None

            # link metadata
            rel = link.rel
            url = link.href

            if (not (rel + '_' + url) in usedRels):

                # request
                http_method = link.request.http_method
                if (link.request and link.request.body and hasattr(link.request.body, 'type_')):
                    body_type = link.request.body.type_

                # response
                response = link.response
                if (link.response and hasattr(link.response, 'type_')):
                    response_type = StringUtils.toSingular(
                                           response.type_,
                                           RsdlCodegen.COLLECTION_TO_ENTITY_EXCEPTIONS
                                    )

                # get relations
                splitted_url = url.strip()[1:].split('/')
                splitted_url.pop(0)

                # append resource/method/rel
                self.__appendResource(rel, url, http_method, body_type, link,
                                      response_type, TypeUtil.toOrderedMap(splitted_url),
                                      collectionsHolder, RsdlCodegen.KNOWN_ACTIONS)

                usedRels.append(rel + '_' + url)

        # create root collection/s instances in entry point
        self.__appendRootCollections(collectionsHolder)

        # store content
        self.__persist(collectionsHolder)

    def __persist(self, collectionsHolder):
        '''
        Persist generated content
        
        @param collectionsHolder: generated content holder
        '''
        try:
            brokers_file = ''
            api_file = ''

            coll_candidates = ''
            root_coll_candidates = []

            brokers_file += Import.getimports()

            keys = collectionsHolder.keys()
            keys.sort()

            for k in keys:
                if collectionsHolder[k].has_key('sub_collections'):
                    collectionsHolder[k]['body'] = \
                        (collectionsHolder[k]['body'].replace(
                                      Resource.SUB_COLLECTIONS_FIXME,
                                      Resource.addSubCollectionInstances('self',  # k.lower(),
                                                                         collectionsHolder[k]['sub_collections']))) \
                                                     .replace(Resource.SUB_COLLECTIONS_FIXME, '')

                brokers_file += collectionsHolder[k]['body']

                coll_candidate = EntryPoint.collection(k, collectionsHolder[k])
                if coll_candidate is not None:
                    coll_candidates += coll_candidate
                    root_coll_candidates.append(k)

            api_file += EntryPoint.entryPoint(self.__api, root_coll_candidates, coll_candidates)
        finally:
            FileUtils.save(RsdlCodegen.BROKERS_FILE, brokers_file)
            FileUtils.save(RsdlCodegen.ENTRY_POINT_FILE, api_file)

    def __appendRootCollections(self, collectionsHolder={}):
        '''
        Appends RootCollections
        
        @param collectionsHolder: collections holder
        '''
        collections = ''
        for v in collectionsHolder.values():
            if (v.has_key('root_collection') and v['root_collection'] == True):
                collections += v['name'] + ' = ' + self.__toResourceType(v['name']) + '()'

    def __appendResource(self, rel, url, http_method, body_type, link, response_type,
                         resources={}, collectionsHolder={}, known_actions=[]):
        '''
        Appends resource and it's method/action
        
        @param rel: URL rel
        @param url: URI
        @param http_method: HTTP method to use
        @param body_type: body type
        @param link: DetailedLink
        @param response_type: response type
        @param resources: resources holder
        @param collectionsHolder: collections holder
        @param known_actions: known action types
        '''
        i = 0
        ln = len(resources)
        #=========================================================

        # resources {'vms':xxx,'disks':yyy,'snapshots':zzz}
        # vms/xxx/disks/yyy/snapshots/zzz

        # 1.coll         vms/None:1
        # 2.res          vms/xxx :1
        # 3.sub-coll     vms/xxx/disks/None :2
        # 4.sub-res      vms/xxx/disks/yyy  :2
        # 5.sub-sub-col  vms/xxx/disks/yyy/snapshots/None :3
        # 6.sub-sub-res  vms/xxx/disks/yyy/snapshots/zzz  :3

        # N.sub-sub-res  vms/xxx/disks/yyy/snapshots/zzz/^N  :3

        # num of permutations for N=K is K
        # num of pairs        for N=K is k/2 (to differ between the res & coll check the last pair val)

        root_coll = None
        for k, v in resources.items():
            i += 1
            if(ln is 1):  # vms/xxx
                # coll = k
                coll = ParseHelper.getXmlWrapperType(k)
                if (v is None):
                    self.__extendCollection(
                                coll,
                                url,
                                rel,
                                http_method,
                                body_type,
                                link,
                                response_type,
                                collectionsHolder
                        )
                else:
                    self.__extendResource(coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
            elif(ln is 2):  # vms/xxx/disks/yyy
                if (i is 1):  # vms/xxx
                    # root_coll = k
                    root_coll = ParseHelper.getXmlWrapperType(k)
                if (i is 2):  # disks/yyy
                    # sub_coll = k
                    sub_coll = ParseHelper.getXmlWrapperType(k)
                    if (v is None and self.__isCollection(link)):
                        self.__extendSubCollection(root_coll, sub_coll, url, rel, http_method,
                                                   body_type, link, response_type, collectionsHolder)
                    elif((v is None or v.find(':id') == -1) and http_method == 'POST'):
                        if v is None:
                            self.__createAction(root_coll, None, sub_coll, url, rel, http_method,
                                                body_type, link, response_type, collectionsHolder)
                        else:
                            self.__createAction(root_coll, sub_coll, v, url, rel, http_method,
                                                body_type, link, response_type, collectionsHolder, collection_action=True)
                    else:
                        self.__extendSubResource(root_coll, sub_coll, url, rel, http_method,
                                                 body_type, link, response_type, collectionsHolder)
            elif(ln >= 3):
                if (i is 1):
                    root_coll = ParseHelper.getXmlWrapperType(k)
                if (i is 2):
                    sub_coll = ParseHelper.getXmlWrapperType(k)
                    if (v is None and self.__isCollection(link)):
                        self.__extendSubCollection(root_coll, sub_coll, url, rel, http_method,
                                                   body_type, link, response_type, collectionsHolder)
                    elif(v is None):
                        self.__createAction(root_coll, None, sub_coll, url, rel, http_method,
                                            body_type, link, response_type, collectionsHolder)
                    else:
                        self.__extendSubResource(root_coll, sub_coll, url, rel, http_method,
                                                 body_type, link, response_type, collectionsHolder, extend_only=(ln > i))
                if (i is 3 and v is None and not self.__isCollection(link)):
                    self.__createAction(root_coll, sub_coll, k, url, rel, http_method,
                                        body_type, link, response_type, collectionsHolder)
                elif(i >= 3):
                    sub_root_coll = StringUtils.toSingular(
                           root_coll, RsdlCodegen.COLLECTION_TO_ENTITY_EXCEPTIONS
                    ) + self.__toResourceType(sub_coll)
                    sub_res_coll = self.__toResourceType(resources.keys()[i - 1])

                    if (v is None and self.__isCollection(link)):
                        self.__extendSubCollection(sub_root_coll, sub_res_coll, url, rel, http_method,
                                                   body_type, link, response_type, collectionsHolder)
                    elif(self.__isAction(link) and i == ln):
                        self.__createAction(sub_root_coll, sub_res_coll, rel, url, rel, http_method,
                                            body_type, link, response_type, collectionsHolder, force_sub_resource=True)
                    else:
                        self.__extendSubResource(sub_root_coll, sub_res_coll, url, rel, http_method,
                                                 body_type, link, response_type, collectionsHolder,
                                                 extend_only=(ln > i))

                    root_coll = StringUtils.toSingular(sub_root_coll)
                    sub_coll = sub_res_coll

    def __extendCollection(self, collection, url, rel, http_method,
                           body_type, link, response_type, collectionsHolder):
        '''
        Extends collection
        
        @param collection: collection to add
        @param url: URI
        @param rel: URL rel
        @param http_method: HTTP method to use
        @param body_type: body type
        @param link: DetailedLink
        @param response_type: response type
        @param collectionsHolder: collections holder
        '''

        if (not collectionsHolder.has_key(collection)):
            collection_body = Collection.collection(collection)
            collectionsHolder[collection] = {'body':collection_body, 'root_collection':True, 'name':collection}

        # ['get', 'add', 'delete', 'update']
        if (rel == 'get'):
            get_method = Collection.get(url, response_type, link, RsdlCodegen.KNOWN_WRAPPER_TYPES)
            collectionsHolder[collection]['body'] += get_method

            list_method = Collection.list(url, response_type, link, RsdlCodegen.KNOWN_WRAPPER_TYPES)
            collectionsHolder[collection]['body'] += list_method

        elif (rel == 'add'):
            add_method = Collection.add(url, body_type, response_type, link, RsdlCodegen.KNOWN_WRAPPER_TYPES)
            collectionsHolder[collection]['body'] += add_method

    def __extendResource(self, collection, url, rel, http_method, body_type,
                         link, response_type, collectionsHolder):
        '''
        Extends resource
        
        @param collection: collection to add
        @param url: URI
        @param rel: URL rel
        @param http_method: HTTP method to use
        @param body_type: body type
        @param link: DetailedLink
        @param response_type: response type
        @param collectionsHolder: collections holder
        '''
        resource = response_type if response_type is not None \
                                 else collection[:len(collection) - 1]

        if (not collectionsHolder.has_key(resource)):
            resource_body = Resource.resource(self.__toResourceType(resource), [], RsdlCodegen.KNOWN_WRAPPER_TYPES)
            collectionsHolder[resource] = {'body':resource_body}

        # ['get', 'add', 'delete', 'update']
        if (rel == 'delete'):
            del_method = Resource.delete(url, body_type, link, resource)
            collectionsHolder[resource]['body'] += del_method
        elif (rel == 'update'):
            upd_method = Resource.update(url, self.__toResourceType(resource), link, RsdlCodegen.KNOWN_WRAPPER_TYPES)
            collectionsHolder[resource]['body'] += upd_method

    def __createAction(self, root_coll, sub_coll, action_name, url, rel,
                       http_method, body_type, link, response_type, collectionsHolder,
                       collection_action=False, force_sub_resource=False):
        '''
        Creates action
        
        @param root_coll: root collection
        @param sub_coll: sub collection
        @param action_name: action name
        @param url: URI
        @param rel: URL rel
        @param http_method: HTTP method to use
        @param body_type: body type
        @param link: DetailedLink
        @param response_type: response type
        @param collectionsHolder: collections holder
        @param collection_action: is action to be interpritated as collection action
        '''
        resource = root_coll[:len(root_coll) - 1]
        sub_resource = sub_coll[:len(sub_coll) - 1] if sub_coll is not None and not collection_action else None if sub_coll is None else sub_coll
        action_name = self.__adaptActionName(action_name, sub_resource if sub_resource is not None
                                                                       else resource)
        if (sub_coll is None or sub_coll == '') and not force_sub_resource:
            if (not collectionsHolder.has_key(resource)):
                self.__extendCollection(root_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
            action_body = Resource.action(url, body_type, link, action_name, resource, http_method, {})
            collectionsHolder[resource]['body'] += action_body
        else:
            if not force_sub_resource:
                nested_collection = root_coll[:len(root_coll) - 1] + sub_coll
                nested_resource = nested_collection[:len(nested_collection) - 1] if not collection_action else nested_collection

                if (not collectionsHolder.has_key(nested_collection)and not force_sub_resource):
                    self.__extendSubCollection(root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)

                if (not collectionsHolder.has_key(nested_resource) and not force_sub_resource):
                    self.__extendSubResource(root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)

                action_body = SubResource.action(url, link, action_name, resource, body_type, sub_resource, http_method, {}, collection_action)

                collectionsHolder[nested_resource]['body'] += action_body
            else:
                action_body = SubResource.action(url, link, action_name, resource, body_type, sub_resource, http_method, {}, collection_action)

                collectionsHolder[resource]['body'] += action_body

    # rename /preserved/ names
    def __adaptActionName(self, action_name, resource):
        '''
        Adapts action name in case it has py preserved name
        
        @param action_name: action name
        @param resource: resource name to be appended as ACTIONNAME_RESOURCE
                         when action name in py preserved name/s
        '''
        if action_name in RsdlCodegen.PRESERVED_NAMES:
            return action_name + '_' + resource.lower()
        return action_name

    def __isCollection(self, link):
        '''
        Checks if URI is an collection
        
        @param link: DetailedLink
        '''
        return (link.href.endswith('s') or link.href.split('/')[-1].capitalize() in RsdlCodegen.COLLECTION_TO_ENTITY_EXCEPTIONS) \
                and not self.__isAction(link)

    def __isAction(self, link):
        '''
        Checks if URI is an action
        
        @param link: DetailedLink
        '''
        return link.href.endswith('/' + link.rel) and link.request.http_method == 'POST'

    def __toResourceType(self, candidate):
        '''
        Formats candidate in to ResourceType
        
        @param candidate: candidate to format
        '''
        return candidate[0:1].upper() + candidate[1:len(candidate)]

    @staticmethod
    def __getParentCache(collectionsHolder, parent, KNOWN_WRAPPER_TYPES={}):
        '''
        Fetches ParentCache
        
        @param collectionsHolder: collections holder
        @param parent: parent to process
        @param KNOWN_WRAPPER_TYPES: KNOWN_WRAPPER_TYPES
        '''
        if collectionsHolder.has_key(parent):
            return collectionsHolder[parent]

        actual_parent = TypeUtil.getValueByKeyOrNone(parent.lower(), KNOWN_WRAPPER_TYPES)
        if actual_parent is not None and collectionsHolder.has_key(actual_parent):
            return collectionsHolder[actual_parent]

        return None

    def __extendSubCollection(self, root_coll, sub_coll, url, rel, http_method,
                              body_type, link, response_type, collectionsHolder):
        '''
        Extends sub-collection
        
        @param root_coll: root collection
        @param sub_coll: sub collection
        @param url: URI
        @param rel: URL rel
        @param http_method: HTTP method to use
        @param body_type: body type
        @param link: DetailedLink
        @param response_type: response type
        @param collectionsHolder: collections holder
        '''
        root_res = StringUtils.toSingular(root_coll, RsdlCodegen.COLLECTION_TO_ENTITY_EXCEPTIONS)
        sub_res = response_type if response_type is not None \
                                else sub_coll[:len(sub_coll) - 1]
        sub_coll_type = root_res + sub_coll
        sub_res_type = StringUtils.toSingular(sub_coll_type, RsdlCodegen.COLLECTION_TO_ENTITY_EXCEPTIONS)

        if (not collectionsHolder.has_key(sub_coll_type)):
            sub_coll_body = SubCollection.collection(sub_coll_type, root_res)

            collectionsHolder[sub_coll_type] = {'body':sub_coll_body}

        parentCache = self.__getParentCache(collectionsHolder, root_res, RsdlCodegen.KNOWN_WRAPPER_TYPES)
        if parentCache is None:
            print 'failed locating cache for: %s, at url: %s \n' % (root_res, url)
        else:
            if not parentCache.has_key('sub_collections'): parentCache['sub_collections'] = {}
            parentCache['sub_collections'][sub_coll.lower()] = (sub_coll_type)

        # ['get', 'add']
        if (rel == 'get'):
            get_method_body = SubCollection.get(url, link, root_res,
                                                self.__toResourceType(sub_res_type),
                                                sub_res, RsdlCodegen.KNOWN_WRAPPER_TYPES,
                                                RsdlCodegen.NAMING_ENTITY_EXCEPTIONS
                                            )
            collectionsHolder[sub_coll_type]['body'] += get_method_body

            list_method = SubCollection.list(url, link, root_res, self.__toResourceType(sub_res_type),
                                              sub_res, RsdlCodegen.KNOWN_WRAPPER_TYPES, RsdlCodegen.NAMING_ENTITY_EXCEPTIONS)

            collectionsHolder[sub_coll_type]['body'] += list_method

        elif (rel == 'add'):
            add_method = SubCollection.add(url, link, body_type, root_res, self.__toResourceType(sub_res_type), RsdlCodegen.KNOWN_WRAPPER_TYPES)
            collectionsHolder[sub_coll_type]['body'] += add_method

    def __extendSubResource(self, root_coll, sub_coll, url, rel, http_method, body_type,
                            link, response_type, collectionsHolder, extend_only=False):
        '''
        Extends sub-resource
        
        @param root_coll: root collection
        @param sub_coll: sub collection
        @param url: URI
        @param rel: URL rel
        @param http_method: HTTP method to use
        @param body_type: body type
        @param link: DetailedLink
        @param response_type: response type
        @param collectionsHolder: collections holder
        '''
        root_res = StringUtils.toSingular(root_coll, RsdlCodegen.COLLECTION_TO_ENTITY_EXCEPTIONS)
        sub_res = StringUtils.toSingular(sub_coll, RsdlCodegen.COLLECTION_TO_ENTITY_EXCEPTIONS)
        sub_res_type = root_res + sub_res

        if (not collectionsHolder.has_key(sub_res_type)):
            sub_resource_body = SubResource.resource(sub_res_type, self.__toResourceType(sub_res), root_res, RsdlCodegen.KNOWN_WRAPPER_TYPES)
            collectionsHolder[sub_res_type] = {'body':sub_resource_body}

        if not extend_only:
            # ['delete', 'update']
            if (rel == 'delete'):
                del_method = SubResource.delete(url, link, root_res, sub_res, body_type)
                collectionsHolder[sub_res_type]['body'] += del_method
            elif (rel == 'update'):
                update_method = SubResource.update(url, link, root_res,
                                                   self.__toResourceType(sub_res),
                                                   sub_res_type, RsdlCodegen.KNOWN_WRAPPER_TYPES)

                collectionsHolder[sub_res_type]['body'] += update_method

    def doClean(self, path):
        '''
        Cleans the package
        
        @param path: path to clean
        '''
        FileUtils.delete(RsdlCodegen.BROKERS_FILE)

    def doPreGenerate(self):
        '''
        Pre-generate call
        '''

        # refreshes previously generated sources
        reload(params)
