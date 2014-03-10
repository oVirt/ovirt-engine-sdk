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

import org.ovirt.engine.sdk.generator.rsdl.templates.CollectionAddTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.CollectionGetNotSearchableTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.CollectionGetSearchableTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.CollectionListNotSearchableTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.CollectionListSearchableTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.CollectionTemplate;
import org.ovirt.engine.sdk.generator.templates.AbstractTemplate;
import org.ovirt.engine.sdk.generator.utils.HeaderUtils;
import org.ovirt.engine.sdk.generator.utils.ParamUtils;
import org.ovirt.engine.sdk.generator.utils.ParamsContainer;
import org.ovirt.engine.sdk.generator.xsd.XsdData;
import org.ovirt.engine.sdk.entities.DetailedLink;

public class Collection {
    public static String collection(String collectionName) {
        CollectionTemplate template = new CollectionTemplate();
        template.set("collection_name", collectionName);
        return template.evaluate();
    }

    public static String get(
        String url,
        String resourceType,
        DetailedLink link,
        Map<String, String> knownWrapperTypes
    )
    {
        String actualResourceType = knownWrapperTypes.get(resourceType.toLowerCase());
        String actualResourceNameLc = XsdData.getInstance().getXmlTypeInstance(resourceType.toLowerCase()).toLowerCase();

        Object[] result = ParamUtils.getMethodParamsByUrlParamsMeta(link);
        String prmsStr = (String) result[0];
        Map<String, String> methodParams = (Map) result[1];
        Map<String, String> urlParams = (Map) result[2];

        result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        if (!headersMethodParamsStr.isEmpty()) {
            headersMethodParamsStr += ", ";
        }

        Map<String, String> values = new LinkedHashMap<>();
        values.put("url", url);
        values.put("resource_name_lc", actualResourceNameLc);
        values.put("headers_method_params_str", headersMethodParamsStr);
        values.put("headers_map_params_str", headersMapParamsStr);
        values.put("resource_type", actualResourceType != null ? actualResourceType : resourceType);

        Map<String, String> docsParams = new LinkedHashMap<>();
        docsParams.put(ParamsContainer.ID_SEARCH_PARAM, "False");
        docsParams.put(ParamsContainer.NAME_SEARCH_PARAM, "False");
        String docs = Documentation.document(link, docsParams, new LinkedHashMap<String, String>());
        values.put("docs", docs);

        // Capabilities resource has unique structure which is not
        // fully comply with RESTful collection pattern, but preserved
        // in sake of backward compatibility
        if (url.equals("/capabilities")) {
            return CollectionExceptions.get(
                url,
                link,
                prmsStr,
                methodParams,
                urlParams,
                headersMethodParamsStr,
                headersMapParamsStr,
                values
            );
        }

        // /disks search-by-name paradigm was broken by the engine
        // should be fixed later on
        if (url.equals("/disks")) {
            return CollectionExceptions.get(
                url,
                link,
                prmsStr,
                methodParams,
                urlParams,
                headersMethodParamsStr,
                headersMapParamsStr,
                values
            );
        }

        AbstractTemplate template;
        if (urlParams.containsKey("search:query")) {
            template = new CollectionGetSearchableTemplate();
        }
        else {
            template = new CollectionGetNotSearchableTemplate();
        }

        template.set(values);
        return template.evaluate();
    }

    public static String list(
        String url,
        String resourceType,
        DetailedLink link,
        Map<String,
        String> knownWrapperTypes
    )
    {
        String actualResourceType = knownWrapperTypes.get(resourceType.toLowerCase());
        String actualResourceNameLc = XsdData.getInstance().getXmlTypeInstance(resourceType.toLowerCase()).toLowerCase();

        Object[] result = ParamUtils.getMethodParamsByUrlParamsMeta(link);
        String prmsStr = (String) result[0];
        Map<String, String> methodParams = (Map<String, String>) result[1];
        Map<String, String> urlParams = (Map<String, String>) result[2];

        result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        Map<String, String> methodParamsCopy = new LinkedHashMap<>(methodParams);
        methodParams.put("**kwargs", "**kwargs");

        Map<String, String> values = new LinkedHashMap<>();
        values.put("url", url);
        values.put("resource_name_lc", actualResourceNameLc);
        values.put("resource_type", actualResourceType != null ? actualResourceType : resourceType);

        // Capabilities resource has unique structure which is not
        // fully comply with RESTful collection pattern, but preserved
        // in sake of backward compatibility
        if (url.equals("/capabilities")) {
            return CollectionExceptions.list();
        }
        else if (!prmsStr.isEmpty() || !headersMethodParamsStr.isEmpty()) {
            String combinedMethodParams = prmsStr + (
                !prmsStr.isEmpty() && !headersMethodParamsStr.isEmpty()? ", ": ""
                ) + headersMethodParamsStr;

            Map<String, String> docsParams = new LinkedHashMap<>();
            docsParams.put(ParamsContainer.KWARGS_PARAMS, "False");
            docsParams.put(ParamsContainer.QUERY_PARAMS, "False");
            String docs = Documentation.document(link, docsParams, methodParams);
            values.put("docs", docs);

            values.put("url_params",
                ParamUtils.toDictStr(
                    urlParams.keySet(),
                    methodParamsCopy.keySet()
                )
            );

            values.put("headers_map_params_str", headersMapParamsStr);
            values.put("combined_method_params", combinedMethodParams);

            CollectionListSearchableTemplate template = new CollectionListSearchableTemplate();
            template.set(values);
            return template.evaluate();
        }
        else {
            Map<String, String> docsParams = new LinkedHashMap<>();
            docsParams.put(ParamsContainer.KWARGS_PARAMS, "False");
            String docs = Documentation.document(link, docsParams, new LinkedHashMap<String, String>());
            values.put("docs", docs);

            CollectionListNotSearchableTemplate template = new CollectionListNotSearchableTemplate();
            template.set(values);
            return template.evaluate();
        }
    }

    public static String add(
        String url,
        String bodyType,
        String responseType,
        DetailedLink link,
        Map<String, String> knownWrapperTypes
    )
    {
        String actualResourceType = knownWrapperTypes.get(responseType.toLowerCase());

        String[] result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = result[0];
        String headersMapParamsStr = result[1];

        headersMethodParamsStr = !headersMethodParamsStr.isEmpty()?
            ", " + headersMethodParamsStr:
            headersMethodParamsStr;

        CollectionAddTemplate template = new CollectionAddTemplate();
        template.set("url", url);
        template.set("resource_to_add_lc", bodyType.toLowerCase());
        template.set("headers_method_params_str", headersMethodParamsStr);
        template.set("docs", Documentation.document(link));
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("resource_type", firstNotNull(actualResourceType, responseType));

        return template.evaluate();
    }
}
