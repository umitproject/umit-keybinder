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

import pythoncom, pyHook

class Keybinder(object):
    """
    """
    
    def __init__(self):
        """
        """
        # create a hook manager
        hm = pyHook.HookManager()
        # watch for all keyboard events
        hm.KeyDown = self.OnKeyboardEvent
        # set the hook
        hm.HookKeyboard()
        
        self.binds = {}
        self.modifiers = ['Lmenu', 'Rmenu', 'Lcontrol', 'Rcontrol', 'Lshift', 'Rshift']
        self.modifier = None 

    def bind(self, modifier, key, handler, param=None):
        """
        Bind a key to an handler function
        """
        key = key.upper()
        if modifier==None:
            self.binds[(None,key)] = [handler, param]
        else:
            self.binds[(modifier[0],key)] = [handler, param]
            self.binds[(modifier[1],key)] = [handler, param]
    
    def unbind(self, modifier, key, handler):
        """
        Unbind an already binded key
        """
        key = key.upper()
        if modifier==None:
            if key in self.binds:
                del self.binds[(None, key)]
        else:
            if (modifier[0],key) in self.binds:
                del self.binds[(modifier[0],key)]
            if (modifier[1],key) in self.binds:
                del self.binds[(modifier[0],key)]
            
    def OnKeyboardEvent(self, event):
        """
        """        
        key = event.Key
        
        changed = False
        
        if key in self.modifiers:
            self.modifier = key

        if (self.modifier,key) in self.binds:
            func = self.binds[(self.modifier,key)][0]
            params = self.binds[(self.modifier,key)][1]
            func(params)
            
        if key not in self.modifiers:
            self.modifier = None
                    
        return True