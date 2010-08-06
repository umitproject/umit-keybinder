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

import platform

if platform.system() == "Windows":
    from win_keybinder import Keybinder
    
    Modifiers = {
        'alt'     : ['Lmenu', 'Rmenu'],
        'ctrl'    : ['Lcontrol', 'Rcontrol'],
        'shift'   : ['Lshift', 'Rshift']
        }
else:
    from linux_keybinder import Keybinder
    
    Modifiers = {
        'alt'     : '<alt>',
        'ctrl'    : '<ctrl>',
        'shift'   : '<shift>'
        }
	
kb = Keybinder()

binds = []

def bind(modifiers, key, handler, param=None):
    """
    Bind a key combination to an handler if keys aren't already binded
    """
    if check_bind(modifiers, key) and kb.bind(modifiers, key, handler, param):
        binds.append((modifiers, key, handler))
        return True
    else:
        return False
    
def unbind(modifiers, key, handler):
    """
    Remove previous created bind
    """
    if not check_bind(modifiers, key):
        kb.unbind(modifiers, key, handler)
        binds.remove((modifiers, key, handler))
        return True
    else:
        return False
    
def unbind_all():
    """
    Remove all binds created
    """
    _binds = list(binds)
    for b in _binds:
        (modifiers, key, handler) = b
        unbind(modifiers, key, handler)
        
def check_bind(modifiers, key):
    """
    Verify if the keyshortcut doesn't exist
    return True if key combination available, False otherwise
    """
    for b in binds:
        (b_modifiers, b_key, _) = b
        if b_modifiers == modifiers and b_key == key:
            return False
    return True