from django.db import models
import datetime
from taggit.managers import TaggableManager

class Entry(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    published = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(default=datetime.datetime.now)
    slug = models.CharField(max_length=100)
    tags = TaggableManager(blank=True)
    
    class Meta:
        ordering = ['-updated']
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title
    
    def save(self):
        if not self.id:
            self.published = datetime.date.today()
        self.updated = datetime.datetime.today()
        super(Entry, self).save()

