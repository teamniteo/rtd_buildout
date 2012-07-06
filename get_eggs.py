#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get the eggs name from setup.py. For all subdirectories of a directory.

Usualy you want to add all the eggs build in a directory (usualy in src/).
So the simplest way is to look up the name via "python setup.py --name"

This script has to be rewriten to somethong like buildout.eggtractor
"""

from os import listdir, path
from subprocess import check_output

def get_setup_paths(dir="src"):
    """Return a list of all setup.py rel paths."""
    paths = []

    for subdir in listdir(dir):
        if "setup.py" in listdir(path.join(dir, subdir)):
                paths.append(path.join(dir, subdir, "setup.py"))

    return paths

def get_egg_names(paths):
    """Return a list of egg names."""
    eggs = []

    for _path in paths:
        egg = check_output(["python", path.basename(_path), "--name"], cwd=path.dirname(_path))
        egg = egg.strip()
        eggs.append(egg)

    return eggs

if __name__ == "__main__":
    paths = get_setup_paths()
    for egg in get_egg_names(paths):
        print egg
