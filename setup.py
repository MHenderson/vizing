#!/usr/bin/env python

from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name = "vizing",
    packages = ["vizing"],
    version = "0.0.11",
    description = "List-colouring of graphs",
    author = "Matthew Henderson",
    author_email = "matthew.james.henderson@gmail.com",
    url = "http://packages.python.org/vizing/",
    download_url = "http://pypi.python.org/pypi/vizing/",
    keywords = [""],
    classifiers = [
        "Programming Language :: Python",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = readme(),
    )
