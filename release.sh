#!/bin/bash
#
# PyPI release automation.
# https://gist.github.com/boppreh/ac7522b3a4ac46b4f6010eecddc57f21
#

set -e
set -o nounset

clean()
{
    rm -rf dist build *.egg-info .coverage* &> /dev/null
}

clean
./setup.py sdist bdist_wheel
python3 -m twine upload dist/*
clean
