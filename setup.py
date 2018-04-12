"""A setuptools based setup module for quadis"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    'click',
    'PyQt5',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='quadis',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="insert short description here",
    long_description=readme + '\n\n' + history,
    author="Josiah Atwell",
    author_email='jlatwell@protonmail.com',
    url='https://github.com/bottomnotch/quadis',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts':[
            'quadis=quadis.cli:cli',
            'quadis-gui=quadis.gui:gui',
            'quadis-qt5=quadis.guiQt5:gui',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="BSD 3 Clause",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD 3 Clause License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
