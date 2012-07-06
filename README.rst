========================
Read the docs (buildout)
========================

Buildout for internally running ReadTheDocs.
This is an alternative installation procedure. For people who are not using
virtualenv on servers.

Installation
============

Start::

    bin/buildout
    bin/supervisord


Problems
========

Requrements changed
+++++++++++++++++++

If the pip requrements change you can update them with the script included.

You need to transform the requrements for virtualenv. To eggs and sources (for mr.developer). There is a script included.

Run::

     python pip2buildout.py src/readthedocs/pip_requirements.txt pip.cfg

This will transform the pip_requirements.txt to pip.cfg (buildout deps configuration style)

You need to change src-eggs (all egs in src/) option as well.

Run::

    python  get_eggs.py

This will print the correct names of the eggs in src.

Please inform us if dependencies have changed.
