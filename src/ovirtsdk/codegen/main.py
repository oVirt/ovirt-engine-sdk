'''
Created on Oct 23, 2011

@author: mpastern@redhat.com
'''

from collections import OrderedDict
from ovirtsdk.api import API

from ovirtsdk.infrastructure import contextmanager

from ovirtsdk.xml import params

from ovirtsdk.utils.parsehelper import ParseHelper
from ovirtsdk.codegen.imp.imprt import Import
from ovirtsdk.codegen.collection.resource import Resource
from ovirtsdk.codegen.entrypoint.entrypoint import EntryPoint
from ovirtsdk.codegen.collection.collection import Collection
from ovirtsdk.codegen.subcollection.subresource import SubResource
from ovirtsdk.codegen.utils.typeutil import TypeUtil
from ovirtsdk.codegen.subcollection.subcollection import SubCollection
from ovirtsdk.utils.reflectionhelper import ReflectionHelper

SERVER = 'http://server:port'
USER = 'user@domain'
PASSWORD = 'password'

BROKERS_FILE = '../infrastructure/brokers.py'
ENTRY_POINT_FILE = '../api.py'

KNOWN_ACTIONS = ['get', 'add', 'delete', 'update']

#TODO:should be fixed on server side
COLLECTION_TO_ENTITY_EXCEPTIONS = ['Capabilities', 'Storage']

#names that should not be used as method/s names
PRESERVED_NAMES = ['import', 'from']

#xml wrapper (actual server) types 
KNOWN_WRAPPER_TYPES = {}

DEBUG = False

class CodeGen():
    def gen(self):
        API(url=SERVER, username=USER, password=PASSWORD)

        collectionsHolder = {}
        usedRels = []
        for link in contextmanager.get('proxy').request('GET', '/api?rsdl').links.link:

            response_type = None
            body_type = None

            #link metadata
            rel = link.rel
            url = link.href

            if (not (rel + '_' + url) in usedRels):
                #request
                http_method = link.request.http_method
                if (link.request and link.request.body and hasattr(link.request.body, 'type_')):
                    body_type = link.request.body.type_

                #response
                response = link.response
                if (link.response and hasattr(link.response, 'type_')):
                    response_type = self.__toSingular(response.type_)

                #get relations
                splitted_url = url.strip()[1:].split('/')
                entry_point = splitted_url.pop(0)

                #check for exceptions from known pattern
                #self.__checkIfTooDeep(splitted_url, rel, url, http_method)

                #append resource/method/rel
                self.__appendResource(rel,
                                      url,
                                      http_method,
                                      body_type,
                                      link,
                                      response_type,
                                      self.__toMap(rel, splitted_url),
                                      collectionsHolder,
                                      KNOWN_ACTIONS)

                usedRels.append(rel + '_' + url)

        #create root collection/s instances in entry point
        self.__appendRootCollections(collectionsHolder)

        #store content
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
                    collectionsHolder[k]['body'] = collectionsHolder[k]['body'].replace(Resource.SUB_COLLECTIONS_FIXME,
                                                                                        Resource.addSubCollectionInstances(k.lower(),
                                                                                                                           collectionsHolder[k]['sub_collections']))
                f.write(collectionsHolder[k]['body'])
                f.flush()

                coll_candidate = EntryPoint.collection(k, collectionsHolder[k])
                if coll_candidate is not None:
                    coll_candidates += coll_candidate
                    root_coll_candidates.append(k)

            f_api.write(EntryPoint.entryPoint(root_coll_candidates, coll_candidates))
            f_api.flush()
        finally:
            f.close()
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
        for k, v in collectionsHolder.items():
            if (v.has_key('root_collection') and v['root_collection'] == True):
                collections += v['name'] + ' = ' + self.__toResourceType(v['name']) + '()'

    def __appendResource(self, rel, url, http_method, body_type, link, response_type, resources={}, collectionsHolder={}, known_actions=[]):
        '''appends to class_map (collectionsHolder) resource/method/action'''
        i = 0
        ln = len(resources)        # NOTE currently supported deep is ^3+NONE (^3||^N is TODO:)
        #=========================================================

        #resources {'vms':xxx,'disks':yyy,'snapshots':zzz}
        #vms/xxx/disks/yyy/snapshots/zzz

        #1.coll         vms/None:1
        #2.res          vms/xxx :1
        #3.sub-coll     vms/xxx/disks/None :2
        #4.sub-res      vms/xxx/disks/yyy  :2
        #5.sub-sub-col  vms/xxx/disks/yyy/snapshots/None :3
        #6.sub-sub-res  vms/xxx/disks/yyy/snapshots/zzz  :3

        #N.sub-sub-res  vms/xxx/disks/yyy/snapshots/zzz/^N  :3

        #num of permutations for N=K is K
        #num of pairs        for N=K is k/2 (to differ between the res & coll check the last pair val)

        root_coll = None
        for k, v in resources.items():
            i += 1
            if(ln is 1):   #vms/xxx
                #coll = k
                coll = ParseHelper.getXmlWrapperType(k)
                if (v is None):
                    self.__extendCollection(coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
                else:
                    self.__extendResource(coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
            elif(ln is 2): #vms/xxx/disks/yyy
                if (i is 1): #vms/xxx
                    #root_coll = k
                    root_coll = ParseHelper.getXmlWrapperType(k)
                if (i is 2): #disks/yyy
                    #sub_coll = k
                    sub_coll = ParseHelper.getXmlWrapperType(k)
                    if (v is None and self.__isCollection(k)):
                        self.__extendSubCollection(root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
#                    elif(v is None):
                    elif(v is None and http_method == 'POST'):
#FIXME: remove http_methond cond                        
                        self.__createAction(root_coll, None, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
                    else:
                        self.__extnedSubResource(root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
            elif(ln is 3): #/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/activate
                if (i is 1): #vms/xxx
                    #root_coll = k
                    root_coll = ParseHelper.getXmlWrapperType(k)
                if (i is 2): #disks/yyy             
                    #sub_coll = k
                    sub_coll = ParseHelper.getXmlWrapperType(k)
                    if (v is None and self.__isCollection(k)):
                        self.__extendSubCollection(root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
                    elif(v is None):
                        self.__createAction(root_coll, None, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
                    else:
                        if(resources.values()[i] is None):
                            self.__extnedSubResource(root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder)
                if (i is 3 and v is None and not self.__isCollection(k)):
                    self.__createAction(root_coll, sub_coll, k, url, rel, http_method, body_type, link, response_type, collectionsHolder)
                elif(i is 3 and resources.values()[2] is not None):
                    self.__extnedSubResource(root_coll + self.__toResourceType(resources.keys()[1]),
                                             self.__toResourceType(resources.keys()[2]), url, rel, http_method, body_type, link, response_type, collectionsHolder)
            elif(ln > 3):  #vms/xxx/disks/yyy/snapshots/zzz or deeper
                if(DEBUG): print 'WARNING: unsupported deep(' + str(len(resources)) + "): url: " + url

    def __extendCollection(self, collection, url, rel, http_method, body_type, link, response_type, collectionsHolder):
        if (not collectionsHolder.has_key(collection)):
            collection_body = Collection.collection(collection)
            collectionsHolder[collection] = {'body':collection_body,
                                             'root_collection':True,
                                             'name':collection}

            if(DEBUG): print '[root] creating collection: ' + collection + ', for url: ' + url
            if(DEBUG): print '/n' + collection_body

        #['get', 'add', 'delete', 'update']
        if (rel == 'get'):
            get_method = Collection.get(url, response_type, link, KNOWN_WRAPPER_TYPES)
            collectionsHolder[collection]['body'] += get_method
            if(DEBUG): print 'adding to collection: ' + collection + ', url: ' + url + ', get() method:\n' + get_method

            list_method = Collection.list(url, response_type, link, KNOWN_WRAPPER_TYPES)
            collectionsHolder[collection]['body'] += list_method
            if(DEBUG): print 'adding to collection: ' + collection + ', url: ' + url + ', list() method:\n' + list_method

        elif (rel == 'add'):
            add_method = Collection.add(url, body_type, response_type, link, KNOWN_WRAPPER_TYPES)
            collectionsHolder[collection]['body'] += add_method
            if(DEBUG): print 'adding to collection: ' + collection + ', url: ' + url + ', add() method:\n' + add_method

    def __extendResource(self, collection, url, rel, http_method, body_type, link, response_type, collectionsHolder):
        resource = response_type if response_type is not None \
                                 else collection[:len(collection) - 1]

        if (not collectionsHolder.has_key(resource)):
            resource_body = Resource.resource(self.__toResourceType(resource), [], KNOWN_WRAPPER_TYPES)
            collectionsHolder[resource] = {'body':resource_body}
            if(DEBUG): print '[res] creating resource: ' + resource + ', at collection: ' + collection + ', for url: ' + url
            if(DEBUG): print 'adding to resource: ' + resource + ' body:\n\n' + resource_body

        #['get', 'add', 'delete', 'update']
        if (rel == 'delete'):
            del_method = Resource.delete(url, body_type, link, resource)
            collectionsHolder[resource]['body'] += del_method
            if(DEBUG): print 'adding to resource: ' + resource + ' delete method:\n\n' + del_method
        elif (rel == 'update'):
            upd_method = Resource.update(url, self.__toResourceType(resource), link, KNOWN_WRAPPER_TYPES)
            collectionsHolder[resource]['body'] += upd_method
            if(DEBUG): print 'adding to resource: ' + self.__toResourceType(resource) + ' update method:\n\n' + upd_method

    def __createAction(self, root_coll, sub_coll, action_name, url, rel, http_method, body_type, link, response_type, collectionsHolder):
        resource = root_coll[:len(root_coll) - 1]
        sub_resource = sub_coll[:len(sub_coll) - 1] if sub_coll is not None else None
        action_name = self.__adaptActionName(action_name, sub_resource if sub_resource is not None
                                                                       else resource)
        if (sub_coll is None or sub_coll == ''):
            if (not collectionsHolder.has_key(resource)):
                self.__extendCollection(root_coll, url, rel, http_method, body_type, response_type, collectionsHolder)
#TODO: add real action params
            action_body = Resource.action(url, body_type, link, action_name, resource, http_method, {})
            collectionsHolder[resource]['body'] += action_body
            if(DEBUG): print '[act] creating action: ' + action_name + '() on resource: ' + resource + ', for url: ' + url
            if(DEBUG): print '\n' + action_body
        else:
            #nested_collection = self.__toResourceType(root_coll[:len(root_coll)-1]) + self.__toResourceType(sub_coll)
            nested_collection = root_coll[:len(root_coll) - 1] + sub_coll
            nested_resource = nested_collection[:len(nested_collection) - 1]

            sub_resource = sub_coll[:len(sub_coll) - 1]

            if (not collectionsHolder.has_key(nested_collection)):
                self.__extendSubCollection(root_coll, sub_coll, url, rel, http_method, body_type, response_type, collectionsHolder)

            if (not collectionsHolder.has_key(nested_resource)):
                self.__extnedSubResource(root_coll, sub_coll, url, rel, http_method, body_type, response_type, collectionsHolder)

            action_body = SubResource.action(url, link, action_name, resource, body_type, sub_resource, http_method, {})
            collectionsHolder[nested_resource]['body'] += action_body
#TODO: add real action params
            if(DEBUG): print '[act] creating action: ' + action_name + '() on sub-resource: ' + nested_resource + ', for url: ' + url
            if(DEBUG): print '\n' + action_body

    #rename /preserved/ names
    def __adaptActionName(self, action_name, resource):
        if action_name in PRESERVED_NAMES:
            return action_name + '_' + resource.lower()
        return action_name

    @staticmethod
    def __isCollection(candidate):
#TODO: find better way to distinguish between the collection & resource
        return candidate.endswith('s')

    def __toResourceType(self, candidate):
        return candidate[0:1].upper() + candidate[1:len(candidate)]

    @staticmethod
    def __getParentCache(collectionsHolder, parent, KNOWN_WRAPPER_TYPES={}):
        actual_parent = TypeUtil.getValueByKeyOrNone(parent.lower(), KNOWN_WRAPPER_TYPES)
        if actual_parent is not None and collectionsHolder.has_key(actual_parent):
            return collectionsHolder[actual_parent]
        return None

    def __extendSubCollection(self, root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder):
        #str: /api/clusters/{cluster:id}/permissions

        root_res = root_coll[:len(root_coll) - 1]
        sub_res = response_type if response_type is not None \
                                else sub_coll[:len(sub_coll) - 1]
        #sub_coll_type = self.__toResourceType(root_res) + self.__toResourceType(sub_coll)
        sub_coll_type = root_res + sub_coll
        sub_res_type = sub_coll_type[:len(sub_coll_type) - 1]

        if (not collectionsHolder.has_key(sub_coll_type)):
            sub_coll_body = SubCollection.collection(sub_coll_type, root_res)

            parentCache = self.__getParentCache(collectionsHolder, root_res, KNOWN_WRAPPER_TYPES)
            if parentCache is None:
                if(DEBUG): print 'failed locating cache for: %s, at url: %s \n' % (root_res, url)
            else:
                if(DEBUG): print 'add sub-coll %s, for: %s, at url: %s \n' % (sub_coll_type, root_res, url)
                if not parentCache.has_key('sub_collections'): parentCache['sub_collections'] = {}
                parentCache['sub_collections'][sub_coll.lower()] = (sub_coll_type)

            collectionsHolder[sub_coll_type] = {'body':sub_coll_body}
            if(DEBUG): print '[sub] creating sub-collection: ' + sub_coll_type + ', at resource: ' + root_res + ', for url: ' + url
            if(DEBUG): print '\n' + sub_coll_body

        #['get', 'add', 'delete', 'update']
        if (rel == 'get'):
            get_method_body = SubCollection.get(url, link, root_res, self.__toResourceType(sub_res_type), sub_res, KNOWN_WRAPPER_TYPES)
            collectionsHolder[sub_coll_type]['body'] += get_method_body
            if(DEBUG): print 'adding to sub-collection: ' + sub_coll_type + ', url: ' + url + ', get() method:\n' + get_method_body

            list_method = SubCollection.list(url, link, root_res, self.__toResourceType(sub_res_type), sub_res, KNOWN_WRAPPER_TYPES)
            collectionsHolder[sub_coll_type]['body'] += list_method
            if(DEBUG): print 'adding to sub-collection: ' + sub_coll_type + ', url: ' + url + ', list() method:\n' + list_method

        elif (rel == 'add'):
            add_method = SubCollection.add(url, link, body_type, root_res, self.__toResourceType(sub_res_type), KNOWN_WRAPPER_TYPES)
            collectionsHolder[sub_coll_type]['body'] += add_method
            if(DEBUG): print 'adding to sub-collection: ' + sub_coll_type + ', url: ' + url + ', add() method:\n' + add_method

    def __extnedSubResource(self, root_coll, sub_coll, url, rel, http_method, body_type, link, response_type, collectionsHolder):
        root_res = root_coll[:len(root_coll) - 1]
        sub_res = sub_coll[:len(sub_coll) - 1] if self.__isCollection(sub_coll) else sub_coll
        sub_res_type = root_res + sub_res

        if (not collectionsHolder.has_key(sub_res_type)):
            sub_resource_body = SubResource.resource(sub_res_type, self.__toResourceType(sub_res), root_res, KNOWN_WRAPPER_TYPES)
            collectionsHolder[sub_res_type] = {'body':sub_resource_body}
            if(DEBUG): print '[sub-res] creating sub-resource: ' + sub_res_type + ', with parent: ' + root_res + ', for url: ' + url
            if(DEBUG): print sub_resource_body

        #['get', 'add', 'delete', 'update']
        if (rel == 'delete'):
            del_method = SubResource.delete(url, link, root_res, sub_res, body_type)
            collectionsHolder[sub_res_type]['body'] += del_method
            if(DEBUG): print 'adding to sub-resource: ' + sub_res_type + ' delete() method:\n\n' + del_method
        elif (rel == 'update'):
            update_method = SubResource.update(url, link, root_res, self.__toResourceType(sub_res), sub_res_type, KNOWN_WRAPPER_TYPES)
            collectionsHolder[sub_res_type]['body'] += update_method
            if(DEBUG): print 'adding to sub-resource: ' + sub_res_type + ' update() method:\n\n' + update_method


    def __checkIfTooDeep(self, splitted_url, rel, url, http_method):
        '''check for exceptions from known pattern'''
        dlen = len(splitted_url)
        if (dlen > 4 and (dlen % 2 is 0)):#and rel is not in ['get']):
            if(DEBUG): print 'WARNING: found deep dependency (' + str(dlen) + '): ' + 'rel: ' + rel + ', url: ' + url + ', method: ' + http_method + ', for url: ' + url

if __name__ == "__main__":
    KNOWN_WRAPPER_TYPES = ReflectionHelper.getClassNames(params)
    CodeGen().gen()
