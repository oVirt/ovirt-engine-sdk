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

import static org.ovirt.engine.sdk.generator.utils.StringUtils.firstNotNull;

import java.util.LinkedHashMap;
import java.util.Map;

import org.ovirt.engine.sdk.generator.rsdl.templates.SubResourceActionTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubResourceCollectionActionTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubResourceDeleteTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubResourceDeleteWithBodyTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubResourceDeleteWithUrlParamsAndBodyTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubResourceDeleteWithUrlParamsTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubResourceTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubResourceUpdateTemplate;
import org.ovirt.engine.sdk.generator.templates.AbstractTemplate;
import org.ovirt.engine.sdk.generator.utils.HeaderUtils;
import org.ovirt.engine.sdk.generator.utils.ParamUtils;
import org.ovirt.engine.sdk.generator.utils.UrlUtils;
import org.ovirt.engine.sdk.generator.xsd.XsdData;
import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.entities.HttpMethod;

public class SubResource {
    public static String resource(
        String subResType,
        String encapsulatingEntity,
        String parent,
        Map<String, String> knownWrapperTypes
    )
    {
        String actualXmlEntity = knownWrapperTypes.get(encapsulatingEntity.toLowerCase());

        String actualXmlType = XsdData.getInstance().getXmlType(encapsulatingEntity);

        String actualSubResType = knownWrapperTypes.get(subResType.toLowerCase());

        SubResourceTemplate template = new SubResourceTemplate();
        template.set("encapsulating_entity", firstNotNull(actualSubResType, subResType));
        template.set("sub_res_type", firstNotNull(actualSubResType, actualXmlEntity, actualXmlType, encapsulatingEntity));
        template.set("parent", parent.toLowerCase());
        template.set("encapsulated_entity", encapsulatingEntity.toLowerCase());
        template.set("fixme", Resource.SUB_COLLECTIONS_FIXME);
        return template.evaluate();
    }

    public static String action(
        String url,
        DetailedLink link,
        String actionName,
        String parentResourceNameLc,
        String bodyType,
        String resourceNameLc,
        HttpMethod method,
        Map<String, String> actionParams,
        boolean collectionAction
    )
    {
        String[] result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = result[0];
        String headersMapParamsStr = result[1];

        headersMethodParamsStr = !headersMethodParamsStr.isEmpty()?
            ", " + headersMethodParamsStr:
            headersMethodParamsStr;

        Map<String, String> values = new LinkedHashMap<>();
        values.put("url", url);
        values.put("action_name", actionName);
        values.put("method", method.toString());
        values.put("parent_resource_name_lc", parentResourceNameLc.toLowerCase());
        values.put("body_type", bodyType);
        values.put("body_type_lc", bodyType.toLowerCase());
        values.put("headers_map_params_str", headersMapParamsStr);
        values.put("headers_method_params_str", headersMethodParamsStr);
        values.put("resource_name_lc", resourceNameLc.toLowerCase());
        values.put("docs", Documentation.document(link));
        values.put("add_method_params", Resource.addMethodParams(actionParams.keySet()));
        values.put("add_action_parans", Resource.addActionParams(actionParams));
        values.put("url_params",
            UrlUtils.generateUrlIdentifiersReplacements(
                link,
                "                ",
                true,
                false
            )
        );

        AbstractTemplate template;
        if (collectionAction) {
            template = new SubResourceCollectionActionTemplate();
        }
        else {
            template = new SubResourceActionTemplate();
        }

        template.set(values);
        return template.evaluate();
    }

    public static String update(
        String url,
        DetailedLink link,
        String parentResourceNameLc,
        String resourceName,
        String returnedType,
        Map<String, String> knownWrapperTypes
    )
    {
        String combinedMethodParams = "";

        String actualXmlEntity = knownWrapperTypes.get(returnedType.toLowerCase());

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
            link,
            "            ",
            true,
            false
        );

        SubResourceUpdateTemplate template = new SubResourceUpdateTemplate();
        template.set("url", url);
        template.set("parent_resource_name_lc", parentResourceNameLc.toLowerCase());
        template.set("resource_name", resourceName);
        template.set("resource_name_lc", resourceName.toLowerCase());
        template.set("url_identifiers_replacments", urlIdentifiersReplacements);
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("combined_method_params", combinedMethodParams);
        template.set("url_params_separator", !urlParamsStr.isEmpty()? ", " + urlParamsStr: "");
        template.set("docs", Documentation.document(link, new LinkedHashMap<String, String>(), methodParams));
        template.set("returned_type", actualXmlEntity != null? actualXmlEntity: returnedType);

        return template.evaluate();
    }

    public static String delete(
        String url,
        DetailedLink link,
        String parentResourceNameLc,
        String resourceNameLc,
        String bodyType
    )
    {
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

        Map<String, String> values = new LinkedHashMap<>();
        values.put("url", url);
        values.put("body_type_lc", bodyType != null ? bodyType.toLowerCase() : null);
        values.put("parent_resource_name_lc", parentResourceNameLc.toLowerCase());
        values.put("headers_map_params_str_with_no_ct", headersMapParamsStrWithNoCt);
        values.put("combined_method_params", combinedMethodParams);
        values.put("resource_name_lc", resourceNameLc.toLowerCase());
        values.put("body_instance_str", bodyInstanceStr);
        values.put("headers_map_params_str", headersMapParamsStr);
        values.put("url_params", ParamUtils.toDictStr(urlParams.keySet(), methodParams.keySet()));

        AbstractTemplate templateWithBody;
        AbstractTemplate templateWithoutBody;
        if (!prmsStr.isEmpty() || !headersMethodParamsStr.isEmpty()) {
            values.put("docs", Documentation.document(link, new LinkedHashMap<String, String>(), methodParams));
            values.put("url_identifyiers",
                UrlUtils.generateUrlIdentifiersReplacements(
                    link,
                    "            ",
                    false,
                    false
                )
            );

            templateWithBody = new SubResourceDeleteWithUrlParamsAndBodyTemplate();
            templateWithoutBody = new SubResourceDeleteWithUrlParamsTemplate();
        }
        else {
            values.put("docs", Documentation.document(link));
            values.put("url_identifyiers",
                UrlUtils.generateUrlIdentifiersReplacements(
                    link,
                    "                ",
                    true,
                    false
                )
            );
            values.put("url_identifyiers_with_body",
                UrlUtils.generateUrlIdentifiersReplacements(
                    link,
                    "                                                               ",
                    false,
                    false
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
