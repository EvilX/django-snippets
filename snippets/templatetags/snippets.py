"""
This module offers one templatetag called ``include_snippet``.

``include_snippet`` acts like an ``{% include %}``, that loads a template
and renders it with the current context, but the template content
comes from database.

It accepts 2 parameter:

    slug
        The slug/key of the text (for example 'comment_list'). There
        are two ways you can pass the slug to the templatetag: (1) by
        its name or (2) as a variable.

        If you want to pass it by name, you have to use quotes on it.
        Otherwise just use the variable name.

    cache_time
        The number of seconds that text should get cached after it has
        been fetched from the database.

        This field is option and defaults to no caching.

Syntax::

    {% include_snippet [name] ([cache]) %}

Example usage::

    {% load snippets %}

    ...

    {% include_snippet "comment_list" %}
    {% include_snippet name_in_variable 3600 %}

"""

from django import template
from django.db import models
from django.core.cache import cache

register = template.Library()

Snippet = models.get_model('snippets', 'snippet')
CACHE_PREFIX = "snippet_"

class SnippetNode(template.Node):
    def __init__(self, slug, is_variable, cache_time=0):
       self.slug = slug
       self.is_variable = is_variable
       self.cache_time = cache_time

    def render(self, context):
        if self.is_variable:
            real_slug = template.Variable(self.slug).resolve(context)
        else:
            real_slug = self.slug
        try:
            cache_key = CACHE_PREFIX + real_slug
            snippet = cache.get(cache_key)
            if snippet is None:
                snippet = Snippet.objects.get(slug=real_slug)
                cache.set(cache_key, snippet, int(self.cache_time))
            t = template.Template(snippet.content)
            return t.render(context)
        except Snippet.DoesNotExist:
            return ''

class BasicSnippetWrapper(object):
    def prepare(self, parser, token):
        tokens = token.split_contents()
        self.is_variable = False
        self.slug = None
        if len(tokens) < 2 or len(tokens) > 3:
            raise template.TemplateSyntaxError, \
                "%r tag should have either 2 or 3 arguments" % (tokens[0],)
        if len(tokens) == 2:
            tag_name, slug = tokens
            self.cache_time = 0
        if len(tokens) == 3:
            tag_name, slug, self.cache_time = tokens
        # Check to see if the slug is properly double/single quoted
        if not (slug[0] == slug[-1] and slug[0] in ('"', "'")):
            self.is_variable = True
            self.slug = slug
        else:
            self.slug = slug[1:-1]

    def __call__(self, parser, token):
        self.prepare(parser, token)
        return SnippetNode(self.slug, self.is_variable, self.cache_time)

do_include_snippet = BasicSnippetWrapper()

register.tag('include_snippet', do_include_snippet)
