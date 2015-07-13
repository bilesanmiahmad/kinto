import platform
import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()

with codecs.open(os.path.join(here, 'CHANGELOG.rst'), encoding='utf-8') as f:
    CHANGELOG = f.read()

with codecs.open(os.path.join(here, 'CONTRIBUTORS.rst'),
                 encoding='utf-8') as f:
    CONTRIBUTORS = f.read()

installed_with_pypy = platform.python_implementation() == 'PyPy'

REQUIREMENTS = [
    'colander',
    'cornice >= 1.0',  # Disable request binding.
    'dealer',  # For git.revision
    'python-dateutil',
    'pyramid_multiauth >= 0.5',  # Pluggable authz
    'redis',  # Default backend
    'requests',
    'six',
    'structlog',
]

if installed_with_pypy:
    # We install psycopg2cffi instead of psycopg2 when dealing with pypy
    # Note: JSONB support landed after psycopg2cffi 2.7.0
    POSTGRESQL_REQUIRES = [
        'psycopg2cffi>2.7.0',
    ]
else:
    # ujson is not pypy compliant, as it uses the CPython C API
    REQUIREMENTS.append('ujson')
    POSTGRESQL_REQUIRES = [
        'psycopg2>2.5',
    ]

DEPENDENCY_LINKS = [
]

MONITORING_REQUIRES = [
    'raven',
    'statsd',
    'newrelic',
    'werkzeug',
]

ENTRY_POINTS = {
    'console_scripts': [
        'cliquet = cliquet.scripts.cliquet:main'
    ]
}


setup(name='cliquet',
      version='2.3',
      description='cliquet',
      long_description=README + "\n\n" + CHANGELOG + "\n\n" + CONTRIBUTORS,
      license='Apache License (2.0)',
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "License :: OSI Approved :: Apache Software License"
      ],
      keywords="web services",
      author='Mozilla Services',
      author_email='services-dev@mozilla.com',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=REQUIREMENTS,
      extras_require={
          'postgresql': POSTGRESQL_REQUIRES,
          'monitoring': MONITORING_REQUIRES,
      },
      dependency_links=DEPENDENCY_LINKS,
      entry_points=ENTRY_POINTS)
