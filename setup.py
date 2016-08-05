#!/usr/bin/env python

from setuptools import setup
import dj_cache_url


def read(name):
    with open(name) as fd:
        return fd.read()

setup(
    name='dj-cache-url',
    version=dj_cache_url.__version__,
    url=dj_cache_url.__url__,
    license=dj_cache_url.__license__,
    author=dj_cache_url.__author__,
    author_email=dj_cache_url.__email__,
    description=dj_cache_url.__doc__,
    long_description=read('README.rst'),
    py_modules=['dj_cache_url'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
