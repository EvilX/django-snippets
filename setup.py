try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from snippets import get_version

setup(
    name = 'django-snippets',
    version = get_version(),
    description = ('Provides a templatetag for Django acting as an '
                   '{% include %}, but the template content comes from '
                   'database.'),
    long_description = ('django-snippets provides a templatetag called '
                        'include_snippet for Django projects.\n\n'
                        'include_snippet acts as an {% include %}, that loads '
                        'a template and renders it with the current context, '
                        'but the template content comes from database.'),
    keywords = 'django apps template',
    license = 'New BSD License',
    author = 'Guilherme Gondim',
    author_email = 'semente@taurinus.org',
    url = 'http://github.com/semente/django-snippets/',
    dependency_links = [],
    classifiers = [
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    zip_safe = False,
)
