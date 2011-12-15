
import os
import sys

from distutils.command.build import build
from setuptools import setup, Command


version_info = {
    'name': 'ovirt-engine-sdk',
    'version': '1.0-SNAPSHOT',
    'description': 'A SDK interface to oVirt'
                   ' Virtualization',
    'author': 'Unknown',
    'author_email': 'engine-devel@ovirt.org',
    'url': 'www.ovirt.org',
    'license': 'ASL2',
    'classifiers': [
        'Development Status :: 1 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: ASL2 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7' ],
}


setup(
    package_dir={ '': 'src' },
    packages=[ 'ovirtsdk.infrastructure', 'ovirtsdk.utils', 'ovirtsdk.web', 'ovirtsdk.xml'],
    install_requires=[],
    entry_points={},
    **version_info
)
