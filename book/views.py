from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializerBasic
# Create your views here.


def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializerBasic(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializerBasic(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)