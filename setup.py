#!/usr/bin/env python
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyfilm",
    version = "0.1.0",
    author = "Ferdinand van Wyk",
    author_email = 'ferdinandvwyk@gmail.com',
    description = "Easily create films of 1D and 2D python arrays.",
    license = "GNU",
    keywords = ['film', 'animation', 'array', 'numpy'],
    packages=['pyfilm', 'tests', 'docs'],
    long_description=read('README.rst'),
    url = 'git@github.com:ferdinandvwyk/pyfilm.git',
    classifiers=[],
)
