#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys

__VERSION__ = "1.0" 

requires = ['BeautifulSoup4']

setup(
    name = "pcl",
    version = __VERSION__,
    url = 'http://hecor.github.com/',
    author = 'hecor',
    author_email = 'hustpzy@qq.com',
    description = "python common libs",
    long_description=open('README.md').read(),
    packages = ['pcl', 'pcl.text'],
    #include_package_data = True,
    install_requires = requires,
    scripts = [],
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
)

