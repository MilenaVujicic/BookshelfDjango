from rest_framework import serializers
from .models import Book
from author.serializers import AuthorSerializerBasic
from publisher.serializers import PublisherSerializerBasic
from shelf.serializers import ShelfSerializerBasic
from drf_extra_fields.fields import Base64ImageField


class BookSerializer(serializers.ModelSerializer):
    cover = Base64ImageField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'pages', 'description', 'isbn', 'read', 'lent',
                  'cover', 'private', 'publisher', 'owner']


class BookSerializerAll(serializers.ModelSerializer):
    cover = Base64ImageField()
    authors = AuthorSerializerBasic(read_only=True, many=True)
    publisher = PublisherSerializerBasic(read_only=True)
    shelves = ShelfSerializerBasic(read_only=True, many=True)

    class Meta:
        model = Book
        fields = '__all__'

