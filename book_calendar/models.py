from django.db import models

# Create your models here.


class BookCalendar(models.Model):
    date_reserved = models.DateField()
    date_returned = models.DateField()