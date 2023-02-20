from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from liste.models import Cadeau

# Create your models here.
class Reservation(models.Model):
  #Mains Fields
  nom = models.CharField(max_length=100)
  email = models.EmailField()
  participation_partielle = models.BooleanField(default=False)
  montant = models.FloatField(null=True, blank=True)
  discret = models.BooleanField(default=False)
  message = models.TextField(null=True, blank=True)

  #Related Fields
  cadeau = models.ForeignKey('liste.Cadeau',null=True, related_name='reservation', on_delete=models.CASCADE)

  # Utility Variable
  uniqueId = models.CharField(null=True, blank=True, max_length=100)
  date_created = models.DateTimeField(blank=True, null=True)
  last_updated = models.DateTimeField(blank=True, null=True)

  def save(self, *args, **kwargs):
      if self.date_created is None:
          self.date_created = timezone.localtime(timezone.now())
      if self.uniqueId is None:
          self.uniqueId = str(uuid4()).split('-')[4]
      self.last_updated = timezone.localtime(timezone.now())
      
      super(Reservation, self).save(*args, **kwargs)