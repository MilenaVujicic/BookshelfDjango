from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Publisher
from .serializers import PublisherSerializerBasic
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
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


@csrf_exempt
def publisher_entity(request, id):
    try:
        publisher = Publisher.objects.get(id=id)
    except Publisher.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        publisher.delete()
        return HttpResponse(status=200)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PublisherSerializerBasic(publisher, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'GET':
        serializer = PublisherSerializerBasic(publisher)
        return JsonResponse(serializer.data, status=200)
