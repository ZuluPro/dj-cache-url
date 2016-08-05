# -*- coding: utf-8 -*-

import os

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


# Register database schemes in URLs.
urlparse.uses_netloc.append('memcached')
urlparse.uses_netloc.append('db')
urlparse.uses_netloc.append('database')
urlparse.uses_netloc.append('file')
urlparse.uses_netloc.append('locmem')
urlparse.uses_netloc.append('dummy')
urlparse.uses_netloc.append('redis')

DEFAULT_ENV = 'CACHE_URL'

SCHEMES = {
    'memcached': 'django.core.cache.backends.memcached.MemcachedCache',
    'db': 'django.core.cache.backends.db.DatabaseCache',
    'database': 'django.core.cache.backends.db.DatabaseCache',
    'file': 'django.core.cache.backends.filebased.FileBasedCache',
    'locmem': 'django.core.cache.backends.locmem.LocMemCache',
    'dummy': 'django.core.cache.backends.dummy.DummyCache',
    'redis': 'django_redis.cache.RedisCache',
}


def config(env=DEFAULT_ENV, default=None, backend=None, timeout=300,
           key_prefix='', version=None, key_function=None):
    """Returns configured CACHE dictionary from CACHE_URL."""
    config = {}
    s = os.environ.get(env, default)
    if s:
        config = parse(s, backend, timeout, key_prefix, version, key_function)
    return config


def parse_memcached(url):
    return {
        'LOCATION': "%s:%s" % (url.hostname, url.port),
    }


def parse_db(url):
    return {
        'LOCATION': url.hostname,
    }


def parse_file(url):
    return {
        'LOCATION': url.path,
    }


def parse_locmem(url):
    return {
        'LOCATION': url.hostname,
    }


def parse_dummy(url):
    return {}


def parse_redis(url):
    return {
        'LOCATION': url.geturl(),
    }


SCHEME_PARSERS = {
    'memcached': parse_memcached,
    'db': parse_db,
    'file': parse_file,
    'locmem': parse_locmem,
    'redis': parse_redis,
    'dummy': parse_dummy,
    'default': parse_dummy,
}


def get_config(url):
    if url.scheme in SCHEME_PARSERS:
        scheme_parser = SCHEME_PARSERS[url.scheme]
    else:
        scheme_parser = SCHEME_PARSERS['default']
    return scheme_parser(url)


def parse(url, backend=None, timeout=300, key_prefix='', version=None,
          key_function=None):
    """Parses a cache URL."""
    config = {}

    url = urlparse.urlparse(url)

    # Split query strings from path.
    path = url.path[1:]
    if '?' in path and not url.query:
        path, query = path.split('?', 2)
    else:
        path, query = path, url.query
    query = urlparse.parse_qs(query)

    # Handle postgres percent-encoded paths.
    hostname = url.hostname or ''
    if '%2f' in hostname.lower():
        hostname = hostname.replace('%2f', '/').replace('%2F', '/')

    # Update with environment configuration.
    config.update(get_config(url))
    config['TIMEOUT'] = timeout
    if key_prefix:
        config['KEY_PREFIX'] = key_prefix
    if version is not None:
        config['VERSION'] = version
    if key_function is not None:
        config['KEY_FUNCTION'] = key_function

    # Lookup specified backend.
    backend = SCHEMES[url.scheme] if backend is None else backend

    if backend:
        config['BACKEND'] = backend

    options = {}
    for key, values in query.items():
        options[key] = values[-1]
    if options:
        config['OPTIONS'] = options

    return config
