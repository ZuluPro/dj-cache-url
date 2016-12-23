DJ-Cache-URL
~~~~~~~~~~~~

**DO NOT USE THIS PROJECT, IT WAS CREATED DURING A BORING NIGHT AND NOT MAINTENED**

**If you want there is: https://github.com/ghickman/django-cache-url**

.. image:: https://secure.travis-ci.org/ZuluPro/dj-cache-url.png?branch=master
   :target: http://travis-ci.org/ZuluPro/dj-cache-url

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

Support currently exists for Memcached, locmem, database, dummy, filesystem,
redis.

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

    CACHES['default'] = dj_cache_url.config(default='memcached://...')

Parse an arbitrary Database URL::

    CACHES['default'] = dj_cache_url.parse('memcached://...', timeout=600)

URL schema
----------

+-------------+----------------------------------------------------------------+--------------------------+
| Engine      | Django Backend                                                 | URL                      |
+=============+================================================================+==========================+
| Memcached   | ``django.core.cache.backends.memcached.MemcachedCache``        | ``memcached://LOCATION`` |
+-------------+----------------------------------------------------------------+--------------------------+
| Database    | ``django.core.cache.backends.db.DatabaseCache``                | ``database://LOCATION``  |
+-------------+----------------------------------------------------------------+--------------------------+
| Filesystem  | ``django.django.core.cache.backends.filebased.FileBasedCache`` | ``file:///PATH`` [1]_    |
+-------------+----------------------------------------------------------------+--------------------------+
| locmem      | ``django.django.core.cache.backends.locmem.LocMemCache``       | ``locmem://LOCATION``    |
+-------------+----------------------------------------------------------------+--------------------------+
| Dummy       | ``django.core.cache.backends.dummy.DummyCache``                | ``dummy://foo``          |
+-------------+----------------------------------------------------------------+--------------------------+
| Redis       | ``django_redis.cache.RedisCache``                              | ``redis://LOCATION``     |
+-------------+----------------------------------------------------------------+--------------------------+

.. [1] File system backend takes full path to a directory
       (for example ``file:///tmp/dir``)
