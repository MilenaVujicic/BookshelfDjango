from rest_framework import serializers
from .models import BookCalendar
from book.serializers import BookSerializer


class BookCalendarSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BookCalendar
        fields = ('id', 'date_reserved', 'date_returned', 'book')


class BookCalendarSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = BookCalendar
        field = ('id', 'date_reserved', 'date_returned')

