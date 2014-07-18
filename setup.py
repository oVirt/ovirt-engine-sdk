
import os
import sys

from distutils.command.build import build
from setuptools import setup, Command


version_info = {
    'name': 'ovirt-engine-sdk-python',
    'version': '3.5.0.4',
    'description': 'A SDK interface to oVirt Virtualization',
    'author': 'Michael Pasternak',
    'author_email': 'mpastern@redhat.com',
    'url': 'http://www.ovirt.org/wiki/SDK',
    'license': 'ASL2',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6' ],
}


setup(
    package_dir={ '': 'src' },
    packages=[ 'ovirtsdk.infrastructure', 'ovirtsdk.utils', 'ovirtsdk.web', 'ovirtsdk.xml'],
    py_modules=['ovirtsdk.api'],
    install_requires=['lxml >= 2.2.3'],
    entry_points={},
    **version_info
)
