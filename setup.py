#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='jsbsim_manager',
    version='0.1.0',
    description="Manager for JSBSim case files and support for running simulations in parallel",
    long_description=readme + '\n\n' + history,
    author="Nathan Bergey",
    author_email='nathan.bergey@gmail.com',
    url='https://github.com/open-aerospace/jsbsim-manager',
    packages=[
        'jsbsim_manager',
    ],
    package_dir={'jsbsim_manager':
                 'jsbsim_manager'},
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='JSBSim simulation aerospace',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
