#!/usr/bin/env python

from setuptools import setup

setup(
    name='osx-mirror-tags',
    version='0.1',
    packages=['osx_mirror_tags'],
    description='Module to mirror OS X Finder tags from a directory tree to a mirrored directory tree',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'biplist',
        'xattr',
        'osx_tags',
    ],
    license='MIT',
    url='https://github.com/carlosmalt/osx-mirror-tags',
    zip_safe=True
)
