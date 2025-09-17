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

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Formatter;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.function.Function;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.commons.io.FileUtils;

/**
 * This class is a buffer intended to simplify generation of Python source code. It stores the name of the module, the
 * list of imports and the rest of the source separately, so that imports can be added on demand while generating the
 * rest of the source.
 */
public class PythonBuffer {
    // The name of the file:
    private String fileName;

    // The name of the module:
    private String moduleName;

    // The imports:
    private Set<String> imports = new HashSet<>();

    // The source lines:
    private List<String> lines = new ArrayList<>();

    // The current indentation level:
    private int level;

    /**
     * Sets the file name.
     * @param newFileName the new file name.
     */
    public void setFileName(String newFileName) {
        fileName = newFileName;
    }

    /**
     * Sets the module name:
     * @param newModuleName the new module name.
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
     * Adds one import.
     * @param format A format string as described in Format string syntax
     * @param args Arguments referenced by the format specifiers in the format string. If there are more arguments than format specifiers, the extra arguments are ignored. The maximum number of arguments is limited by the maximum dimension of a Java array as defined by The Java™ Virtual Machine Specification
     */
    public void addImport(String format, Object ... args) {
        // Format the line:
        StringBuilder buffer = new StringBuilder();
        try (Formatter formatter = new Formatter(buffer)) {
            formatter.format(format, args);
        }
        // Add the line to the set:
        imports.add(buffer.toString());
    }

    /**
     * Adds multiple imports.
     * @param imports the imports to add, each one is a string that will be added as an import.
     */
    public void addImports(List<String> imports) {
        imports.forEach(this::addImport);
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
     * @param format A format string as described in Format string syntax
     * @param args Arguments referenced by the format specifiers in the format string. If there are more arguments than format specifiers, the extra arguments are ignored. The maximum number of arguments is limited by the maximum dimension of a Java array as defined by The Java™ Virtual Machine Specification
     */
    public void addLine(String format, Object ... args) {
        // Format the line:
        StringBuilder buffer = new StringBuilder();
        try (Formatter formatter = new Formatter(buffer)) {
            formatter.format(format, args);
        }
        // Indent the line if not empty:
        if (buffer.length() > 0) {
            for (int i = 0; i < level; i++) {
                buffer.insert(0, "    ");
            }
        }

        // Add the line to the list:
        lines.add(buffer.toString());
    }

    /**
     * Adds a non-formatted line to the body of the class.
     * @param line the non formatted line in question
     */
    public void addRawLine(String line) {
        StringBuilder buffer = new StringBuilder(line);
        // Indent the line:
        if (buffer.length() > 0) {
            for (int i = 0; i < level; i++) {
                buffer.insert(0, "    ");
            }
        }

        // Add the line to the list:
        lines.add(buffer.toString());
    }

    /**
     * Assure xref hyperlinks with pdoc links are replaced
     */
    public void prepParameterLine(String line) {
        if (line.contains("xref:")) {
            // Only process lines that contain xref references
            // to avoid unnecessary processing
            String prepLine = line.strip();
            prepLine = replaceServiceMethodsXrefs(prepLine);
            prepLine = replaceServiceXrefs(prepLine);
            prepLine = replaceTypeAttributeXrefs(prepLine);
            prepLine = replaceTypeXrefs(prepLine);
            addRawLine(prepLine);
        } else if (line.contains("<<documents/003_common_concepts/follow, here>>")){
            String prepLine = line.strip();
            prepLine = prepLine.replace("<<documents/003_common_concepts/follow, here>>", 
            "[here](https://ovirt.github.io/ovirt-engine-api-model/master/#documents/003_common_concepts/follow)");
            addRawLine(prepLine);
        } else {
            addRawLine(line);
        }
    }

    /**
     * Replaces the xref types with attributes with the corresponding pdoc link.
     */
    public String replaceTypeAttributeXrefs(String input) {
        return replaceWithPattern(input, "xref:types/([^\\[]+)/attributes/([^\\]]+)\\[([^\\]]+)]", match -> {  
            String typeName = match.group(1);
            String attributeName = match.group(2);
            return "`ovirtsdk4.types." + underscoretoCamelCase(typeName) + "." + attributeName + "`";
        });
    }

    /**
     * Replaces the xref services with methods with the corresponding pdoc link.
     */
    public String replaceServiceMethodsXrefs(String input) {
        return replaceWithPattern(input, "xref:services/([^-\\]]+(?:-[^-\\]]+)*)/methods/([^-\\]]+)\\[([^\\]]+)]", match -> {
            String serviceName = match.group(1);
            String methodName = match.group(2);
            return "`" + underscoretoCamelCase(serviceName) + "Service" + "." + methodName + "`";
        });
    }

    /**
     * Replaces the xref services with the corresponding pdoc link.
     */
    public String replaceServiceXrefs(String input) {
        return replaceWithPattern(input, "xref:services/([^\\[]+)\\[([^\\]]+)]", match -> {
            String serviceName = match.group(1);
            return "`" + underscoretoCamelCase(serviceName) + "Service`";
        });
    }

    /**
     * Replaces the xref types with the corresponding pdoc link.
     */
    public String replaceTypeXrefs(String input) {
        return replaceWithPattern(input, "xref:types/([^\\[]+)\\[[^\\]]+]", match -> {
            String typeString = match.group(1);
            return "`ovirtsdk4.types." + underscoretoCamelCase(typeString) + "`";
        });
    }

    private String underscoretoCamelCase(String doc) {
        String[] words = doc.split("_");
        StringBuilder result = new StringBuilder();
        for (String word : words) {
            if (word.isEmpty()) {
                continue;
            }
            result.append(Character.toUpperCase(word.charAt(0)));
            result.append(word.substring(1));
        }
        return result.toString();
    }

    /**
     * Generic method to replace patterns in a string using a formatter function
     */
    private String replaceWithPattern(String input, String patternStr, Function<Matcher, String> formatter) {
        StringBuffer result = new StringBuffer();
        Pattern pattern = Pattern.compile(patternStr);
        Matcher match = pattern.matcher(input);
        boolean found = false;
        while (match.find()) {
            found = true;
            match.appendReplacement(result, formatter.apply(match));
        }
        match.appendTail(result);
        return found ? result.toString() : input;
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
        buffer.append("# Copyright oVirt Authors\n");
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

        // Add the imports:
        if (!imports.isEmpty()) {
            imports.stream().sorted().forEach(line -> {
                buffer.append(line);
                buffer.append("\n");
            });
            buffer.append("\n");
            buffer.append("\n");
        }

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
