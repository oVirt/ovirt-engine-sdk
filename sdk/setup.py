#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2016 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import codecs
import distutils.extension
import glob
import os
import setuptools
import sys

# Load the long description from the README:
root_dir = os.path.abspath(os.path.dirname(__file__))
doc_file = os.path.join(root_dir, 'README.adoc')
with codecs.open(doc_file, encoding='utf-8') as doc_fd:
    long_description = doc_fd.read()

# Required packages:
requires = [
    'pycurl >= 7.19.0',
    'six',
]

# Python before version 3.4 doesn't support enum types, which we need,
# so we need to use the "enum34" package:
if sys.version_info < (3, 4):
  requires.append('enum34')

# Setup the package:
setuptools.setup(
    name='ovirt-engine-sdk-python',
    version='4.0.0a6',
    description='Python SDK for oVirt Engine API',
    long_description=long_description,
    author='Michael Pasternak, Juan Hernandez, Ondra Machacek',
    author_email=(
        'mishka8520@yahoo.com, '
        'juan.hernandez@redhat.com, '
        'omachace@redhat.com'
    ),
    license='ASL2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    package_dir={'': 'lib'},
    packages=setuptools.find_packages('lib'),
    install_requires=requires,
    ext_modules=[
        distutils.extension.Extension(
            name='ovirtsdk4.xml',
            include_dirs=[
                '/usr/include/libxml2',
            ],
            libraries=[
                'xml2',
            ],
            sources=glob.glob('ext/*.c'),
        ),
    ]
)
