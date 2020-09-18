from django.db import models


class Shelf(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    description = models.CharField(max_length=256)
