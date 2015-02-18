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

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.ovirt.engine.sdk.generator.rsdl.templates.ResourceDeleteTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.ResourceDeleteWithBodyAndParamsTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.ResourceDeleteWithBodyTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.ResourceDeleteWithParamsTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.ResourceTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.ResourceUpdateTemplate;
import org.ovirt.engine.sdk.generator.templates.AbstractTemplate;
import org.ovirt.engine.sdk.generator.utils.HeaderUtils;
import org.ovirt.engine.sdk.generator.utils.ParamUtils;
import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.generator.utils.Tree;

public class Resource {
    public static String resource(Tree<Location> entityTree) {
        String entityType = SchemaRules.getSchemaType(entityTree);
        String brokerType = BrokerRules.getBrokerType(entityTree);
        String superClassParameterName = entityType.toLowerCase().replace("_", "");

        ResourceTemplate template = new ResourceTemplate();
        template.set("entity_type", entityType);
        template.set("broker_type", brokerType);
        template.set("superclass_parameter_name", superClassParameterName);
        return template.evaluate();
    }

    public static String addSubCollectionInstances(String parent, Map<String, String> subCollections) {
        String tmpl = "        self.%s = %s(%s, context)\n";

        String newTmpl = "";
        List<String> keys = new ArrayList<>(subCollections.keySet());
        Collections.sort(keys);
        for (String k : keys) {
            String v = subCollections.get(k);
            newTmpl += String.format(tmpl, k.toLowerCase(), v, parent);
        }

        return newTmpl;
    }

    public static String delete(Tree<Location> entityTree, DetailedLink link) {
        Object[] result = ParamUtils.getMethodParamsByUrlParamsMeta(link);
        String prmsStr = (String) result[0];
        Map<String, String> methodParams = (Map<String, String>) result[1];
        Map<String, String> urlParams = (Map<String, String>) result[2];

        result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        String combinedMethodParams =
            prmsStr +
            (!headersMethodParamsStr.isEmpty()? ", ": "") +
            headersMethodParamsStr;

        String bodyInstance = ParamUtils.getBodyInstance(link);
        String bodyInstanceStr = !bodyInstance.isEmpty()? "=" + bodyInstance: "";

        String bodyType = null;
        if (link.isSetRequest() && link.getRequest().isSetBody()) {
            bodyType = link.getRequest().getBody().getType();
        }

        Map<String, String> values = new LinkedHashMap<>();
        values.put("url", link.getHref());
        values.put("body_type", bodyType);
        values.put("resource_name_lc", LocationRules.getName(entityTree));
        values.put("body_type_lc", bodyType != null ? bodyType.toLowerCase() : null);
        values.put("combined_method_params", combinedMethodParams);
        values.put("headers_map_params_str_with_no_ct",
            !headersMapParamsStr.equals("{}")?
                headersMapParamsStr.replace("}", ",\"Content-type\":None}") :
                "{\"Content-type\":None}"
        );
        values.put("url_params",
            ParamUtils.toDictStr(urlParams.keySet(), methodParams.keySet())
        );
        values.put("body_instance_str", bodyInstanceStr);
        values.put("headers_map_params_str", headersMapParamsStr);

        AbstractTemplate resourceDeleteTemplate;
        AbstractTemplate bodyResourceDeleteTemplate;
        if (!prmsStr.isEmpty() || !headersMethodParamsStr.isEmpty()) {
            values.put("docs", Documentation.document(link, new LinkedHashMap<>(), methodParams));

            resourceDeleteTemplate = new ResourceDeleteWithParamsTemplate();
            bodyResourceDeleteTemplate = new ResourceDeleteWithBodyTemplate();
        }
        else {
            values.put("docs", Documentation.document(link));

            resourceDeleteTemplate = new ResourceDeleteTemplate();
            bodyResourceDeleteTemplate = new ResourceDeleteWithBodyAndParamsTemplate();
        }

        if (bodyType == null || bodyType.isEmpty()) {
            resourceDeleteTemplate.set(values);
            return resourceDeleteTemplate.evaluate();
        }
        else {
            bodyResourceDeleteTemplate.set(values);
            return bodyResourceDeleteTemplate.evaluate();
        }
    }

    public static String update(Tree<Location> entityTree, DetailedLink link) {
        Object[] result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        headersMethodParamsStr = !headersMethodParamsStr.isEmpty()? ", " + headersMethodParamsStr: "";

        ResourceUpdateTemplate template = new ResourceUpdateTemplate();
        template.set("url", link.getHref());
        template.set("entity_name", LocationRules.getName(entityTree));
        template.set("entity_broker_type", BrokerRules.getBrokerType(entityTree));
        template.set("docs", Documentation.document(link));
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("headers_method_params_str", headersMethodParamsStr);

        return template.evaluate();
    }
}
