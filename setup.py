# -*- coding: utf-8 -*-
"""
dj-cache-url
~~~~~~~~~~~~~~~

.. image:: https://secure.travis-ci.org/kennethreitz/dj-cache-url.png?branch=master
   :target: http://travis-ci.org/kennethreitz/dj-cache-url

This simple Django utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``CACHE_URL`` environment variable to configure your Django application.

The ``dj_cache_url.config`` method returns a Django cache connection
dictionary, populated with all the data specified in your URL. There is
also a `conn_max_age` argument to easily enable Django's connection pool.

If you'd rather not use an environment variable, you can pass a URL in directly
instead to ``dj_cache_url.parse``.

Supported Databases
-------------------

Support currently exists for PostgreSQL, PostGIS, MySQL, MySQL (GIS),
Oracle, Oracle (GIS), and SQLite.

Installation
------------

Installation is simple::

    $ pip install dj-cache-url

Usage
-----

Configure your cache in ``settings.py`` from ``CACHE_URL``::

    import dj_cache_url

    CACHES['default'] = dj_cache_url.config(conn_max_age=600)

Provide a default::

    CACHES['default'] = dj_cache_url.config(default='postgres://...'}

Parse an arbitrary Database URL::

    CACHES['default'] = dj_cache_url.parse('postgres://...', conn_max_age=600)

The ``conn_max_age`` attribute is the lifetime of a cache connection in seconds
and is available in Django 1.6+. If you do not set a value, it will default to ``0``
which is Django's historical behavior of using a new cache connection on each
request. Use ``None`` for unlimited persistent connections.


"""

from setuptools import setup

setup(
    name='dj-cache-url',
    version='0.4.1',
    url='https://github.com/ZuluPro/dj-cache-url',
    license='BSD',
    author='Anthony Monthe (ZuluPro)',
    author_email='anthony.monthe@gmail.com',
    description='Use Database URLs in your Django Application.',
    long_description=__doc__,
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
