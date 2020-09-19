from django.db import models
from django.conf import settings


class Publisher(models.Model):
    name = models.CharField(null=False, blank=False, max_length=512)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

