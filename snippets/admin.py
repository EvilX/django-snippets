from django.contrib import admin
from snippets.models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    ordering = ['slug',]
    list_display = ('slug', 'content')
    list_filter = ('sites',)
    search_fields = ('slug', 'content')

admin.site.register(Snippet, SnippetAdmin)
