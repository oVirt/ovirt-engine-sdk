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

package org.ovirt.engine.sdk.generator.utils;

import static org.ovirt.engine.sdk.generator.utils.CollectionsUtils.setOf;

import java.util.Set;

import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.entities.Header;

public class HeaderUtils {
    private static final Set<String> HEADERS_EXCLUDE = setOf(
        "Content-Type",
        "Filter"
    );

    public static String[] generateMethodParams(DetailedLink link) {
        String paramsStr = "";
        String headersStr = "";
        if (link.isSetRequest() && link.getRequest().isSetHeaders()) {
            for (Header headerParameter : link.getRequest().getHeaders().getHeaders()) {
                if (!HEADERS_EXCLUDE.contains(headerParameter.getName())) {
                    String headerName = headerParameter.getName().toLowerCase().replace("-", "_");
                    if (headerParameter.isRequired()) {
                        paramsStr += headerName + ", ";
                    }
                    else {
                        paramsStr += headerName + "=None, ";
                    }
                    headersStr += ", \"" + headerParameter.getName() + "\":" + headerParameter.getName().toLowerCase().replace("-", "_");
                }
            }
            if (!headersStr.isEmpty()) {
                headersStr = headersStr.substring(2);
            }
        }
        String[] result = new String[2];
        result[0] = !paramsStr.isEmpty()? paramsStr.substring(0, paramsStr.length() - 2): paramsStr;
        result[1] = "{" + headersStr + "}";
        return result;
    }
}
