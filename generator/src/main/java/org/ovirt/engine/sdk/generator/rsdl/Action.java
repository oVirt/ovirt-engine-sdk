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

package org.ovirt.engine.sdk.generator.rsdl;

import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.generator.rsdl.templates.ResourceActionTemplate;
import org.ovirt.engine.sdk.generator.templates.AbstractTemplate;
import org.ovirt.engine.sdk.generator.utils.HeaderUtils;
import org.ovirt.engine.sdk.generator.utils.Tree;
import org.ovirt.engine.sdk.generator.utils.UrlUtils;

public class Action {
    public static String action(Tree<Location> destinationTree, DetailedLink link, String entityName, String actionName) {
        Object[] result = HeaderUtils.generateMethodParams(link);
        String headersMethodParamsStr = (String) result[0];
        String headersMapParamsStr = (String) result[1];

        headersMethodParamsStr = !headersMethodParamsStr.isEmpty()?
            ", " + headersMethodParamsStr:
            headersMethodParamsStr;

        AbstractTemplate template = new ResourceActionTemplate();
        template.set("url", link.getHref());
        template.set("action_name", actionName.toLowerCase());
        template.set("method", link.getRequest().getHttpMethod().toString());
        template.set("resource_name", entityName);
        template.set("docs", Documentation.document(link));
        template.set("headers_map_params_str", headersMapParamsStr);
        template.set("headers_method_params_str", headersMethodParamsStr);
        template.set("url_params",
            UrlUtils.generateUrlIdentifiersReplacements(
                destinationTree,
                "                "
            )
        );

        return template.evaluate();
    }
}
