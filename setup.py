#!/usr/bin/env python
""" Distutils setup file """
from setuptools import setup

def readme():
    """ Returns Readme.rst as loaded RST for documentation """
    with open('Readme.rst', 'r') as filename:
        return filename.read()
setup(
    name='sphinx_computron',
    version='0.1',
    platforms=['any'],
    packages=['sphinx_computron'],
    url='https://github.com/pavel-kirienko/sphinx-computron',
    license='MIT',
    author='JP Senior, Pavel Kirienko',
    author_email='pavel.kirienko@gmail.com',
    description='Sphinx support for execution of python code from code blocks or files. Original code by JP Senior.',
    long_description=readme(),
    install_requires=['docutils', 'sphinx'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='sphinx extension directive execute code',
)
