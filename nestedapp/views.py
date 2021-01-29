from django.shortcuts import render
from rest_framework import generics

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from . serializers import AuthorSerializer, BookSerializer
from . models import Author, Book

class AuthorListAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # basic authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
