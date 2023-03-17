#include <stdio.h>
#include <string.h>
#include "Python.h"
void print_python_bytes(PyObject *p);
/**
 * print_python_list_info - it prints the info of the given list
 * @p: the list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	int i;

	list = (PyListObject *) p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < list->ob_base.ob_size; i++)
	{
		/* changing between -> and . may cause unpredictable error */
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
	 if (strcmp(list->ob_item[i]->ob_type->tp_name, "bytes") == 0)
	{
	print_python_bytes((PyObject *) list->ob_item[i]);
}
}}
void print_python_bytes(PyObject *p)
{
	PyBytesObject *pb;
	long unsigned int i, size;
	
	printf("[.] bytes object info\n");
	/* checks if the given PyObject is a valid PyByteObject */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	pb = (PyBytesObject *) p;
	/* returns the size of the PyByteObject,
	 *  the reason we don't use strlen is 
	 *  because it terminates at unwanted 0 byte but this one doesn't*/
	size = PyBytes_Size(p);
	printf("  size: %lu\n", size);
	/* pb->ob_sval is the data which the byte object is stored*/
	printf("  trying string: %s\n", pb->ob_sval);
	if (size < 10)
		printf("  first %lu bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i < 10 && i <= size; i++)
	{
		if (pb->ob_sval[i] == 0)
			printf(" 00");
		else
			printf(" %hhx",(char) pb->ob_sval[i]);
	} 
	printf("\n");
}
