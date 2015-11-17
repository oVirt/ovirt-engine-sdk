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

package org.ovirt.engine.sdk.generator.python;

import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;

import org.ovirt.engine.sdk.generator.BrokerRules;
import org.ovirt.engine.sdk.generator.Location;
import org.ovirt.engine.sdk.generator.LocationRules;
import org.ovirt.engine.sdk.generator.SchemaRules;
import org.ovirt.engine.sdk.generator.python.templates.SubCollectionAddTemplate;
import org.ovirt.engine.sdk.generator.python.templates.SubCollectionGetTemplate;
import org.ovirt.engine.sdk.generator.python.templates.SubCollectionListTemplate;
import org.ovirt.engine.sdk.generator.python.templates.SubCollectionListWithParamsTemplate;
import org.ovirt.engine.sdk.generator.python.templates.SubCollectionTemplate;
import org.ovirt.engine.sdk.generator.templates.AbstractTemplate;
import org.ovirt.engine.sdk.generator.python.utils.HeaderUtils;
import org.ovirt.engine.sdk.generator.python.utils.ParamUtils;
import org.ovirt.engine.sdk.generator.utils.Tree;
import org.ovirt.engine.sdk.generator.python.utils.UrlUtils;
import org.ovirt.engine.sdk.entities.DetailedLink;

public class SubCollection {
    public static String collection(Tree<Location> collectionTree) {
        Tree<Location> entityTree = collectionTree.getParent();

        String brokerType = BrokerRules.getBrokerType(collectionTree);
        String entityType = SchemaRules.getSchemaType(entityTree);
        String parentClassParameterName = entityType.toLowerCase().replace("_", "");

        SubCollectionTemplate template = new SubCollectionTemplate();
        template.set("broker_type", brokerType);
        template.set("parentclass_parameter_name", parentClassParameterName);
        return template.evaluate();
    }

    public static String get(Tree<Location> collectionTree, DetailedLink link) {
        Tree<Location> entityTree = collectionTree.getChild(LocationRules::isEntity);

        String[] result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamStr = result[0];
        String headersMapParamsStr = result[1];

        headersMethodParamStr = !headersMethodParamStr.isEmpty()? headersMethodParamStr + ", ": headersMethodParamStr;

        SubCollectionGetTemplate template = new SubCollectionGetTemplate();
        template.set("url", link.getHref());
        template.set("entity_broker_type", BrokerRules.getBrokerType(entityTree));
        template.set("getter_name", SchemaRules.getElementName(collectionTree));
        template.set("headers_method_params_str", headersMethodParamStr);
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("url_params_id",
            UrlUtils.generateUrlIdentifiersReplacements(
                collectionTree,
                "                            "
            )
        );
        template.set("url_params_name",
            UrlUtils.generateUrlIdentifiersReplacements(
                collectionTree,
                "                    "
            )
        );

        Map<String, String> docsParams = new LinkedHashMap<>();
        docsParams.put("id  : string (the id of the entity)", "False");
        docsParams.put("name: string (the name of the entity)", "False");
        String docs = Documentation.document(link, docsParams, new LinkedHashMap<>());
        template.set("docs", docs);

        return template.evaluate();
    }

    public static String list(Tree<Location> collectionTree, DetailedLink link) {
        Tree<Location> entityTree = collectionTree.getChild(LocationRules::isEntity);

        Object[] result = ParamUtils.getMethodParamsByUrlParamsMeta(link);
        String prmsStr = (String) result[0];
        Map<String, String> methodParams = (Map) result[1];
        Map<String, String> urlParams = (Map) result[2];

        result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        String combinedMethodParams =
            prmsStr +
            (!prmsStr.isEmpty() && !headersMethodParamStr.isEmpty()? ", ": "") +
            headersMethodParamStr;

        Map<String, String> methodParamsCopy = new LinkedHashMap<>(methodParams);
        methodParams.put("**kwargs", "**kwargs");

        Map<String, String> values = new LinkedHashMap<>();
        values.put("url", link.getHref());
        values.put("entity_broker_type", BrokerRules.getBrokerType(entityTree));
        values.put("getter_name", SchemaRules.getElementName(collectionTree));
        values.put("combined_method_params", combinedMethodParams);
        values.put("headers_map_params_str", headersMapParamsStr);
        values.put("url_query_params", ParamUtils.toDictStr(urlParams.keySet(), methodParamsCopy.keySet()));

        AbstractTemplate template;
        if (!prmsStr.isEmpty() || !headersMethodParamStr.isEmpty()) {
            Map<String, String> customParams = new LinkedHashMap<>();
            customParams.put("**kwargs: dict (property based filtering)\"", "False");
            customParams.put("query: string (oVirt engine search dialect query)", "False");
            String docs = Documentation.document(link, customParams, methodParams);
            values.put("docs", docs);
            values.put("url_params",
                UrlUtils.generateUrlIdentifiersReplacements(
                    collectionTree,
                    "                    "
                )
            );
            template = new SubCollectionListWithParamsTemplate();
        }
        else {
            Map<String, String> customParams = new LinkedHashMap<>();
            customParams.put("**kwargs: dict (property based filtering)\"", "False");
            String docs = Documentation.document(link, customParams, new LinkedHashMap<>());
            values.put("docs", docs);
            values.put("url_params",
                UrlUtils.generateUrlIdentifiersReplacements(
                    collectionTree,
                    "                "
                )
            );
            template = new SubCollectionListTemplate();
        }

        template.set(values);
        return template.evaluate();
    }

    public static String add(Tree<Location> collectionTree, DetailedLink link) {
        Tree<Location> entityTree = collectionTree.getChild(LocationRules::isEntity);
        String elementName = SchemaRules.getElementName(collectionTree);

        Object[] result = ParamUtils.getMethodParamsByUrlParamsMeta(link);
        String prmsStr = (String) result[0];
        Map<String, String> methodParams = (Map) result[1];
        Map<String, String> urlParams = (Map) result[2];

        result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        StringBuilder combinedMethodParams = new StringBuilder();
        if (!headersMethodParamStr.isEmpty()) {
            combinedMethodParams.append(", ");
            combinedMethodParams.append(headersMethodParamStr);
        }
        if (!prmsStr.isEmpty()) {
            combinedMethodParams.append(", ");
            combinedMethodParams.append(prmsStr);
        }

        SubCollectionAddTemplate template = new SubCollectionAddTemplate();
        template.set("parameter_name", elementName.replaceAll("_", ""));
        template.set("url", link.getHref());
        template.set("entity_broker_type", BrokerRules.getBrokerType(entityTree));
        template.set("combined_method_params", combinedMethodParams);
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("url_query_params", ParamUtils.toDictStr(urlParams.keySet(), methodParams.keySet()));
        template.set("docs", Documentation.document(link, Collections.emptyMap(), methodParams));
        template.set("url_params",
            UrlUtils.generateUrlIdentifiersReplacements(
                collectionTree,
                "                    "
            )
        );

        return template.evaluate();
    }
}
