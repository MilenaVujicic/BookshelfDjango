from rest_framework import serializers
from .models import Publisher
from book.serializers import BookSerializer


class PublisherSerializer(serializers.ModelSerializer):
    book_set = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'book_set')


class PublisherSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name')
