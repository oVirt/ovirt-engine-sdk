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

import static org.ovirt.engine.sdk.generator.rsdl.LocationRules.isAction;
import static org.ovirt.engine.sdk.generator.rsdl.LocationRules.isCollection;
import static org.ovirt.engine.sdk.generator.rsdl.LocationRules.isEntity;
import static org.ovirt.engine.sdk.generator.rsdl.LocationRules.isSubCollection;
import static org.ovirt.engine.sdk.generator.rsdl.LocationRules.isSubEntity;
import static org.ovirt.engine.sdk.generator.utils.CollectionsUtils.setOf;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.apache.commons.io.FileUtils;
import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.generator.utils.Tree;

/**
 * Provides RSDL related generator capabilities.
 */
public class RsdlCodegen {
    private static final File BROKERS_FILE = new File("../src/ovirtsdk/infrastructure/brokers.py");
    private static final File ENTRY_POINT_FILE = new File("../src/ovirtsdk/api.py");

    private static final String SUB_COLLECTIONS_FIXME = "        #SUB_COLLECTIONS";

    // names that should not be used as method/s names
    private static final Set<String> PRESERVED_NAMES = setOf(
        "import",
        "from"
    );

    /**
     * The keys of this map are the names of the broker types, and the content is the generated code.
     */
    private Map<String, CodeHolder> code = new LinkedHashMap<>();

    public void generate() throws IOException {
        // Get the root of the tree of locations:
        Tree<Location> root = RsdlData.getInstance().getRoot();

        // Generate the code:
        root.getDescendants().forEach(this::generateCode);

        // Store the generated code:
        persist();
    }

    /**
     * Persist generated content.
     */
    private void persist() throws IOException {
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
                    SUB_COLLECTIONS_FIXME,
                    Resource.addSubCollectionInstances(
                        "self",
                        holder.getSubCollections()
                    ).replace(SUB_COLLECTIONS_FIXME, "")
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

        FileUtils.writeStringToFile(BROKERS_FILE, brokersFile);
        FileUtils.writeStringToFile(ENTRY_POINT_FILE, apiFile);
    }

    private void generateCode(Tree<Location> tree) {
        for (DetailedLink link : tree.get().getLinks()) {
            generateCode(tree, link);
        }
    }

    private void generateCode(Tree<Location> tree, DetailedLink link) {
        if (isEntity(tree)) {
            if (isSubEntity(tree)) {
                extendSubResource(tree, link);
            }
            else {
                extendResource(tree, link);
            }
        }
        else if (isCollection(tree)) {
            if (isSubCollection(tree)) {
                extendSubCollection(tree, link);
            }
            else {
                extendCollection(tree, link);
            }
        }
        else if (isAction(tree)) {
            createAction(tree, link);
        }
    }

    private void extendCollection(Tree<Location> collectionTree, DetailedLink link) {
        String collectionBrokerType = BrokerRules.getBrokerType(collectionTree);

        CodeHolder holder = code.get(collectionBrokerType);
        if (holder == null) {
            String body = Collection.collection(collectionBrokerType);
            holder = new CodeHolder();
            holder.setRoot(true);
            holder.setName(collectionBrokerType);
            holder.setBody(body);
            code.put(collectionBrokerType, holder);
        }

        switch (link.getRel()) {
            case "get":
                String getMethod = Collection.get(collectionTree, link);
                holder.appendBody(getMethod);
                String listMethod = Collection.list(collectionTree, link);
                holder.appendBody(listMethod);
                break;
            case "add":
                String addMethod = Collection.add(collectionTree, link);
                holder.appendBody(addMethod);
                break;
        }
    }

    private void extendResource(Tree<Location> entityTree, DetailedLink link) {
        String entityBrokerType = BrokerRules.getBrokerType(entityTree);

        CodeHolder holder = code.get(entityBrokerType);
        if (holder == null) {
            String body = Resource.resource(entityTree);
            holder = new CodeHolder();
            holder.setName(entityBrokerType);
            holder.setBody(body);
            code.put(entityBrokerType, holder);
        }

        switch (link.getRel()) {
        case "delete":
            String deleteMethod = Resource.delete(entityTree, link);
            holder.appendBody(deleteMethod);
            break;
        case "update":
            String updateMethod = Resource.update(entityTree, link);
            holder.appendBody(updateMethod);
            break;
        }
    }

    private void createAction(Tree<Location> actionTree, DetailedLink link) {
        Tree<Location> parentTree = actionTree.getParent();

        // The methods corresponding to collection actions could perfection be added to the collection broker, but for
        // historical reasons they are added to the broker for the parent entity instead. Except if that parent entity
        // is a top level entity, in that case the method is added to the collection (this is what happens with the
        // "setupnetworks" action, for example).
        Tree<Location> destinationTree = null;
        if (isEntity(parentTree)) {
            destinationTree = parentTree;
        }
        else if (isCollection(parentTree)) {
            if (isSubCollection(parentTree)) {
                Tree<Location> grandparentLocation = parentTree.getParent();
                if (isSubEntity(grandparentLocation)) {
                    destinationTree = grandparentLocation;
                }
                else {
                    destinationTree = parentTree;
                }
            }
            else {
                // Actions on top level collections aren't supported.
                System.out.println(
                    "The action for link \"" + link.getHref() + "\" will be ignored because actions on top level " +
                    "collections aren't currently supported."
                );
                return;
            }
        }

        String actionName = LocationRules.getName(actionTree);
        String parentName = LocationRules.getName(parentTree);

        actionName = adaptActionName(actionName, parentName);

        String destinationBrokerType = BrokerRules.getBrokerType(destinationTree);

        CodeHolder holder = code.get(destinationBrokerType);
        if (holder == null) {
            holder = new CodeHolder();
            holder.setName(destinationBrokerType);
            code.put(destinationBrokerType, holder);
        }

        String actionMethod = Action.action(destinationTree, link, parentName, actionName);
        holder.appendBody(actionMethod);
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

    private void extendSubCollection(Tree<Location> collectionTree, DetailedLink link) {
        Tree<Location> parentEntityTree = collectionTree.getParent();

        String parentEntityBrokerType = BrokerRules.getBrokerType(parentEntityTree);
        String collectionBrokerType = BrokerRules.getBrokerType(collectionTree);

        CodeHolder holder = code.get(collectionBrokerType);
        if (holder == null) {
            String body = SubCollection.collection(collectionTree);
            holder = new CodeHolder();
            holder.setName(collectionBrokerType);
            holder.setBody(body);
            code.put(collectionBrokerType, holder);
        }

        CodeHolder parentHolder = code.get(parentEntityBrokerType);
        if (parentHolder == null) {
            System.out.printf("failed locating cache for: %s, at url: %s\n", SchemaRules.getSchemaType(parentEntityTree), link.getHref());
        }
        else {
            parentHolder.addSubCollection(LocationRules.getName(collectionTree), collectionBrokerType);
        }

        switch (link.getRel()) {
        case "get":
            String getMethod = SubCollection.get(collectionTree, link);
            holder.appendBody(getMethod);
            String listMethod = SubCollection.list(collectionTree, link);
            holder.appendBody(listMethod);
            break;
        case "add":
            String addMethod = SubCollection.add(collectionTree, link);
            holder.appendBody(addMethod);
            break;
        }
    }

    private void extendSubResource(Tree<Location> entityTree, DetailedLink link) {
        String entityBrokerType = BrokerRules.getBrokerType(entityTree);

        CodeHolder holder = code.get(entityBrokerType);
        if (holder == null) {
            String body = SubResource.resource(entityTree);
            holder = new CodeHolder();
            holder.setName(entityBrokerType);
            holder.setBody(body);
            code.put(entityBrokerType, holder);
        }

        switch (link.getRel()) {
        case "delete":
            String deleteMethod = SubResource.delete(entityTree, link);
            holder.appendBody(deleteMethod);
            break;
        case "update":
            String updateMethod = SubResource.update(entityTree, link);
            holder.appendBody(updateMethod);
            break;
        }
    }
}
