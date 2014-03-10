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

package org.ovirt.engine.sdk.generator.templates;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

public abstract class AbstractTemplate {
    /**
     * The key that surrounds variables in the template text.
     */
    private String KEY_WRAP = "$";

    /**
     * The name of the template.
     */
    private String name;

    /**
     * The text of the template.
     */
    private String template;

    /**
     * The values of the variables to substitute in the generated text.
     */
    private Map<String, Object> variables = new HashMap<>();

    public AbstractTemplate() {
        this.name = getClass().getSimpleName();
        this.template = loadTemplate();
    }

    /**
     * Loads template in given context
     * 
     * @return template
     */
    public String loadTemplate() {
        try (InputStream in = this.getClass().getResourceAsStream(name)) {
            if (in == null) {
                throw new RuntimeException("Template \"" + name + "\" not found.");
            }
            try (ByteArrayOutputStream out = new ByteArrayOutputStream()) {
                byte[] buffer = new byte[1024];
                int count;
                while ((count = in.read(buffer)) != -1) {
                    out.write(buffer, 0, count);
                }
                return new String(out.toByteArray(), "UTF-8");
            }
        }
        catch (IOException exception) {
            throw new RuntimeException("Error loading template \"" + name + "\".", exception);
        }
    }

    /**
     * Assigns a value to a variable.
     */
    public void set(String name, Object value) {
        variables.put(name, value);
    }

    /**
     * Assign values to several variables.
     */
    public void set(Map<String, String> map) {
        variables.putAll(map);
    }

    /**
     * Evaluates the template and returns the generated text.
     */
    public String evaluate() {
        String text = template;
        for (Map.Entry<String, Object> variable : variables.entrySet()) {
            String key = KEY_WRAP + variable.getKey() + KEY_WRAP;
            Object value = variable.getValue();
            if (value != null) {
                text = text.replace(key, value.toString());
            }
        }
        return text;
    }
}
