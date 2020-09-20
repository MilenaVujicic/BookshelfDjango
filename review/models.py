from django.db import models
from django.conf import settings
from book.models import Book


class Review(models.Model):
    rating = models.PositiveIntegerField()
    content = models.TextField()
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

