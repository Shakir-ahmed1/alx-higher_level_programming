#include <stdio.h>
#include <string.h>
#include "Python.h"
/**
 * print_python_string - prints python string using c
 * @p: the pyobject pointer
 */
void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p)) {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // Get string type and length
    const char *type = PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object";
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    
    // Get string value
    const char *value = PyUnicode_AsUTF8(p);

    // Print string object information
    printf("[.] string object info\n");
    printf("  type: %s\n", type);
    printf("  length: %zd\n", length);
    printf("  value: %s\n", value);
}