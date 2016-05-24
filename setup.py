#!/usr/bin/env python

"""
Installation configuration for unittest-probedock
"""

from setuptools import setup

with open("README.rst") as f:
    long_descr = f.read()

setup(
    name='unittest-probedock',
    version='0.1.0',
    py_modules=['unittest_probedock'],
    url='https://github.com/probedock/probedock-py-unittest',
    license='MIT',
    author='Benjamin Schubert',
    author_email='ben.c.schubert@gmail.com',
    description='Pytest plugin for reporting test results to ProbeDock CI',
    long_description=long_descr,

    install_requires=[
        "probedock", 'requests',
    ],

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
)
