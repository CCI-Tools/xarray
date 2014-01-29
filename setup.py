 #!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name='scidata',
      version='0.01',
      description='Objects for holding self describing scientific data in python',
      author='Alex Kleeman',
      author_email='TODO',
      install_requires=['scipy >= 0.10.0', 'numpy >= 1.7', 'netCDF4 >= 1.0.6'],
      tests_require=['nose >= 1.0'],
      url='https://github.com/akleeman/scidata',
      test_suite='nose.collector',
      packages=['polyglot'],
      package_dir={'': 'src'})
