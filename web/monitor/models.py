from django.db import models
from django.utils.timezone import now

# Create your models here.
class Monitor(models.Model):
  img_url = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  landing_url = models.CharField(max_length=200)
  created_at = models.DateTimeField(default=now)
