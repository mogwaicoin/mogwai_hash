from distutils.core import setup, Extension

mogwai_hash_module = Extension('mogwai_hash',
                                 sources = ['mogwaimodule.c',
                                            'mogwai.c',
                                            'crypto/neoscrypt.c',
                                            'crypto/neoscrypt_old.c'],
                               include_dirs=['.', './crypto'])

setup (name = 'mogwai_hash',
       version = '1.0.0',
       description = 'Binding for Mogwai NeoScrypt proof of work hashing.',
       ext_modules = [mogwai_hash_module])
