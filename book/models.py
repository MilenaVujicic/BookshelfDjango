from django.db import models
from author.models import Author
from publisher.models import Publisher
from shelf.models import Shelf
from django.conf import settings


class Book(models.Model):
    title = models.CharField(blank=False, null=False, max_length=512)
    pages = models.PositiveSmallIntegerField(default=1)
    description = models.TextField()
    isbn = models.CharField(max_length=13)
    read = models.BooleanField(default=False)
    lent = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers', blank=True, null=True)
    private = models.BooleanField(default=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='books')
    shelves = models.ManyToManyField(Shelf)

