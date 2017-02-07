/*
Copyright (c) 2017 Red Hat, Inc.

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
import javax.inject.Inject;

import org.ovirt.api.metamodel.concepts.Model;

/**
 * This class is responsible for generating the file that contains the version number information.
 */
public class VersionGenerator implements PythonGenerator {
    // The directory were the output will be generated:
    private File out;

    // Reference to the objects used to generate the code:
    @Inject private PythonNames pythonNames;

    // The buffer used to generate the Ruby code:
    private PythonBuffer buffer;

    public void setOut(File newOut) {
        out = newOut;
    }

    public void generate(Model model) throws IOException {
        // Prepare the buffer:
        buffer = new PythonBuffer();
        buffer.setModuleName(pythonNames.getVersionModuleName());

        // Generate the source:
        generateVersion();

        // Write the file:
        try {
            buffer.write(out);
        }
        catch (IOException exception) {
            throw new IllegalStateException("Error writing version file", exception);
        }
    }

    public void generateVersion() {
        // Generate the version constant:
        String version = pythonNames.getVersion();
        buffer.addLine("# The version of the SDK:");
        buffer.addLine("VERSION = '%1$s'", version.toLowerCase());
        buffer.addLine();

        // Generate the main method:
        buffer.addLine("# This module is executed as a script during the build process, and it");
        buffer.addLine("# should print to the output the value of the version:");
        buffer.addLine("if __name__ == '__main__':");
        buffer.startBlock();
        buffer.addLine("print(VERSION)");
        buffer.endBlock();
    }
}

