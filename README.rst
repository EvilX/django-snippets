django-snippets
===============

django-snippets acts like an {% include %}, that loads a template and
renders it with the current context, but is editable and served
dynamically from database.

Usage
-----

Once you've created some instances of the ``snippets.models.Snippet``
model, you can load it it using the ``snippets_tags`` templatetag-library::
    
    {% load snippets_tags %}
    {% load comments %}
    
    <!-- ... -->

    <h1>{{ entry.title }}</h1>

    {{ entry.body }}

    {% get_comment_list for entry as comment_list  %}	
    {% if comment_list %}
      <h2>Comments</h2>
      {% get_snippet "comment_list" %}
    {% endif %}

    <!-- ... -->

This way you can include a snippet with the name "comment_list". If you 
have the name of a snippet in a template variable, leave out the quotes.

This tag also accepts an optional argument where you can specify the number
of seconds, the that snippet should be cached::
    
    {% get_snippet "comment_list" 3600 %}

History
-------

Since this application targets use-cases that are basically applicable to 
most web-projects out there, there are tons of solutions similar to this one.
In fact, this app is a fork originally from `django-chunks`_ developed by 
Clint Ecker.

In November 2008 Kevin Fricovsky created the `original fork`_ in order to add
an additional "active"-flag to each chunk. That project was later on `forked 
by Peter Baumgardner`_ who removed that flag again and added a "header"-field 
in order to directly associate and optional title with each text block.

This fork aims now to add more features like variable chunks and also
integrate some of the features developed by H. Waara and S. Cranford in
the `django-better-chunks`_ fork (``django.contrib.site``- and i18n-support).


.. _`original fork`: http://github.com/howiworkdaily/django-flatblock/
.. _`django-chunks`: http://code.google.com/p/django-chunks/
.. _`django-better-chunks`: http://bitbucket.org/hakanw/django-better-chunks/
.. _`forked by Peter Baumgardner`: http://github.com/lincolnloop/django-flatblock/
