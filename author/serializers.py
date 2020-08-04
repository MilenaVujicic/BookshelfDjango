from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=512)
    surname = serializers.CharField(max_length=512)

    def create(self, validated_data):
        return Author.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.save()
        return instance

