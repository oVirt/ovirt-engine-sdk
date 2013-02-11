#!/usr/bin/python
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

from ovirtsdk.api import API
from codegen.imp.imprt import Import
from codegen.collection.resource import Resource
from codegen.entrypoint.entrypoint import EntryPoint
from codegen.utils.typeutil import TypeUtil
from ovirtsdk.utils.reflectionhelper import ReflectionHelper
from ovirtsdk.web.connection import Connection
from genparams import paramsHandle
from ovirtsdk.infrastructure.errors import RequestError
from ovirtsdk.infrastructure.context import context
from ovirtsdk.utils.ordereddict import OrderedDict

SERVER = 'http://localhost:8080'
USER = 'admin@internal'
PASSWORD = 'letmein!'

BROKERS_FILE = '../ovirtsdk/infrastructure/brokers.py'
ENTRY_POINT_FILE = '../ovirtsdk/api.py'
XML_PARAMS_FILE = '../ovirtsdk/xml/params.py'
XML_PARAMS_TMP_FILE = '/tmp/params.py'
SCHEMA_FILE = '/tmp/api.py'

KNOWN_ACTIONS = ['get', 'add', 'delete', 'update']

# TODO:should be fixed on server side
COLLECTION_TO_ENTITY_EXCEPTIONS = ['Capabilities', 'Storage', 'VersionCaps']

# TODO:should be fixed on server side (naming inconsistency)
NAMING_ENTITY_EXCEPTIONS = {'host_storage':'storage'}

# names that should not be used as method/s names
PRESERVED_NAMES = ['import', 'from']

# xml wrapper (actual server) types
KNOWN_WRAPPER_TYPES = {}

class CodeGen():
    """ Generates oVirt python bindings based on api RSDL meta """

    def __init__(self):
        self.__api = API(url=SERVER, username=USER, password=PASSWORD)
        self.context = self.__api.id
        self.__conn = Connection(url=SERVER, port=None, key_file=None, cert_file=None,
                               ca_file=None, strict=False, timeout=None, username=USER,
                               password=PASSWORD, manager=self, debug=False)

    def generate(self):
        """ Generates resources brokers """

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
                    response_type = self.__toSingular(response.type_)

                # get relations
                splitted_url = url.strip()[1:].split('/')
                splitted_url.pop(0)

                # append resource/method/rel
                self.__appendResource(rel, url, http_method, body_type, link,
                                      response_type, self.__toMap(rel, splitted_url),
                                      collectionsHolder, KNOWN_ACTIONS)

                usedRels.append(rel + '_' + url)

        # create root collection/s instances in entry point
        self.__appendRootCollections(collectionsHolder)

        # store content
        self.__persist(collectionsHolder)

    def __persist(self, collectionsHolder):
        try:
            f = open(BROKERS_FILE, 'w')
            f_api = open(ENTRY_POINT_FILE, 'w')
            coll_candidates = ''
            root_coll_candidates = []

            f.write(Import.getimports())

            keys = collectionsHolder.keys()
            keys.sort()
            for k in keys:
                if collectionsHolder[k].has_key('sub_collections'):
                    collectionsHolder[k]['body'] = \
                        (collectionsHolder[k]['body'].replace(Resource.SUB_COLLECTIONS_FIXME,
                                                              Resource.addSubCollectionInstances('self',  # k.lower(),
                                                                                                 collectionsHolder[k]['sub_collections']))) \
                                                     .replace(Resource.SUB_COLLECTIONS_FIXME, '')
                f.write(collectionsHolder[k]['body'])
                f.flush()

                coll_candidate = EntryPoint.collection(k, collectionsHolder[k])
                if coll_candidate is not None:
                    coll_candidates += coll_candidate
                    root_coll_candidates.append(k)

            f_api.write(EntryPoint.entryPoint(self.__api, root_coll_candidates, coll_candidates))
            f_api.flush()
        finally:
            if f and not f.closed:
                f.close()
            if f_api and not f_api.closed:
                f_api.close()

    def __toMap(self, rel, resources=[]):
        dct = OrderedDict()
        for i in range(len(resources)):
            if (i % 2 is 0):
                coll = resources[i]
                res = resources[i + 1] if ((i + 1 < len(resources))) else None
                dct[coll] = res
        return dct

    def __toSingular(self, typ):
        if typ and typ.endswith('s') and typ not in COLLECTION_TO_ENTITY_EXCEPTIONS:
            return typ[0:len(typ) - 1]
        return typ

    def __appendRootCollections(self, collectionsHolder={}):
        collections = ''
        for v in collectionsHolder.values():
            if (v.has_key('root_collection') and v['root_collection'] == True):
                collections += v['name'] + ' = ' + self.__toResourceType(v['name']) + '()'

    def __appendResource(self, rel, url, http_method, body_type, link, response_type,
                         resources={}, collectionsHolder={}, known_actions=[]):
        '''appends to class_map (collectionsHolder) resource/method/action'''
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
                    self.__extendCollection(coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
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
            elif(ln is 3):
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
                elif(i is 3):
                    sub_root_coll = self.__toSingular(root_coll) + self.__toResourceType(sub_coll)
                    sub_res_coll = self.__toResourceType(resources.keys()[2])
                    if (v is None and self.__isCollection(link)):
                        self.__extendSubCollection(sub_root_coll, sub_res_coll, url, rel, http_method,
                                                   body_type, link, response_type, collectionsHolder)
                    elif(self.__isAction(link)):
                        self.__createAction(sub_root_coll, None, sub_coll, url, rel, http_method,
                                            body_type, link, response_type, collectionsHolder)
                    else:
                        self.__extendSubResource(sub_root_coll, sub_res_coll, url, rel, http_method,
                                                 body_type, link, response_type, collectionsHolder)
            elif(ln > 3):
                print 'WARNING: unsupported deep(' + str(len(resources)) + "): url: " + url

    def __extendCollection(self, collection, url, rel, http_method, body_type, link, response_type, collectionsHolder):
        if (not collectionsHolder.has_key(collection)):
            collection_body = Collection.collection(collection)
            collectionsHolder[collection] = {'body':collection_body, 'root_collection':True, 'name':collection}

        # ['get', 'add', 'delete', 'update']
        if (rel == 'get'):
            get_method = Collection.get(url, response_type, link, KNOWN_WRAPPER_TYPES)
            collectionsHolder[collection]['body'] += get_method

            list_method = Collection.list(url, response_type, link, KNOWN_WRAPPER_TYPES)
            collectionsHolder[collection]['body'] += list_method

        elif (rel == 'add'):
            add_method = Collection.add(url, body_type, response_type, link, KNOWN_WRAPPER_TYPES)
            collectionsHolder[collection]['body'] += add_method

    def __extendResource(self, collection, url, rel, http_method, body_type, link, response_type, collectionsHolder):
        resource = response_type if response_type is not None \
                                 else collection[:len(collection) - 1]

        if (not collectionsHolder.has_key(resource)):
            resource_body = Resource.resource(self.__toResourceType(resource), [], KNOWN_WRAPPER_TYPES)
            collectionsHolder[resource] = {'body':resource_body}

        # ['get', 'add', 'delete', 'update']
        if (rel == 'delete'):
            del_method = Resource.delete(url, body_type, link, resource)
            collectionsHolder[resource]['body'] += del_method
        elif (rel == 'update'):
            upd_method = Resource.update(url, self.__toResourceType(resource), link, KNOWN_WRAPPER_TYPES)
            collectionsHolder[resource]['body'] += upd_method

    def __createAction(self, root_coll, sub_coll, action_name, url, rel, http_method, body_type, link, response_type, collectionsHolder, collection_action=False):
        resource = root_coll[:len(root_coll) - 1]
        sub_resource = sub_coll[:len(sub_coll) - 1] if sub_coll is not None and not collection_action else None if sub_coll is None else sub_coll
        action_name = self.__adaptActionName(action_name, sub_resource if sub_resource is not None
                                                                       else resource)
        if (sub_coll is None or sub_coll == ''):
            if (not collectionsHolder.has_key(resource)):
                self.__extendCollection(root_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
            action_body = Resource.action(url, body_type, link, action_name, resource, http_method, {})
            collectionsHolder[resource]['body'] += action_body
        else:
            nested_collection = root_coll[:len(root_coll) - 1] + sub_coll
            nested_resource = nested_collection[:len(nested_collection) - 1] if not collection_action else nested_collection

            if (not collectionsHolder.has_key(nested_collection)):
                self.__extendSubCollection(root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)

            if (not collectionsHolder.has_key(nested_resource)):
                self.__extendSubResource(root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)

            action_body = SubResource.action(url, link, action_name, resource, body_type, sub_resource, http_method, {}, collection_action)
            collectionsHolder[nested_resource]['body'] += action_body

    # rename /preserved/ names
    def __adaptActionName(self, action_name, resource):
        if action_name in PRESERVED_NAMES:
            return action_name + '_' + resource.lower()
        return action_name

    @staticmethod
    def __isCollection(link):
        return (link.href.endswith('s') or link.href.split('/')[-1].capitalize() in COLLECTION_TO_ENTITY_EXCEPTIONS) \
                and not CodeGen.__isAction(link)

    @staticmethod
    def __isAction(link):
        return link.href.endswith('/' + link.rel) and link.request.http_method == 'POST'

    def __toResourceType(self, candidate):
        return candidate[0:1].upper() + candidate[1:len(candidate)]

    @staticmethod
    def __getParentCache(collectionsHolder, parent, KNOWN_WRAPPER_TYPES={}):
        if collectionsHolder.has_key(parent):
            return collectionsHolder[parent]

        actual_parent = TypeUtil.getValueByKeyOrNone(parent.lower(), KNOWN_WRAPPER_TYPES)
        if actual_parent is not None and collectionsHolder.has_key(actual_parent):
            return collectionsHolder[actual_parent]

        return None


    def __toPlural(self, cand):
        return cand + 's' if not cand.endswith('s') else cand


    def __extendSubCollection(self, root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder):

        root_res = self.__toSingular(root_coll)
        sub_res = response_type if response_type is not None \
                                else sub_coll[:len(sub_coll) - 1]
        sub_coll_type = root_res + sub_coll
        sub_res_type = self.__toSingular(sub_coll_type)

        if (not collectionsHolder.has_key(sub_coll_type)):
            sub_coll_body = SubCollection.collection(sub_coll_type, root_res)

            collectionsHolder[sub_coll_type] = {'body':sub_coll_body}

        parentCache = self.__getParentCache(collectionsHolder, root_res, KNOWN_WRAPPER_TYPES)
        if parentCache is None:
            print 'failed locating cache for: %s, at url: %s \n' % (root_res, url)
        else:
            if not parentCache.has_key('sub_collections'): parentCache['sub_collections'] = {}
            parentCache['sub_collections'][sub_coll.lower()] = (sub_coll_type)

        # ['get', 'add']
        if (rel == 'get'):
            get_method_body = SubCollection.get(url, link, root_res, self.__toResourceType(sub_res_type), sub_res, KNOWN_WRAPPER_TYPES, NAMING_ENTITY_EXCEPTIONS)
            collectionsHolder[sub_coll_type]['body'] += get_method_body

            list_method = SubCollection.list(url, link, root_res, self.__toResourceType(sub_res_type), sub_res, KNOWN_WRAPPER_TYPES, NAMING_ENTITY_EXCEPTIONS)
            collectionsHolder[sub_coll_type]['body'] += list_method

        elif (rel == 'add'):
            add_method = SubCollection.add(url, link, body_type, root_res, self.__toResourceType(sub_res_type), KNOWN_WRAPPER_TYPES)
            collectionsHolder[sub_coll_type]['body'] += add_method

    def __extendSubResource(self, root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder, extend_only=False):
        root_res = self.__toSingular(root_coll)
        sub_res = self.__toSingular(sub_coll)
        sub_res_type = root_res + sub_res

        if (not collectionsHolder.has_key(sub_res_type)):
            sub_resource_body = SubResource.resource(sub_res_type, self.__toResourceType(sub_res), root_res, KNOWN_WRAPPER_TYPES)
            collectionsHolder[sub_res_type] = {'body':sub_resource_body}

        if not extend_only:
            # ['delete', 'update']
            if (rel == 'delete'):
                del_method = SubResource.delete(url, link, root_res, sub_res, body_type)
                collectionsHolder[sub_res_type]['body'] += del_method
            elif (rel == 'update'):
                update_method = SubResource.update(url, link, root_res, self.__toResourceType(sub_res), sub_res_type, KNOWN_WRAPPER_TYPES)
                collectionsHolder[sub_res_type]['body'] += update_method


    def __checkIfTooDeep(self, splitted_url, rel, url, http_method):
        '''check for exceptions from known pattern'''
        dlen = len(splitted_url)
        if (dlen > 4 and (dlen % 2 is 0)):  # and rel is not in ['get']):
            print 'WARNING: found deep dependency (' + str(dlen) + '): ' + 'rel: ' + rel + ', url: ' + url + ', method: ' + http_method + ', for url: ' + url


    def __doRequest(self, method, url, body=None, headers={}):
        self.__conn.doRequest(method=method, url=url, body=body, headers=headers)
        response = self.__conn.getResponse()
        if response.status >= 400:
            raise RequestError, response
        return response.read()

    def generateSchemaBindings(self):
        context.manager[self.context].add('filter', False)
        schema = self.__doRequest(method='GET', url='/api?schema')
        with open(SCHEMA_FILE, 'w') as f:
            f.write('%s' % schema)
        paramsHandle(SCHEMA_FILE, XML_PARAMS_FILE, XML_PARAMS_TMP_FILE)

if __name__ == "__main__":

    # CodeGen instance
    codegen = CodeGen()

    # generate python2xml bindings
    codegen.generateSchemaBindings()

    # import modules required for generate()
    from ovirtsdk.xml import params
    from ovirtsdk.utils.parsehelper import ParseHelper
    from codegen.collection.collection import Collection
    from codegen.subcollection.subresource import SubResource
    from codegen.subcollection.subcollection import SubCollection

    # cache known python2xml bindings types
    KNOWN_WRAPPER_TYPES = ReflectionHelper.getClassNames(params)

    # generate resources brokers
    codegen.generate()
