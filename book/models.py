from django.db import models
from publisher.models import Publisher
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
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE, primary_key=True, null=False)
    authors = models.ManyToManyField(Author)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to='covers', null=True)
    calendars = models.ForeignKey(BookCalendar, on_delete=models.CASCADE, null=True)


