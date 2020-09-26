from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
from django.views.decorators.csrf import csrf_exempt
from app_user.models import AppUser
from publisher.models import Publisher
import base64
from author.models import Author
from author.serializers import AuthorSerializerBasic
from shelf.models import Shelf
# Create your views here.


@csrf_exempt
def books(request, username):
    try:
        user = AppUser.objects.get(username=username)
    except AppUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        user_books = Book.objects.filter(owner=user.id)
        serializer = BookSerializer(user_books, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
def new_book(request, username, publisher):
    if request.method == 'POST':
        try:
            user = AppUser.objects.get(username=username)
        except AppUser.DoesNotExist:
            return HttpResponse(status=404)

        data = JSONParser().parse(request)
        data['owner'] = user.id
        data['publisher'] = publisher
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def book_entity(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=200)


@csrf_exempt
def book_author(request, bid):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            book = Book.objects.get(id=bid)
        except Book.DoesNotExist:
            return HttpResponse(status=404)
        for author_id in data:
            book.authors.add(author_id)

        return HttpResponse(status=200)
    elif request.method == 'GET':
        books = bid
        authors = Author.objects.filter(books=books)
        serializer = AuthorSerializerBasic(authors, many = True)
        return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
def book_shelf(request, bid):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            book = Book.objects.get(id=bid)
        except Book.DoesNotExist:
            return HttpResponse(status=404)
        for shelf_id in data:
            book.shelves.add(shelf_id)

        return HttpResponse(status=200)


@csrf_exempt
def shelf_book(request, username, sid):
    if request.method == 'GET':
        books = Book.objects.filter(shelves=sid)

        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)



@csrf_exempt
def all_books(request):
    if request.method == 'GET':
        books = Book.objects.filter(private=False)

        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

