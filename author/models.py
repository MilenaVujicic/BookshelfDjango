from django.db import models


class Author(models.Model):
    name = models.CharField(blank=True, null=True, max_length=512)
    surname = models.CharField(blank=False, null=False, max_length=512)

    def __str__(self):
        return self.name

