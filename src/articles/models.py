from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

class Article(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    short_description = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=False, blank=True)

    published = models.BooleanField(default=False)

    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Article, self).save(*args, **kwargs)