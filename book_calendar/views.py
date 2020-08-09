from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from .models import BookCalendar
from .serializers import BookCalendarSerializerBasic

# Create your views here.


def book_calendar_list(request):
    if request.method == 'GET':
        book_calendars = BookCalendar.objects.all()
        serializer = BookCalendarSerializerBasic(book_calendars, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookCalendarSerializerBasic(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)