from django.db import models
from publisher.models import Publisher
from author.models import Author


class Book(models.Model):
    title = models.CharField(blank=False, null=False, max_length=512)
    pages = models.PositiveSmallIntegerField(default=1)
    description = models.TextField()
    isbn = models.CharField(max_length=13)
    status = models.TextChoices("READ", "TO BE READ")
    lent = models.BooleanField(default=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
