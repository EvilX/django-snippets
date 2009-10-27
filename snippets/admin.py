from django.contrib import admin
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _
from snippets.models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    ordering = ['slug',]
    list_display = ('slug', '_get_content')
    list_filter = ('sites',)
    search_fields = ('slug', 'content')

    def _get_content(self, obj):
        tmpl = "<i>%s</i>"
        if len(obj.content) > 385:
            return (tmpl + " <b>[...]</b>") % escape(obj.content)[:385]
        return tmpl % escape(obj.content)
    _get_content.allow_tags = True
    _get_content.short_description = _("content")

admin.site.register(Snippet, SnippetAdmin)
