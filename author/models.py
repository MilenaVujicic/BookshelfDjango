from django.db import models


class Author(models.Model):
    name = models.CharField(blank=True, null=True, max_length=512)
    surname = models.TextField(blank=False, null=False, max_length=512)
