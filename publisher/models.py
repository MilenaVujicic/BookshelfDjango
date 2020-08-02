from django.db import models


class Publisher(models.Model):
    name = models.CharField(null=False, blank=False, max_length=512)
