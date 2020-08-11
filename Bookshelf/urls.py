"""Bookshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from author.views import author_list, author_entity
from book.views import book_list
from book_calendar.views import book_calendar_list
from publisher.views import publisher_list
from review.views import review_list

urlpatterns = [
    path('author/', author_list),
    path('author/<int:id>/', author_entity),
    path('book/', book_list),
    path('book_calendar/', book_calendar_list),
    path('publisher/', publisher_list),
    path('review/', review_list),
    path('admin/', admin.site.urls)
]
