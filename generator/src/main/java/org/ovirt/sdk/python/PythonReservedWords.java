/*
The oVirt Project - Ovirt Engine SDK

Copyright oVirt Authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package org.ovirt.sdk.python;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import javax.annotation.PostConstruct;
import javax.enterprise.inject.Produces;
import javax.inject.Singleton;

import org.ovirt.api.metamodel.tool.ReservedWords;

/**
 * This class is a producer of the set of Python reserved words.
 */
@Singleton
public class PythonReservedWords {
    private Set<String> words;

    @PostConstruct
    private void init() {
        // Create the set:
        words = new HashSet<>();

        // Keywords:
        words.add("False");
        words.add("None");
        words.add("True");
        words.add("and");
        words.add("as");
        words.add("assert");
        words.add("async");
        words.add("await");
        words.add("break");
        words.add("class");
        words.add("continue");
        words.add("def");
        words.add("del");
        words.add("elif");
        words.add("else");
        words.add("except");
        words.add("finally");
        words.add("for");
        words.add("from");
        words.add("global");
        words.add("if");
        words.add("import");
        words.add("in");
        words.add("is");
        words.add("lambda");
        words.add("nonlocal");
        words.add("not");
        words.add("or");
        words.add("pass");
        words.add("raise");
        words.add("return");
        words.add("try");
        words.add("while");
        words.add("with");
        words.add("yield");

        // Wrap the set so that it is unmodifiable:
        words = Collections.unmodifiableSet(words);
    }

    /**
     * Produces the set of Python reserved words.
     * @return a set filled with the reserved words in Python as strings.
     */
    @Produces
    @ReservedWords(language = "python")
    public Set<String> getWords() {
        return words;
    }
}
