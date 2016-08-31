/*
Copyright (c) 2016 Red Hat, Inc.

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
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Formatter;
import java.util.List;
import javax.inject.Inject;

import org.apache.commons.io.FileUtils;

/**
 * This class is a buffer intended to simplify generation of Python source code. It stores the name of the module, the
 * list of imports and the rest of the source separately, so that imports can be added on demand while generating the
 * rest of the source.
 */
public class PythonBuffer {
    // Reference to the object used to generate names:
    @Inject private PythonNames pythonNames;

    // The name of the file:
    private String fileName;

    // The name of the module:
    private String moduleName;

    // The source lines:
    private List<String> lines = new ArrayList<>();

    // The current indentation level:
    private int level;

    /**
     * Sets the file name.
     */
    public void setFileName(String newFileName) {
        fileName = newFileName;
    }

    /**
     * Sets the module name:
     */
    public void setModuleName(String newModuleName) {
        moduleName = newModuleName;
    }

    /**
     * Starts an indented block.
     */
    public void startBlock() {
        level++;
    }

    /**
     * Ends an indented block.
     */
    public void endBlock() {
        if (level > 0) {
            level--;
        }
    }

    /**
     * Adds an empty line to the body of the class.
     */
    public void addLine() {
        lines.add("");
    }

    /**
     * Adds a formatted line to the body of the class. The given {@code args} are formatted using the
     * provided {@code format} using the {@link String#format(String, Object...)} method.
     */
    public void addLine(String format, Object ... args) {
        // Format the line:
        StringBuilder buffer = new StringBuilder();
        Formatter formatter = new Formatter(buffer);
        formatter.format(format, args);

        // Indent the line:
        for (int i = 0; i < level; i++) {
            buffer.insert(0, "    ");
        }

        // Add the line to the list:
        lines.add(buffer.toString());
    }

    /**
     * Adds a non-formatted line to the body of the class.
     */
    public void addRawLine(String line) {
        StringBuilder buffer = new StringBuilder(line);
        // Indent the line:
        for (int i = 0; i < level; i++) {
            buffer.insert(0, "    ");
        }

        // Add the line to the list:
        lines.add(buffer.toString());
    }

    /**
     * Starts a multi line comment.
     */
    public void startComment() {
        addLine("\"\"\"");
    }

    /**
     * Ends a multi line comment.
     */
    public void endComment() {
        addLine("\"\"\"");
    }

    /**
     * Generates the complete source code of the class.
     */
    public String toString() {
        StringBuilder buffer = new StringBuilder();

        // Encoding:
        buffer.append("# -*- coding: utf-8 -*-\n");
        buffer.append("\n");

        // License:
        buffer.append("#\n");
        buffer.append("# Copyright (c) 2016 Red Hat, Inc.\n");
        buffer.append("#\n");
        buffer.append("# Licensed under the Apache License, Version 2.0 (the \"License\");\n");
        buffer.append("# you may not use this file except in compliance with the License.\n");
        buffer.append("# You may obtain a copy of the License at\n");
        buffer.append("#\n");
        buffer.append("#   http://www.apache.org/licenses/LICENSE-2.0\n");
        buffer.append("#\n");
        buffer.append("# Unless required by applicable law or agreed to in writing, software\n");
        buffer.append("# distributed under the License is distributed on an \"AS IS\" BASIS,\n");
        buffer.append("# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n");
        buffer.append("# See the License for the specific language governing permissions and\n");
        buffer.append("# limitations under the License.\n");
        buffer.append("#\n");

        // Two blank lines, as required by PEP8:
        buffer.append("\n");
        buffer.append("\n");

        // Remove empty lines at the end of the file, as required by PEP8:
        for (;;) {
            if (lines.isEmpty()) {
                break;
            }
            int index = lines.size() - 1;
            String last = lines.get(index);
            if (!last.isEmpty()) {
                break;
            }
            lines.remove(index);
        }

        // Body:
        for (String line : lines) {
            buffer.append(line);
            buffer.append("\n");
        }

        return buffer.toString();
    }

    /**
     * Creates a {@code .py} source file and writes the source. The required intermediate directories will be created
     * if they don't exist.
     *
     * @param dir the base directory for the source code
     * @throws IOException if something fails while creating or writing the file
     */
    public void write(File dir) throws IOException {
        // Calculate the complete file name:
        if (fileName == null) {
            fileName = moduleName.replace('.', File.separatorChar);
        }
        File file = new File(dir, fileName + ".py");

        // Create the directory and all its parent if needed:
        File parent = file.getParentFile();
        FileUtils.forceMkdir(parent);

        // Write the file:
        System.out.println("Writing file \"" + file.getAbsolutePath() + "\".");
        try (Writer writer = new OutputStreamWriter(new FileOutputStream(file), StandardCharsets.UTF_8)) {
            writer.write(toString());
        }
    }
}
