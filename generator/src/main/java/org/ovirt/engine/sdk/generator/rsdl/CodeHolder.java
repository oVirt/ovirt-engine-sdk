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

public class CodeHolder {
    private Map<String, String> subCollections = new LinkedHashMap<>();
    private StringBuilder body = new StringBuilder();
    private boolean isRoot;
    private String name;

    public boolean hasSubcollections() {
        return !subCollections.isEmpty();
    }

    public Map<String, String> getSubCollections() {
        return subCollections;
    }

    public void addSubCollection(String name, String value) {
        subCollections.put(name, value);
    }

    public String getBody() {
        return body.toString();
    }

    public void setBody(String newBody) {
        body.setLength(0);
        body.append(newBody);
    }

    public boolean isRoot() {
        return isRoot;
    }

    public void setRoot(boolean flag) {
        isRoot = flag;
    }

    public String getName() {
        return name;
    }

    public void setName(String newName) {
        name = newName;
    }

    public void appendBody(String newBody) {
        body.append(newBody);
    }
}
