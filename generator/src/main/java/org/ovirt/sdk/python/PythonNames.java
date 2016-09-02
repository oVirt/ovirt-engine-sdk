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

import static java.util.stream.Collectors.joining;

import java.util.List;
import java.util.Set;
import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;

import org.ovirt.api.metamodel.concepts.EnumType;
import org.ovirt.api.metamodel.concepts.ListType;
import org.ovirt.api.metamodel.concepts.Model;
import org.ovirt.api.metamodel.concepts.Name;
import org.ovirt.api.metamodel.concepts.NameParser;
import org.ovirt.api.metamodel.concepts.PrimitiveType;
import org.ovirt.api.metamodel.concepts.Service;
import org.ovirt.api.metamodel.concepts.StructType;
import org.ovirt.api.metamodel.concepts.Type;
import org.ovirt.api.metamodel.tool.ReservedWords;
import org.ovirt.api.metamodel.tool.Words;

/**
 * This class contains the rules used to calculate the names of generated Python concepts.
 */
@ApplicationScoped
public class PythonNames {
    // The names of the base classes:
    public static final Name READER_NAME = NameParser.parseUsingCase("Reader");
    public static final Name SERVICE_NAME = NameParser.parseUsingCase("Service");
    public static final Name WRITER_NAME = NameParser.parseUsingCase("Writer");

    // The relative names of the modules:
    public static final String READERS_MODULE = "readers";
    public static final String SERVICES_MODULE = "services";
    public static final String TYPES_MODULE = "types";
    public static final String WRITERS_MODULE = "writers";

    // Reference to the object used to do computations with words.
    @Inject
    private Words words;

    // We need the Python reserved words in order to avoid producing names that aren't legal:
    @Inject
    @ReservedWords(language = "python")
    private Set<String> reservedWords;

    // The name of the root module:
    private String rootModuleName = "ovirtsdk4";

    /**
     * Get the name of the root module.
     */
    public String getRootModuleName() {
        return rootModuleName;
    }

    /**
     * Get the name of the types module.
     */
    public String getTypesModuleName() {
        return getModuleName(TYPES_MODULE);
    }

    /**
     * Get the name of the readers module.
     */
    public String getReadersModuleName() {
        return getModuleName(READERS_MODULE);
    }

    /**
     * Get the name of the writers module.
     */
    public String getWritersModuleName() {
        return getModuleName(WRITERS_MODULE);
    }

    /**
     * Get the name of the services module.
     */
    public String getServicesModuleName() {
        return getModuleName(SERVICES_MODULE);
    }

    /**
     * Get the complete name of the given module.
     */
    public String getModuleName(String... relativeNames) {
        StringBuilder buffer = new StringBuilder();
        buffer.append(rootModuleName);
        if (relativeNames != null || relativeNames.length > 0) {
            for (String relativeName : relativeNames) {
                buffer.append('.');
                buffer.append(relativeName);
            }
        }
        return buffer.toString();
    }

    /**
     * Calculates the Python name that corresponds to the given type.
     */
    public PythonClassName getTypeName(Type type) {
        return buildClassName(type.getName(), null, TYPES_MODULE);
    }

    /**
     * Calculates that should be used in Python to reference the given type. For example, for the boolean type it will
     * return the {@code bool} string.
     */
    public PythonTypeReference getTypeReference(Type type) {
        PythonTypeReference reference = new PythonTypeReference();
        if (type instanceof PrimitiveType) {
            Model model = type.getModel();
            if (type == model.getBooleanType()) {
                reference.setText("bool");
            }
            else if (type == model.getIntegerType()) {
                reference.setText("int");
            }
            else if (type == model.getDecimalType()) {
                reference.setText("float");
            }
            else if (type == model.getStringType()) {
                reference.setText("str");
            }
            else if (type == model.getDateType()) {
                reference.addImport("import datatime");
                reference.setText("datetime.date");
            }
            else {
                throw new IllegalArgumentException(
                    "Don't know how to build reference for primitive type \"" + type + "\""
                );
            }
        }
        else if (type instanceof StructType || type instanceof EnumType) {
            reference.addImport(String.format("from %1$s import %2$s", getRootModuleName(), TYPES_MODULE));
            reference.setText(TYPES_MODULE + "." + getTypeName(type).getClassName());
        }
        else if (type instanceof ListType) {
            reference.setText("list");
        }
        else {
            throw new IllegalArgumentException("Don't know how to build reference for type \"" + type + "\"");
        }
        return reference;
    }
    /**
     * Calculates the Python name of the base class of the services.
     */
    public PythonClassName getBaseServiceName() {
        return buildClassName(SERVICE_NAME, null, SERVICES_MODULE);
    }

    /**
     * Calculates the Python name that corresponds to the given service.
     */
    public PythonClassName getServiceName(Service service) {
        return buildClassName(service.getName(), SERVICE_NAME, SERVICES_MODULE);
    }

    /**
     * Calculates the Python name of the reader for the given type.
     */
    public PythonClassName getReaderName(Type type) {
        return buildClassName(type.getName(), READER_NAME, READERS_MODULE);
    }

    /**
     * Calculates the Python name of the writer for the given type.
     */
    public PythonClassName getWriterName(Type type) {
        return buildClassName(type.getName(), WRITER_NAME, WRITERS_MODULE);
    }

    /**
     * Builds a Python name from the given base name, suffix, and module.
     *
     * The suffix can be {@code null} or empty, in that case then won't be added.
     *
     * @param base the base name
     * @param suffix the suffix to add to the name
     * @param module the module name
     * @return the calculated Python class name
     */
    private PythonClassName buildClassName(Name base, Name suffix, String module) {
        List<String> words = base.getWords();
        if (suffix != null) {
            words.addAll(suffix.getWords());
        }
        Name name = new Name(words);
        PythonClassName result = new PythonClassName();
        result.setClassName(getClassStyleName(name));
        result.setModuleName(getModuleName(module));
        return result;
    }

    /**
     * Returns a representation of the given name using the capitalization style typically used for Python classes.
     */
    public String getClassStyleName(Name name) {
        return name.words().map(words::capitalize).collect(joining());
    }

    /**
     * Returns a representation of the given name using the capitalization style typically used for Python members.
     */
    public String getMemberStyleName(Name name) {
        String result = name.words().map(String::toLowerCase).collect(joining("_"));
        if (reservedWords.contains(result)) {
            result += "_";
        }
        return result;
    }

    /**
     * Returns a representation of the given name using the capitalization style typically used for Python constants.
     */
    public String getConstantStyleName(Name name) {
        return name.words().map(String::toUpperCase).collect(joining("_"));
    }

    /**
     * Returns a representation of the given name using the capitalization style typically used for Python modules.
     */
    public String getModuleStyleName(Name name) {
        String result = name.words().map(String::toLowerCase).collect(joining("_"));
        if (reservedWords.contains(result)) {
            result += "_";
        }
        return result;
    }
}

