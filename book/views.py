from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer, BookSerializerAll
from django.views.decorators.csrf import csrf_exempt
from app_user.models import AppUser
from publisher.models import Publisher
import base64
from author.models import Author
from author.serializers import AuthorSerializerBasic
from shelf.models import Shelf
from shelf.serializers import ShelfSerializerBasic
import base64
from django.core.files.base import ContentFile
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
    try:
        user = AppUser.objects.get(username=username)
    except AppUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':

        data = JSONParser().parse(request)
        data['owner'] = user.id
        data['publisher'] = publisher
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        data['owner'] = user.id
        data['publisher'] = publisher
        book = Book.objects.get(id=data['id'])

        book.title = data['title']

        book.pages = data['pages']
        book.description = data['description']
        book.isbn = data['isbn']
        book.read = data['read']
        book.lent = data['lent']

        if data['cover'] != '':
            format, imgstr = data['cover'].split(';base64,')
            ext = format.split('/')[-1]
            name = username+str(book.id)+'.'+ext
            book.cover = ContentFile(base64.b64decode(imgstr), name=name)

        book.private = data['private']
        book.publisher_id = publisher
        book.save()
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data, status=201)


@csrf_exempt
def book_entity(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=200)
    elif request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data, status=200)


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
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            book = Book.objects.get(id=bid)
        except Book.DoesNotExist:
            return HttpResponse(status=404)
        book.authors.clear()
        for author_id in data:
            book.authors.add(author_id)

        book.save()
        return HttpResponse(status=201)


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
    elif request.method == 'GET':
        books = bid
        shelves = Shelf.objects.filter(book=books)
        serializer = ShelfSerializerBasic(shelves, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            book = Book.objects.get(id=bid)
        except Book.DoesNotExist:
            return HttpResponse(status=404)
        book.shelves.clear()
        for shelf_id in data:
            book.shelves.add(shelf_id)
        book.save()
        return HttpResponse(status=201)

@csrf_exempt
def shelf_book(request, username, sid):
    if request.method == 'GET':
        books = Book.objects.filter(shelves=sid)

        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)



@csrf_exempt
def all_books(request):
    if request.method == 'GET':
        books = Book.objects.filter(private=False, lent=False)

        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
def book_rating(request, bid):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=bid)
        except Book.DoesNotExist:
            return HttpResponse(status=404)

        avg_rating = 0
        if book.review_set.count() > 0:
            for review in book.review_set.all():
                avg_rating += review.rating

            avg_rating = avg_rating / book.review_set.count()

        return HttpResponse(avg_rating)


@csrf_exempt
def book_lend(request, bid, username):
    if request.method == 'PUT':
        try:
            book = Book.objects.get(id=bid)
        except Book.DoesNotExist:
            return HttpResponse(status=404)

        try:
            user = AppUser.objects.get(username=username)
        except AppUser.DoesNotExist:
            return HttpResponse(status=404)

        book.lent = True
        book.lent_to_id = user.id
        book.save()
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data, status=200)



@csrf_exempt
def all_lent_books(request, username):
    if request.method == 'GET':
        try:
            user = AppUser.objects.get(username=username)
        except AppUser.DoesNotExist:
            return HttpResponse(status=404)

        books = Book.objects.filter(lent_to_id=user.id)

        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
def return_book(request, bid):
    if request.method == 'PUT':
        try:
            book = Book.objects.get(id=bid)
        except Book.DoesNotExist:
            return HttpResponse(status=404)

        book.lent_to_id = None
        book.lent = False

        book.save()

        return HttpResponse(status=200)
