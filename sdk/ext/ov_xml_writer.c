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

#include <libxml/xmlwriter.h>
#include <libxml/xmlstring.h>

#include "ov_xml_module.h"
#include "ov_xml_writer.h"
#include "ov_xml_utils.h"

/* Imported modules: */
static PyObject* io_module;

/* Imported classes: */
static PyObject* bytes_io_class;

typedef struct {
    PyObject_HEAD
    PyObject* io;
    xmlTextWriterPtr writer;
} ov_xml_writer_object;

static void
ov_xml_writer_dealloc(ov_xml_writer_object* self) {
    /* Free the libxml reader: */
    xmlTextWriterPtr tmp = self->writer;
    if (tmp != NULL) {
        self->writer = NULL;
        xmlFreeTextWriter(tmp);
    }

    /* Decrease references to other objects: */
    Py_XDECREF(self->io);
    self->io = NULL;

    /* Free this object: */
    Py_TYPE(self)->tp_free((PyObject*) self);
}

static int
ov_xml_writer_callback(void* context, const char* buffer, int length) {
    PyObject* data = NULL;
    PyObject* io = NULL;
    PyObject* result = NULL;

    /* The context is a reference to the IO object: */
    io = (PyObject*) context;

    /* Convert the buffer to a Python array of bytes and write it to the IO object, using the "write" method: */
#if PY_MAJOR_VERSION >= 3
    data = PyBytes_FromStringAndSize(buffer, length);
#else
    data = PyString_FromStringAndSize(buffer, length);
#endif
    if (data == NULL) {
        return -1;
    }
    result = PyObject_CallMethod(io, "write", "O", data);
    if (result == NULL) {
        return -1;
    }
    return length;
}

static int
ov_xml_writer_init(ov_xml_writer_object* self, PyObject* args, PyObject* kwds) {
    static char* kwlist[] = {
        "io",
        "indent",
        NULL
    };
    PyObject* indent = NULL;
    PyObject* io = NULL;
    PyObject* write = NULL;

    /* Extract the values of the parameters: */
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|O", kwlist, &io, &indent)) {
        return -1;
    }

    /* Check that the 'indent' parameter is a boolean: */
    if (indent != NULL && !PyBool_Check(indent)) {
        PyErr_Format(PyExc_TypeError, "The 'indent' parameter must be a boolean");
        return -1;
    }

    /* If the 'io' parameter is None then we need to create a new BytesIO object. Otherwise we need to check
       that it has 'write' method, as this catches most errors caused by passing a wrong type of object: */
    if (io == Py_None) {
        io = PyObject_CallObject(bytes_io_class, NULL);
        if (io == NULL) {
            PyErr_Format(
                PyExc_Exception,
                "Can't create a new instance of 'BytesIO'"
            );
            return -1;
        }
    }
    else {
        write = PyObject_GetAttrString(io, "write");
        if (write == NULL) {
            PyErr_Format(
                PyExc_TypeError,
                "The 'io' parameter doesn't look like an IO object, doesn't have a 'write' method"
            );
            return -1;
        }
        Py_DECREF(write);
    }
    Py_INCREF(io);
    self->io = io;

    /* Create the libxml buffer that writes to the IO object: */
    xmlOutputBufferPtr buffer = xmlOutputBufferCreateIO(ov_xml_writer_callback, NULL, self->io, NULL);
    if (buffer == NULL) {
        Py_DECREF(self->io);
        self->io = NULL;
        PyErr_Format(PyExc_Exception, "Can't create XML buffer");
        return -1;
    }

    /* Create the libxml writer: */
    self->writer = xmlNewTextWriter(buffer);
    if (self->writer == NULL) {
        Py_DECREF(self->io);
        self->io = NULL;
        xmlOutputBufferClose(buffer);
        PyErr_Format(PyExc_Exception, "Can't create XML writer");
        return -1;
    }

    /* Enable indentation: */
    if (indent == Py_True) {
        xmlTextWriterSetIndent(self->writer, 1);
        xmlTextWriterSetIndentString(self->writer, BAD_CAST "  ");
    }

    return 0;
}

static PyObject*
ov_xml_writer_write_start(ov_xml_writer_object* self, PyObject* name) {
    xmlChar* c_name = NULL;
    int rc = 0;

    /* Extract the values of the parameters: */
    c_name = ov_xml_get_string_parameter("name", name);
    if (c_name == NULL) {
        return NULL;
    }

    /* Start the element: */
    rc = xmlTextWriterStartElement(self->writer, c_name);
    if (rc < 0) {
        PyErr_Format(PyExc_Exception, "Can't start XML element with name '%s'", c_name);
        xmlFree(c_name);
        return NULL;
    }

    xmlFree(c_name);
    Py_RETURN_NONE;
}

static PyObject*
ov_xml_writer_write_end(ov_xml_writer_object* self) {
    int rc = 0;

    /* End the element: */
    rc = xmlTextWriterEndElement(self->writer);
    if (rc < 0) {
        PyErr_Format(PyExc_Exception, "Can't end XML element");
        return NULL;
    }

    Py_RETURN_NONE;
}

static PyObject*
ov_xml_writer_write_attribute(ov_xml_writer_object* self, PyObject* args) {
    PyObject* name = NULL;
    PyObject* value = NULL;
    int rc = 0;
    xmlChar* c_name = NULL;
    xmlChar* c_value = NULL;

    /* Extract the values of the parameters: */
    if (!PyArg_ParseTuple(args, "OO", &name, &value)) {
        return NULL;
    }
    c_name = ov_xml_get_string_parameter("name", name);
    if (c_name == NULL) {
        return NULL;
    }
    c_value = ov_xml_get_string_parameter("value", value);
    if (c_value == NULL) {
        xmlFree(c_name);
        return NULL;
    }

    /* Write the attribute: */
    rc = xmlTextWriterWriteAttribute(self->writer, c_name, c_value);
    if (rc < 0) {
        PyErr_Format(PyExc_Exception, "Can't write attribute with name '%s' and value '%s'", c_name, c_value);
        xmlFree(c_name);
        xmlFree(c_value);
        return NULL;
    }

    xmlFree(c_name);
    xmlFree(c_value);
    Py_RETURN_NONE;
}

static PyObject*
ov_xml_writer_write_element(ov_xml_writer_object* self, PyObject* args) {
    PyObject* name = NULL;
    PyObject* value = NULL;
    int rc = 0;
    xmlChar* c_name = NULL;
    xmlChar* c_value = NULL;

    /* Extract the values of the parameters: */
    if (!PyArg_ParseTuple(args, "OO", &name, &value)) {
        return NULL;
    }
    c_name = ov_xml_get_string_parameter("name", name);
    if (c_name == NULL) {
        return NULL;
    }
    c_value = ov_xml_get_string_parameter("value", value);
    if (c_value == NULL) {
        xmlFree(c_name);
        return NULL;
    }

    /* Write the element: */
    rc = xmlTextWriterWriteElement(self->writer, c_name, c_value);
    if (rc < 0) {
        PyErr_Format(PyExc_Exception, "Can't write element with name '%s' and value '%s'", c_name, c_value);
        xmlFree(c_name);
        xmlFree(c_value);
        return NULL;
    }

    xmlFree(c_name);
    xmlFree(c_value);
    Py_RETURN_NONE;
}

static PyObject*
ov_xml_writer_flush(ov_xml_writer_object* self) {
    int rc;

    rc = xmlTextWriterFlush(self->writer);
    if (rc < 0) {
        PyErr_Format(PyExc_Exception, "Can't flush XML writer");
        return NULL;
    }
    Py_RETURN_NONE;
}

static PyObject*
ov_xml_writer_string(ov_xml_writer_object* self) {
    PyObject* raw = NULL;
    PyObject* decoded = NULL;

    /* Flush the writer: */
    if (ov_xml_writer_flush(self) == NULL) {
        return NULL;
    }

    /* Extract the raw bytes from the 'io' object: */
    raw = PyObject_CallMethod(self->io, "getvalue", NULL);
    if (raw == NULL) {
        return NULL;
    }

    /* Convert the raw bytes to UTF-8: */
    decoded = PyObject_CallMethod(raw, "decode", "s", "UTF-8", NULL);
    Py_DECREF(raw);
    if (decoded == NULL) {
        return NULL;
    }

    return decoded;
}

static PyObject*
ov_xml_writer_close(ov_xml_writer_object* self) {
    xmlFreeTextWriter(self->writer);
    self->writer = NULL;
    Py_RETURN_NONE;
}

static PyMethodDef ov_xml_writer_methods[] = {
    {
        "write_start",
        (PyCFunction) ov_xml_writer_write_start,
        METH_O,
        "Writes the start of an element with the given name."
    },

    {
        "write_end",
        (PyCFunction) ov_xml_writer_write_end,
        METH_NOARGS,
        "Writes the end of the current element."
    },

    {
        "write_attribute",
        (PyCFunction) ov_xml_writer_write_attribute,
        METH_VARARGS,
        "Writes an attribute with the given name and value."
    },

    {
        "write_element",
        (PyCFunction) ov_xml_writer_write_element,
        METH_VARARGS,
        "Writes an element with the given name and value."
    },

    {
        "flush",
        (PyCFunction) ov_xml_writer_flush,
        METH_NOARGS,
        "Flushes this writer, sending all the pending output th the underlying IO object."
    },

    {
        "string",
        (PyCFunction) ov_xml_writer_string,
        METH_NOARGS,
        "Return the XML document text generated by this writer so far."
    },

    {
        "close",
        (PyCFunction) ov_xml_writer_close,
        METH_NOARGS,
        "Closes this writer, releasing all the resources it uses. Note that this doesn't close the IO object."
    },

    { NULL }
};

static PyTypeObject ov_xml_writer_type = {
#if PY_MAJOR_VERSION >= 3
    PyVarObject_HEAD_INIT(NULL, 0)
#else
    PyObject_HEAD_INIT(NULL)
    /* ob_size           */ 0,
#endif
    /* tp_name           */ OV_XML_MODULE_NAME "." "XmlWriter",
    /* tp_basicsize      */ sizeof(ov_xml_writer_object),
    /* tp_itemsize       */ 0,
    /* tp_dealloc        */ (destructor) ov_xml_writer_dealloc,
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
    "This is an utility class used to generate XML documents using an streaming approach. It is intended for use by "
    "other components of the SDK. Refrain from using it directly, as backwards compatibility isn't guaranteed.",
    /* tp_traverse       */ 0,
    /* tp_clear          */ 0,
    /* tp_richcompare    */ 0,
    /* tp_weaklistoffset */ 0,
    /* tp_iter           */ 0,
    /* tp_iternext       */ 0,
    /* tp_methods        */ ov_xml_writer_methods,
    /* tp_members        */ 0,
    /* tp_geteset        */ 0,
    /* tp_base           */ 0,
    /* tp_dict           */ 0,
    /* tp_descr_get      */ 0,
    /* tp_descr_set      */ 0,
    /* tp_dictoffset     */ 0,
    /* tp_init           */ (initproc) ov_xml_writer_init,
    /* tp_alloc          */ 0,
    /* tp_new            */ 0,
};

void ov_xml_writer_define(void) {
    /* Create the class: */
    ov_xml_writer_type.tp_new = PyType_GenericNew;
    if (PyType_Ready(&ov_xml_writer_type) < 0) {
        return;
    }

    /* Add the classes to the module: */
    Py_INCREF(&ov_xml_writer_type);
    PyModule_AddObject(ov_xml_module, "XmlWriter", (PyObject*) &ov_xml_writer_type);

    /* Import modules: */
    io_module = PyImport_ImportModule("io");
    if (io_module == NULL) {
        PyErr_Format(PyExc_Exception, "Can't import the 'io' module");
        return;
    }
    Py_INCREF(io_module);

    /* Locate classes: */
    bytes_io_class = PyObject_GetAttrString(io_module, "BytesIO");
    if (bytes_io_class == NULL) {
        PyErr_Format(PyExc_Exception, "Can't locate the 'io.BytesIO' class");
        return;
    }
    Py_INCREF(bytes_io_class);
}
