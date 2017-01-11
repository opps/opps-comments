#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

from opps import comments


VERSION = (0, 1, 2)

__version__ = ".".join(map(str, VERSION))
__status__ = "Development"
__description__ = u"comments App for Opps CMS"

__author__ = u"Bruno Cezar Rocha"
__credits__ = []
__email__ = u"rochacbruno@gmail.com"
__license__ = u"YACOWS LICENSE"
__copyright__ = u"Copyright 2013, YACOWS"


install_requires = ["opps"]

classifiers = ["Development Status :: 4 - Beta",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Framework :: Opps",
               'Programming Language :: Python',
               "Programming Language :: Python :: 2.7",
               "Operating System :: OS Independent",
               "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
               'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.rst').read()
except:
    long_description = comments.__description__

setup(
    name='opps-comments',
    namespace_packages=['opps'],
    version=__version__,
    description=__description__,
    long_description=long_description,
    classifiers=classifiers,
    keywords='comments opps cms django apps magazines websites',
    author=__author__,
    author_email=__email__,
    url='http://oppsproject.org',
    download_url="https://github.com/opps/opps-comments/tarball/master",
    license=__license__,
    packages=find_packages(exclude=('doc', 'docs',)),
    package_dir={'opps': 'opps'},
    install_requires=install_requires,
    include_package_data=True,
    package_data={
        'comments': ['templates/*']
    }
)
