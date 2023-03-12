#include <stdio.h>
#include "Python.h"
/**
 * print_python_list_info - it prints the info of the given list
 * @p: the list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;

	list = (PyListObject *) p;
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
}
