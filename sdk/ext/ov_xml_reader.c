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
#include <structmember.h>

#include <libxml/xmlreader.h>
#include <libxml/xmlstring.h>

#include "ov_xml_module.h"
#include "ov_xml_reader.h"
#include "ov_xml_utils.h"

typedef struct {
    PyObject_HEAD
    PyObject* io;
    xmlTextReaderPtr reader;
} ov_xml_reader_object;

static void
ov_xml_reader_dealloc(ov_xml_reader_object* self) {
    /* Free the libxml reader: */
    xmlTextReaderPtr tmp = self->reader;
    if (tmp != NULL) {
        self->reader = NULL;
        xmlFreeTextReader(tmp);
    }

    /* Decrease references to other objects: */
    Py_XDECREF(self->io);
    self->io = NULL;

    /* Free this object: */
    Py_TYPE(self)->tp_free((PyObject*) self);
}

static int
ov_xml_reader_callback(void* context, char* buffer, int length) {
    PyObject* data = NULL;
    PyObject* io = NULL;
    char* c_data = NULL;
    int c_length = 0;

    /* The context is a reference to the IO object: */
    io = (PyObject*) context;

    /* Read from the Python IO object, and copy the result to the buffer: */
    data = PyObject_CallMethod(io, "read", "i", length);
    if (data == NULL) {
        return 0;
    }
    if (!PyBytes_Check(data)) {
        Py_DECREF(data);
        PyErr_Format(PyExc_Exception, "The read data isn't an array of bytes");
        return -1;
    }
    c_length = PyBytes_Size(data);
    c_data = PyBytes_AsString(data);
    memcpy(buffer, c_data, c_length);
    Py_DECREF(data);

    return c_length;
}

static int
ov_xml_reader_init(ov_xml_reader_object* self, PyObject* args, PyObject* kwds) {
    PyObject* read = NULL;

    /* Extract the values of the parameters: */
    if (!PyArg_ParseTuple(args, "O", &self->io)) {
        return -1;
    }
    if (self->io == NULL) {
        PyErr_Format(PyExc_Exception, "The 'io' parameter is mandatory");
        return -1;
    }
    Py_INCREF(self->io);

    /* Check that the "io" parameter has a "read" method, as this catches most errors caused by passing a wrong
       type of object: */
    read = PyObject_GetAttrString(self->io, "read");
    if (read == NULL) {
        Py_DECREF(self->io);
        self->io = NULL;
        PyErr_Format(
            PyExc_TypeError,
            "The 'io' parameter doesn't look like an IO object, doesn't have a 'read' method"
        );
        return -1;
    }
    Py_DECREF(read);

    /* Create the libxml reader: */
    self->reader = xmlReaderForIO(ov_xml_reader_callback, NULL, self->io, NULL, NULL, 0);
    if (self->reader == NULL) {
        Py_DECREF(self->io);
        self->io = NULL;
        PyErr_Format(PyExc_Exception, "Can't create reader");
        return -1;
    }

    /* Move the cursor to the first node: */
    int rc = xmlTextReaderRead(self->reader);
    if (rc == -1) {
        Py_DECREF(self->io);
        self->io = NULL;
        xmlFreeTextReader(self->reader);
        self->reader = NULL;
        PyErr_Format(PyExc_Exception, "Can't read first node");
        return -1;
    }

    return 0;
}

static PyObject*
ov_xml_reader_read(ov_xml_reader_object* self) {
    int rc = 0;

    rc = xmlTextReaderRead(self->reader);
    if (rc == 0) {
        Py_RETURN_FALSE;
    }
    if (rc == 1) {
        Py_RETURN_TRUE;
    }
    PyErr_Format(PyExc_Exception, "Can't move to next node");
    return NULL;
}

static PyObject*
ov_xml_reader_forward(ov_xml_reader_object* self) {
    int c_type = 0;
    int rc = 0;

    for (;;) {
        c_type = xmlTextReaderNodeType(self->reader);
        if (c_type == -1) {
            PyErr_Format(PyExc_Exception, "Can't get current node type");
            return NULL;
        }
        else if (c_type == XML_READER_TYPE_ELEMENT) {
            Py_RETURN_TRUE;
        }
        else if (c_type == XML_READER_TYPE_END_ELEMENT || c_type == XML_READER_TYPE_NONE) {
            Py_RETURN_FALSE;
        }
        else {
            rc = xmlTextReaderRead(self->reader);
            if (rc == -1) {
                PyErr_Format(PyExc_Exception, "Can't move to next node");
                return NULL;
            }
        }
    }
}

static PyObject*
ov_xml_reader_node_name(ov_xml_reader_object* self) {
    const xmlChar* c_name = NULL;

    c_name = xmlTextReaderConstName(self->reader);
    if (c_name == NULL) {
        Py_RETURN_NONE;
    }
    return PyUnicode_FromString((char*) c_name);
}

static PyObject*
ov_xml_reader_empty_element(ov_xml_reader_object* self) {
    int c_empty = 0;

    c_empty = xmlTextReaderIsEmptyElement(self->reader);
    if (c_empty == -1) {
        PyErr_Format(PyExc_Exception, "Can't check if current element is empty");
        return NULL;
    }
    if (c_empty) {
        Py_RETURN_TRUE;
    }
    Py_RETURN_FALSE;
}

static PyObject*
ov_xml_reader_get_attribute(ov_xml_reader_object* self, PyObject* name) {
    PyObject* value = NULL;
    xmlChar* c_name = NULL;
    xmlChar* c_value = NULL;

    c_name = ov_xml_get_string_parameter("name", name);
    if (c_name == NULL) {
        return NULL;
    }
    c_value = xmlTextReaderGetAttribute(self->reader, c_name);
    if (c_value == NULL) {
        xmlFree(c_name);
        Py_RETURN_NONE;
    }
#if PY_MAJOR_VERSION >= 3
    value = PyUnicode_FromString((char*) c_value);
#else
    value = PyString_FromString((char*) c_value);
#endif
    xmlFree(c_name);
    xmlFree(c_value);
    return value;
}

static PyObject*
ov_xml_reader_read_element(ov_xml_reader_object* self) {
    PyObject* value = NULL;
    int c_empty = 0;
    int c_type = 0;
    int rc = 0;
    xmlChar* c_value = NULL;

    /* Check the type of the current node: */
    c_type = xmlTextReaderNodeType(self->reader);
    if (c_type == -1) {
        PyErr_Format(PyExc_Exception, "Can't get current node type");
        return NULL;
    }
    if (c_type != XML_READER_TYPE_ELEMENT) {
        PyErr_Format(PyExc_Exception, "Current node isn't the start of an element");
        return NULL;
    }

    /* Check if the current node is empty: */
    c_empty = xmlTextReaderIsEmptyElement(self->reader);
    if (c_empty == -1) {
        PyErr_Format(PyExc_Exception, "Can't check if current element is empty");
        return NULL;
    }

    /* For empty values elements is no need to read the value. For non empty values we need to read the value, and check
       if it is NULL, as that means that the value is an empty string. */
    if (c_empty) {
        c_value = NULL;
    }
    else {
        c_value = xmlTextReaderReadString(self->reader);
        if (c_value == NULL) {
            c_value = xmlCharStrdup("");
            if (c_value == NULL) {
                PyErr_Format(PyExc_Exception, "Can't allocate XML string");
                return NULL;
            }
        }
    }

    /* Move to the next element: */
    rc = xmlTextReaderNext(self->reader);
    if (rc == -1) {
        if (c_value != NULL) {
            xmlFree(c_value);
        }
        PyErr_Format(PyExc_Exception, "Can't move to the next element");
        return NULL;
    }

    /* Return the result: */
    if (c_value == NULL) {
        Py_RETURN_NONE;
    }
#if PY_MAJOR_VERSION >= 3
    value = PyUnicode_FromString((char*) c_value);
#else
    value = PyString_FromString((char*) c_value);
#endif
    xmlFree(c_value);
    return value;
}

static PyObject*
ov_xml_reader_read_elements(ov_xml_reader_object* self) {
    PyObject* element = NULL;
    PyObject* list = NULL;
    int c_empty = 0;
    int c_type = 0;
    int rc = 0;

    /* This method assumes that the reader is positioned at the element that contains the values to read. For example
       if the XML document is the following:

       <list>
         <value>first</value>
         <value>second</value>
       </list>

       The reader should be positioned at the <list> element. The first thing we need to do is to check that: */
    c_type = xmlTextReaderNodeType(self->reader);
    if (c_type == -1) {
        PyErr_Format(PyExc_Exception, "Can't get current node type");
        goto error;
    }
    if (c_type != XML_READER_TYPE_ELEMENT) {
        PyErr_Format(PyExc_Exception, "Current node isn't the start of an element");
        goto error;
    }

    /* If we are indeed posititoned in the first element, then we need to check if it is empty, <list/>, as we will need
       this later, after discarding the element: */
    c_empty = xmlTextReaderIsEmptyElement(self->reader);
    if (c_empty == -1) {
        PyErr_Format(PyExc_Exception, "Can't check if current element is empty");
        goto error;
    }

    /* Now we need to discard the current element, as we are interested only in the nested <value>...</value>
       elements: */
    rc = xmlTextReaderRead(self->reader);
    if (rc == -1) {
        PyErr_Format(PyExc_Exception, "Can't move to next node");
        goto error;
    }

    /* Create the list that will contain the results: */
    list = PyList_New(0);
    if (list == NULL) {
        PyErr_Format(PyExc_Exception, "Can't allocate list");
        goto error;
    }

    /* At this point, if the start element was empty, we don't need to do anything else: */
    if (c_empty) {
        goto success;
    }

    /* Process the nested elements: */
    for (;;) {
        c_type = xmlTextReaderNodeType(self->reader);
        if (c_type == -1) {
            PyErr_Format(PyExc_Exception, "Can't get current node type");
            goto error;
        }
        else if (c_type == XML_READER_TYPE_ELEMENT) {
            element = ov_xml_reader_read_element(self);
            if (element == NULL) {
                goto error;
            }
            rc = PyList_Append(list, element);
            if (rc == -1) {
                PyErr_Format(PyExc_Exception, "Can't extend list");
                goto error;
            }
        }
        else if (c_type == XML_READER_TYPE_END_ELEMENT || c_type == XML_READER_TYPE_NONE) {
            break;
        }
        else {
            rc = xmlTextReaderNext(self->reader);
            if (rc == -1) {
                PyErr_Format(PyExc_Exception, "Can't move to the next node");
                goto error;
            }
        }
    }

    /* Once all the nested <value>...</value> elements are processed the reader will be positioned at the closing
       </list> element, or at the end of the document. If it is the closing element then we need to discard it. */
    if (c_type == XML_READER_TYPE_END_ELEMENT) {
        rc = xmlTextReaderRead(self->reader);
        if (rc == -1) {
            PyErr_Format(PyExc_Exception, "Can't move to the next node");
            goto error;
        }
    }

success:
    return list;

error:
    if (list != NULL) {
        Py_DECREF(list);
    }
    return NULL;
}

static PyObject*
ov_xml_reader_next_element(ov_xml_reader_object* self) {
    int rc;

    rc = xmlTextReaderNext(self->reader);
    if (rc == 0) {
        Py_RETURN_FALSE;
    }
    if (rc == 1) {
        Py_RETURN_TRUE;
    }
    PyErr_Format(PyExc_Exception, "Can't move to the next element");
    return NULL;
}

static PyObject*
ov_xml_reader_close(ov_xml_reader_object* self) {
    xmlFreeTextReader(self->reader);
    self->reader = NULL;
    Py_RETURN_NONE;
}

static PyMethodDef ov_xml_reader_methods[] = {
    {
        "read",
        (PyCFunction) ov_xml_reader_read,
        METH_NOARGS,
        "Reads the next XML event from the input."
    },

    {
        "forward",
        (PyCFunction) ov_xml_reader_forward,
        METH_NOARGS,
        "Jumps to the next start tag, end tag or end of document. Returns `True` if stopped at an start tag, `False` "
        "otherwise."
    },

    {
        "node_name",
        (PyCFunction) ov_xml_reader_node_name,
        METH_NOARGS,
        "Returns the name of the current element."
    },

    {
         "empty_element",
         (PyCFunction) ov_xml_reader_empty_element,
         METH_NOARGS,
         "Returns a boolean value indicating if the current element is empty."
    },

    {
         "get_attribute",
         (PyCFunction) ov_xml_reader_get_attribute,
         METH_O,
         "Gets the value of the given attribute."
    },

    {
         "read_element",
         (PyCFunction) ov_xml_reader_read_element,
         METH_NOARGS,
         "Reads a string value, assuming that the cursor is positioned at the start element that contains the value."
    },

    {
         "read_elements",
         (PyCFunction) ov_xml_reader_read_elements,
         METH_NOARGS,
         "Reads a list of string values, assuming that the cursor is positioned at the start element of the element "
         "that contains the first value."
    },

    {
         "next_element",
         (PyCFunction) ov_xml_reader_next_element,
         METH_NOARGS,
         "Jumps to the beginning of the next element."
    },

    {
         "close",
         (PyCFunction) ov_xml_reader_close,
         METH_NOARGS,
         "Closes this XML reader and releases all the related resources."
    },

    { NULL }
};

static PyTypeObject ov_xml_reader_type = {
#if PY_MAJOR_VERSION >= 3
    PyVarObject_HEAD_INIT(NULL, 0)
#else
    PyObject_HEAD_INIT(NULL)
    /* ob_size           */ 0,
#endif
    /* tp_name           */ OV_XML_MODULE_NAME "." "XmlReader",
    /* tp_basicsize      */ sizeof(ov_xml_reader_object),
    /* tp_itemsize       */ 0,
    /* tp_dealloc        */ (destructor) ov_xml_reader_dealloc,
    /* tp_print          */ 0,
    /* tp_getattr        */ 0,
    /* tp_setattr        */ 0,
    /* tp_compare        */ 0,
    /* tp_repr           */ 0,
    /* tp_as_number      */ 0,
    /* tp_as_sequence    */ 0,
    /* tp_as_mapping     */ 0,
    /* tp_hash           */ 0,
    /* tp_call           */ 0,
    /* tp_str            */ 0,
    /* tp_getattro       */ 0,
    /* tp_setattro       */ 0,
    /* tp_as_buffer      */ 0,
    /* tp_flags          */ Py_TPFLAGS_DEFAULT,
    /* tp_doc            */
    "This is an utility class used to read XML documents using an streaming approach. It is intended for use by other "
    "components of the SDK. Refrain from using it directly, as backwards compatibility isn't guaranteed. ",
    /* tp_traverse       */ 0,
    /* tp_clear          */ 0,
    /* tp_richcompare    */ 0,
    /* tp_weaklistoffset */ 0,
    /* tp_iter           */ 0,
    /* tp_iternext       */ 0,
    /* tp_methods        */ ov_xml_reader_methods,
    /* tp_members        */ 0,
    /* tp_geteset        */ 0,
    /* tp_base           */ 0,
    /* tp_dict           */ 0,
    /* tp_descr_get      */ 0,
    /* tp_descr_set      */ 0,
    /* tp_dictoffset     */ 0,
    /* tp_init           */ (initproc) ov_xml_reader_init,
    /* tp_alloc          */ 0,
    /* tp_new            */ 0,
};

void ov_xml_reader_define(void) {
    /* Create the class: */
    ov_xml_reader_type.tp_new = PyType_GenericNew;
    if (PyType_Ready(&ov_xml_reader_type) < 0) {
        return;
    }

    /* Add the classes to the module: */
    Py_INCREF(&ov_xml_reader_type);
    PyModule_AddObject(ov_xml_module, "XmlReader", (PyObject*) &ov_xml_reader_type);
}
