from rest_framework import serializers
from .models import Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'owner')


class PublisherSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name')
