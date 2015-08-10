#!/usr/bin/env python
import os
from setuptools import setup

setup(
    name = "pyfilm",
    version = "0.1.0",
    author = "Ferdinand van Wyk",
    author_email = 'ferdinandvwyk@gmail.com',
    description = "Easily create films of 1D and 2D python arrays.",
    license = "GNU",
    keywords = ['film', 'animation', 'array', 'numpy'],
    packages=['pyfilm', 'tests', 'docs'],
    url = 'git@github.com:ferdinandvwyk/pyfilm.git',
    classifiers=[],
)
