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

import java.util.LinkedHashMap;
import java.util.Map;

import org.ovirt.engine.sdk.generator.rsdl.templates.CollectionGetCapabilitiesTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.CollectionGetDisksTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.CollectionListCapabilitiesTemplate;
import org.ovirt.engine.sdk.entities.DetailedLink;

public class CollectionExceptions {
    public static String get(
        String url,
        DetailedLink link,
        String prmsStr,
        Map<String, String> methodParams,
        Map<String, String> urlParams,
        String headersMethodParamsStr, String headersMapParamsStr,
        Map<String, String> collectionGetTemplateValues
    )
    {
        // Capabilities resource has unique structure which is not
        // fully comply with RESTful collection pattern, but preserved
        // in sake of backward compatibility
        if (url.equals("capabilities")) {
            CollectionGetCapabilitiesTemplate template = new CollectionGetCapabilitiesTemplate();
            return template.evaluate();
        }

        if (url.equals("disks")) {
            Map<String, String> docsParams = new LinkedHashMap<>();
            docsParams.put("id   : string (the id of the entity)", "False");
            docsParams.put("alias: string (the alias of the entity)", "False");
            String docs = Documentation.document(link, docsParams, new LinkedHashMap<String, String>());
            collectionGetTemplateValues.put("docs", docs);
            collectionGetTemplateValues.put("headers_method_params_str", headersMethodParamsStr);
            collectionGetTemplateValues.put("headers_map_params_str", headersMapParamsStr);
            CollectionGetDisksTemplate template = new CollectionGetDisksTemplate();
            template.set(collectionGetTemplateValues);
            return template.evaluate();
        }

        return "";

    }

    public static String list() {
        CollectionListCapabilitiesTemplate template = new CollectionListCapabilitiesTemplate();
        return template.evaluate();
    }
}
