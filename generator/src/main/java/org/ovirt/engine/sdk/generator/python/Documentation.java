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

import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.entities.Header;
import org.ovirt.engine.sdk.entities.Parameter;
import org.ovirt.engine.sdk.entities.ParametersSet;

public class Documentation {
    private static final String DOC_OFFSET = "        ";
    private static final String OVERLOAD_TEMPLATE = "Overload";

    private static final Set<String> HEADERS_EXCLUDE = new HashSet<>();

    static {
        HEADERS_EXCLUDE.add("Content-Type");
        HEADERS_EXCLUDE.add("Filter");
    }

    public static String document(DetailedLink link) {
        return document(link, new LinkedHashMap<>(), new LinkedHashMap<>());
    }

    public static String document(
        DetailedLink link,
        Map<String, String> customParams,
        Map<String, String> mapper
    )
    {
        int i = 0;
        String offset = DOC_OFFSET;

        String docStr = "";
        String docStrIn = offset + "'''\n";
        String docStrOut = offset + "'''\n";

        String typeDoc = offset + String.format("@type %s:\n\n", getRequestType(link));
        String returnDoc = offset + String.format("@return %s:\n", getResponseType(link));

        String parametersSetTemplate = offset + OVERLOAD_TEMPLATE + " %s:\n";
        String parametersSetOffset = "  ";
        String collectionParametersSetOffset = "  ";
        String mandParamDocTemplate = "@param %s: %s\n";
        String optParamDocTemplate = "[@param %s: %s]\n";
        String mandIvarDocTEmplate = "@ivar %s: %s\n";
        String optIvarDocTemplate = "[@ivar %s: %s]\n";

        String customMandParamDocTemplate = "@param %s\n";
        String customOptParamDocTemplate = "[@param %s]\n";

        docStr += docStrIn;
        docStr += typeDoc.indexOf("@type None:") == -1? typeDoc: "";
        if (link.isSetRequest() && link.getRequest().isSetBody() && link.getRequest().getBody().isSetParametersSets()) {
            for (ParametersSet parametersSet : link.getRequest().getBody().getParametersSets()) {
                String mandParams = "";
                String optParams = "";
                String[] result;
                if (link.getRequest().getBody().getParametersSets().size() > 1) {
                    i += 1;
                    docStr += String.format(parametersSetTemplate, i);
                    result = doDocSubResource(
                        mandParams,
                        optParams,
                        parametersSet,
                        offset,
                        collectionParametersSetOffset,
                        parametersSetOffset,
                        mandParamDocTemplate,
                        optParamDocTemplate,
                        mandIvarDocTEmplate,
                        optIvarDocTemplate
                    );
                }
                else {
                    result = doDocResource(
                        parametersSet,
                        mandParams,
                        optParams,
                        offset,
                        collectionParametersSetOffset,
                        mandParamDocTemplate,
                        optParamDocTemplate,
                        mandIvarDocTEmplate,
                        optIvarDocTemplate
                    );
                }
                mandParams = result[0];
                optParams = result[1];
                docStr += mandParams;
                docStr += optParams;
            }
        }

        for (Map.Entry<String, String> entry : customParams.entrySet()) { // TODO: revisit - not optimal in terms of overload
            String k = entry.getKey();
            if (mapper.isEmpty() || isMapperHasKey(mapper, k)) {
                if (customParams.get(k).equalsIgnoreCase("true")) {
                    docStr += offset + String.format(customMandParamDocTemplate, k);
                }
                else {
                    docStr += offset + String.format(customOptParamDocTemplate, k);
                }
            }
        }

        for (Map.Entry<String, String> entry : mapper.entrySet()) {
            String k = entry.getKey();
            String v = entry.getValue();
            if (docStr.indexOf(k + ":") == -1) {
                docStr += offset + String.format(optParamDocTemplate, k, v);
            }
        }

        // Document HTTP header parameters:
        if (link.isSetRequest() && link.getRequest().isSetHeaders()) {
            for (Header headerParameter : link.getRequest().getHeaders().getHeaders()) {
                String headerName = headerParameter.getName().toLowerCase().replace("-", "_");
                if (!HEADERS_EXCLUDE.contains(headerParameter.getName())) {
                    if (headerParameter.isRequired()) {
                        docStr += DOC_OFFSET + String.format(mandParamDocTemplate, headerName, headerParameter.getValue());
                    }
                    else {
                        docStr += DOC_OFFSET + String.format(optParamDocTemplate, headerName, headerParameter.getValue());
                    }
                }
            }
        }

        docStr += !docStr.equals(offset + "'''\n")? "\n" + returnDoc: returnDoc;

        docStr += docStrOut;

        return docStr;
    }

    private static String[] doDocResource(
        ParametersSet parametersSet,
        String mandParams,
        String optParams,
        String offset,
        String collectionParametersSetOffset,
        String mandParamDocTemplate,
        String optParamDocTemplate,
        String mandIvarDocTEmplate,
        String optIvarDocTemplate
    )
    {
        for (Parameter parameter : parametersSet.getParameters()) {
            if (parameter.getType().equals("collection")) {
                if (parameter.isSetParametersSet() && parameter.getParametersSet().isSetParameters()) {
                    if (parameter.isRequired()) {
                        mandParams +=
                            offset +
                            String.format(
                                mandParamDocTemplate,
                                parameter.getName(),
                                parameter.getType().replace("xs:", "")
                            );
                        mandParams +=
                            offset +
                            "{\n";
                    }
                    else {
                        optParams +=
                            offset +
                            String.format(
                                optParamDocTemplate,
                                parameter.getName(),
                                parameter.getType().replace("xs:", "")
                            );
                        optParams +=
                            offset +
                            "{\n";
                    }
                }
                for (Parameter collectionParameter : parameter.getParametersSet().getParameters()) {
                    if (parameter.isRequired()) {
                        mandParams +=
                            offset +
                            collectionParametersSetOffset +
                            String.format(
                                mandIvarDocTEmplate,
                                collectionParameter.getName(),
                                collectionParameter.getType().replace("xs:", "")
                            );
                    }
                    else {
                        optParams +=
                            offset +
                            collectionParametersSetOffset +
                            String.format(
                                optIvarDocTemplate,
                                collectionParameter.getName(),
                                collectionParameter.getType().replace("xs:", "")
                            );
                    }
                    if (collectionParameter.getType().equals("collection")) {
                        if (parameter.isRequired()) {
                            mandParams += offset + collectionParametersSetOffset + "{\n";
                        }
                        else {
                            optParams += offset + collectionParametersSetOffset + "{\n";
                        }
                        String[] result = doDocResource(
                            collectionParameter.getParametersSet(),
                            mandParams,
                            optParams,
                            offset + collectionParametersSetOffset + collectionParametersSetOffset,
                            collectionParametersSetOffset,
                            mandParamDocTemplate,
                            optParamDocTemplate,
                            mandIvarDocTEmplate,
                            optIvarDocTemplate
                        );
                        mandParams = result[0];
                        optParams = result[1];

                        if (parameter.isRequired()) {
                            mandParams += offset + collectionParametersSetOffset + "}\n";
                        }
                        else {
                            optParams += offset + collectionParametersSetOffset + "}\n";
                        }
                    }
                }
                if (parameter.isRequired()) {
                    mandParams += offset + "}\n";
                }
                else {
                    optParams += offset + "}\n";
                }
            }
            else {
                if (parameter.isRequired()) {
                    mandParams +=
                        offset +
                        String.format(
                            mandParamDocTemplate,
                            parameter.getName(),
                            parameter.getType().replace("xs:", "")
                        );
                }
                else {
                    optParams +=
                        offset +
                        String.format(
                            optParamDocTemplate,
                            parameter.getName(),
                            parameter.getType().replace("xs:", "")
                        );
                }
            }
        }

        String[] result = new String[2];
        result[0] = mandParams;
        result[1] = optParams;
        return result;
    }

    private static boolean isMapperHasKey(Map<String, String> mapper, String k) {
        if (mapper != null && mapper.size() > 0) {
            for (String key : mapper.keySet()) {
                if (k.startsWith(key + ":")) {
                    return true;
                }
            }
        }
        return false;
    }

    private static String[] doDocSubResource(
        String mandParams,
        String optParams,
        ParametersSet parametersSet,
        String offset,
        String collectionParametersSetOffset,
        String parametersSetOffset,
        String mandParamDocTemplate,
        String optParamDocTemplate,
        String mandIvarDocTEmplate,
        String optIvarDocTemplate
    )
    {
        for (Parameter parameter : parametersSet.getParameters()) {
            if (parameter.getType().equals("collection")) {
                if (parameter.isSetParametersSet() && parameter.getParametersSet().isSetParameters()) {
                    if (parameter.isRequired()) {
                        mandParams +=
                            offset +
                            collectionParametersSetOffset +
                            String.format(
                                mandParamDocTemplate,
                                parameter.getName(),
                                parameter.getType().replace("xs:", "")
                            );
                        mandParams +=
                            offset +
                            parametersSetOffset +
                            "{\n";
                    }
                    else {
                        optParams +=
                            offset +
                            collectionParametersSetOffset +
                            String.format(
                                optParamDocTemplate,
                                parameter.getName(),
                                parameter.getType().replace("xs:", "")
                            );
                        optParams +=
                            offset +
                            parametersSetOffset +
                            "{\n";
                    }

                    for (Parameter collectionParameter : parameter.getParametersSet().getParameters()) {
                        if (parameter.isRequired()) {
                            mandParams +=
                                offset +
                                parametersSetOffset +
                                collectionParametersSetOffset +
                                String.format(
                                    mandIvarDocTEmplate,
                                    collectionParameter.getName(),
                                    collectionParameter.getType().replace("xs:", "")
                                );
                        }
                        else {
                            optParams +=
                                offset +
                                parametersSetOffset +
                                collectionParametersSetOffset +
                                String.format(
                                    optIvarDocTemplate,
                                    collectionParameter.getName(),
                                    collectionParameter.getType().replace("xs:", "")
                                );

                        }
                        if (collectionParameter.getType().equals("collection")) {
                            if (parameter.isRequired()) {
                                mandParams +=
                                    offset +
                                    collectionParametersSetOffset +
                                    parametersSetOffset +
                                    "{\n";
                            }
                            else {
                                optParams +=
                                    offset +
                                    collectionParametersSetOffset +
                                    parametersSetOffset +
                                    "{\n";
                            }

                            String[] result = doDocSubResource(
                                mandParams,
                                optParams,
                                collectionParameter.getParametersSet(),
                                offset + collectionParametersSetOffset + collectionParametersSetOffset,
                                collectionParametersSetOffset,
                                parametersSetOffset,
                                mandParamDocTemplate,
                                optParamDocTemplate,
                                mandIvarDocTEmplate,
                                optIvarDocTemplate
                            );
                            mandParams = result[0];
                            optParams = result[1];

                            if (parameter.isRequired()) {
                                mandParams +=
                                    offset +
                                    collectionParametersSetOffset +
                                    parametersSetOffset +
                                    "}\n";
                            }
                            else {
                                optParams +=
                                    offset +
                                    collectionParametersSetOffset +
                                    parametersSetOffset +
                                    "}\n";
                            }
                        }
                    }

                    if (parameter.isRequired()) {
                        mandParams +=
                            offset +
                            parametersSetOffset +
                            "}\n";
                    }
                    else {
                        optParams +=
                            offset +
                            parametersSetOffset +
                            "}\n";
                    }
                }
            }
            else {
                if (parameter.isRequired()) {
                    mandParams +=
                        offset +
                        parametersSetOffset +
                        String.format(
                            mandParamDocTemplate,
                            parameter.getName(),
                            parameter.getType().replace("xs:", "")
                        );
                }
                else {
                    optParams +=
                       offset +
                       parametersSetOffset +
                       String.format(
                           optParamDocTemplate,
                           parameter.getName(),
                           parameter.getType().replace("xs:", "")
                       );
                }
            }
        }

        String[] result = new String[2];
        result[0] = mandParams;
        result[1] = optParams;
        return result;
    }

    private static String getRequestType(DetailedLink link) {
        if (!link.getRel().equals("update") &&
            link.isSetRequest() &&
            link.getRequest().isSetBody() &&
            link.getRequest().getBody().isSetType()) {
            return link.getRequest().getBody().getType();
        }
        return "None";
    }

    private static String getResponseType(DetailedLink link) {
        if (link.isSetResponse() && link.getResponse().isSetType()) {
            return link.getResponse().getType();
        }
        return "None";
    }

}
