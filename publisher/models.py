from django.db import models
from book.models import Book


class Publisher(models.Model):
    name = models.CharField(null=False, blank=False, max_length=512)
    books = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)

