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

import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.entities.RSDL;
import org.ovirt.engine.sdk.entities.Response;
import org.ovirt.engine.sdk.generator.utils.Tree;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

/**
 * This class contains the information extracted from the RSDL metadata.
 */
public class RsdlData {
    /**
     * This is a singleton, and this is the reference to the instance.
     */
    private static final RsdlData instance = new RsdlData();

    /**
     * Get the reference to the instance of this singleton.
     */
    public static RsdlData getInstance() {
        return instance;
    }

    /**
     * The file containing the RSDL metadata.
     */
    private File file;

    /**
     * The root of the tree of locations.
     */
    private Tree<Location> root = new Tree<>();

    /**
     * Returns the file that contains the RSDL metadata.
     */
    public File getFile() {
        return file;
    }

    /**
     * Returns the root of the tree of locations populated from the RSDL metadata. Note that the returned object is
     * the one used internally, not a copy, so try to avoid modifying it.
     */
    public Tree<Location> getRoot() {
        return root;
    }

    /**
     * Loads the RSDL metadata from a file and extracts the information required to build the tree of locations.
     *
     * @param file the file that contains the RSDL metadata
     * @throws IOException if something fails while loading the metadata or building the tree of locations
     */
    public void load(File file) throws IOException {
        // Save the reference to the file:
        this.file = file;

        // Load the RSDL document:
        RSDL rsdl = load();

        // The RSDL provided by the server doesn't include some links that are needed by the code generator, so we need
        // to add them explicitly:
        addMissingLinks(rsdl);

        // Build the tree of URLs scanning all the links:
        root.set(new Location());
        for (DetailedLink link : rsdl.getLinks().getLinks()) {
            List<String> path = Arrays.asList(link.getHref().split("/"));
            Tree<Location> tree = root.getDescendant(path);
            if (tree == null) {
                tree = root.addDescendant(path);
            }
            Location location = tree.get();
            if (location == null) {
                location = new Location();
                tree.set(location);
            }
            location.addLink(link);
        }

        // Get all the tree nodes:
        List<Tree<Location>> locations = root.getDescendants();

        // The previous process may have created intermediate nodes without a location object associated, and that may
        // cause null pointer exceptions later, so to avoid that we need to make sure that all the nodes of the tree
        // have a location, even if it is empty:
        for (Tree<Location> tree : locations) {
            Location location = tree.get();
            if (location == null) {
                location = new Location();
                tree.set(location);
            }
        }
    }

    private void addMissingLinks(RSDL rsdl) {
        addMissingLink(rsdl, "users/{user:id}/roles/{role:id}", "Role");
        addMissingLink(rsdl, "users/{user:id}/roles/{role:id}/permits/{permit:id}", "Permit");
        addMissingLink(rsdl, "groups/{group:id}/roles/{role:id}", "Role");
        addMissingLink(rsdl, "groups/{group:id}/roles/{role:id}/permits/{permit:id}", "Permit");
    }

    private void addMissingLink(RSDL rsdl, String href, String type) {
        DetailedLink link = new DetailedLink();
        link.setHref(href);
        link.setRel("get");
        Response response = new Response();
        response.setType(type);
        link.setResponse(response);
        rsdl.getLinks().getLinks().add(link);
    }

    /**
     * Loads the RSDL metadata from a file.
     *
     * @return the RSDL object populated with the data loaded from the file
     * @throws IOException if something while loading the metadata
     */
    private RSDL load() throws IOException {
        try {
            JAXBContext context = JAXBContext.newInstance(RSDL.class);
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Source source = new StreamSource(file);
            JAXBElement<RSDL> element = unmarshaller.unmarshal(source, RSDL.class);
            return element.getValue();
        }
        catch (JAXBException exception) {
            throw new IOException(exception);
        }
    }
}
