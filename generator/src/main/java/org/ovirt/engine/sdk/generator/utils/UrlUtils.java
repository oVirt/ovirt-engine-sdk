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

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;

import org.ovirt.engine.sdk.entities.DetailedLink;

public class UrlUtils {
    /**
     * Replaces identifiers with real names.
     */
    public static String generateUrlIdentifiersReplacements(
        DetailedLink link,
        String offset,
        boolean continues,
        boolean isCollection
    )
    {
        String url = "";
        List<String> replacementCandidates = getReplacementCandidates(getPeriods(link));
        int replacementCandidatesLen = replacementCandidates.size();
        if (!replacementCandidates.isEmpty()) {
            for (int i = 0; i < replacementCandidatesLen; i++) {
                if (replacementCandidates.size() == 1) {
                    url += (!continues? offset: "") + "{'" + replacementCandidates.get(i) + "': " +
                        generateParentClassIdentifiers(replacementCandidatesLen - i) + "}";
                    return url;
                }
                else {
                    int replacementOffset;
                    if (!isCollection) {
                        replacementOffset = i + 1;
                    }
                    else {
                        replacementOffset = i;
                    }
                    if (i == 0) {
                        url += (!continues? offset: "") + "{'" + replacementCandidates.get(i) + "' : " +
                            generateParentClassIdentifiers(replacementCandidatesLen - replacementOffset);
                        if (replacementCandidates.size() == 1) {
                            return url;
                        }
                    }
                    else if (i != replacementCandidatesLen - 1) {
                        url += ",\n";
                        url += offset + " '" + replacementCandidates.get(i) + "': " +
                            generateParentClassIdentifiers(replacementCandidatesLen - replacementOffset);
                    }
                    else {
                        url += ",\n";
                        url += offset + " '" + replacementCandidates.get(i) + "': " +
                            generateParentClassIdentifiers(replacementCandidatesLen - replacementOffset) + "}";
                    }
                }
            }
        }

        return url;
    }

    private static String generateParentClassIdentifiers(int num) {
        String res = "self";
        for (int i = 0; i < num; i++) {
            res += ".parentclass";
        }
        res += ".get_id()";
        return res;
    }

    private static List<String> getReplacementCandidates(LinkedHashMap<String, String> resources) {
        List<String> cands = new ArrayList<>();
        for (String item : resources.values()) {
            if (item != null && item.endsWith(":id}")) {
                cands.add(item);
            }
        }
        return cands;
    }

    private static LinkedHashMap<String, String> getPeriods(DetailedLink link) {
        String url = link.getHref();
        List<String> sUrl = new ArrayList<>(Arrays.asList(url.split("/")));
        sUrl.remove(0);
        return listToDict(sUrl);
    }

    private static LinkedHashMap<String, String> listToDict(List<String> lst) {
        LinkedHashMap<String, String> dct = new LinkedHashMap<>();
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 == 0) {
                String coll = lst.get(i);
                String res = i + 1 < lst.size()? lst.get(i + 1): null;
                dct.put(coll, res);
            }
        }
        return dct;
    }
}