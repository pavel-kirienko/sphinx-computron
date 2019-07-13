"""
The module sphinx-computron provides the "computron_injection" directive for Sphinx.
To use this module, add: extensions.append('sphinx_computron').
Originally authored by JP Senior, forked and reworked by Pavel Kirienko.

Usage:

.. computron_injection:

   print('*This is a valid ReST!*')

See README.rst for documentation details
"""
import sys
import os
import io
import sphinx.util.nodes
import docutils.statemachine
from docutils.parsers.rst import Directive, directives
from docutils import nodes

__docformat__ = 'restructuredtext'
__version__ = '0.1'


class ComputronInjectionDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 1

    option_spec = {
        'filename': directives.path,
    }

    def run(self):
        filename = self.options.get('filename')
        if filename is not None:
            with open(filename, 'r') as source_file:
                source = source_file.read()
        else:
            source = '\n'.join(self.content)

        execution_output = _execute_python_and_return_stdout_or_stderr(source)

        vl = docutils.statemachine.ViewList()
        for index, el in enumerate(execution_output.splitlines()):
            vl.append(el, '<execution-output>', index + 1)

        node = nodes.section()
        node.document = self.state.document

        sphinx.util.nodes.nested_parse_with_titles(self.state, vl, node)

        return node.children


def _execute_python_and_return_stdout_or_stderr(source: str) -> str:
    original_stdout_stderr = sys.stdout, sys.stderr
    local_stdout_stderr = io.StringIO(), io.StringIO()
    sys.stdout, sys.stderr = local_stdout_stderr
    try:
        # For some reason execution fails with a NameError unless globals are provided explicitly,
        # reporting that a new item defined inside the exec'd scope is not defined. Weird.
        # pylint: disable=exec-used
        exec(source, {'sys': 'sys'})
    finally:
        sys.stdout, sys.stderr = original_stdout_stderr

    for lr in local_stdout_stderr:
        val = lr.getvalue()
        if val:
            return val
    return ''


def setup(app):
    app.add_directive('computron_injection', ComputronInjectionDirective)
    return {'version': __version__}
