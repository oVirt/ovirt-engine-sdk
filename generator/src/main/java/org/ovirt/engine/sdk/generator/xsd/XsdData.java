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

package org.ovirt.engine.sdk.generator.xsd;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import javax.xml.XMLConstants;
import javax.xml.namespace.NamespaceContext;
import javax.xml.namespace.QName;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class XsdData {
    private static final XsdData instance = new XsdData();

    public static XsdData getInstance() {
        return instance;
    }

    /**
     * This maps stores the relationship between XML tag names and Python type names.
     */
    private Map<String, String> typesByTag = new LinkedHashMap<>();

    /**
     * This map stores the relationship between Python type names and XML tags. Note that this isn't the inverse of the
     * previous one, as some types don't have a tag because they don't appear as top level element declarations in the
     * XML schema, thus they can't appear as root elements in a valid XML document.
     */
    private Map<String, String> tagsByType = new LinkedHashMap<>();

    /**
     * This map contains the DOM trees of all the top level element definitions that appear in the XML schema, indexed
     * by name.
     */
    private Map<String, Element> elementsIndex = new HashMap<>();

    /**
     * This map contains the DOM trees of all the complex types that appear in the XML schema, indexed by name.
     */
    private Map<String, Element> complexTypesIndex = new HashMap<>();

    /**
     * We will create and reuse this XPath expression.
     */
    private XPath xpath;

    private XsdData() {
    }

    public void load(String xsd) throws IOException {
        // Parse the XML schema document:
        Document schema;
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            factory.setNamespaceAware(true);
            DocumentBuilder parser = factory.newDocumentBuilder();
            schema = parser.parse(new File(xsd));
        }
        catch (Exception exception) {
            throw new IOException("Can't parse XML schema.", exception);
        }

        // Prepare the xpath engine with the required namespace mapping:
        xpath = XPathFactory.newInstance().newXPath();
        xpath.setNamespaceContext(
            new NamespaceContext() {
                @Override
                public String getNamespaceURI(String prefix) {
                    switch (prefix) {
                    case "xs":
                        return "http://www.w3.org/2001/XMLSchema";
                    default:
                        return XMLConstants.NULL_NS_URI;
                    }
                }

                @Override
                public String getPrefix(String namespaceURI) {
                    throw new UnsupportedOperationException();
                }

                @Override
                public Iterator getPrefixes(String namespaceURI) {
                    throw new UnsupportedOperationException();
                }
            }
        );

        // Populate the indexes:
        populateElementsIndex(schema);
        populateComplexTypesIndex(schema);

        // Exclude all the simple types:
        Set<String> excluded = new HashSet<>();
        NodeList nodes = (NodeList) evaluate("//xs:simpleType/@name", schema, XPathConstants.NODESET);
        for (int i = 0; i < nodes.getLength(); i++) {
            Node name = nodes.item(i);
            excluded.add(name.getNodeValue());
        }

        // Exclude infrastructure types:
        excluded.add("BaseDevice");
        excluded.add("BaseDevices");
        excluded.add("BaseResource");
        excluded.add("BaseResources");
        excluded.add("DetailedLink");
        excluded.add("ErrorHandlingOptions");

        // Exclude the VM summary because it conflicts with the API summary:
        excluded.add("VmSummary");

        // Populate the types by tag map, including all the element definitions that appear in the XML schema, even
        // those that aren't top level and thus not valid as roots of valid XML documents:
        NodeList elements = (NodeList) evaluate("//xs:element", schema, XPathConstants.NODESET);
        for (int i = 0; i < elements.getLength(); i++) {
            Element element = (Element) elements.item(i);
            String name = element.getAttribute("name");
            String type = element.getAttribute("type");
            if (!name.isEmpty() && !type.isEmpty()) {
                if (!type.startsWith("xs:") && !excluded.contains(type)) {
                    typesByTag.put(name, type);
                }
            }
        }

        // There are several conflicts with "version", so force it:
        typesByTag.put("version", "VersionCaps");

        // Populate the tags by type name, including only the top level element definitions that appear in the XML
        // schema, those that can appear as roots of valid XML documents:
        elements = (NodeList) evaluate("/xs:schema/xs:element", schema, XPathConstants.NODESET);
        for (int i = 0; i < elements.getLength(); i++) {
            Element element = (Element) elements.item(i);
            String name = element.getAttribute("name");
            String type = element.getAttribute("type");
            if (!name.isEmpty() && !type.isEmpty()) {
                if (!type.startsWith("xs:") && !excluded.contains(type)) {
                    tagsByType.put(type, name);
                }
            }
        }
    }

    private void populateElementsIndex(Document schema) {
        NodeList nodes = (NodeList) evaluate("/xs:schema/xs:element", schema, XPathConstants.NODESET);
        for (int i = 0; i < nodes.getLength(); i++) {
            Element node = (Element) nodes.item(i);
            String name = node.getAttribute("name");
            if (!name.isEmpty()) {
                elementsIndex.put(name, node);
            }
        }
    }

    private void populateComplexTypesIndex(Document schema) {
        NodeList nodes = (NodeList) evaluate("/xs:schema/xs:complexType", schema, XPathConstants.NODESET);
        for (int i = 0; i < nodes.getLength(); i++) {
            Element node = (Element) nodes.item(i);
            String name = node.getAttribute("name");
            if (!name.isEmpty()) {
                complexTypesIndex.put(name, node);
            }
        }
    }

    private Object evaluate(String expression, Object item, QName returnType) {
        try {
            return xpath.evaluate(expression, item, returnType);
        }
        catch (XPathExpressionException exception) {
            throw new RuntimeException("Can't evaluate XPath expression \"" + expression + "\".");
        }
    }

    public Map<String, String> getTypesByTag() {
        return typesByTag;
    }

    public Map<String, String> getTagsByType() {
        return tagsByType;
    }

    /**
     * Checks if the complex type represented by the given DOM node is an extension (directly or recursively) of the
     * complex type with the given name.
     *
     * @param node the DOM node representing the complex type
     * @param name the name of the base complex type
     */
    private boolean isExtensionOf(Element node, String name) {
        String base = (String) evaluate(
            "xs:complexContent/" +
            "xs:extension/" +
            "@base",
            node,
            XPathConstants.STRING
        );
        if (base == null) {
            return false;
        }
        if (base.equals(name)) {
            return false;
        }
        Element next = getComplexType(base);
        if (next == null) {
            return false;
        }
        return isExtensionOf(next, name);
    }

    public Element getElement(String name) {
        return elementsIndex.get(name);
    }
    public Element getComplexType(String name) {
        return complexTypesIndex.get(name);
    }

    public String getEntityElementForCollectionType(String collectionType) {
        Element collectionTypeNode = getComplexType(collectionType);
        if (collectionTypeNode == null) {
            return null;
        }
        return getEntityElementForCollectionType(collectionTypeNode);
    }

    private String getEntityElementForCollectionType(Element collectionTypeNode) {
        NodeList contentNodes = (NodeList) evaluate(
            "xs:complexContent/" +
            "xs:extension/" +
            "xs:sequence/" +
            "xs:element",
            collectionTypeNode,
            XPathConstants.NODESET
        );
        String entityElement = null;
        for (int i = 0; entityElement == null && i < contentNodes.getLength(); i++) {
            Element contentNode = (Element) contentNodes.item(i);
            String ref = contentNode.getAttribute("ref");
            if (!ref.isEmpty()) {
                entityElement = ref;
            }
        }
        if (entityElement == null) {
            for (int i = 0; entityElement == null && i < contentNodes.getLength(); i++) {
                Element contentNode = (Element) contentNodes.item(i);
                String name = contentNode.getAttribute("name");
                String type = contentNode.getAttribute("type");
                if (!name.isEmpty() && !type.isEmpty()) {
                    entityElement = name;
                }
            }
        }
        return entityElement;
    }

    public String getEntityTypeForCollectionType(String collectionType) {
        Element collectionTypeNode = getComplexType(collectionType);
        if (collectionTypeNode == null) {
            return null;
        }
        return getEntityTypeForCollectionType(collectionTypeNode);
    }

    private String getEntityTypeForCollectionType(Element collectionTypeNode) {
        NodeList contentNodes = (NodeList) evaluate(
            "xs:complexContent/" +
            "xs:extension/" +
            "xs:sequence/" +
            "xs:element",
            collectionTypeNode,
            XPathConstants.NODESET
        );
        String entityType = null;
        for (int i = 0; entityType == null && i < contentNodes.getLength(); i++) {
            Element contentNode = (Element) contentNodes.item(i);
            String ref = contentNode.getAttribute("ref");
            if (!ref.isEmpty()) {
                Element elementNode = getElement(ref);
                if (elementNode != null) {
                    String type = elementNode.getAttribute("type");
                    if (!type.isEmpty()) {
                        entityType = type;
                    }
                }
            }
        }
        if (entityType == null) {
            for (int i = 0; entityType == null && i < contentNodes.getLength(); i++) {
                Element element = (Element) contentNodes.item(i);
                String name = element.getAttribute("name");
                String type = element.getAttribute("type");
                if (!name.isEmpty() && !type.isEmpty()) {
                    entityType = type;
                }
            }
        }
        return entityType;
    }
}
