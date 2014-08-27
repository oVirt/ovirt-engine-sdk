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

import static org.ovirt.engine.sdk.generator.utils.CollectionsUtils.mapOf;

import java.io.File;
import java.io.IOException;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import javax.xml.XMLConstants;
import javax.xml.namespace.NamespaceContext;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class XsdData {
    private static final XsdData instance = new XsdData();

    private static final Map<String, String> XML_TYPE_INSTANCE_EXCEPTIONS = mapOf(
        "template", "Template"
    );

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
        XPath xpath = XPathFactory.newInstance().newXPath();
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

        // Exclude all the simple types:
        Set<String> excluded = new HashSet<>();
        try {
            NodeList names = (NodeList) xpath.evaluate("//xs:simpleType/@name", schema, XPathConstants.NODESET);
            for (int i = 0; i < names.getLength(); i++) {
                Node name = names.item(i);
                excluded.add(name.getNodeValue());
            }
        }
        catch (XPathExpressionException exception) {
            throw new IOException("Can't find simple types.", exception);
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
        try {
            NodeList elements = (NodeList) xpath.evaluate("//xs:element", schema, XPathConstants.NODESET);
            for (int i = 0; i < elements.getLength(); i++) {
                Node element = elements.item(i);
                NamedNodeMap attrs = element.getAttributes();
                Attr nameAttr = (Attr) attrs.getNamedItem("name");
                Attr typeAttr = (Attr) attrs.getNamedItem("type");
                if (nameAttr != null && typeAttr != null) {
                    String name = nameAttr.getValue();
                    String type = typeAttr.getValue();
                    if (!type.startsWith("xs:") && !excluded.contains(type)) {
                        typesByTag.put(name, type);
                    }
                }
            }
        }
        catch (XPathExpressionException exception) {
            throw new IOException("Can't find elements.", exception);
        }

        // There are several conflicts with "version", so force it:
        typesByTag.put("version", "VersionCaps");

        // Populate the tags by type name, including only the top level element definitions that appear in the XML
        // schema, those that can appear as roots of valid XML documents:
        try {
            NodeList elements = (NodeList) xpath.evaluate("/xs:schema/xs:element", schema, XPathConstants.NODESET);
            for (int i = 0; i < elements.getLength(); i++) {
                Node element = elements.item(i);
                NamedNodeMap attrs = element.getAttributes();
                Attr nameAttr = (Attr) attrs.getNamedItem("name");
                Attr typeAttr = (Attr) attrs.getNamedItem("type");
                if (nameAttr != null && typeAttr != null) {
                    String name = nameAttr.getValue();
                    String type = typeAttr.getValue();
                    if (!type.startsWith("xs:") && !excluded.contains(type)) {
                        tagsByType.put(type, name);
                    }
                }
            }
        }
        catch (XPathExpressionException exception) {
            throw new IOException("Can't find elements.", exception);
        }

    }

    public Map<String, String> getTypesByTag() {
        return typesByTag;
    }

    public Map<String, String> getTagsByType() {
        return tagsByType;
    }

    public String getXmlWrapperType(String typeName) {
        String tn = typeName.toLowerCase();
        for (Map.Entry<String, String> entry : typesByTag.entrySet()) {
            String k = entry.getKey();
            String v = entry.getValue();
            if (v.toLowerCase().equals(tn) || k.toLowerCase().equals(tn) || k.replace("_", "").equals(tn)) {
                return v;
            }
        }
        return typeName;
    }

    public String getXmlTypeInstance(String typeName) {
        String tn = typeName.toLowerCase();
        String result = XML_TYPE_INSTANCE_EXCEPTIONS.get(tn);
        if (result == null) {
            for (Map.Entry<String, String> entry : typesByTag.entrySet()) {
                String v = entry.getValue();
                if (v.toLowerCase().equals(tn)) {
                    result = entry.getKey();
                    break;
                }
            }
            if (result == null) {
                result = typeName;
            }
        }
        return result;
    }

    public String getXmlType(String typeName) {
        if (typeName != null && !typeName.isEmpty()) {
            String tn = typeName.toLowerCase();
            for (Map.Entry<String, String> entry : typesByTag.entrySet()) {
                String k = entry.getKey();
                String v = entry.getValue();
                if (v.toLowerCase().equals(tn) || k.toLowerCase().equals(tn)) {
                    return v;
                }
            }
        }
        return null;
    }
}
