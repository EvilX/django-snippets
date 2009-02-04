from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
from snippets import get_version

setup(
    name = 'django-snippets',
    version = get_version(),
    description = 'django-snippets provides a templatetag acting as an '
                  '{% include %}, but the template content comes from '
                  'database.',
    long_description = open('README.rst').read(),
    keywords = 'django apps template',
    license = 'New BSD License',
    author = 'Guilherme Gondim',
    author_email = 'semente@taurinus.org',
    url = 'http://github.com/semente/django-snippets/',
    dependency_links = [],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)
