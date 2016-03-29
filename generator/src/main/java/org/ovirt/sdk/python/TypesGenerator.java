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

import static java.util.stream.Collectors.toCollection;
import static java.util.stream.Collectors.toSet;

import java.io.File;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Stream;
import javax.inject.Inject;

import org.ovirt.api.metamodel.concepts.EnumType;
import org.ovirt.api.metamodel.concepts.EnumValue;
import org.ovirt.api.metamodel.concepts.Model;
import org.ovirt.api.metamodel.concepts.Name;
import org.ovirt.api.metamodel.concepts.StructMember;
import org.ovirt.api.metamodel.concepts.StructType;
import org.ovirt.api.metamodel.concepts.Type;

/**
 * This class is responsible for generating the classes that represent the types of the model.
 */
public class TypesGenerator implements PythonGenerator {
    // The directory were the output will be generated:
    protected File out;

    // Reference to the objects used to generate the code:
    @Inject
    private PythonNames pythonNames;

    // The buffer used to generate the code:
    private PythonBuffer buffer;

    public void setOut(File newOut) {
        out = newOut;
    }

    public void generate(Model model) {
        // Prepare the buffer:
        buffer = new PythonBuffer();
        buffer.setModuleName(pythonNames.getTypesModuleName());

        // Generate the code:
        generateTypes(model);

        // Write the file:
        try {
            buffer.write(out);
        }
        catch (IOException exception) {
            throw new RuntimeException("Error writing types module", exception);
        }
    }

    private void generateTypes(Model model) {
        // Generate the import statements for structs that aren't generated:
        String rootModuleName = pythonNames.getRootModuleName();
        buffer.addLine("from enum import Enum, unique", rootModuleName);
        buffer.addLine("from %1$s.list import List", rootModuleName);
        buffer.addLine("from %1$s.struct import Struct", rootModuleName);
        buffer.addLine();
        buffer.addLine();

        // The declarations of struct types need to appear in inheritance order, otherwise some symbols won't be
        // defined and that will produce errors. To order them correctly we need first to sort them by name, and
        // then sort again so that bases are before extensions.
        Deque<StructType> pending = model.types()
            .filter(StructType.class::isInstance)
            .map(StructType.class::cast)
            .sorted()
            .collect(toCollection(ArrayDeque::new));
        Deque<StructType> structs = new ArrayDeque<>(pending.size());
        while (!pending.isEmpty()) {
            StructType current = pending.removeFirst();
            StructType base = (StructType) current.getBase();
            if (base == null || structs.contains(base)) {
                structs.addLast(current);
            }
            else {
                pending.addLast(current);
            }
        }
        structs.stream()
            .forEach(this::generateStruct);

        // Enum types don't need any special order, so we sort them only by name:
        model.types()
            .filter(EnumType.class::isInstance)
            .map(EnumType.class::cast)
            .sorted()
            .forEach(this::generateEnum);
    }

    private void generateStruct(StructType type) {
        // Begin class:
        PythonClassName typeName = pythonNames.getTypeName(type);
        Type base = type.getBase();
        String baseName = base != null? pythonNames.getTypeName(base).getClassName(): "Struct";
        buffer.addLine("class %1$s(%2$s):", typeName.getClassName(), baseName);
        buffer.startBlock();
        buffer.addLine();

        // Constructor with a named parameter for each attribute and link:
        Set<StructMember> allMembers = Stream.concat(type.attributes(), type.links())
            .collect(toSet());
        Set<StructMember> declaredMembers = Stream.concat(type.declaredAttributes(), type.declaredLinks())
            .collect(toSet());
        Set<StructMember> inheritedMembers = new HashSet<>(allMembers);
        inheritedMembers.removeAll(declaredMembers);
        buffer.addLine("def __init__(");
        buffer.startBlock();
        buffer.addLine("self,");
        allMembers.stream().sorted().forEach(this::generateMemberFormalParameter);
        buffer.endBlock();
        buffer.addLine("):");
        buffer.startBlock();
        buffer.addLine("super(%1$s, self).__init__(", typeName.getClassName());
        buffer.startBlock();
        inheritedMembers.stream().sorted().forEach(this::generateMemberPropagate);
        buffer.endBlock();
        buffer.addLine(")");
        if (!declaredMembers.isEmpty()) {
            declaredMembers.stream().sorted().forEach(this::generateMemberInitialization);
        }
        else {
            buffer.addLine("pass");
        }
        buffer.endBlock();
        buffer.addLine();

        // Generate getters and setters for attributes and links:
        declaredMembers.forEach(this::generateMember);

        // End class:
        buffer.endBlock();
        buffer.addLine();
    }

    private void generateMember(StructMember member) {
        generateGetter(member);
        generateSetter(member);
    }

    private void generateGetter(StructMember member) {
        Name name = member.getName();
        String property = pythonNames.getMemberStyleName(name);
        buffer.addLine("@property");
        buffer.addLine("def %1$s(self):", property);
        buffer.startBlock();
        buffer.startComment();
        buffer.addLine("Returns the value of the `%1$s` property.", property);
        buffer.endComment();
        buffer.addLine("return self._%1$s", property);
        buffer.endBlock();
        buffer.addLine();
    }

    private void generateSetter(StructMember member) {
        Name name = member.getName();
        String property = pythonNames.getMemberStyleName(name);
        buffer.addLine("@%1$s.setter", property);
        buffer.addLine("def %1$s(self, value):", property);
        buffer.startBlock();
        buffer.startComment();
        buffer.addLine("Sets the value of the `%1$s` property.", property);
        buffer.endComment();
        generateCheckType(member, "value");
        buffer.addLine("self._%1$s = value", property);
        buffer.endBlock();
        buffer.addLine();
    }

    private void generateCheckType(StructMember member, String value) {
        Type type = member.getType();
        if (type instanceof StructType || type instanceof EnumType) {
            Name name = member.getName();
            String property = pythonNames.getMemberStyleName(name);
            PythonClassName typeName = pythonNames.getTypeName(type);
            buffer.addLine("Struct._check_type('%1$s', %2$s, %3$s)", property, value, typeName.getClassName());
        }
    }

    private void generateEnum(EnumType type) {
        // Begin class:
        PythonClassName typeName = pythonNames.getTypeName(type);
        buffer.addLine("@unique");
        buffer.addLine("class %1$s(Enum):", typeName.getClassName());

        // Begin body:
        buffer.startBlock();

        // Values:
        type.values().sorted().forEach(this::generateEnumValue);
        buffer.addLine();

        // Constructor:
        buffer.addLine("def __init__(self, image):");
        buffer.startBlock();
        buffer.addLine("self._image = image");
        buffer.endBlock();
        buffer.addLine();

        // Method to convert to string:
        buffer.addLine("def __str__(self):");
        buffer.startBlock();
        buffer.addLine("return self._image");
        buffer.endBlock();
        buffer.addLine();

        // End body:
        buffer.endBlock();
        buffer.addLine();
    }

    private void generateEnumValue(EnumValue value) {
        String constantName = pythonNames.getConstantStyleName(value.getName());
        String constantValue = pythonNames.getMemberStyleName(value.getName());
        buffer.addLine("%1$s = '%2$s'", constantName, constantValue);
    }

    private void generateMemberFormalParameter(StructMember member) {
        buffer.addLine("%1$s=None,", pythonNames.getMemberStyleName(member.getName()));
    }

    private void generateMemberInitialization(StructMember member) {
        buffer.addLine("self.%1$s = %1$s", pythonNames.getMemberStyleName(member.getName()));
    }

    private void generateMemberPropagate(StructMember member) {
        buffer.addLine("%1$s=%1$s,", pythonNames.getMemberStyleName(member.getName()));
    }
}

