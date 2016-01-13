from django.db import models
from django.utils.text import slugify
from django.conf import settings
from unidecode import unidecode
from django.utils.translation import ugettext_lazy as _
from thumbnailfield.fields import ThumbnailField
import datetime

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Article(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name=_("title"))
    category = models.ForeignKey('Category', null=True, blank=True, verbose_name=_("category"))
    short_description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_("short description"))
    description = models.TextField(null=True, blank=True, verbose_name=_("description"))
    author = models.ForeignKey(AUTH_USER_MODEL, default='auth.User', verbose_name=_("author"))
    published = models.BooleanField(default=False, verbose_name=_("published"))
    img = ThumbnailField(_('thumbnail'), upload_to='img/articles', null=True, blank=True,
        pil_save_options={
            'quality': 100,
        },
        patterns={
            None: (800, 400, 'resize'),
            'large': ((640, 480, 'resize'),),
            'small': (300, 300, 'resize'),
            'tiny': (160, 120),
        })
    slug = models.SlugField(unique=True, null=False, blank=False)

    date_published = models.DateTimeField(null=True, blank=True, verbose_name=_("publication date"))
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name=_("updated"))
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_("created"))

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.published:
            self.date_published = datetime.datetime.now()
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['date_published', 'title']
        verbose_name = _("article")
        verbose_name_plural = _("articles")


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"), unique=True)
    parent = models.ForeignKey('Category', blank=True, null=True, verbose_name=_("parent"))
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_("description"))
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = _("category")
        verbose_name_plural = _("categories")

