from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
# Create your models here.
class Cadeau(models.Model):

    # Mains Fields
    titre = models.CharField(max_length=200, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    prix = models.FloatField(null=True, blank=True)
    url = models.URLField()
    web_site = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='img', default='default.jpg')

    # Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.titre

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(
                self.titre, self.uniqueId))
        if self.web_site is None:
          self.web_site = self.url.split('/')[2]
        
        self.slug = slugify('{} {}'.format(self.titre, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        
        super(Cadeau, self).save(*args, **kwargs)