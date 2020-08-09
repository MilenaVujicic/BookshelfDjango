from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Author
from .serializers import AuthorSerializerBasic


# Create your views here.

def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializerBasic(authors, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializerBasic(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
