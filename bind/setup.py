# Copyright (C) 2010 Adriano Monteiro Marques.
#
# Author: Diogo Pinheiro <diogormpinheiro@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import os
import sys
import shutil

from distutils.core import setup, Extension


def getoutput(cmd):
    """Return output (stdout or stderr) of executing cmd in a shell."""
    return getstatusoutput(cmd)[1]

def getstatusoutput(cmd):
    """Return (status, output) of executing cmd in a shell."""
    if sys.platform == 'win32':
        pipe = os.popen(cmd, 'r')
        text = pipe.read()
        sts = pipe.close() or 0
        if text[-1:] == '\n':
            text = text[:-1]
        return sts, text
    else:
        from commands import getstatusoutput
        return getstatusoutput(cmd)

def pkc_get_include_dirs(names):
    if not isinstance(names, tuple):
        names = (names,)
    retval = []
    for name in names:
        output = getoutput('pkg-config --cflags-only-I %s' % name)
        retval.extend(output.replace('-I', '').split())
    retval.append('../')
    return retval

def pkc_get_libraries(names):
    if not isinstance(names, tuple):
        names = (names,)
    retval = []
    for name in names:
        output = getoutput('pkg-config --libs-only-l %s' % name)
        retval.extend(output.replace('-l', '').split())
    return retval

def pkc_get_library_dirs(names):
    if not isinstance(names, tuple):
        names = (names,)
    retval = []
    for name in names:
        output = getoutput('pkg-config --libs-only-L %s' % name)
        retval.extend(output.replace('-L', '').split())
    return retval


keybinder_module = Extension('keybinder',
                          include_dirs=pkc_get_include_dirs('gtk+-2.0 gdk-2.0'),
                          libraries=pkc_get_libraries('gtk+-2.0 gdk-2.0'),
                          library_dirs=pkc_get_library_dirs('gtk+-2.0 gdk-2.0'),
                          extra_compile_args = ['-Wall', '-ggdb'],
                          sources = ['keybindermodule.c'])

setup (name = 'umit-keybinder',
       version = '0.1',
       author='Diogo Pinheiro',
       author_email='diogopinheiro@gmail.com',
       description = 'Umit keybinder',
       ext_modules = [keybinder_module])
