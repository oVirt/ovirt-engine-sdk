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

package org.ovirt.engine.sdk.generator.common;

import java.io.IOException;

/**
 * Base class for code generators.
 */
public abstract class AbstractCodegen {

    private final String distPath;

    /**
     * @param distPath
     *            path to generate the code in
     */
    public AbstractCodegen(String distPath) {
        super();
        this.distPath = distPath;
    }

    /**
     * Cleans the package, generates new code and compiles it.
     */
    public void generate() throws IOException {
        doGenerate(this.distPath);
    }

    /**
     * Generates the code
     *
     * @param distPath
     *            directory to generates the code at
     */
    protected abstract void doGenerate(String distPath) throws IOException;
}
