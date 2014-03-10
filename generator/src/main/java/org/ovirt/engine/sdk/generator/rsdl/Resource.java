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
import java.util.Set;

import org.ovirt.engine.sdk.generator.rsdl.templates.ResourceActionTemplate;
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
import org.ovirt.engine.sdk.entities.HttpMethod;

public class Resource {
    public static final String SUB_COLLECTIONS_FIXME = "        #SUB_COLLECTIONS";

    public static String resource(
        String xmlEntity,
        String[] subCollections,
        Map<String, String> knownWrapperTypes
    )
    {
        String actualXmlEntity = knownWrapperTypes.get(xmlEntity.toLowerCase());
        ResourceTemplate template = new ResourceTemplate();
        template.set("xml_entity_lc", xmlEntity.toLowerCase());
        template.set("sub_collections", subCollections);
        template.set("fixme", SUB_COLLECTIONS_FIXME);
        template.set("xml_entity", actualXmlEntity != null ? actualXmlEntity : xmlEntity);
        return template.evaluate();
    }

    public static String addSubCollectionInstances(
        String parent,
        Map<String, String> subCollections
    )
    {
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

    public static String delete(
        String url,
        String bodyType,
        DetailedLink link,
        String resourceName
    )
    {
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

        Map<String, String> values = new LinkedHashMap<>();
        values.put("url", url);
        values.put("body_type", bodyType);
        values.put("resource_name_lc", resourceName.toLowerCase());
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
            values.put("docs", Documentation.document(link, new LinkedHashMap<String, String>(), methodParams));

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

    public static String update(
        String url,
        String resourceName,
        DetailedLink link,
        Map<String, String> knownWrapperTypes
    )
    {
        String actualXmlEntity = knownWrapperTypes.get(resourceName.toLowerCase());

        Object[] result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        headersMethodParamsStr = !headersMethodParamsStr.isEmpty()? ", " + headersMethodParamsStr: "";

        ResourceUpdateTemplate template = new ResourceUpdateTemplate();
        template.set("url", url);
        template.set("resource_name_lc", resourceName.toLowerCase());
        template.set("docs", Documentation.document(link));
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("headers_method_params_str", headersMethodParamsStr);
        template.set("actual_self_name", actualXmlEntity != null? actualXmlEntity: resourceName);

        return template.evaluate();
    }

    public static String action(
        String url,
        String bodyType,
        DetailedLink link,
        String actionName,
        String resourceNameLc,
        HttpMethod method,
        Map<String, String> actionParams
    )
    {
        Object[] result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        headersMethodParamsStr = !headersMethodParamsStr.isEmpty()?
            ", " + headersMethodParamsStr:
            headersMethodParamsStr;

        AbstractTemplate template = new ResourceActionTemplate();
        template.set("url", url);
        template.set("body_type", bodyType);
        template.set("body_type_lc", bodyType.toLowerCase());
        template.set("action_name", actionName.toLowerCase());
        template.set("method", method);
        template.set("resource_name_lc", resourceNameLc.toLowerCase());
        template.set("method_params",  addMethodParams(actionParams.keySet()));
        template.set("action_params", addActionParams(actionParams));
        template.set("docs", Documentation.document(link));
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("headers_method_params_str", headersMethodParamsStr);

        return template.evaluate();
    }

    public static String addActionParams(
        Map<String, String> actionParams
    )
    {
        StringBuilder buffer = new StringBuilder();
        for (Map.Entry<String, String> entry : actionParams.entrySet()) {
            String k = entry.getKey();
            String v = entry.getValue();
            buffer.append("        action.");
            buffer.append(k);
            buffer.append("=");
            buffer.append(v);
            buffer.append("\n");
        }
        return buffer.toString();
    }

    public static String addMethodParams(
        Set<String> params
    )
    {
        StringBuilder buffer = new StringBuilder();
        for (String item : params) {
            buffer.append(", ");
            buffer.append(item);
        }
        return buffer.toString();
    }
}
