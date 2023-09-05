#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - A function that prints bytes info
 * @p: Object of python
 *
 * Return: No return
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, n, limits;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Objects\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", str);

	if (size >= 10)
		limits = 10;
	else
		limits = size + 1;
	printf(" first %ld bytes:", limits);

	for (n = 0; n < limits; n++)
		if (str[n] >= 0)
			printf(" %02x", str[n]);
		else
			printf(" %2x", 256 + str[n]);
	printf("\n");
}

/**
 * print_python_list - Function that prints list info
 * @p: Object of python
 * Return: No return
 */
void print_python_list(PyObject *p)
{
	long int size, n;
	PyListObject *lists;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	lists = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", lists->allocated);

	for (n = 0; n < size; n++)
	{
		obj = ((PyListObject *)p)->ob_item[n];
		printf("Element %ld: %s\n", n, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
