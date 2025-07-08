/*
Copyright (c) 2015 Red Hat, Inc.

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

import java.io.File;
import java.io.IOException;

import org.ovirt.api.metamodel.concepts.Model;

/**
 * The interface to be implemented by code generators. The tool will locate all the code generators, and for each
 * of them it will set the output file and invoke the {@link #generate(Model)} method. No specific order will be
 * used when there are multiple generators.
 */
public interface PythonGenerator {
    /**
     * Set the directory were the output should be generated.
     *  @param out the path to the output directory.
     */
    void setOut(File out);

    /**
     * Generates the code for the given model.
     * @param model the model to be used to generate the code.
     * @throws IOException in case of I/O errors.
     */
    void generate(Model model) throws IOException;
}

