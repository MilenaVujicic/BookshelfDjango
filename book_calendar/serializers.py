from rest_framework import serializers
from .models import BookCalendar


class BookCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCalendar
        fields = ('id', 'date_reserved', 'date_returned')

