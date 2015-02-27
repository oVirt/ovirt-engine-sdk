//
// Copyright (c) 2015 Red Hat, Inc.
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

package org.ovirt.engine.sdk.generator;

import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.generator.utils.Tree;

/**
 * This class contains methods that implement various rules and calculations associated with the XML schema.
 */
public class SchemaRules {
    /**
     * Get the name of the XML schema type associated to a location.
     *
     * @param tree the location to extract the type from
     * @return the schema type associated to the location, or {@code null} if it can't be determined
     */
    public static String getSchemaType(Tree<Location> tree) {
        // The best way to find out what is the type corresponding to a location is to find the link corresponding to
        // the GET method and get the body type from it:
        String type = null;
        for (DetailedLink link : tree.get().getLinks()) {
            if (link.getRel().equals("get")) {
                if (link.isSetResponse() && link.getResponse().isSetType()) {
                    type = link.getResponse().getType();
                }
            }
        }
        if (type != null) {
            return type;
        }

        // But for some resources the GET method isn't implemented, and thus there isn't any link, in this case we can
        // find the type of the parent location (recursively) and then extract the information from the XML schema:
        Tree<Location> parent = tree.getParent();
        if (parent != null) {
            String parentType = getSchemaType(parent);
            if (parentType != null) {
                type = XsdData.getInstance().getEntityTypeForCollectionType(parentType);
                if (type != null) {
                    return type;
                }
            }
        }

        // No luck:
        return null;
    }

    /**
     * Returns the name of the XML element that is used to represent elements of a collection. For example, for the
     * {@code scheduling_policies} collection it will return {@code scheduling_policy}. This information is extracted
     * from the XML schema.
     *
     * @param tree the location to extract the type from
     * @return the name of the XML element used to represent element of the collection
     */
    public static String getElementName(Tree<Location> tree) {
        return XsdData.getInstance().getEntityElementForCollectionType(getSchemaType(tree));
    }
}
