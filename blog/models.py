from django.db import models
from taggit.managers import TaggableManager


class Entry(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    slug = models.CharField(max_length=100)
    tags = TaggableManager(blank=True)
    hide = models.BooleanField()

    class Meta:
        ordering = ['-updated']
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title
