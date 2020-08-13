from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializerBasic
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
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


@csrf_exempt
def book_entity(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=200)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookSerializerBasic(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'GET':
        serializer = BookSerializerBasic(book)
        return JsonResponse(serializer.data, status=200)

