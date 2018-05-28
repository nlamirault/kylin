#!/usr/bin/env python

# Copyright (C) 2017-2018 Nicolas Lamirault <nicolas.lamirault@gmail.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
import os

from kylin import version


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fn:
        return fn.read()


# with open('requirements.txt') as f:
#     required = f.read().splitlines()


# with open('requirements-test.txt') as f:
#     required_for_tests = f.read().splitlines()


setup(
    name='kylin',
    version=version.RELEASE,
    description='Library to read Teleinfo frames',
    long_description=read('README.rst'),
    url='https://github.com/nlamirault/kylin',
    author='Nicolas Lamirault',
    author_email='nicolas.lamirault@gmail.com',
    packages=['kylin'],
    install_requires=[
        "pyserial==3.4"
    ],
    license='License :: OSI Approved :: Apache Software License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Environment :: No Input/Output (Daemon)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Operating System :: Unix',
    ],
    keywords='teleinfo',
    platforms=['Linux'],
    test_suite='kylin/tests',
    tests_require=[
        "pytest==3.2.3",
        "pytest-cov==2.5.1",
        "pytest-sugar==0.9.0",
        "flake8==3.4.1",
    ],
    zip_safe=True
)
