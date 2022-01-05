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

#include <Python.h>

#include "ov_xml_module.h"
#include "ov_xml_reader.h"
#include "ov_xml_writer.h"

#if PY_MAJOR_VERSION >= 3
PyObject* PyInit_xml(void) {
#else
void initxml(void) {
#endif

    /* Define the module: */
    ov_xml_module_define();
#if PY_MAJOR_VERSION >= 3
    if (ov_xml_module == NULL) {
        return NULL;
    }
#endif

    /* Define the classes: */
    ov_xml_reader_define();
    ov_xml_writer_define();

#if PY_MAJOR_VERSION >= 3
    return ov_xml_module;
#endif
}
