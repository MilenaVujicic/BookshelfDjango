from django.db import models
from book.models import Book


class Shelf(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    description = models.CharField(max_length=256)
    books = models.ManyToManyField(Book)
