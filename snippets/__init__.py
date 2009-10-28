"""
**snippets** is a application for Django projects that provides a
templatetag acting as an ``{% include %}``, but the template content
comes from database.
"""

VERSION = (0, 1, 2)

def get_version():
    """
    Returns the version as a human-format string.
    """
    v = '.'.join([str(i) for i in VERSION])
    return v

__author__ = 'See the file AUTHORS.txt.'
__license__ = 'New BSD License'
__url__ = 'http://github.com/semente/django-snippets/'
__version__ = get_version()
