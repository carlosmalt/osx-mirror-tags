#!/usr/bin/env python

from setuptools import setup

setup(
    name='osx-mirror-tags',
    version='0.1',
    packages=['osx_mirror_tags'],
    description='Module to mirror OS X Finder tags on mirrored directory trees',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'biplist',
        'xattr',
    ],
    license='MIT',
    url='https://github.com/scooby/osx-mirror-tags',
    zip_safe=True
)
