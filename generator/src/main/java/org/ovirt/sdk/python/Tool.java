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
import javax.enterprise.context.ApplicationScoped;
import javax.enterprise.inject.Any;
import javax.enterprise.inject.Instance;
import javax.inject.Inject;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import org.apache.commons.io.FileUtils;
import org.ovirt.api.metamodel.analyzer.ModelAnalyzer;
import org.ovirt.api.metamodel.concepts.Attribute;
import org.ovirt.api.metamodel.concepts.Model;
import org.ovirt.api.metamodel.concepts.NameParser;
import org.ovirt.api.metamodel.concepts.StructType;

@ApplicationScoped
public class Tool {
    // The names of the command line options:
    private static final String MODEL_OPTION = "model";
    private static final String OUT_OPTION = "out";

    // Reference to the objects used to calculate Python names:
    @Inject private PythonNames pythonNames;

    // References to the generators:
    @Inject @Any
    private Instance<PythonGenerator> generators;

    public void run(String[] args) throws Exception {
        // Create the command line options:
        Options options = new Options();

        // Options for the locations of files and directories:
        options.addOption(Option.builder()
            .longOpt(MODEL_OPTION)
            .desc("The directory or .jar file containing the source model files.")
            .type(File.class)
            .required(true)
            .hasArg(true)
            .argName("DIRECTORY|JAR")
            .build()
        );

        // Options for the location of the generated Python sources:
        options.addOption(Option.builder()
            .longOpt(OUT_OPTION)
            .desc("The directory where the generated Python source will be created.")
            .type(File.class)
            .required(false)
            .hasArg(true)
            .argName("DIRECTORY")
            .build()
        );

        // Parse the command line:
        CommandLineParser parser = new DefaultParser();
        CommandLine line = null;
        try {
            line = parser.parse(options, args);
        }
        catch (ParseException exception) {
            HelpFormatter formatter = new HelpFormatter();
            formatter.setSyntaxPrefix("Usage: ");
            formatter.printHelp("python-tool [OPTIONS]", options);
            System.exit(1);
        }

        // Extract the locations of files and directories from the command line:
        File modelFile = (File) line.getParsedOptionValue(MODEL_OPTION);
        File outDir = (File) line.getParsedOptionValue(OUT_OPTION);

        // Analyze the model files:
        Model model = new Model();
        ModelAnalyzer modelAnalyzer = new ModelAnalyzer();
        modelAnalyzer.setModel(model);
        modelAnalyzer.analyzeSource(modelFile);

        // Add the built-in types:
        addBuiltinTypes(model);

        // Run the generators:
        if (outDir != null) {
            FileUtils.forceMkdir(outDir);
            for (PythonGenerator generator : generators) {
                generator.setOut(outDir);
                generator.generate(model);
            }
        }
    }

    /**
     * Adds built-in types to the model.
     */
    private void addBuiltinTypes(Model model) {
        // Note that the order is important. For example, the "Fault" type must be added before the "Action" type
        // because actions have elements whose type is "Fault".
        addFaultType(model);
        addActionType(model);
    }

    /**
     * Adds the {@code Fault} type to the model.
     */
    private void addFaultType(Model model) {
        // Create the tyep:
        StructType faultType = new StructType();
        faultType.setName(NameParser.parseUsingCase("Fault"));

        // Add the "reason" attribute:
        Attribute reasonAttribute = new Attribute();
        reasonAttribute.setName(NameParser.parseUsingCase("Reason"));
        reasonAttribute.setType(model.getStringType());
        reasonAttribute.setDeclaringType(faultType);
        faultType.addAttribute(reasonAttribute);

        // Add the "detail" attribute:
        Attribute detailAttribute = new Attribute();
        detailAttribute.setName(NameParser.parseUsingCase("Detail"));
        detailAttribute.setType(model.getStringType());
        detailAttribute.setDeclaringType(faultType);
        faultType.addAttribute(detailAttribute);

        // Add the type to the model:
        model.addType(faultType);
    }

    /**
     * Adds the {@code Action} type to the model.
     */
    private void addActionType(Model model) {
        // Create the type:
        StructType actionType = new StructType();
        actionType.setName(NameParser.parseUsingCase("Action"));

        // Add the "status" attribute:
        Attribute statusAttribute = new Attribute();
        statusAttribute.setName(NameParser.parseUsingCase("Status"));
        statusAttribute.setType(model.getType(NameParser.parseUsingCase("Status")));
        statusAttribute.setDeclaringType(actionType);
        actionType.addAttribute(statusAttribute);

        // Add the "fault" attribute:
        Attribute faultAttribute = new Attribute();
        faultAttribute.setName(NameParser.parseUsingCase("Fault"));
        faultAttribute.setType(model.getType(NameParser.parseUsingCase("Fault")));
        faultAttribute.setDeclaringType(actionType);
        actionType.addAttribute(faultAttribute);

        // Add the type to the model:
        model.addType(actionType);
    }
}
