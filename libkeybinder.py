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

def bind(modifiers, key, handler, param=None):
    """
    """
    kb.bind(modifiers, key, handler, param)
    
def unbind(modifiers, key, handler):
    """
    """
    kb.unbind(modifiers, key, handler)