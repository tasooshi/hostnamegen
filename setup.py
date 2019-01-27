# -*- coding: utf-8 -*-
#######################################################################
# License: BSD-3-Clause (http://opensource.org/licenses/BSD-3-Clause) #
# Homepage: https://github.com/tasooshi/hostnamegen/                  #
# Version: 0.9.0                                                      #
#######################################################################

from __future__ import (
    absolute_import,
    unicode_literals,
)

import setuptools


with open('README.md') as f:
    long_description = f.read()


setuptools.setup(
    name='hostnamegen',
    version='0.9.0',
    author='tasooshi',
    author_email='tasooshi@pm.me',
    description='Random host name generator',
    license='BSD 3-Clause "New" or "Revised" License (BSD-3-Clause)',
    keywords=[
        'host',
        'name',
        'generator',
        'random',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tasooshi/hostnamegen',
    packages=[
        'hostnamegen',
    ],
    install_requires=(
        'Faker==1.0.1',
        'python-slugify==2.0.1',
        'click==6.7',
    ),
    entry_points={
        'console_scripts': (
            'hostnamegen=hostnamegen:main',
        ),
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
