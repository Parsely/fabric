#!/usr/bin/env python

from __future__ import with_statement

from setuptools import setup, find_packages

from fabric.version import get_version


long_description = """
Fabric39 is a fork of `Fabric 3 <https://github.com/mathiasertl/fabric>`_ to provide compatibility with Python3.9+. Fabric3 is a deprecated fork of `Fabric <http://fabfile.org>`_ to provide compatability
with Python 2.7 and 3.4+. Here is the originaly description of Fabric 3:

The goal is to stay 100% compatible with the original Fabric.  Any new releases
of Fabric will also be released here.  Please file issues for any differences
you find. Known differences are `documented on github
<https://github.com/mathiasertl/fabric/>`.

To find out what's new in this version of Fabric, please see `the changelog
<http://fabfile.org/changelog.html>`_ of the original Fabric.

For more information, please see the Fabric website or execute ``fab --help``.
"""

install_requires=['paramiko>=2.0,<3.0', 'six>=1.10.0', 'pathos==0.2.8']

setup(
    name='Fabric39',
    version=get_version('short'),
    description='Fabric is a simple, Pythonic tool for remote execution and deployment (py2.7/py3.4+ compatible fork).',
    long_description=long_description,
    author='Jeff Forcier',
    author_email='jeff@bitprophet.org',
    maintainer='Brian Abelson',
    maintainer_email='brian.abelson@parsely.com',
    url='https://github.com/Parsely/fabric/',
    packages=find_packages(),
    test_suite='nose.collector',
    tests_require=['nose<2.0', 'fudge<1.0', 'jinja2<3.0'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'fab = fabric.main:main',
        ]
    },
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Clustering',
          'Topic :: System :: Software Distribution',
          'Topic :: System :: Systems Administration',
    ],
)
