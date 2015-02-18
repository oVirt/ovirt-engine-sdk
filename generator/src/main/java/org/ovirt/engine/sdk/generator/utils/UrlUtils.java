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

package org.ovirt.engine.sdk.generator.utils;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.ovirt.engine.sdk.generator.rsdl.Location;
import org.ovirt.engine.sdk.generator.rsdl.LocationRules;

import static java.util.stream.Collectors.toList;

public class UrlUtils {
    /**
     * Replaces identifiers with real names.
     */
    public static String generateUrlIdentifiersReplacements(Tree<Location> location, String offset) {
        List<Tree<Location>> branch = location.getBranch();
        Collections.reverse(branch);

        List<String> items = new ArrayList<>();
        for (String variable : getReplacementCandidates(location)) {
            int distance = LocationRules.isEntity(location)? 0: 1;
            for (Tree<Location> current : branch) {
                if (LocationRules.isVariable(current)) {
                    if (current.getLabel().equals(variable)) {
                        break;
                    }
                    distance += 1;
                }
            }
            items.add("'" + variable + "': " + generateParentClassIdentifiers(distance) + ",");
        }

        StringBuilder buffer = new StringBuilder();
        buffer.append("{\n");
        for (String line : items) {
            buffer.append(offset);
            buffer.append("    ");
            buffer.append(line);
            buffer.append("\n");
        }
        buffer.append(offset);
        buffer.append("}");
        return buffer.toString();
    }

    private static String generateParentClassIdentifiers(int num) {
        StringBuilder buffer = new StringBuilder();
        buffer.append("self");
        for (int i = 0; i < num; i++) {
            buffer.append(".parentclass");
        }
        buffer.append(".get_id()");
        return buffer.toString();
    }

    private static List<String> getReplacementCandidates(Tree<Location> location) {
        return location.getBranch().stream()
           .filter(LocationRules::isVariable)
           .map(Tree::getLabel)
           .collect(toList());
    }
}