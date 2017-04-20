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
import javax.inject.Inject;

import org.ovirt.api.metamodel.concepts.EnumType;
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
 * This class is responsible for generating the classes that take instances of model types and generate the
 * corresponding XML documents.
 */
public class WritersGenerator implements PythonGenerator {
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
        buffer.setModuleName(pythonNames.getWritersModuleName());

        // Generate the code:
        generateWriters(model);

        // Write the file:
        try {
            buffer.write(out);
        }
        catch (IOException exception) {
            throw new RuntimeException("Error writing readers module", exception);
        }
    }

    private void generateWriters(Model model) {
        // Generate the imports:
        String rootModuleName = pythonNames.getRootModuleName();
        buffer.addImport("from %1$s import List", rootModuleName);
        buffer.addImport("from %1$s import types", rootModuleName);
        buffer.addImport("from %1$s.writer import Writer", rootModuleName);

        // Generate the writer classes:
        model.types()
            .filter(StructType.class::isInstance)
            .map(StructType.class::cast)
            .sorted()
            .forEach(this::generateWriter);

        // Generate code to register the writers:
        model.types()
            .filter(StructType.class::isInstance)
            .map(StructType.class::cast)
            .sorted()
            .forEach(type -> {
                PythonClassName typeName = pythonNames.getTypeName(type);
                PythonClassName writerName = pythonNames.getWriterName(type);
                buffer.addLine(
                    "Writer.register(types.%1$s, %2$s.write_one)",
                    typeName.getClassName(),
                    writerName.getClassName()
                );
            });
    }

    private void generateWriter(StructType type) {
        // Begin class:
        PythonClassName writerName = pythonNames.getWriterName(type);
        buffer.addLine("class %1$s(Writer):", writerName.getClassName());
        buffer.addLine();

        // Begin body:
        buffer.startBlock();

        // Constructor:
        buffer.addLine("def __init__(self):");
        buffer.startBlock();
        buffer.addLine("super(%1$s, self).__init__()", writerName.getClassName());
        buffer.endBlock();
        buffer.addLine();

        // Methods:
        generateMethods(type);

        // End body:
        buffer.endBlock();
        buffer.addLine();
    }

    private void generateMethods(StructType type) {
        // Get the tags:
        PythonClassName writerName = pythonNames.getWriterName(type);
        Name singularName = type.getName();
        Name pluralName = names.getPlural(singularName);
        String singularTagName = schemaNames.getSchemaTagName(singularName);
        String pluralTagName = schemaNames.getSchemaTagName(pluralName);

        // Generate the method that writes one object:
        buffer.addLine("@staticmethod");
        buffer.addLine("def write_one(obj, writer, singular=None):");
        buffer.startBlock();
        buffer.addLine("if singular is None:");
        buffer.startBlock();
        buffer.addLine("singular = '%1$s'", singularTagName);
        buffer.endBlock();
        buffer.addLine("writer.write_start(singular)");
        buffer.addLine("href = obj.href");
        buffer.addLine("if href is not None:");
        buffer.startBlock();
        buffer.addLine("writer.write_attribute('href', href)");
        buffer.endBlock();
        generateMembersWrite(type);
        buffer.addLine("writer.write_end()");
        buffer.endBlock();
        buffer.addLine();

        // Generate the method that writes one object:
        buffer.addLine("@staticmethod");
        buffer.addLine("def write_many(objs, writer, singular=None, plural=None):");
        buffer.startBlock();
        buffer.addLine("if singular is None:");
        buffer.startBlock();
        buffer.addLine("singular = '%1$s'", singularTagName);
        buffer.endBlock();
        buffer.addLine("if plural is None:");
        buffer.startBlock();
        buffer.addLine("plural = '%1$s'", pluralTagName);
        buffer.endBlock();
        buffer.addLine("writer.write_start(plural)");
        buffer.addLine("if type(objs) == List:");
        buffer.startBlock();
        buffer.addLine("href = objs.href");
        buffer.addLine("if href is not None:");
        buffer.startBlock();
        buffer.addLine("writer.write_attribute('href', href)");
        buffer.endBlock();
        buffer.endBlock();
        buffer.addLine("for obj in objs:");
        buffer.startBlock();
        buffer.addLine("%1$s.write_one(obj, writer, singular)", writerName.getClassName());
        buffer.endBlock();
        buffer.addLine("writer.write_end()");
        buffer.endBlock();
        buffer.addLine();
    }

    private void generateMembersWrite(StructType type) {
        // Generate the code that writes the members that are represented as XML attributes:
        type.attributes()
            .filter(x -> schemaNames.isRepresentedAsAttribute(x.getName()))
            .sorted()
            .forEach(this::generateMemberWriteAsAttribute);
        type.links()
            .filter(x -> schemaNames.isRepresentedAsAttribute(x.getName()))
            .sorted()
            .forEach(this::generateMemberWriteAsAttribute);

        // Generate the code that writes the members that are represented as inner elements:
        type.attributes()
            .filter(x -> !schemaNames.isRepresentedAsAttribute(x.getName()))
            .sorted()
            .forEach(this::generateMemberWriteAsElement);
        type.links()
            .filter(x -> !schemaNames.isRepresentedAsAttribute(x.getName()))
            .sorted()
            .forEach(this::generateMemberWriteAsElement);
    }

    private void generateMemberWriteAsAttribute(StructMember member) {
        Name name = member.getName();
        Type type = member.getType();
        String property = pythonNames.getMemberStyleName(name);
        String attribute = schemaNames.getSchemaTagName(name);
        if (type instanceof PrimitiveType) {
            generateWritePrimitivePropertyAsAttribute((PrimitiveType) type, attribute, "obj." + property);
        }
        else if (type instanceof EnumType) {
            generateWriteEnumPropertyAsAttribute((EnumType) type, attribute, "obj." + property);
        }
    }

    private void generateWritePrimitivePropertyAsAttribute(PrimitiveType type, String tag, String value) {
        Model model = type.getModel();
        buffer.addLine("if %1$s is not None:", value);
        buffer.startBlock();
        if (type == model.getStringType()) {
            buffer.addLine("writer.write_attribute('%1$s', %2$s)", tag, value);
        }
        else if (type == model.getBooleanType() || type == model.getIntegerType() || type == model.getDecimalType()) {
            buffer.addLine("writer.write_attribute('%1$s', str(%2$s))", tag, value);
        }
        else if (type == model.getDateType()) {
            buffer.addLine("writer.write_attribute('%1$s', %2$s.isoformat()", tag, value);
        }
        buffer.endBlock();
    }

    private void generateWriteEnumPropertyAsAttribute(EnumType type, String attribute, String value) {
        buffer.addLine("if %1$s is not None:", value);
        buffer.startBlock();
        buffer.addLine("writer.write_attribute('%1$s', %2$s.value)", attribute, value);
        buffer.endBlock();
    }

    private void generateMemberWriteAsElement(StructMember member) {
        Name name = member.getName();
        Type type = member.getType();
        String property = pythonNames.getMemberStyleName(name);
        String tag = schemaNames.getSchemaTagName(name);
        if (type instanceof PrimitiveType) {
            generateWritePrimitivePropertyAsElement((PrimitiveType) type, tag, "obj." + property);
        }
        else if (type instanceof EnumType) {
            generateWriteEnumPropertyAsElement((EnumType) type, tag, "obj." + property);
        }
        else if (type instanceof StructType) {
            generateWriteStructPropertyAsElement(member);
        }
        else if (type instanceof ListType) {
            generateWriteListPropertyAsElement(member);
        }
    }

    private void generateWritePrimitivePropertyAsElement(PrimitiveType type, String tag, String value) {
        Model model = type.getModel();
        buffer.addLine("if %1$s is not None:", value);
        buffer.startBlock();
        if (type == model.getStringType()) {
            buffer.addLine("Writer.write_string(writer, '%1$s', %2$s)", tag, value);
        }
        else if (type == model.getBooleanType()) {
            buffer.addLine("Writer.write_boolean(writer, '%1$s', %2$s)", tag, value);
        }
        else if (type == model.getIntegerType()) {
            buffer.addLine("Writer.write_integer(writer, '%1$s', %2$s)", tag, value);
        }
        else if (type == model.getDecimalType()) {
            buffer.addLine("Writer.write_decimal(writer, '%1$s', %2$s)", tag, value);
        }
        else if (type == model.getDateType()) {
            buffer.addLine("Writer.write_date(writer, '%1$s', %2$s)", tag, value);
        }
        buffer.endBlock();
    }

    private void generateWriteEnumPropertyAsElement(EnumType type, String tag, String value) {
        buffer.addLine("if %1$s is not None:", value);
        buffer.startBlock();
        buffer.addLine("Writer.write_string(writer, '%1$s', %2$s.value)", tag, value);
        buffer.endBlock();
    }

    private void generateWriteStructPropertyAsElement(StructMember member) {
        Name name = member.getName();
        Type type = member.getType();
        String property = pythonNames.getMemberStyleName(name);
        String tag = schemaNames.getSchemaTagName(name);
        PythonClassName writerName = pythonNames.getWriterName(type);
        buffer.addLine("if obj.%1$s is not None:", property);
        buffer.startBlock();
        buffer.addLine("%1$s.write_one(obj.%2$s, writer, '%3$s')", writerName.getClassName(), property, tag);
        buffer.endBlock();
    }

    private void generateWriteListPropertyAsElement(StructMember member) {
        Name name = member.getName();
        Type type = member.getType();
        ListType listType = (ListType) type;
        Type elementType = listType.getElementType();
        String property = pythonNames.getMemberStyleName(name);
        String pluralTag = schemaNames.getSchemaTagName(name);
        String singularTag = schemaNames.getSchemaTagName(names.getSingular(name));
        if (elementType instanceof PrimitiveType || elementType instanceof EnumType) {
            buffer.addLine("if obj.%1$s is not None:", property);
            buffer.startBlock();
            buffer.addLine("writer.write_start('%1$s')", pluralTag);
            buffer.addLine("for item in obj.%1$s:", property);
            buffer.startBlock();
            if (elementType instanceof PrimitiveType) {
                generateWritePrimitivePropertyAsElement((PrimitiveType) elementType, singularTag, "item");
            }
            else if (elementType instanceof EnumType) {
                generateWriteEnumPropertyAsElement((EnumType) elementType, singularTag, "item");
            }
            buffer.endBlock();
            buffer.addLine("writer.write_end()");
            buffer.endBlock();
        }
        else if (elementType instanceof StructType) {
            PythonClassName elementWriterName = pythonNames.getWriterName(elementType);
            String elementTag = schemaNames.getSchemaTagName(elementType.getName());
            buffer.addLine("if obj.%1$s is not None:", property);
            buffer.startBlock();
            buffer.addLine(
                "%1$s.write_many(obj.%2$s, writer, '%3$s', '%4$s')",
                elementWriterName.getClassName(),
                property,
                elementTag,
                pluralTag
            );
            buffer.endBlock();
        }
    }
}

