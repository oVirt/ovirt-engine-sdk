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
import static java.util.stream.Collectors.toList;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.stream.Stream;
import javax.inject.Inject;

import org.ovirt.api.metamodel.concepts.EnumType;
import org.ovirt.api.metamodel.concepts.Link;
import org.ovirt.api.metamodel.concepts.ListType;
import org.ovirt.api.metamodel.concepts.Model;
import org.ovirt.api.metamodel.concepts.Name;
import org.ovirt.api.metamodel.concepts.PrimitiveType;
import org.ovirt.api.metamodel.concepts.StructMember;
import org.ovirt.api.metamodel.concepts.StructType;
import org.ovirt.api.metamodel.concepts.Type;
import org.ovirt.api.metamodel.tool.Names;
import org.ovirt.api.metamodel.tool.SchemaNames;

/**
 * This class is responsible for generating the classes that create instances of model types from XML documents.
 */
public class ReadersGenerator implements PythonGenerator {
    // The directory were the output will be generated:
    protected File out;

    // Reference to the objects used to generate the code:
    @Inject private Names names;
    @Inject private SchemaNames schemaNames;
    @Inject private PythonNames pythonNames;

    // The buffer used to generate the code:
    private PythonBuffer buffer;

    public void setOut(File newOut) {
        out = newOut;
    }

    public void generate(Model model) {
        // Prepare the buffer:
        buffer = new PythonBuffer();
        buffer.setModuleName(pythonNames.getReadersModuleName());

        // Generate the code:
        generateReaders(model);

        // Write the file:
        try {
            buffer.write(out);
        }
        catch (IOException exception) {
            throw new RuntimeException("Error writing readers module", exception);
        }
    }

    private void generateReaders(Model model) {
        // Generate the imports:
        String rootModuleName = pythonNames.getRootModuleName();
        buffer.addImport("from %1$s import List", rootModuleName);
        buffer.addImport("from %1$s import types", rootModuleName);
        buffer.addImport("from %1$s.reader import Reader", rootModuleName);

        // Generate the classes:
        model.types()
            .filter(StructType.class::isInstance)
            .map(StructType.class::cast)
            .sorted()
            .forEach(this::generateReader);

        // Generate code to register the readers:
        model.types()
            .filter(StructType.class::isInstance)
            .map(StructType.class::cast)
            .sorted()
            .forEach(type -> {
                Name typeName = type.getName();
                String singularTag = schemaNames.getSchemaTagName(typeName);
                String pluralTag = schemaNames.getSchemaTagName(names.getPlural(typeName));
                String className = pythonNames.getReaderName(type).getClassName();
                buffer.addLine("Reader.register('%1$s', %2$s.read_one)", singularTag, className);
                buffer.addLine("Reader.register('%1$s', %2$s.read_many)", pluralTag, className);
            });
    }

    private void generateReader(StructType type) {
        // Begin class:
        PythonClassName readerName = pythonNames.getReaderName(type);
        buffer.addLine("class %1$s(Reader):", readerName.getClassName());
        buffer.addLine();

        // Begin body:
        buffer.startBlock();

        // Constructor:
        buffer.addLine("def __init__(self):");
        buffer.startBlock();
        buffer.addLine("super(%1$s, self).__init__()", readerName.getClassName());
        buffer.endBlock();
        buffer.addLine();

        // Methods:
        generateMethods(type);

        // End body:
        buffer.endBlock();
        buffer.addLine();
    }

    private void generateMethods(StructType type) {
        PythonClassName typeName = pythonNames.getTypeName(type);
        PythonClassName readerName = pythonNames.getReaderName(type);

        // Generate the method that reads one instance:
        buffer.addLine("@staticmethod");
        buffer.addLine("def read_one(reader):");
        buffer.startBlock();
        buffer.addLine("# Do nothing if there aren't more tags:");
        buffer.addLine("if not reader.forward():");
        buffer.startBlock();
        buffer.addLine("return None");
        buffer.endBlock();
        buffer.addLine();
        buffer.addLine("# Create the object:");
        buffer.addLine("obj = types.%1$s()", typeName.getClassName());
        buffer.addLine();
        buffer.addLine("# Process the attributes:");
        buffer.addLine("obj.href = reader.get_attribute('href')");
        generateAttributesRead(type);
        buffer.addLine();
        buffer.addLine("# Discard the start tag:");
        buffer.addLine("empty = reader.empty_element()");
        buffer.addLine("reader.read()");
        buffer.addLine("if empty:");
        buffer.startBlock();
        buffer.addLine("return obj");
        buffer.endBlock();
        buffer.addLine();
        buffer.addLine("# Process the inner elements:");
        generateElementsRead(type);
        buffer.addLine();
        buffer.addLine("# Discard the end tag:");
        buffer.addLine("reader.read()");
        buffer.addLine();
        buffer.addLine("return obj");
        buffer.endBlock();
        buffer.addLine();

        // Generate the method that reads many instances:
        buffer.addLine("@staticmethod");
        buffer.addLine("def read_many(reader):");
        buffer.startBlock();
        buffer.addLine("# Do nothing if there aren't more tags:");
        buffer.addLine("objs = List()");
        buffer.addLine("if not reader.forward():");
        buffer.startBlock();
        buffer.addLine("return objs");
        buffer.endBlock();
        buffer.addLine();
        buffer.addLine("# Process the attributes:");
        buffer.addLine("objs.href = reader.get_attribute('href')");
        buffer.addLine();
        buffer.addLine("# Discard the start tag:");
        buffer.addLine("empty = reader.empty_element()");
        buffer.addLine("reader.read()");
        buffer.addLine("if empty:");
        buffer.startBlock();
        buffer.addLine("return objs");
        buffer.endBlock();
        buffer.addLine();
        buffer.addLine("# Process the inner elements:");
        buffer.addLine("while reader.forward():");
        buffer.startBlock();
        buffer.addLine("objs.append(%1$s.read_one(reader))", readerName.getClassName());
        buffer.endBlock();
        buffer.addLine();
        buffer.addLine("# Discard the end tag:");
        buffer.addLine("reader.read()");
        buffer.addLine();
        buffer.addLine("return objs");
        buffer.endBlock();
        buffer.addLine();

        // Generate the method that reads links to lists:
        List<Link> links = type.links()
            .filter(link -> link.getType() instanceof ListType)
            .sorted()
            .collect(toList());
        if (!links.isEmpty()) {
            buffer.addLine("@staticmethod");
            buffer.addLine("def _process_link(link, obj):");
            buffer.startBlock();
            buffer.addLine(  "# Process the attributes:");
            buffer.addLine(  "rel = link[0]");
            buffer.addLine(  "href = link[1]");
            buffer.addLine(  "if href and rel:");
            buffer.startBlock();

            boolean firstLink = true;
            for (Link link : links) {
                String keyword = firstLink ? "if" : "elif";
                String field = pythonNames.getMemberStyleName(link.getName());
                String rel = link.getName().words().map(String::toLowerCase).collect(joining());
                buffer.addLine("%1$s rel == \"%2$s\":", keyword, rel);
                buffer.startBlock();
                buffer.addLine("if obj.%1$s is not None:", field);
                buffer.startBlock();
                buffer.addLine("obj.%1$s.href = href", field);
                buffer.endBlock();
                buffer.addLine("else:");
                buffer.startBlock();
                buffer.addLine("obj.%1$s = List(href)", field);
                buffer.endBlock();
                buffer.endBlock();
                firstLink = false;
            }

            buffer.endBlock(); // End if
            buffer.endBlock();  // End method
            buffer.addLine();
        }
    }

    private void generateAttributesRead(StructType type) {
        Stream.concat(type.attributes(), type.links())
            .filter(x -> schemaNames.isRepresentedAsAttribute(x.getName()))
            .sorted()
            .forEach(this::generateAttributeRead);
    }

    private void generateAttributeRead(StructMember member) {
        Name name = member.getName();
        Type type = member.getType();
        PythonClassName typeName = pythonNames.getTypeName(type);
        String property = pythonNames.getMemberStyleName(name);
        String tag = schemaNames.getSchemaTagName(name);
        buffer.addLine("value = reader.get_attribute('%s')", tag);
        buffer.addLine("if value is not None:");
        buffer.startBlock();
        if (type instanceof PrimitiveType) {
            Model model = type.getModel();
            if (type == model.getStringType()) {
                buffer.addLine("obj.%1$s = value", property);
            }
            else if (type == model.getBooleanType()) {
                buffer.addLine("obj.%1$s = Reader.parse_boolean(value)", property);
            }
            else if (type == model.getIntegerType()) {
                buffer.addLine("obj.%1$s = Reader.parse_integer(value)", property);
            }
            else if (type == model.getDecimalType()) {
                buffer.addLine("obj.%1$s = Reader.parse_decimal(value)", property);
            }
            else if (type == model.getDateType()) {
                buffer.addLine("obj.%1$s = Reader.parse_date(value)", property);
            }
        }
        else if (type instanceof EnumType) {
            buffer.addLine("obj.%1$s = types.%2$s(value.lower())", property, typeName.getClassName());
        }
        buffer.endBlock();
    }

    private void generateElementsRead(StructType type) {
        long listLinksCount = type.links()
            .filter(link -> link.getType() instanceof ListType)
            .count();
        List<StructMember> members = Stream.concat(type.attributes(), type.links())
            .filter(x -> !schemaNames.isRepresentedAsAttribute(x.getName()))
            .sorted()
            .collect(toList());
        if (!members.isEmpty()) {
            buffer.addLine("links = []");
            buffer.addLine("while reader.forward():");
            buffer.startBlock();
            buffer.addLine("tag = reader.node_name()");
            members.stream().limit(1).forEach(member -> generateElementRead(member, true));
            members.stream().skip(1).forEach(member -> generateElementRead(member, false));
            if (listLinksCount > 0) {
                buffer.addLine("elif tag == 'link':");
                buffer.startBlock();
                buffer.addLine("links.append((reader.get_attribute('rel'), reader.get_attribute('href')))");
                buffer.addLine("reader.next_element()");
                buffer.endBlock();
            }
            buffer.addLine("else:");
            buffer.startBlock();
            buffer.addLine("reader.next_element()");
            buffer.endBlock();
            buffer.endBlock();

            // Process the links:
            buffer.addLine("for link in links:");
            buffer.startBlock();
            buffer.addLine("%1$s._process_link(link, obj)", pythonNames.getReaderName(type).getClassName());
            buffer.endBlock();
        }
        else {
            buffer.addLine("reader.next_element()");
        }
    }

    private void generateElementRead(StructMember member, boolean first) {
        Name name = member.getName();
        Type type = member.getType();
        String property = pythonNames.getMemberStyleName(name);
        String tag = schemaNames.getSchemaTagName(name);
        String variable = String.format("obj.%1$s", property);
        String keyword = first? "if": "elif";
        buffer.addLine("%1$s tag == '%2$s':", keyword, tag);
        buffer.startBlock();
        if (type instanceof PrimitiveType) {
            generateReadPrimitive(member, variable);
        }
        else if (type instanceof EnumType) {
            generateReadEnum(member, variable);
        }
        else if (type instanceof StructType) {
            generateReadStruct(member, variable);
        }
        else if (type instanceof ListType) {
            generateReadList(member, variable);
        }
        else {
            buffer.addLine("reader.next_element()");
        }
        buffer.endBlock();
    }

    private void generateReadPrimitive(StructMember member, String variable) {
        Type type = member.getType();
        Model model = type.getModel();
        if (type == model.getStringType()) {
            buffer.addLine("%1$s = Reader.read_string(reader)", variable);
        }
        else if (type == model.getBooleanType()) {
            buffer.addLine("%1$s = Reader.read_boolean(reader)", variable);
        }
        else if (type == model.getIntegerType()) {
            buffer.addLine("%1$s = Reader.read_integer(reader)", variable);
        }
        else if (type == model.getDecimalType()) {
            buffer.addLine("%1$s = Reader.read_decimal(reader)", variable);
        }
        else if (type == model.getDateType()) {
            buffer.addLine("%1$s = Reader.read_date(reader)", variable);
        }
        else {
            buffer.addLine("reader.next_element()");
        }
    }

    private void generateReadEnum(StructMember member, String variable) {
        PythonClassName typeName = pythonNames.getTypeName(member.getType());
        buffer.addLine(
            "%1$s = Reader.read_enum(types.%2$s, reader)",
            variable,
            typeName.getClassName()
        );
    }

    private void generateReadStruct(StructMember member, String variable) {
        PythonClassName readerName = pythonNames.getReaderName(member.getType());
        buffer.addLine("%1$s = %2$s.read_one(reader)", variable, readerName.getClassName());
    }

    private void generateReadList(StructMember member, String variable) {
        ListType type = (ListType) member.getType();
        Type elementType = type.getElementType();
        if (elementType instanceof PrimitiveType) {
            generateReadPrimitives((PrimitiveType) elementType, variable);
        }
        else if (elementType instanceof EnumType) {
            generateReadEnums((EnumType) elementType, variable);
        }
        else if (elementType instanceof StructType) {
            PythonClassName readerName = pythonNames.getReaderName(elementType);
            buffer.addLine("%1$s = %2$s.read_many(reader)", variable, readerName.getClassName());
        }
        else {
            buffer.addLine("reader.next_element()");
        }
    }

    private void generateReadPrimitives(PrimitiveType type, String variable) {
        Model model = type.getModel();
        if (type == model.getStringType()) {
            buffer.addLine("%1$s = Reader.read_strings(reader)", variable);
        }
        else if (type == model.getBooleanType()) {
            buffer.addLine("%1$s = Reader.read_booleans(reader)", variable);
        }
        else if (type == model.getIntegerType()) {
            buffer.addLine("%1$s = Reader.read_integers(reader)", variable);
        }
        else if (type == model.getDecimalType()) {
            buffer.addLine("%1$s = Reader.read_decimals(reader)", variable);
        }
        else if (type == model.getDateType()) {
            buffer.addLine("%1$s = Reader.read_dates(reader)", variable);
        }
        else {
            buffer.addLine("reader.next_element");
        }
    }

    private void generateReadEnums(EnumType type, String variable) {
        buffer.addLine(
            "%1$s = Reader.read_enums(types.%2$s, reader)",
            variable,
            pythonNames.getClassStyleName(type.getName())
        );
    }
}

