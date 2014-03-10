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

import org.ovirt.engine.sdk.generator.rsdl.templates.SubCollectionAddTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubCollectionGetTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubCollectionListTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubCollectionListWithParamsTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.SubCollectionTemplate;
import org.ovirt.engine.sdk.generator.templates.AbstractTemplate;
import org.ovirt.engine.sdk.generator.utils.HeaderUtils;
import org.ovirt.engine.sdk.generator.utils.ParamUtils;
import org.ovirt.engine.sdk.generator.utils.UrlUtils;
import org.ovirt.engine.sdk.generator.xsd.XsdData;
import org.ovirt.engine.sdk.entities.DetailedLink;

public class SubCollection {
    public static String collection(
        String subCollectionName,
        String parentResourceNameLc
    )
    {
        SubCollectionTemplate template = new SubCollectionTemplate();
        template.set("sub_collection_name", subCollectionName);
        template.set("parent_resource_name_lc", parentResourceNameLc.toLowerCase());
        return template.evaluate();
    }

    public static String get(
        String url,
        DetailedLink link,
        String parentResourceNameLc,
        String encapsulatingResource,
        String actualResourceNameCandidate,
        Map<String, String> knownWrapperTypes,
        Map<String, String> namingEntityExceptions
    )
    {
        String actualEncapsulatingResource = knownWrapperTypes.get(encapsulatingResource.toLowerCase());

        String actualResourceNameLc = XsdData.getInstance().getXmlTypeInstance(
            actualEncapsulatingResource != null? actualEncapsulatingResource: actualResourceNameCandidate
        ).toLowerCase();

        if (namingEntityExceptions.containsKey(actualResourceNameLc)) {
            actualResourceNameLc = namingEntityExceptions.get(actualResourceNameLc);
        }

        String[] result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamStr = result[0];
        String headersMapParamsStr = result[1];

        headersMethodParamStr = !headersMethodParamStr.isEmpty()? headersMethodParamStr + ", ": headersMethodParamStr;

        SubCollectionGetTemplate template = new SubCollectionGetTemplate();
        template.set("url", url);
        template.set("parent_resource_name_lc", parentResourceNameLc.toLowerCase());
        template.set("resource_name_lc", encapsulatingResource.toLowerCase());
        template.set("actual_resource_name_lc", actualResourceNameLc);
        template.set("headers_method_params_str", headersMethodParamStr);
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("url_params_id",
            UrlUtils.generateUrlIdentifiersReplacements(
                link,
                "                            ",
                true,
                true
            )
        );
        template.set("url_params_name",
            UrlUtils.generateUrlIdentifiersReplacements(
                link,
                "                    ",
                true,
                true
            )
        );
        template.set("encapsulating_resource", actualEncapsulatingResource != null? actualEncapsulatingResource: encapsulatingResource);

        Map<String, String> docsParams = new LinkedHashMap<>();
        docsParams.put("id  : string (the id of the entity)", "False");
        docsParams.put("name: string (the name of the entity)", "False");
        String docs = Documentation.document(link, docsParams, new LinkedHashMap<String, String>());
        template.set("docs", docs);

        return template.evaluate();
    }

    public static String list(
        String url,
        DetailedLink link,
        String parentResourceNameLc,
        String encapsulatingResource,
        String actualResourceNameCandidate,
        Map<String, String> knownWrapperTypes,
        Map<String, String> namingEntityExceptions
    )
    {
        String actualEncapsulatingResource = knownWrapperTypes.get(encapsulatingResource.toLowerCase());

        String actualResourceNameLc = XsdData.getInstance().getXmlTypeInstance(
            actualEncapsulatingResource != null? actualEncapsulatingResource: actualResourceNameCandidate.toLowerCase()
        ).toLowerCase();

        if (namingEntityExceptions.containsKey(actualResourceNameLc)) {
            actualResourceNameLc = namingEntityExceptions.get(actualResourceNameLc);
        }

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
        values.put("url", url);
        values.put("parent_resource_name_lc", parentResourceNameLc.toLowerCase());
        values.put("actual_resource_name_lc", actualResourceNameLc);
        values.put("combined_method_params", combinedMethodParams);
        values.put("headers_map_params_str", headersMapParamsStr);
        values.put("encapsulating_resource", firstNotNull(actualEncapsulatingResource, encapsulatingResource));
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
                    link,
                    "                ",
                    true,
                    true
                )
            );
            template = new SubCollectionListWithParamsTemplate();
        }
        else {
            Map<String, String> customParams = new LinkedHashMap<>();
            customParams.put("**kwargs: dict (property based filtering)\"", "False");
            String docs = Documentation.document(link, customParams, new LinkedHashMap<String, String>());
            values.put("docs", docs);
            values.put("url_params",
                UrlUtils.generateUrlIdentifiersReplacements(
                    link,
                    "                ",
                    true,
                    true
                )
            );
            template = new SubCollectionListTemplate();
        }

        template.set(values);
        return template.evaluate();
    }

    public static String add(
        String url,
        DetailedLink link,
        String bodyType,
        String parentResourceNameLc,
        String encapsulatingEntity,
        Map<String, String> knownWrapperTypes
    )
    {
        String actualEncapsulatingEntity = knownWrapperTypes.get(encapsulatingEntity.toLowerCase());

        String[] result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamStr = result[0];
        String headersMapParamsStr = result[1];

        headersMethodParamStr = !headersMethodParamStr.isEmpty()?
            ", " + headersMethodParamStr:
            headersMethodParamStr;

        SubCollectionAddTemplate template = new SubCollectionAddTemplate();
        template.set("resource_to_add", bodyType.toLowerCase());
        template.set("url", url);
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("headers_method_params_str", headersMethodParamStr);
        template.set("parent_resource_name_lc", parentResourceNameLc.toLowerCase());
        template.set("encapsulating_entity", firstNotNull(actualEncapsulatingEntity, encapsulatingEntity));
        template.set("docs", Documentation.document(link));
        template.set("url_params",
            UrlUtils.generateUrlIdentifiersReplacements(
                link,
                "                ",
                true,
                true
            )
        );

        return template.evaluate();
    }
}
