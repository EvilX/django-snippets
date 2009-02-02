from django.conf import settings
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

class Snippet(models.Model):
    slug = models.CharField(
        _('slug'),
        max_length=255,
        unique=True,
        help_text=_('A unique name used for reference in the templates')
    )
    content = models.TextField(_('content'), blank=True, null=True)
    sites = models.ManyToManyField(Site, default=[settings.SITE_ID])

    objects   = models.Manager()
    on_site   = CurrentSiteManager('sites')

    class Meta:
        verbose_name = _('snippet')
        verbose_name_plural = _('snippets')
        ordering = ('slug',)

    def __unicode__(self):
        return u'%s' % (self.slug,)
