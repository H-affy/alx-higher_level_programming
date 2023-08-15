<<<<<<< HEAD
#include <python.h>
=======
#include <Python.h>
>>>>>>> 7bf58fba3bce75565b2ba13a1f0ee1764fe5b2ee
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
<<<<<<< HEAD
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", ohj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
=======
        long int size = PyList_Size(p);
        int i;
        PyListObject *obj = (PyListObject *)p;

        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", obj->allocated);
        for (i = 0; i < size; i++)
                printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
>>>>>>> 7bf58fba3bce75565b2ba13a1f0ee1764fe5b2ee
}
