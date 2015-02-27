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

import java.util.LinkedHashMap;
import java.util.Map;

import org.ovirt.engine.sdk.generator.BrokerRules;
import org.ovirt.engine.sdk.generator.Location;
import org.ovirt.engine.sdk.generator.SchemaRules;
import org.ovirt.engine.sdk.generator.python.templates.SubResourceDeleteTemplate;
import org.ovirt.engine.sdk.generator.python.templates.SubResourceDeleteWithBodyTemplate;
import org.ovirt.engine.sdk.generator.python.templates.SubResourceDeleteWithUrlParamsAndBodyTemplate;
import org.ovirt.engine.sdk.generator.python.templates.SubResourceDeleteWithUrlParamsTemplate;
import org.ovirt.engine.sdk.generator.python.templates.SubResourceTemplate;
import org.ovirt.engine.sdk.generator.python.templates.SubResourceUpdateTemplate;
import org.ovirt.engine.sdk.generator.templates.AbstractTemplate;
import org.ovirt.engine.sdk.generator.python.utils.HeaderUtils;
import org.ovirt.engine.sdk.generator.python.utils.ParamUtils;
import org.ovirt.engine.sdk.generator.utils.Tree;
import org.ovirt.engine.sdk.generator.python.utils.UrlUtils;
import org.ovirt.engine.sdk.entities.DetailedLink;

public class SubResource {
    public static String resource(Tree<Location> entityTree) {
        Tree<Location> grandparentTree = entityTree.getParent().getParent();

        String entityType = SchemaRules.getSchemaType(entityTree);
        String grandparentType = SchemaRules.getSchemaType(grandparentTree);
        String brokerType = BrokerRules.getBrokerType(entityTree);
        String superClassParameterName = entityType.toLowerCase().replace("_", "");
        String parentClassParameterName = grandparentType.toLowerCase().replace("_", "");

        SubResourceTemplate template = new SubResourceTemplate();
        template.set("entity_type", entityType);
        template.set("broker_type", brokerType);
        template.set("superclass_parameter_name", superClassParameterName);
        template.set("parentclass_parameter_name", parentClassParameterName);

        return template.evaluate();
    }

    public static String update(Tree<Location> entityTree, DetailedLink link) {
        String combinedMethodParams = "";

        Object[] result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        headersMethodParamsStr = !headersMethodParamsStr.isEmpty()?
            ", " + headersMethodParamsStr:
            headersMethodParamsStr;

        result = ParamUtils.getMethodParamsByUrlParamsMeta(link);
        String prmsStr = (String) result[0];
        Map<String, String> methodParams = (Map) result[1];
        Map<String, String> urlParams = (Map) result[2];

        if (!prmsStr.isEmpty() || !headersMethodParamsStr.isEmpty()) {
            combinedMethodParams = !prmsStr.isEmpty() && !prmsStr.startsWith(",")? ", ": "";
            combinedMethodParams += prmsStr + headersMethodParamsStr;
        }

        Map<String, String> methodParamsCopy = new LinkedHashMap<>(methodParams);

        String urlParamsStr = ParamUtils.toDictStr(
            urlParams.keySet(), methodParamsCopy.keySet()
        );

        String urlIdentifiersReplacements = UrlUtils.generateUrlIdentifiersReplacements(
            entityTree,
            "            "
        );

        SubResourceUpdateTemplate template = new SubResourceUpdateTemplate();
        template.set("url", link.getHref());
        template.set("entity_broker_type", BrokerRules.getBrokerType(entityTree));
        template.set("url_identifiers_replacments", urlIdentifiersReplacements);
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("combined_method_params", combinedMethodParams);
        template.set("url_params_separator", !urlParamsStr.isEmpty()? ", " + urlParamsStr: "");
        template.set("docs", Documentation.document(link, new LinkedHashMap<>(), methodParams));

        return template.evaluate();
    }

    public static String delete(Tree<Location> collectionTree, DetailedLink link) {
        Object[] result = ParamUtils.getMethodParamsByUrlParamsMeta(link);
        String prmsStr = (String) result[0];
        LinkedHashMap<String, String> methodParams = (LinkedHashMap) result[1];
        LinkedHashMap<String, String> urlParams = (LinkedHashMap) result[2];

        result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        String combinedMethodParams =
            prmsStr +
            (!prmsStr.isEmpty() && !headersMethodParamsStr.isEmpty()? ", ": "") +
            headersMethodParamsStr;

        String headersMapParamsStrWithNoCt =
            !headersMapParamsStr.equals("{}")?
                headersMapParamsStr.replace("}", ",\"Content-type\":None}"):
                "{\"Content-type\":None}";

        String bodyInstance = ParamUtils.getBodyInstance(link);
        String bodyInstanceStr = !bodyInstance.isEmpty()? "=" + bodyInstance: "";

        String bodyType = null;
        if (link.isSetRequest() && link.getRequest().isSetBody()) {
            bodyType = link.getRequest().getBody().getType();
        }

        Map<String, String> values = new LinkedHashMap<>();
        values.put("url", link.getHref());
        values.put("body_type_lc", bodyType != null ? bodyType.toLowerCase() : null);
        values.put("headers_map_params_str_with_no_ct", headersMapParamsStrWithNoCt);
        values.put("combined_method_params", combinedMethodParams);
        values.put("body_instance_str", bodyInstanceStr);
        values.put("headers_map_params_str", headersMapParamsStr);
        values.put("url_params", ParamUtils.toDictStr(urlParams.keySet(), methodParams.keySet()));

        AbstractTemplate templateWithBody;
        AbstractTemplate templateWithoutBody;
        if (!prmsStr.isEmpty() || !headersMethodParamsStr.isEmpty()) {
            values.put("docs", Documentation.document(link, new LinkedHashMap<>(), methodParams));
            values.put("url_identifyiers",
                UrlUtils.generateUrlIdentifiersReplacements(
                    collectionTree,
                    "            "
                )
            );

            templateWithBody = new SubResourceDeleteWithUrlParamsAndBodyTemplate();
            templateWithoutBody = new SubResourceDeleteWithUrlParamsTemplate();
        }
        else {
            values.put("docs", Documentation.document(link));
            values.put("url_identifyiers",
                UrlUtils.generateUrlIdentifiersReplacements(
                    collectionTree,
                    "                "
                )
            );
            values.put("url_identifyiers_with_body",
                UrlUtils.generateUrlIdentifiersReplacements(
                    collectionTree,
                    "                                                               "
                )
            );

            templateWithBody = new SubResourceDeleteWithBodyTemplate();
            templateWithoutBody = new SubResourceDeleteTemplate();
        }

        if (bodyType == null || bodyType.isEmpty()) {
            templateWithoutBody.set(values);
            return templateWithoutBody.evaluate();
        }
        else {
            templateWithBody.set(values);
            return templateWithBody.evaluate();
        }
    }
}
