"""
The module sphinx-computron provides the "computron_injection" directive for Sphinx.
See README.rst for documentation details.
Originally authored by JP Senior, forked and reworked by Pavel Kirienko.
"""

import os
import io
import sys

import docutils.nodes
import docutils.parsers.rst
import docutils.statemachine

import sphinx.util.nodes


class ComputronInjectionDirective(docutils.parsers.rst.Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 1

    option_spec = {
        'filename': docutils.parsers.rst.directives.path,
    }

    def run(self):
        filename = self.options.get('filename')
        source = ''
        if filename is not None:
            with open(filename, 'r') as source_file:
                source = source_file.read() + '\n'
        source += '\n'.join(self.content)

        execution_output = _execute_python_collect_stdout(source)

        vl = docutils.statemachine.ViewList()
        for index, el in enumerate(execution_output.splitlines()):
            vl.append(el, '<computron-injection-output>', index + 1)

        node = docutils.nodes.section()
        node.document = self.state.document

        sphinx.util.nodes.nested_parse_with_titles(self.state, vl, node)

        return node.children


def _execute_python_collect_stdout(source: str) -> str:
    """
    Executes the supplied Python source and returns its stdout output. Stderr is not captured;
    that is, it is delivered into the host process' stderr destination (usually the terminal running Sphinx).
    """
    original_stdout, sys.stdout = sys.stdout, io.StringIO()
    try:
        # For some reason execution fails with a NameError unless globals are provided explicitly,
        # reporting that a new item defined inside the exec'd scope is not defined. Weird.
        exec(source, {'sys': 'sys'})
        return sys.stdout.getvalue()
    finally:
        sys.stdout = original_stdout


def setup(app):
    app.add_directive('computron_injection', ComputronInjectionDirective)
    return {}
