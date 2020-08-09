from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Publisher
from .serializers import PublisherSerializerBasic
# Create your views here.


def publisher_list(request):
    if request.method == 'GET':
        publishers = Publisher.objects.all()
        serializer = PublisherSerializerBasic(publishers, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublisherSerializerBasic(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)