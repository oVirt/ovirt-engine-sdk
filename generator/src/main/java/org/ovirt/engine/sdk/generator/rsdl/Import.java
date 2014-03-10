//
// Copyright (c) 2014 Red Hat, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

package org.ovirt.engine.sdk.generator.rsdl;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.ovirt.engine.sdk.generator.rsdl.templates.CopyrightTemplate;
import org.ovirt.engine.sdk.generator.rsdl.templates.ImportsTemplate;

public class Import {
    public static String getImports() {
        String copyrightText = new CopyrightTemplate().evaluate();
        String importsText = new ImportsTemplate().evaluate();
        return
            copyrightText +
            "'''Generated at: " +
                new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSSSSS").format(new Date()) +
            "'''\n\n" +
            importsText
        ;
    }
}
