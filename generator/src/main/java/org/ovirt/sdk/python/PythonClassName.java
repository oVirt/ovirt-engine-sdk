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

/**
 * This class represents the fully qualified name of a Python class, composed by the module name and the class.
 */
public class PythonClassName {
    private String moduleName;
    private String className;

    public String getModuleName() {
        return moduleName;
    }

    public void setModuleName(String newModuleName) {
        moduleName = newModuleName;
    }

    public String getClassName() {
        return className;
    }

    public void setClassName(String newClassName) {
        className = newClassName;
    }

    @Override
    public String toString() {
        StringBuilder buffer = new StringBuilder();
        buffer.append(moduleName);
        buffer.append(".");
        buffer.append(className);
        return buffer.toString();
    }
}

