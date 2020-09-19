from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import AppUser
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = AppUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)


@csrf_exempt
def user_entity(request, username):
    try:
        user = AppUser.objects.get(username=username)
    except AppUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=200)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, status=200)

