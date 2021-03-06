from rest_framework import serializers
from .models import Shelf


class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ['id', 'name', 'description', 'owner']


class ShelfSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ['id', 'name', 'description']

