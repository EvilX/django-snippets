from setuptools import setup, find_packages
from snippets import get_version

setup(
    name = 'django-snippets',
    version = get_version(),
    description = 'django-snippets acts like an {% include %}, that loads a '
                  'template and renders it with the current context, but is '
                  'editable and served dynamically from database.',
    long_description = open('README.rst').read(),
    keywords = 'django apps',
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
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)
