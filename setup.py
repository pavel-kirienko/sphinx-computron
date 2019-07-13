#!/usr/bin/env python

from setuptools import setup

setup(
    name='sphinx_computron',
    version='0.1.0',
    packages=['sphinx_computron'],
    url='https://github.com/pavel-kirienko/sphinx-computron',
    license='MIT',
    author='JP Senior, Pavel Kirienko',
    author_email='pavel.kirienko@gmail.com',
    description='Sphinx support for execution of python code from code blocks or files. Original code by JP Senior.',
    long_description=open('README.rst').read(),
    install_requires=[
        'docutils',
        'sphinx'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='sphinx extension directive',
)
