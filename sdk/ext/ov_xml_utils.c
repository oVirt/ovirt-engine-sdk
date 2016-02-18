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

#include <libxml/xmlstring.h>

#include "ov_xml_utils.h"

xmlChar*
ov_xml_get_string_parameter(const char* name, PyObject* value) {
#if PY_MAJOR_VERSION >= 3
#else
    PyObject* encoded = NULL;
#endif
    xmlChar* result = NULL;

#if PY_MAJOR_VERSION >= 3
    if (PyUnicode_Check(value)) {
        result = xmlCharStrdup(PyUnicode_AsUTF8(value));
        if (result == NULL) {
            PyErr_Format(PyExc_TypeError, "Can't allocate XML string");
            return NULL;
        }
        return result;
    }
#else
    if (PyString_Check(value)) {
        result = xmlCharStrdup(PyString_AsString(value));
        if (result == NULL) {
            PyErr_Format(PyExc_TypeError, "Can't allocate XML string");
            return NULL;
        }
        return result;
    }
    if (PyUnicode_Check(value)) {
        encoded = PyUnicode_AsUTF8String(value);
        if (encoded == NULL) {
            return NULL;
        }
        result = xmlCharStrdup(PyString_AsString(encoded));
        Py_DECREF(encoded);
        if (result == NULL) {
            PyErr_Format(PyExc_TypeError, "Can't allocate XML string");
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError, "The '%s' parameter must be a string", name);
    return NULL;
}
