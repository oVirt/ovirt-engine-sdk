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

import org.ovirt.engine.sdk.generator.utils.Tree;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * This class contains methods that implement various rules associated to locations, like checking if a location
 * corresponds to an entity or collection.
 */
public class LocationRules {
    /**
     * The regular expression used to check if a label is a variable. For example, {@code {cluster:id}} is a variable
     * but {@code cluster} isn't.
     */
    private static final Pattern VARIABLE_PATTERN = Pattern.compile("^\\{(?<name>[^:]+):[^:]+\\}$");

    /**
     * Checks if the label of the given location is a variable, like for example {@code {cluster:id}}.
     *
     * @param tree the location to check
     * @return {@code true} if the label of the location is a variable, {@code false} otherwise
     */
    public static boolean isVariable(Tree<Location> tree) {
        String label = tree.getLabel();
        return label != null && VARIABLE_PATTERN.matcher(label).matches();
    }

    /**
     * Checks if the given location corresponds to an entity resource.
     *
     * @param tree the location to check
     * @return {@code true} if the location corresponds to an entity, {@code false} otherwise
     */
    public static boolean isEntity(Tree<Location> tree) {
        return isVariable(tree);
    }

    /**
     * Checks if the given location corresponds to a collection resource.
     *
     * @param tree the location to check
     * @return {@code true} if the location corresponds to a collection, {@code false} otherwise
     */
    public static boolean isCollection(Tree<Location> tree) {
        return tree.getChildren().stream().anyMatch(LocationRules::isVariable);
    }

    /**
     * Checks if the given location corresponds to a sub-collection resource.
     *
     * @param tree the location to check
     * @return {@code true} if the location corresponds to a sub-collection, {@code false} otherwise
     */
    public static boolean isSubCollection(Tree<Location> tree) {
        Tree<Location> parent = tree.getParent();
        return parent != null && isEntity(parent);
    }

    /**
     * Checks if the given location corresponds to a sub-entity resource.
     *
     * @param tree the location to check
     * @return {@code true} if the location corresponds to a sub-collection, {@code false} otherwise
     */
    public static boolean isSubEntity(Tree<Location> tree) {
        Tree<Location> parent = tree.getParent();
        return parent != null && isSubCollection(parent);
    }

    /**
     * Checks if the given location corresponds to an action.
     *
     * @param tree the location to check
     * @return {@code true} if the location corresponds to an action, {@code false} otherwise
     */
    public static boolean isAction(Tree<Location> tree) {
        return tree.isLeaf() && !isVariable(tree);
    }

    /**
     * Returns the name of a location, not including decorations. In particular for variables the surrounding curly
     * brackets and the {@code :id} suffix will be removed. For example, if the label is {@code {cluster:id}} this
     * method will return just {@code cluster}.
     *
     * @param tree the location to check
     * @return the name of the location, not including decorations
     */
    public static String getName(Tree<Location> tree) {
        String name = tree.getLabel();
        if (name != null) {
            Matcher matcher = VARIABLE_PATTERN.matcher(name);
            if (matcher.matches()) {
                name = matcher.group("name");
            }
        }
        return name;
    }
}
