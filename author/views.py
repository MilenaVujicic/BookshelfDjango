from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Author
from .serializers import AuthorSerializer, AuthorSerializerBasic
from django.views.decorators.csrf import csrf_exempt
from app_user.serializers import UserSerializer
from app_user.models import AppUser

@csrf_exempt
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializerBasic(authors, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializerBasic(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def author_add(request, username):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = AppUser.objects.get(username=username)
        except AppUser.DoesNotExist:
            return HttpResponse(status=404)
        data['owner'] = user.id
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            model = serializer.save()

    return JsonResponse(data, status=200)


@csrf_exempt
def author_entity(request, id):
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        author.delete()
        return HttpResponse(status=200)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AuthorSerializerBasic(author, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'GET':
        serializer = AuthorSerializerBasic(author)
        return JsonResponse(serializer.data, status=200)
