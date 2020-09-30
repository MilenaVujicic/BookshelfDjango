from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Review
from .serializers import ReviewSerializer
from app_user.models import AppUser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def review_owner(request, username, book):
    try:
        user = AppUser.objects.get(username=username)
    except AppUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['reviewer'] = user.id
        data['book'] = book
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        review = Review.objects.filter(reviewer=user.id, book=book)
        review.delete()
        return HttpResponse(status=200)
    elif request.method == "GET":
        review = Review.objects.filter(book=book)
        serializer = ReviewSerializer(review, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
def review_entity(request, review):
    try:
        review = Review.objects.get(id=review)
    except Review.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'DELETE':
        review.delete()
        return HttpResponse(status=200)



