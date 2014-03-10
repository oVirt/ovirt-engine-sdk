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

import java.util.Map;

/**
 * Provides string related services.
 */
public class StringUtils {
    /**
     * Converts string to singular form
     *
     * @param candidate
     *
     * @return singular string
     */
    public static String toSingular(String candidate) {
        if (candidate.length() >= 1 && candidate.endsWith("s")) {
            return candidate.substring(0, candidate.length() - 1);
        }
        return candidate;
    }

    /**
     * Converts string to singular form
     *
     * @param candidate
     *
     * @return singular string
     */
    public static String toSingular(String candidate, Map<String, String> exceptions) {
        if (candidate == null) {
            return null;
        }
        if (exceptions.containsKey(candidate)) {
            return exceptions.get(candidate);
        }
        if (candidate.length() >= 1 && candidate.endsWith("s")) {
            return candidate.substring(0, candidate.length() - 1);
        }
        return candidate;
    }

    /**
     * Returns the first of the given strings that isn't {@code null}.
     */
    public static String firstNotNull(String... values) {
        for (String value : values) {
            if (value != null) {
                return value;
            }
        }
        return null;
    }

    public static String capitalize(String value) {
        if (!value.isEmpty()) {
            return value.substring(0, 1).toUpperCase() + value.substring(1).toLowerCase();
        }
        return value;
    }
}
