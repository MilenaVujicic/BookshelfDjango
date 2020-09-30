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
from book.views import new_book, book_entity, book_author, book_shelf, books, shelf_book, all_books, book_rating, book_lend
from book.views import all_lent_books, return_book
from publisher.views import publisher_list, publisher_entity, publisher_owner
from review.views import review_owner, review_entity
from app_user.views import user_list, user_entity
from shelf.views import shelf_list, shelf_entity, shelf_owner
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from app_user.views import user_username

urlpatterns = [
    path('author/', author_list),
    path('author/<str:username>/', author_owner),
    path('author/<int:id>/<str:username>/', author_entity),
    path('books/<str:username>/', books),
    path('book/<int:book_id>/', book_entity),
    path('book/<str:username>/<int:publisher>/', new_book),
    path('book_author/<int:bid>/', book_author),
    path('book_shelf/<int:bid>/', book_shelf),
    path('books/', all_books),
    path('book_rating/<int:bid>/', book_rating),
    path('book_lend/<int:bid>/<str:username>/', book_lend),
    path('all_lent_books/<str:username>/', all_lent_books),
    path('return_book/<int:bid>/',return_book),
    path('shelf_book/<str:username>/<int:sid>/', shelf_book),
    path('publisher/', publisher_list),
    path('publisher/<str:username>/', publisher_owner),
    path('publisher/<int:id>/<str:username>/', publisher_entity),
    path('review/<str:username>/<int:book>/', review_owner),
    path('review/<int:review>/', review_entity),
    path('shelf/', shelf_list),
    path('shelf/<str:username>/', shelf_owner),
    path('shelf/<int:id>/<str:username>/', shelf_entity),
    path('user/', user_list),
    path('user/log/', obtain_jwt_token),
    path('user/login/', user_username),
    path('user/refresh_jwt/', refresh_jwt_token),
    path('user/<str:username>/', user_entity),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),


]
