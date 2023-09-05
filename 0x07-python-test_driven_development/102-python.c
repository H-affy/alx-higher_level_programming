#include "python.h"

/**
 * print_python_string - function that prints python strings
 * @p: the pyobject string
 */
void print_python_string(PyObject *p)
{
	long int len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->0b_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] invalid String Object\n");
		return;
	}
	length ((PyASCIIObject *)(p))->length;
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		printf(" type: concept unicode  object\n");
	printf(" length: %ld\n", length);
	printf(" value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
