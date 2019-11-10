from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from bookapp.models import Book
from bookapp.serializer import BookSerializer


class BookOperations(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
