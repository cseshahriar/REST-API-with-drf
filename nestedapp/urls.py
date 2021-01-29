from django.urls import path
from . views import (
    AuthorListAPIView,
    AuthorDetailAPIView,
    BookListAPIView,
    BookDetailAPIView
)

urlpatterns = [
    path('authors/list_create', AuthorListAPIView.as_view(), 
    name='author_list_create'),
    path('authors/detail/<int:pk>/', AuthorDetailAPIView.as_view(), 
    name='author_detail'),
    path('books/list_create', BookListAPIView.as_view(), 
    name='book_list_create'),
    path('books/detail/<int:pk>/', BookDetailAPIView.as_view(), 
    name='book_detail'),
]