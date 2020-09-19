from django.db import models
from django.conf import settings


class Author(models.Model):
    name = models.CharField(blank=True, null=True, max_length=512)
    surname = models.CharField(blank=False, null=False, max_length=512)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

