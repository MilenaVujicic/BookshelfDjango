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
from django.urls import path, include
from author.views import author_list, author_entity, author_owner
from book.views import book_list, book_entity
from book_calendar.views import book_calendar_list
from publisher.views import publisher_list, publisher_entity, publisher_owner
from review.views import review_list, review_entity
from app_user.views import user_list, user_entity
from shelf.views import shelf_list, shelf_entity, shelf_owner
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('author/', author_list),
    path('author/<str:username>/', author_owner),
    path('author/<int:id>/<str:username>/', author_entity),
    path('book/', book_list),
    path('book/<int:id>/', book_entity),
    path('book_calendar/', book_calendar_list),
    path('publisher/', publisher_list),
    path('publisher/<str:username>/', publisher_owner),
    path('publisher/<int:id>/<str:username>/', publisher_entity),
    path('review/', review_list),
    path('review/<int:id>/', review_entity),
    path('shelf/', shelf_list),
    path('shelf/<str:username>/', shelf_owner),
    path('shelf/<int:id>/<str:username>/', shelf_entity),
    path('user/', user_list),
    path('user/login/', obtain_jwt_token),
    path('user/refresh_jwt/', refresh_jwt_token),
    path('user/<str:username>/', user_entity),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),


]
