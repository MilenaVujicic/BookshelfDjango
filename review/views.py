from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Review
from .serializers import ReviewSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)


def review_entity(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        review.delete()
        return HttpResponse(status=200)
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = ReviewSerializer(review, data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'GET':
        serializer = ReviewSerializer(review)
        return JsonResponse(serializer.data, status=200)

