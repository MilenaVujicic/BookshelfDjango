from django.db import models
from django.conf import settings


class Shelf(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    description = models.CharField(max_length=256)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

