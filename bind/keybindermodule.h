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

#ifndef BIND_KEYBINDER_H
#define BIND_KEYBINDER_H


#include <stdio.h>

#include <glib.h>


static PyObject *_init(PyObject *self, PyObject *args);
static PyObject *_bind(PyObject *self, PyObject *args);
static PyObject *_unbind(PyObject *self, PyObject *args);


static PyMethodDef keybinderMethods[] = 
{
	{"init",_init,METH_VARARGS, "init keybinder"},
	{"bind",_bind,METH_VARARGS, "bind a key"},
	{"unbind",_unbind,METH_VARARGS, "unbind a key"},
	{NULL,NULL,0,NULL}
};


PyMODINIT_FUNC initkeybinder(void);

#endif

