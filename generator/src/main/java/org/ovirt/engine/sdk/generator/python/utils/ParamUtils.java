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

package org.ovirt.engine.sdk.generator.python.utils;

import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Set;

import org.ovirt.engine.sdk.entities.DetailedLink;
import org.ovirt.engine.sdk.entities.Parameter;
import org.ovirt.engine.sdk.entities.ParametersSet;

public class ParamUtils {
    private static final Set<String> PRESERVED_NAMES = new HashSet<>();

    static {
        PRESERVED_NAMES.add("import");
        PRESERVED_NAMES.add("from");
    }

    public static Object[] getMethodParamsByUrlParamsMeta(DetailedLink link) {
        String methodParameters = "";
        LinkedHashMap<String, String> methodParams = new LinkedHashMap<>();
        LinkedHashMap<String, String> urlParams = new LinkedHashMap<>();

        if (link.isSetRequest() && link.getRequest().isSetUrl() && link.getRequest().getUrl().isSetParametersSets()
            && link.getRequest().getUrl().getParametersSets().size() > 0) {
            for (ParametersSet parametersSet : link.getRequest().getUrl().getParametersSets()) {
                for (Parameter param : parametersSet.getParameters()) {
                    if (param.getValue() == null) {
                        param.setValue("");
                    }
                    if (param.getValue().equals("search query")) {
                        param.setValue("query");
                    }
                    urlParams.put(param.getName() + ":" + param.getContext(), param.getValue());
                    String nameCandidate;
                    if (PRESERVED_NAMES.contains(param.getName())) {
                        nameCandidate = param.getName() + "_" + param.getValue();
                    }
                    else {
                        nameCandidate = param.getName();
                    }
                    if (nameCandidate.equals("search")) {
                        methodParameters += param.getValue() + "=None, ";
                        methodParams.put(param.getValue(), nameCandidate);
                    }
                    else {
                        if (param.getName().equals("case_sensitive")) {
                            methodParameters += nameCandidate + "=True, ";
                        }
                        else {
                            methodParameters += nameCandidate + "=None, ";
                        }
                        if (param.isSetType()) {
                            methodParams.put(nameCandidate, param.getType().replace("xs:", "") +
                                " (" + param.getValue() + ")");
                        }
                        else {
                            methodParams.put(nameCandidate, param.getValue());
                        }
                    }
                }
            }
        }

        // TODO: Obviously this needs to improve.
        Object[] result = new Object[3];
        result[0] = !methodParameters.isEmpty()? methodParameters.substring(0, methodParameters.length() - 2): methodParameters;
        result[1] = methodParams;
        result[2] = urlParams;
        return result;
    }

    public static String toDictStr(Set<String> names, Set<String> values) {
        StringBuilder buffer = new StringBuilder();
        if (names.size() == values.size()) {
            buffer.append("{");
            boolean first = true;
            Iterator<String> i = names.iterator();
            Iterator<String> j = values.iterator();
            while (i.hasNext() && j.hasNext()) {
                String name = i.next();
                String value = j.next();
                if (!first) {
                    buffer.append(",");
                }
                buffer.append("'");
                buffer.append(name);
                buffer.append("':");
                buffer.append(value);
                first = false;
            }
            buffer.append("}");
        }
        return buffer.toString();
    }

    /**
     * Returns body instance if param is optional.
     */
    public static String getBodyInstance(DetailedLink link) {
        if (link.isSetRequest() &&
            link.getRequest().isSetBody() &&
            link.getRequest().getBody().isRequired() != null &&
            link.getRequest().getBody().isSetType()) {
            if (!link.getRequest().getBody().isRequired()) {
                return "params." + link.getRequest().getBody().getType() + "()";
            }
        }
        return "";
    }
}
