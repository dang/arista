#!/usr/bin/env python

"""
	Arista Utilities
	================
	A set of utility methods to do various things inside of Arista.
	
	License
	-------
	Copyright 2009 Daniel G. Taylor <dan@programmer-art.org>
	
	This file is part of Arista.

	Arista is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	Foobar is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with Arista.  If not, see <http://www.gnu.org/licenses/>.
"""

import logging
import os
import sys

def get_search_paths():
    """
        Get a list of paths that are searched for installed resources.
        
        @rtype: list
        @return: A list of paths to search in the order they will be searched
    """
    return [
        os.getcwd(),
        os.path.expanduser(os.path.join("~", ".arista")),
        os.path.join(sys.prefix, "share", "arista"),
        os.path.join(sys.prefix, "local", "share", "arista"),
    ]

def get_path(*parts):
    """
        Get a path, searching first in the current directory, then the user's
        home directory, then sys.prefix, then sys.prefix + "local".
        
            >>> get_path("presets", "computer.xml")
            '/usr/share/arista/presets/computer.xml'
            >>> get_path("presets", "my_cool_preset.xml")
            '/home/dan/.arista/presets/my_cool_preset.xml'
        
        @type parts: str
        @param parts: The parts of the path to get that you would normally 
                      send to os.path.join
        @rtype: str
        @return: The full path to the relative path passed in
        @raise IOError: The path cannot be found in any location
    """
    path = os.path.join(*parts)
    
    for search in get_search_paths():
        full = os.path.join(search, path)
        if os.path.exists(full):
            return full
    else:
        raise IOError("Can't find %s in any known prefix!" % path)
