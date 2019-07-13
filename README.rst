sphinx-computron
================

Sphinx-computron is an extension for Sphinx that allows a document author
to insert arbitrary python code samples in code blocks, or run python code
from python files on the filesystem. The output is interpreted as ReST,
as if the output of the executed code was copy-pasted in-place into the
document.

This was written as an alternative to other code execution functions which
relied on doctest formats, and attempts to be more flexible, similar to
literal-block and code-block statements.

The original author is `JP Senior <https://github.com/jpsenior>`_.
His version of the package appears to be unmantained so I decided to salvage
it by making a hard fork. The name had to be changed to avoid collisions
with his version published on PyPI.

Options
-------
Options are:

filename
    If specified, will load code from a file (relative to sphinx doc root)
    and ignore content.

computron_injection
--------------------
Running 'computron_injection' as a directive allows the administrator to embed exact
python code as if it was pasted in a normal code-block.

Executing python code and showing the result output::

    .. computron_injection::

        print('*This is interpreted as ReST!*')


Executing python code from a file
---------------------------------
computron_injection also allows you to import a python file and execute
it within a document.

Running a Python file::

    .. computron_injection::
       :filename: my_class.py


Activating on Sphinx
====================

To activate the extension, add it to your extensions variable in conf.py
for your project.

Activating the extension in sphinx::

    extensions.append('sphinx_computron')
