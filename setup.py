#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Alan Manning",
    author_email='Alan_Manning@Live.co.uk',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="this is a short desc of the package.",
    entry_points={
        'console_scripts': [
            'sonnetsuiteshelper=sonnetsuiteshelper.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sonnetsuiteshelper',
    name='sonnetsuiteshelper',
    packages=find_packages(include=['sonnetsuiteshelper', 'sonnetsuiteshelper.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Alan-Manning/sonnetsuiteshelper',
    version='0.1.0',
    zip_safe=False,
)
