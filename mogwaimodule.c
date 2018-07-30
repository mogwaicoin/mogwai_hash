#include <Python.h>

#include "mogwai.h"

static PyObject *mogwai_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    mogwai_hash((char *)PyBytes_AsString((PyObject*) input), (int)PyBytes_Size((PyObject*) input), output);
#else
    mogwai_hash((char *)PyString_AsString((PyObject*) input), (int)PyString_Size((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef MogwaiMethods[] = {
    { "getPoWHash", mogwai_getpowhash, METH_VARARGS, "Returns the proof of work hash using mogwai hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef MogwaiModule = {
    PyModuleDef_HEAD_INIT,
    "mogwai_hash",
    "...",
    -1,
    MogwaiMethods
};

PyMODINIT_FUNC PyInit_mogwai_hash(void) {
    return PyModule_Create(&MogwaiModule);
}

#else

PyMODINIT_FUNC initmogwai_hash(void) {
    (void) Py_InitModule("mogwai_hash", MogwaiMethods);
}
#endif
