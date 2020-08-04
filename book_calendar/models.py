from django.db import models
import django
# Create your models here.


class BookCalendar(models.Model):
    date_reserved = models.DateField(default=django.utils.timezone.now)
    date_returned = models.DateField(default=django.utils.timezone.now)