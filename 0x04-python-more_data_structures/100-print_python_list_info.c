#include <stdio.h>
#include "Python.h"
/**
 * print_python_list_info - it prints the info of the given list
 * @p: the list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	int i;

	list = (PyListObject *) p;
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < list->ob_base.ob_size; i++)
	{
		/* changing between -> and . may cause unpredictable error */
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
	}
}
