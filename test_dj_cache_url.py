# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import unittest

import dj_cache_url


class CacheTestSuite(unittest.TestCase):

    def test_memcached_parsing(self):
        url = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.parse(url)

        self.assertEqual(url['BACKEND'], 'django.core.cache.backends.memcached.MemcachedCache')
        self.assertEqual(url['LOCATION'], '127.0.0.1:11211')

    def test_db_parsing(self):
        url = 'db://foo'
        url = dj_cache_url.parse(url)

        self.assertEqual(url['BACKEND'], 'django.core.cache.backends.db.DatabaseCache')
        self.assertEqual(url['LOCATION'], 'foo')

    def test_file_parsing(self):
        url = 'file:///tmp/foo'
        url = dj_cache_url.parse(url)

        self.assertEqual(url['BACKEND'], 'django.core.cache.backends.filebased.FileBasedCache')
        self.assertEqual(url['LOCATION'], '/tmp/foo')

    def test_locmem_parsing(self):
        url = 'locmem://foo'
        url = dj_cache_url.parse(url)

        self.assertEqual(url['BACKEND'], 'django.core.cache.backends.locmem.LocMemCache')
        self.assertEqual(url['LOCATION'], 'foo')

    def test_dummy_parsing(self):
        url = 'dummy://foo'
        url = dj_cache_url.parse(url)

        self.assertEqual(url['BACKEND'], 'django.core.cache.backends.dummy.DummyCache')
        self.assertNotIn('LOCATION', url)

    def test_redis_parsing(self):
        url = 'redis://127.0.0.1:6379/1'
        url = dj_cache_url.parse(url)

        self.assertEqual(url['BACKEND'], 'django_redis.cache.RedisCache')
        self.assertEqual(url['LOCATION'], 'redis://127.0.0.1:6379/1')

    def test_cache_url(self):
        os.environ.pop('CACHE_URL', None)
        a = dj_cache_url.config()
        self.assertFalse(a)

        os.environ['CACHE_URL'] = 'memcached://127.0.0.1:11211'

        url = dj_cache_url.config()

        self.assertEqual(url['BACKEND'], 'django.core.cache.backends.memcached.MemcachedCache')
        self.assertEqual(url['LOCATION'], '127.0.0.1:11211')

    def test_parse_engine_setting(self):
        backend = 'foo.BarBackend'
        url = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.parse(url, backend)

        self.assertEqual(url['BACKEND'], backend)

    def test_config_engine_setting(self):
        backend = 'foo.BarBackend'
        os.environ['CACHE_URL'] = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.config(backend=backend)

        self.assertEqual(url['BACKEND'], backend)

    def test_parse_timeout_setting(self):
        timeout = 600
        url = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.parse(url, timeout=timeout)

        self.assertEqual(url['TIMEOUT'], timeout)

    def test_config_timeout_setting(self):
        timeout = 600
        os.environ['CACHE_URL'] = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.config(timeout=timeout)

        self.assertEqual(url['TIMEOUT'], timeout)

    def test_parse_key_prefix_setting(self):
        key_prefix = 'foo'
        url = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.parse(url, key_prefix=key_prefix)

        self.assertEqual(url['KEY_PREFIX'], key_prefix)

    def test_config_key_prefix_setting(self):
        key_prefix = 'foo'
        os.environ['CACHE_URL'] = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.config(key_prefix=key_prefix)

        self.assertEqual(url['KEY_PREFIX'], key_prefix)

    def test_parse_version_setting(self):
        version = 42
        url = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.parse(url, version=version)

        self.assertEqual(url['VERSION'], version)

    def test_config_version_setting(self):
        version = 42
        os.environ['CACHE_URL'] = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.config(version=version)

        self.assertEqual(url['VERSION'], version)

    def test_parse_key_function_setting(self):
        key_function = 42
        url = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.parse(url, key_function=key_function)

        self.assertEqual(url['KEY_FUNCTION'], key_function)

    def test_config_key_function_setting(self):
        key_function = 42
        os.environ['CACHE_URL'] = 'memcached://127.0.0.1:11211'
        url = dj_cache_url.config(key_function=key_function)

        self.assertEqual(url['KEY_FUNCTION'], key_function)

    def test_options(self):
        url = 'memcached://127.0.0.1:11211?MAX_ENTRIES=1'
        url = dj_cache_url.parse(url)

        self.assertIn('OPTIONS', url)
        self.assertIn('MAX_ENTRIES', url['OPTIONS'])
        self.assertEqual(url['OPTIONS']['MAX_ENTRIES'], '1')


if __name__ == '__main__':
    unittest.main()
