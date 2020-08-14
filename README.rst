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

The package is available on PyPI as `sphinx-computron <https://pypi.org/project/sphinx-computron/>`_.

Options
-------

filename
    If specified, will load code from a file (relative to sphinx doc root)
    and prepend that to the directive's content before its execution.

argv
    Passes the specified whitespace-separated arguments to the script.
    If specified: ``sys.argv = [filename] + argv.split()``.
    If not specified: ``sys.argv = [filename]``.

computron-injection
--------------------

Executing python code and parsing output as ReST::

    .. computron-injection::

        print('*This is interpreted as ReST!*')


Whatever is written into stdout is collected and the injected in-place into
the document. Stderr is not captured.

Executing python code from a file
---------------------------------
computron-injection also allows you to import a python file and execute
it within a document.
The path is specified relative to the source ReST file where the
directive is encountered.

Running a Python file in the same directory::

    .. computron-injection::
       :filename: my_class.py

With arguments ``['Hello', 'world!']``::

    .. computron-injection::
       :filename: my_class.py
       :argv: Hello world!


Activating on Sphinx
====================

To activate the extension, add it to your extensions variable in conf.py
for your project.

Activating the extension in sphinx::

    extensions.append('sphinx_computron')
