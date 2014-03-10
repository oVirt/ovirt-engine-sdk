//
// Copyright (c) 2014 Red Hat, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

package org.ovirt.engine.sdk.generator.rsdl;

import static org.ovirt.engine.sdk.generator.utils.CollectionsUtils.mapOf;
import static org.ovirt.engine.sdk.generator.utils.CollectionsUtils.setOf;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;

import org.ovirt.engine.sdk.generator.common.AbstractCodegen;
import org.ovirt.engine.sdk.generator.utils.FileUtils;
import org.ovirt.engine.sdk.generator.utils.StringUtils;
import org.ovirt.engine.sdk.generator.utils.TypeUtils;
import org.ovirt.engine.sdk.generator.xsd.XsdData;
import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.entities.HttpMethod;
import org.ovirt.engine.sdk.entities.RSDL;

/**
 * Provides RSDL related generator capabilities.
 */
public class RsdlCodegen extends AbstractCodegen {
    private static final String BROKERS_FILE = "../src/ovirtsdk/infrastructure/brokers.py";
    private static final String ENTRY_POINT_FILE = "../src/ovirtsdk/api.py";

    private static final Set<String> KNOWN_ACTIONS = setOf(
        "get",
        "add",
        "delete",
        "update"
    );

    // TODO:should be fixed on server side
    private static final Map<String, String> COLLECTION_TO_ENTITY_EXCEPTIONS = mapOf(
        "Capabilities", "Capabilities",
        "SchedulingPolicies", "SchedulingPolicy",
        "Storage", "Storage",
        "VersionCaps", "VersionCaps"
    );

    // TODO:should be fixed on server side (naming inconsistency)
    private static final Map<String, String> NAMING_ENTITY_EXCEPTIONS = mapOf(
        "host_storage", "storage"
    );

    // cache known python2xml bindings types
    private static Map<String, String> KNOWN_WRAPPER_TYPES = new LinkedHashMap<>();

    // names that should not be used as method/s names
    private static final Set<String> PRESERVED_NAMES = setOf(
        "import",
        "from"
    );

    /**
     * The location of the RSDL file.
     */
    private String rsdlPath;

    private Map<String, CodeHolder> code = new LinkedHashMap<>();

    public RsdlCodegen(String rsdlPath) {
        super("");
        this.rsdlPath = rsdlPath;

        Map<String, String> map = XsdData.getInstance().getMap();
        List<String> names = new ArrayList<>(map.keySet());
        Collections.sort(names);
        for (String name : names) {
            String type = map.get(name);
            KNOWN_WRAPPER_TYPES.put(type.toLowerCase(), type);
        }
    }

    @Override
    protected void doGenerate(String distPath) throws IOException {
        // Load the RSDL document:
        RSDL rsdl = loadRsdl();

        Set<String> usedRels = new HashSet<>();

        // Get all the links from the RSDL document and make them relative:
        List<DetailedLink> links = rsdl.getLinks().getLinks();
        for (DetailedLink link : links) {
            String href = link.getHref();
            href = href.replaceFirst("^/ovirt-engine/api", "");
            link.setHref(href);
        }

        for (DetailedLink link : links) {
            String responseType = null;
            String bodyType = null;

            // Link metadata:
            String rel = link.getRel();
            String url = link.getHref();

            if (!usedRels.contains(rel + "_" + url)) {

                // Request:
                HttpMethod httpMethod = link.getRequest().getHttpMethod();
                if (link.isSetRequest() && link.getRequest().isSetBody() && link.getRequest().getBody().isSetType()) {
                    bodyType = link.getRequest().getBody().getType();
                }

                // Response:
                if (link.isSetResponse() && link.getResponse().isSetType()) {
                    responseType = StringUtils.toSingular(
                        link.getResponse().getType(),
                        COLLECTION_TO_ENTITY_EXCEPTIONS
                    );
                }

                // Get relations:
                String[] splittedUrl = url.trim().substring(1).split("/");

                // Append resource/method/rel
                appendResource(
                    rel,
                    url,
                    httpMethod,
                    bodyType,
                    link,
                    responseType,
                    TypeUtils.toOrderedMap(splittedUrl),
                    RsdlCodegen.KNOWN_ACTIONS
                );

                usedRels.add(rel + "_" + url);
            }
        }

        // store content
        persist();
    }

    /**
     * Persist generated content.
     */
    private void persist() {
        String brokersFile = "";
        String apiFile = "";

        String collCandidates = "";
        List<String> rootCollCandidates = new ArrayList<>();

        brokersFile += Import.getImports();

        List<String> keys = new ArrayList<>(code.keySet());
        Collections.sort(keys);

        for (String k : keys) {
            CodeHolder holder = code.get(k);
            if (holder.hasSubcollections()) {
                String body = holder.getBody();
                body = body.replace(
                    Resource.SUB_COLLECTIONS_FIXME,
                    Resource.addSubCollectionInstances(
                        "self",
                        holder.getSubCollections()
                    ).replace(Resource.SUB_COLLECTIONS_FIXME, "")
                );
                holder.setBody(body);
            }

            brokersFile += holder.getBody();

            String collCandidate = EntryPoint.collection(k, holder);
            if (collCandidate != null) {
                collCandidates += collCandidate;
                rootCollCandidates.add(k);
            }
        }

        apiFile += EntryPoint.entryPoint(rootCollCandidates, collCandidates);

        FileUtils.saveFile(BROKERS_FILE, brokersFile);
        FileUtils.saveFile(ENTRY_POINT_FILE, apiFile);
    }

    private void appendResource(
        String rel,
        String url,
        HttpMethod httpMethod,
        String bodyType,
        DetailedLink link,
        String responseType,
        Map<String, String> resources,
        Set<String> knownActions)
    {
        int i = 0;
        int ln = resources.size();

        // =========================================================

        // resources {'vms':xxx,'disks':yyy,'snapshots':zzz}
        // vms/xxx/disks/yyy/snapshots/zzz

        // 1.coll         vms/None:1
        // 2.res          vms/xxx :1
        // 3.sub-coll     vms/xxx/disks/None :2
        // 4.sub-res      vms/xxx/disks/yyy  :2
        // 5.sub-sub-col  vms/xxx/disks/yyy/snapshots/None :3
        // 6.sub-sub-res  vms/xxx/disks/yyy/snapshots/zzz  :3

        // N.sub-sub-res  vms/xxx/disks/yyy/snapshots/zzz/^N  :3

        // num of permutations for N=K is K
        // num of pairs        for N=K is k/2 (to differ between the res & coll check the last pair val)

        String rootColl = null;
        String subColl = null;
        for (Map.Entry<String, String> entry : resources.entrySet()) {
            String k = entry.getKey();
            String v = entry.getValue();

            i+= 1;
            if (ln == 1) { // vms/xxx
                // coll = k
                String coll = XsdData.getInstance().getXmlWrapperType(k);
                if (v == null) {
                    extendCollection(
                        coll,
                        url,
                        rel,
                        httpMethod,
                        bodyType,
                        link,
                        responseType
                    );
                }
                else {
                    extendResource(
                        coll,
                        url,
                        rel,
                        httpMethod,
                        bodyType,
                        link,
                        responseType
                    );

                }
            }
            else if (ln == 2) { // vms/xxx/disks/yyy
                if (i == 1) { // vms/xxx
                    // rootColl = k
                    rootColl = XsdData.getInstance().getXmlWrapperType(k);
                }
                if (i == 2) { // disk/yyyy
                    // subColl = k
                    subColl = XsdData.getInstance().getXmlWrapperType(k);
                    if (v == null && isCollection(link)) {
                        extendSubCollection(
                            rootColl,
                            subColl,
                            url,
                            rel,
                            httpMethod,
                            bodyType,
                            link,
                            responseType
                        );
                    }
                    else if ((v == null || v.indexOf(":id") == -1) && httpMethod == HttpMethod.POST) {
                        if (v == null) {
                            createAction(
                                rootColl,
                                null,
                                subColl,
                                url,
                                rel,
                                httpMethod,
                                bodyType,
                                link,
                                responseType,
                                false,
                                false
                            );
                        }
                        else {
                            createAction(
                                rootColl,
                                subColl,
                                v,
                                url,
                                rel,
                                httpMethod,
                                bodyType,
                                link,
                                responseType,
                                true,
                                false
                            );
                        }
                    }
                    else {
                        extendSubResource(
                            rootColl,
                            subColl,
                            url,
                            rel,
                            httpMethod,
                            bodyType,
                            link,
                            responseType,
                            false
                        );
                    }
                }
            }
            else if (ln >= 3) {
                if (i == 1) {
                    rootColl = XsdData.getInstance().getXmlWrapperType(k);
                }
                if (i == 2) {
                    subColl = XsdData.getInstance().getXmlWrapperType(k);
                    if (v == null && isCollection(link)) {
                        extendSubCollection(
                            rootColl,
                            subColl,
                            url,
                            rel,
                            httpMethod,
                            bodyType, link,
                            responseType
                        );
                    }
                    else if (v == null) {
                        createAction(
                            rootColl,
                            null,
                            subColl,
                            url,
                            rel,
                            httpMethod,
                            bodyType,
                            link,
                            responseType,
                            false,
                            false
                        );
                    }
                    else {
                        extendSubResource(
                            rootColl,
                            subColl,
                            url,
                            rel,
                            httpMethod,
                            bodyType,
                            link,
                            responseType,
                            /* extend_only */ ln > i
                        );
                    }
                }
                if (i == 3 && v == null && !isCollection(link)) {
                    createAction(
                        rootColl,
                        subColl,
                        k,
                        url,
                        rel,
                        httpMethod,
                        bodyType,
                        link,
                        responseType,
                        false,
                        false
                    );
                }
                else if (i >= 3) {
                    String subRootColl = StringUtils.toSingular(rootColl, COLLECTION_TO_ENTITY_EXCEPTIONS) +
                        toResourceType(subColl);
                    String subResColl = toResourceType(resources.keySet().toArray(new String[0])[i - 1]);
                    if (v == null && isCollection(link)) {
                        extendSubCollection(
                            subRootColl,
                            subResColl,
                            url,
                            rel,
                            httpMethod,
                            bodyType,
                            link,
                            responseType
                        );
                    }
                    else if (isAction(link) && i == ln) {
                        createAction(
                            subRootColl,
                            subResColl,
                            rel,
                            url,
                            rel,
                            httpMethod,
                            bodyType,
                            link,
                            responseType,
                            false,
                            true
                        );
                    }
                    else {
                        extendSubResource(
                            subRootColl,
                            subResColl,
                            url,
                            rel,
                            httpMethod,
                            bodyType,
                            link,
                            responseType,
                            /* extend_only */ ln > i
                        );
                    }

                    rootColl = StringUtils.toSingular(subRootColl);
                    subColl = subResColl;
                }
            }
        }
    }

    private void extendCollection(
        String collection,
        String url,
        String rel,
        HttpMethod httpMethod,
        String bodyType,
        DetailedLink link,
        String responseType
    )
    {
        CodeHolder holder = code.get(collection);
        if (holder == null) {
            String body = Collection.collection(collection);
            holder = new CodeHolder();
            holder.setRoot(true);
            holder.setName(collection);
            holder.setBody(body);
            code.put(collection, holder);
        }

        // ['get', 'add', 'delete', 'update']
        if (rel.equals("get")) {
            String getMethod = Collection.get(url, responseType, link, KNOWN_WRAPPER_TYPES);
            holder.appendBody(getMethod);

            String listMethod = Collection.list(url, responseType, link, KNOWN_WRAPPER_TYPES);
            holder.appendBody(listMethod);
        }

        else if (rel.equals("add")) {
            String addMethod = Collection.add(url, bodyType, responseType, link, KNOWN_WRAPPER_TYPES);
            holder.appendBody(addMethod);
        }
    }

    private void extendResource(
        String collection,
        String url,
        String rel,
        HttpMethod httpMethod,
        String bodyType,
        DetailedLink link,
        String responseType
    )
    {
        String resource = responseType != null? responseType: StringUtils.toSingular(collection, COLLECTION_TO_ENTITY_EXCEPTIONS);

        CodeHolder holder = code.get(resource);
        if (holder == null) {
            String body = Resource.resource(toResourceType(resource), new String[0], KNOWN_WRAPPER_TYPES);
            holder = new CodeHolder();
            holder.setName(resource);
            holder.setBody(body);
            code.put(resource, holder);
        }

        // ['get', 'add', 'delete', 'update']
        if (rel.equals("delete")) {
            String delMethod = Resource.delete(url, bodyType, link, resource);
            holder.appendBody(delMethod);
        }
        else if (rel.equals("update")) {
            String updMethod = Resource.update(url, toResourceType(resource), link, KNOWN_WRAPPER_TYPES);
            holder.appendBody(updMethod);
        }
    }

    private void createAction(
        String rootColl,
        String subColl,
        String actionName,
        String url,
        String rel,
        HttpMethod httpMethod,
        String bodyType,
        DetailedLink link,
        String responseType,
        boolean collectionAction,
        boolean forceSubResource
    )
    {
        String resource = StringUtils.toSingular(rootColl, COLLECTION_TO_ENTITY_EXCEPTIONS);
        String subResource = null;
        if (subColl != null) {
            if (!collectionAction) {
                subResource = StringUtils.toSingular(subColl, COLLECTION_TO_ENTITY_EXCEPTIONS);
            }
            else {
                subResource = subColl;
            }
        }
        actionName = adaptActionName(actionName, subResource != null? subResource: resource);

        if ((subColl == null || subColl.isEmpty()) && !forceSubResource) {
            if (!code.containsKey(resource)) {
                extendCollection(rootColl, url, rel, httpMethod, bodyType, link, responseType);
            }
            CodeHolder holder = getCode(resource);
            String actionBody = Resource.action(url, bodyType, link, actionName, resource, httpMethod, new LinkedHashMap());
            holder.appendBody(actionBody);
        }
        else {
            if (!forceSubResource) {
                String nestedCollection = StringUtils.toSingular(rootColl, COLLECTION_TO_ENTITY_EXCEPTIONS) + subColl;
                String nestedResource = !collectionAction? StringUtils.toSingular(nestedCollection, COLLECTION_TO_ENTITY_EXCEPTIONS): nestedCollection;
                if (!code.containsKey(nestedCollection) && !forceSubResource) {
                    extendSubCollection(rootColl, subColl, url, rel, httpMethod, bodyType, link, responseType);
                }
                if (!code.containsKey(nestedResource) && !forceSubResource) {
                    extendSubResource(rootColl, subColl, url, rel, httpMethod, bodyType, link, responseType, false);
                }
                String actionBody = SubResource.action(url, link, actionName, resource, bodyType, subResource, httpMethod, new LinkedHashMap(), collectionAction);
                CodeHolder holder = getCode(nestedResource);
                holder.appendBody(actionBody);
            }
            else {
                String actionBody = SubResource.action(url, link, actionName, resource, bodyType, subResource, httpMethod, new LinkedHashMap(), collectionAction);
                CodeHolder holder = getCode(resource);
                holder.appendBody(actionBody);
            }
        }
    }

    /**
     * Adapts action name in case it has py preserved name.
     *
     * @param actionName action name
     * @param resource resource name to be appended as ACTIONNAME_RESOURCE when action name in py prserved name/s
     */
    private String adaptActionName(String actionName, String resource) {
        if (PRESERVED_NAMES.contains(actionName)) {
            return actionName + "_" + resource.toLowerCase();
        }
        return actionName;
    }

    /**
     * Checks if URI is a collection.
     */
    private boolean isCollection(DetailedLink link) {
        String href = link.getHref();
        String[] chunks = href.split("/");
        String last = StringUtils.capitalize(chunks[chunks.length - 1]);
        return (href.endsWith("s") || COLLECTION_TO_ENTITY_EXCEPTIONS.containsKey(last)) && !isAction(link);
    }

    /**
     * Chjecks if URI is an action.
     */
    private boolean isAction(DetailedLink link) {
        return link.getHref().endsWith("/" + link.getRel()) && link.getRequest().getHttpMethod() == HttpMethod.POST;
    }

    private String toResourceType(String candidate) {
        return candidate.substring(0, 1).toUpperCase() + candidate.substring(1);
    }

    private CodeHolder getParentCache(String parent, Map<String, String> knownWrapperTypes) {
        CodeHolder holder = code.get(parent);
        if (holder != null) {
            return holder;
        }

        String actualParent = knownWrapperTypes.get(parent.toLowerCase());
        if (actualParent != null) {
            return code.get(actualParent);
        }

        return null;
    }

    private void extendSubCollection(
        String rootColl,
        String subColl,
        String url,
        String rel,
        HttpMethod httpMethod,
        String bodyType,
        DetailedLink link,
        String responseType
    )
    {
        String rootRes = StringUtils.toSingular(rootColl, COLLECTION_TO_ENTITY_EXCEPTIONS);
        String subRes = responseType != null? responseType: StringUtils.toSingular(subColl, COLLECTION_TO_ENTITY_EXCEPTIONS);
        String subCollType = rootRes + subColl;
        String subResType = StringUtils.toSingular(subCollType, COLLECTION_TO_ENTITY_EXCEPTIONS);

        // Avoid situations where the name of the resource type is the same than
        // the name of the sub collection. Currently this only happens with the
        // collection /hosts/{host:id}/storage, which is using a singular name
        // instead of a plural name.
        if (subCollType.equals(subResType)) {
            subCollType = subCollType + "s";
        }

        CodeHolder holder = code.get(subCollType);
        if (holder == null) {
            String body = SubCollection.collection(subCollType, rootRes);
            holder = new CodeHolder();
            holder.setName(subCollType);
            holder.setBody(body);
            code.put(subCollType, holder);
        }

        CodeHolder parentCache = getParentCache(rootRes, KNOWN_WRAPPER_TYPES);
        if (parentCache == null) {
            System.out.printf("failed locating cache for: %s, at url: %s \n", rootRes, url);
        }
        else {
            parentCache.addSubCollection(subColl.toLowerCase(), subCollType);
        }

        // ['get', 'add']
        if (rel.equals("get")) {
            String getMethodBody =  SubCollection.get(url, link, rootRes, toResourceType(subResType), subRes, KNOWN_WRAPPER_TYPES, NAMING_ENTITY_EXCEPTIONS);
            holder.appendBody(getMethodBody);

            String listMethod = SubCollection.list(url, link, rootRes, toResourceType(subResType), subRes, KNOWN_WRAPPER_TYPES, NAMING_ENTITY_EXCEPTIONS);
            holder.appendBody(listMethod);
        }
        else if (rel.equals("add")) {
            String addMethod =  SubCollection.add(url, link, bodyType, rootRes, toResourceType(subResType), KNOWN_WRAPPER_TYPES);
            holder.appendBody(addMethod);
        }
    }

    private void extendSubResource(
        String rootColl,
        String subColl,
        String url,
        String rel,
        HttpMethod httpMethod,
        String bodyType,
        DetailedLink link,
        String responseType,
        boolean extendOnly
    )
    {
        String rootRes = StringUtils.toSingular(rootColl, COLLECTION_TO_ENTITY_EXCEPTIONS);
        String subRes = StringUtils.toSingular(subColl, COLLECTION_TO_ENTITY_EXCEPTIONS);
        String subResType = rootRes + subRes;

        CodeHolder holder = code.get(subResType);
        if (holder == null) {
            String body = SubResource.resource(subResType, toResourceType(subRes), rootRes, KNOWN_WRAPPER_TYPES);
            holder = new CodeHolder();
            holder.setName(subResType);
            holder.setBody(body);
            code.put(subResType, holder);
        }

        if (!extendOnly) {
            // ['delete', 'update']
            if (rel.equals("delete")) {
                String delMethod = SubResource.delete(url, link, rootRes, subRes, bodyType);
                holder.appendBody(delMethod);
            }
            else if (rel.equals("update")) {
                String updateMethod = SubResource.update(url, link, rootRes, toResourceType(subRes), subResType, KNOWN_WRAPPER_TYPES);
                holder.appendBody(updateMethod);
            }
        }
    }

    private RSDL loadRsdl() throws IOException {
        try {
            JAXBContext context = JAXBContext.newInstance(RSDL.class);
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Source source = new StreamSource(new File(rsdlPath));
            JAXBElement<RSDL> element = unmarshaller.unmarshal(source, RSDL.class);
            return element.getValue();
        }
        catch (JAXBException exception) {
            throw new IOException(exception);
        }
    }

    private CodeHolder getCode(String key) {
        CodeHolder holder = code.get(key);
        if (holder == null) {
            holder = new CodeHolder();
            holder.setName(key);
            code.put(key, holder);
        }
        return holder;
    }

}
