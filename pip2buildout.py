#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import remove
import sys

def main(req_file, output_file):
    """docstring for main"""
    try:
        remove(output_file)
    except:
        pass

    eggs = []
    sources = []



    for line in open(req_file):
        line = line.rstrip()
        if line.startswith("#"):
            pass
        elif line.startswith("git+"):
            git_url, egg_name = line.split("#")
            git_url = git_url.split("+")[1]
            egg_name = egg_name.split("=")[1]
            sources.append(egg_name + " = git " + git_url)
        else:
            eggs.append(line)

    with open(output_file, "wa") as file:
        file.write("[sources]\n")
        for source in sources:
            file.write("\n")
            file.write(source)
        file.write("\n\n[pip]\n\neggs =")
        for egg in eggs:
            file.write("\n    ")
            file.write(egg)
        file.write("\n")



if __name__ == "__main__":
    if not len(sys.argv) == 3:
        print "Invalid lenght of arguments"
    main(sys.argv[1], sys.argv[2])
