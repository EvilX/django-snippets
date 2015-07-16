django-snippets
===============

*(django-snippets is no longer supported!)*

**django-snippets** provides a templatetag acting as an ``{% include %}``,
that loads a template and renders it with the current context, but the
template content comes from database.

*django-snippets* is a fork of `django-flatblocks`_, and the main difference
is that *django-snippets* render the content as a Django template.

.. _django-flatblocks: http://github.com/zerok/django-flatblocks/

Usage
-----

Once you've created some instances of the ``snippets.models.Snippet``
model, you can load it it using the ``snippets`` templatetag-library::
    
    {% load snippets ... %}
    
    ...

    {% get_comment_list for entry as comment_list  %}	
    {% if comment_list %}
      <h2>Comments</h2>
      <ol>{% include_snippet "comment_list" %}</ol>
    {% endif %}

This way you can include a snippet with the name "comment_list". If you 
have the name of a snippet in a template variable, leave out the quotes.

``comment_list`` will be rendered as a Django template. This mean that you
can use ``{% for %}``, ``{% if %}`` and others template tags.

This tag also accepts an optional argument where you can specify the number
of seconds, the that snippet should be cached::
    
    {% include_snippet "comment_list" 3600 %}

*If you use a snippet that doesn't exist, ``include_snippet`` will insert the
value of the SNIPPET_STRING_IF_INVALID setting, which is '' (the empty string)
by default.*

License
-------

*django-snippets* is available free software under the New BSD
license. See the file LICENSE.txt for more information.
