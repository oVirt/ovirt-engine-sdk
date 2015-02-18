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

package org.ovirt.engine.sdk.generator.utils;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.function.Predicate;

import static java.util.stream.Collectors.toList;

/**
 * This class is a simple tree data structure. Each tree has a label, a content and a set of children that
 * are themselves trees.
 *
 * @param <T> the type of the content
 */
public class Tree<T> {
    /**
     * A reference to the parent tree.
     */
    private Tree<T> parent;

    /**
     * The label of this tree relative to its parent.
     */
    private String label;

    /**
     * The direct children of this tree.
     */
    private List<Tree<T>> children = new ArrayList<>();

    /**
     * The content of this tree.
     */
    private T content;

    /**
     * Returns the parent of this tree. The result will be {@code null} if this is a root.
     */
    public Tree<T> getParent() {
        return parent;
    }

    /**
     * Changes the parent of this location.
     */
    public void setParent(Tree<T> parent) {
        this.parent = parent;
    }

    /**
     * Changes the label of this location.
     */
    public void setLabel(String label) {
        this.label = label;
    }

    /**
     * Returns the label of this location, including any decorations like the curly brackets surrounding variables.
     */
    public String getLabel() {
        return label;
    }

    /**
     * Sets the content of this tree, replacing any previously existing content.
     */
    public void set(T content) {
        this.content = content;
    }

    /**
     * Gets the content of this tree.
     */
    public T get() {
        return content;
    }

    /**
     * Adds a direct child to this location. If there is already a child with the given label then no new child will be
     * created, and the existing one will be returned.
     *
     * @param label the label of the new child
     * @return the child corresponding to the given label, which may be a previously existing one
     */
    public Tree<T> addChild(String label) {
        Tree<T> child = getChild(label);
        if (child == null) {
            child = new Tree<>();
            child.setParent(this);
            child.setLabel(label);
            children.add(child);
        }
        return child;
    }

    /**
     * Returns the first child of this location that matches the given predicate.
     *
     * @param predicate the predicate that will be used to filter out the children
     * @return the first child that matches the predicate, or {@code null} if no such child exists
     */
    public Tree<T> getChild(Predicate<Tree<T>> predicate) {
        return children.stream().filter(predicate).findFirst().orElse(null);
    }

    /**
     * Returns the first child of this location that has the given label.
     *
     * @param label the label to search for
     * @return the first child that has the given label, or {@code null} if no such child exists
     */
    public Tree<T> getChild(String label) {
        return getChild((Tree<T> child) -> child.label.equals(label));
    }

    /**
     * Returns the list of children of this location. The result will be an empty list if this location doesn't have
     * children. The returned list is the one used internally, not a copy, so care must be taken when iterating or
     * modifying it concurrently.
     */
    public List<Tree<T>> getChildren() {
        return children;
    }

    /**
     * Adds a new descendant to this location with the given labels. Intermediate locations will be created if needed.
     *
     * @param labels a list containing the labels that form the path to the new descendant
     * @return the child corresponding to the given labels, which may be an already existing one
     */
    public Tree<T> addDescendant(List<String> labels) {
        if (labels == null || labels.isEmpty()) {
            return null;
        }
        if (labels.size() == 1) {
            return addChild(labels.get(0));
        }
        Tree<T> child = getChild(labels.get(0));
        if (child == null) {
            child = addChild(labels.get(0));
        }
        return child.addDescendant(labels.subList(1, labels.size()));
    }

    /**
     * Returns the descendant located in the given path. Note the concept os descendant doesn't include this location
     * itself, so it will never be returned, even if the path is {@code null} or an empty list.
     *
     * @param path the path to the descendant
     * @return the location in the given path, or {@code null} if no such descendant exists
     */
    public Tree<T> getDescendant(List<String> path) {
        if (path == null || path.isEmpty()) {
            return null;
        }
        if (path.size() == 1) {
            return getChild(path.get(0));
        }
        Tree<T> child = getChild(path.get(0));
        if (child == null) {
            return null;
        }
        return child.getDescendant(path.subList(1, path.size()));
    }

    /**
     * Gets the list of nodes that exist in the path from the root of the tree and this node, including both the root
     * of the tree and this node. This list will be ordered, starting with the root of the tree and ending with this
     * node.
     *
     * @return a list containing the nodes in the path from the root of the tree to this node
     */
    public List<Tree<T>> getBranch() {
        List<Tree<T>> branch = new LinkedList<>();
        for (Tree<T> current = this; current != null; current = current.parent) {
            branch.add(0, current);
        }
        return branch;
    }

    /**
     * Gets the list of labels of the nodes that exist in the path from the root of the tree and this node, including
     * the labels of the root of the tree and the label of this node. This list will be ordered, starting with the label
     * of the root of the tree and ending with the label of this node.
     *
     * @return a list containing the labels of the nodes in the path from the root of the tree to this node
     */
    public List<String> getPath() {
        return getBranch().stream().map(Tree::getLabel).collect(toList());
    }

    /**
     * Determines is this is a leaf node (a node that doesn't have children).
     *
     * @return {@code true} if this is a leaf node, {@code false} otherwise
     */
    public boolean isLeaf() {
        return children.isEmpty();
    }

    /**
     * Gets all the descendants of this node, not including itself. No order is guaranteed in the returned list.
     *
     * @return a list containing the descendants of this node
     */
    public List<Tree<T>> getDescendants() {
        List<Tree<T>> result = new ArrayList<>();
        getDescendants(result);
        return result;
    }

    private void getDescendants(List<Tree<T>> result) {
        for (Tree<T> child : children) {
            result.add(child);
            child.getDescendants(result);
        }
    }

    @Override
    public String toString() {
        return label;
    }
}
