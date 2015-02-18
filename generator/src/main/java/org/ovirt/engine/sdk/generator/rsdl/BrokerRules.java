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

package org.ovirt.engine.sdk.generator.rsdl;

import org.ovirt.engine.sdk.generator.utils.Tree;

import static java.util.stream.Collectors.joining;

/**
 * This class contains methods that implement various rules and calculations associated to broker class names, like
 * calculating the name of the broker class corresponding to a location.
 */
public class BrokerRules {
    /**
     * Calculate the name of the broker class that will be generated for the entity or collection represented by the
     * given location.
     *
     * @param tree the location whose broker name will be calculated
     * @return the name of the broker class, or {@code null} if it can't be determined
     */
    public static String getBrokerType(Tree<Location> tree) {
        // The name of a broker type is calculated concatenating the names of all the parent entity resources (not the
        // collections, as they are redundant) and the name of the resource itself:
        return tree.getBranch().stream()
            .skip(1)
            .filter(x -> LocationRules.isEntity(x) || x == tree)
            .map(BrokerRules::getCapitalizedName)
            .collect(joining());
    }

    /**
     * Returns the capitalized name of a location. For example, if the name of the location is {@code cluster} it will
     * return {@code Cluster}.
     *
     * @param tree the location to check
     * @return the capitalized name of the location
     */
    private static String getCapitalizedName(Tree<Location> tree) {
        String name = LocationRules.getName(tree);
        if (name != null && !name.isEmpty()) {
            name = Character.toUpperCase(name.charAt(0)) + name.substring(1);
        }
        return name;
    }
}
