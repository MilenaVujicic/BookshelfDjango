from django.db import models
from author.models import Author
from review.models import Review
from book_calendar.models import BookCalendar


class Book(models.Model):
    title = models.CharField(blank=False, null=False, max_length=512)
    pages = models.PositiveSmallIntegerField(default=1)
    description = models.TextField()
    isbn = models.CharField(max_length=13)
    status = models.TextChoices("READ", "TO BE READ")
    lent = models.BooleanField(default=False)
    authors = models.ManyToManyField(Author, related_name='books', blank=True, null=True)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE, blank=True, null=True)
    cover = models.ImageField(upload_to='covers', blank=True, null=True)
    calendars = models.ForeignKey(BookCalendar, on_delete=models.CASCADE, null=True, blank=True)


