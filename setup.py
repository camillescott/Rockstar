#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    author="Camille Scott",
    author_email='cswel@ucdavis.edu',
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'rockstar = rockstar:main'
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description="Utilities for Relion Cryo-EM data processing.",
    license="modified BSD",
    long_description=readme,
    include_package_data=True,
    keywords='rockstar',
    name='rockstar',
    packages=find_packages(include=['rockstar', 'rockstar.*']),
    url='https://github.com/camillescott/Rockstar',
    version='0.1',
    zip_safe=False,
)
