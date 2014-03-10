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

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.ovirt.engine.sdk.generator.rsdl.templates.EntryPointDynamicMethodTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.EntryPointHeadTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.EntryPointMethodsTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.EntryPointStaticMethodTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.EntryPointTemplate;

public class EntryPoint {

    private static String entryPointImports() {
        EntryPointHeadTemplate template = new EntryPointHeadTemplate();
        template.set("timestamp", "'''Generated at: " + new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSSSSS").format(new Date()) + "'''");
        return template.evaluate();
    }

    private static String instanceMethods() {
        Set<String> exclude = new HashSet<>();
        exclude.add("actions");
        exclude.add("href");
        exclude.add("link");
        exclude.add("extensiontype_");
        exclude.add("creation_status");
        exclude.add("id");
        exclude.add("name");
        exclude.add("description");

        Set<String> staticMethods = new HashSet<>();
        staticMethods.add("special_objects");
        staticMethods.add("product_info");
        staticMethods.add("comment");

        String methods = new EntryPointMethodsTemplate().evaluate();

        // TODO: Get the list of attributes from the XML schema, using XSOM.
        List<String> attrs = new ArrayList<>();
        attrs.add("comment");
        attrs.add("special_objects");
        attrs.add("summary");
        attrs.add("time");
        attrs.add("product_info");

        for (String attr : attrs) {
            if (!exclude.contains(attr)) {
                if (staticMethods.contains(attr)) {
                    EntryPointStaticMethodTemplate methodTemplate = new EntryPointStaticMethodTemplate();
                    methodTemplate.set("attr", attr);
                    methods += methodTemplate.evaluate();
                }
                else {
                    EntryPointDynamicMethodTemplate methodTemplate = new EntryPointDynamicMethodTemplate();
                    methodTemplate.set("attr", attr);
                    methods += methodTemplate.evaluate();
                }
            }
        }

        return methods;
    }

    public static String entryPointCustomImports(List<String> types) {
        String entryPointCustomImportsTemplate =
            "from ovirtsdk.infrastructure.brokers import %s\n";

        String imports = "";
        for (String item : types) {
            imports += String.format(entryPointCustomImportsTemplate, item);
        }

        return imports + "\n\n";
    }

    public static String entryPoint(List<String> types, String rootCollections) {
        String apiTemplate =
            entryPointImports() +
            entryPointCustomImports(types) +
            new EntryPointTemplate().evaluate();

        return
            apiTemplate +
            rootCollections +
            instanceMethods();
    }

    public static String collection(String name, CodeHolder item) {
        String entryPointTemplate = "        self.%s = %s(self.id)\n";

        if (item.isRoot()) {
            String collName = item.getName();
            if (collName == null) {
                collName = name;
            }
            return String.format(entryPointTemplate, collName.toLowerCase(), collName);
        }
        return null;
    }
}
