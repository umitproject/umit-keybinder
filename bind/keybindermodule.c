/*
 Copyright (C) 2010 Adriano Monteiro Marques.

 Author: Diogo Pinheiro <diogormpinheiro@gmail.com>

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
*/

#include <Python.h>
#include "../code/bind.c"
#include "keybindermodule.h"


typedef struct UserData_ {
	PyObject *handler;
	PyObject *args;
	char *keystring;
} UserData;

void handler_func (const char *key, gpointer userdata)
{
    UserData *ud = (UserData*) userdata;
    PyEval_CallObject(ud->handler, ud->args);
}


static PyObject *_init(PyObject *self, PyObject *args)
{
    keybinder_init();
    return Py_None;
}

static PyObject *_bind(PyObject *self, PyObject *args)
{
    char* keystring;
    PyObject *handler;
    PyObject *args1, *args2;
    UserData *userdata;

	int size = PyTuple_Size(args);
	
    args1 = PySequence_GetSlice(args, 0, 2);
    args2 = PySequence_GetSlice(args, 2, size);
	    
    PyArg_ParseTuple(args1, "sO", &keystring, &handler);

    if(PyCallable_Check(handler))
    {
		userdata = (UserData*) malloc(sizeof(UserData));
		userdata->handler = handler;
		userdata->args = args2;
		userdata->keystring = g_strdup(keystring);
	
		if(keybinder_bind(keystring, &handler_func, userdata))
			Py_RETURN_TRUE;
		else
			Py_RETURN_FALSE;
    }
    else
    {
		PyErr_SetString(PyExc_TypeError, "parameter must be callable");
		return NULL;
    }

    return NULL;
}

static PyObject *_unbind(PyObject *self, PyObject *args)
{
    char* keystring;
    PyObject *handler;
    PyArg_ParseTuple(args, "sO", &keystring, &handler);
    keybinder_unbind(keystring, &handler_func);
    return Py_None;
}

PyMODINIT_FUNC
initkeybinder(void)
{
	(void)Py_InitModule("keybinder",keybinderMethods);
}
