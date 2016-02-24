//
// Copyright (c) 2015 Red Hat, Inc.
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
import java.util.Map;

import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.generator.Location;
import org.ovirt.engine.sdk.generator.python.templates.ResourceActionTemplate;
import org.ovirt.engine.sdk.generator.python.utils.HeaderUtils;
import org.ovirt.engine.sdk.generator.python.utils.ParamUtils;
import org.ovirt.engine.sdk.generator.python.utils.UrlUtils;
import org.ovirt.engine.sdk.generator.templates.AbstractTemplate;
import org.ovirt.engine.sdk.generator.utils.Tree;

public class Action {
    public static String action(Tree<Location> destinationTree, DetailedLink link, String entityName, String actionName) {
        Object[] result = ParamUtils.getMethodParamsByUrlParamsMeta(link);
        String prmsStr = (String) result[0];
        Map<String, String> methodParams = (Map<String, String>) result[1];
        Map<String, String> urlParams = (Map<String, String>) result[2];

        result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        StringBuilder combinedMethodParams = new StringBuilder();
        if (!headersMethodParamsStr.isEmpty()) {
            combinedMethodParams.append(", ");
            combinedMethodParams.append(headersMethodParamsStr);
        }
        if (!prmsStr.isEmpty()) {
            combinedMethodParams.append(", ");
            combinedMethodParams.append(prmsStr);
        }

        AbstractTemplate template = new ResourceActionTemplate();
        template.set("action_name", actionName.toLowerCase());
        template.set("url", link.getHref());
        template.set("method", link.getRequest().getHttpMethod().toString());
        template.set("resource_name", entityName);
        template.set("url_query_params", ParamUtils.toDictStr(urlParams.keySet(), methodParams.keySet()));
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("combined_method_params", combinedMethodParams);
        template.set("docs", Documentation.document(link, Collections.emptyMap(), methodParams));
        template.set("url_params",
            UrlUtils.generateUrlIdentifiersReplacements(
                destinationTree,
                "                    "
            )
        );

        return template.evaluate();
    }
}
