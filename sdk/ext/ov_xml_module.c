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

#include <Python.h>

#include "ov_xml_module.h"

/* Module: */
PyObject* ov_xml_module;

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef ov_xml_module_definition = {
    PyModuleDef_HEAD_INIT,
    /* m_name     */ OV_XML_MODULE_NAME,
    /* m_doc      */ 0,
    /* m_size     */ 0,
    /* m_methods  */ 0,
    /* m_reload   */ 0,
    /* m_traverse */ 0,
    /* m_clear    */ 0,
    /* m_free     */ 0
};
#endif

void ov_xml_module_define(void) {
#if PY_MAJOR_VERSION >= 3
    ov_xml_module = PyModule_Create(&ov_xml_module_definition);
#else
    ov_xml_module = Py_InitModule(OV_XML_MODULE_NAME, NULL);
#endif
}
