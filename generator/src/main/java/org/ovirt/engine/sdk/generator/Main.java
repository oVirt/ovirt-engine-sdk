//
// Copyright (c) 2012 Red Hat, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//           http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

package org.ovirt.engine.sdk.generator;

import org.ovirt.engine.sdk.generator.rsdl.RsdlCodegen;
import org.ovirt.engine.sdk.generator.rsdl.RsdlData;
import org.ovirt.engine.sdk.generator.xsd.XsdData;
import org.ovirt.engine.sdk.generator.xsd.XsdCodegen;

import java.io.File;

public class Main {
    public static void main(String[] args) throws Exception {
        // Parse the command line parameters:
        File xsdFile = null;
        File rsdlFile = null;
        for (int i = 0; i < args.length; i++) {
            switch (args[i]) {
            case "--xsd":
                i++;
                if (i < args.length) {
                    xsdFile = new File(args[i]);
                }
                break;
            case "--rsdl":
                i++;
                if (i < args.length) {
                    rsdlFile = new File(args[i]);
                }
                break;
            default:
                System.err.println("Unknown command line parameter \"" + args[i] + "\".");
                System.exit(1);
            }
        }
        if (xsdFile == null || rsdlFile == null) {
            System.err.println("Missing required parameters.");
            System.exit(1);
        }

        // Load the XML schema and the RSDL metadata:
        XsdData.getInstance().load(xsdFile);
        RsdlData.getInstance().load(rsdlFile);

        // Generate parameter classes:
        new XsdCodegen().generate();

        // Generate broker classes:
        new RsdlCodegen().generate();
    }
}
