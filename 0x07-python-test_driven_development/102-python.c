#include <stdio.h>
#include <string.h>
#include "Python.h"
/**
 * print_python_string - prints python string using c
 * @p: the pyobject pointer
 */
void print_python_string(PyObject *p)
{
	PyObject *str, *str2;

	(void)str2;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	str2 = PyObject_Repr(p);
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(str));
}
