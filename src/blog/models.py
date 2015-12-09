from django.db import models
from django.utils.text import slugify
from django.conf import settings
from unidecode import unidecode
from django.utils.translation import ugettext_lazy as _


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Article(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name=_("title"))
    short_description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_("short description"))
    description = models.TextField(null=True, blank=True, verbose_name=_("description"))
    author = models.ForeignKey(AUTH_USER_MODEL, default='auth.User', verbose_name=_("author"))
    published = models.BooleanField(default=False, verbose_name=_("published"))
    slug = models.SlugField(unique=True, null=False, blank=True)

    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name=_("updated"))
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_("created"))

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title', 'author']
        verbose_name = _("article")
        verbose_name_plural = _("articles")