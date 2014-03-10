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

import java.util.LinkedHashMap;
import java.util.Map;

public class TypeUtils {
    /**
     * Return key if exists or {@code null}.
     */
    public static String getValueByKeyOrNone(String name, Map<String, String> cache) {
        if (cache.containsKey(name)) {
            return cache.get(name);
        }
        return null;
    }

    /**
     * Formats list in to map preserving list order in map.
     *
     * @param lst list to convert
     */
    public static LinkedHashMap<String, String> toOrderedMap(String[] lst) {
        LinkedHashMap<String, String> dct = new LinkedHashMap<>();
        for (int i = 0; i < lst.length; i++) {
            if (i % 2 == 0) {
                String coll = lst[i];
                String res = i + 1 < lst.length? lst[i + 1]: null;
                dct.put(coll, res);
            }
        }
        return dct;
    }
}
