from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Shelf
from .serializers import ShelfSerializer
from django.views.decorators.csrf import csrf_exempt
from app_user.serializers import UserSerializer
from app_user.models import AppUser

# Create your views here.


@csrf_exempt
def shelf_list(request):
    if request.method == 'GET':
        shelves = Shelf.objects.all()
        serializer = ShelfSerializer(shelves, many=True)
        return JsonResponse(serializer.data, safe=False, status =200)


@csrf_exempt
def shelf_owner(request, username):
    try:
        user = AppUser.objects.get(username=username)
    except AppUser.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['owner'] = user.id
        serializer = ShelfSerializer(data=data)
        if serializer.is_valid():
            model = serializer.save()
            return JsonResponse(data, status=201)
    elif request.method == 'GET':
        id = user.id
        shelves = Shelf.objects.filter(owner=id)
        serializer = ShelfSerializer(shelves, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
def shelf_entity(request, id, username):
    try:
        shelf = Shelf.objects.get(id=id)
    except Shelf.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'DELETE':
        shelf.delete()
        return HttpResponse(status=200)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShelfSerializer(shelf, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'GET':
        serializer = ShelfSerializer(shelf)
        return JsonResponse(serializer.data, status=200)

