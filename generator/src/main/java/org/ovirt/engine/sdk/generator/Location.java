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

import java.util.ArrayList;
import java.util.List;

/**
 * This class stores information relative to each of the available locations of the API, a location being what is
 * accessible using some URL. For example, {@code vms} is a location, where a collection is available,
 * {@code vms/{vm:id}/start} is also a location, where an action is available.
 */
public class Location {
    private List<DetailedLink> links = new ArrayList<>();

    /**
     * Returns the links associated to this location. The returned list is a reference to the one used internally, so
     * care must be taken when manipulating it.
     *
     * @return a list containing the links associated to this location
     */
    public List<DetailedLink> getLinks() {
        return links;
    }

    /**
     * Adds a link to the list of links associated to this collection.
     *
     * @param link the link to add
     */
    public void addLink(DetailedLink link) {
        links.add(link);
    }
}
