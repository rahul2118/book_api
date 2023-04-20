from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Author, Language, Genre, Publisher
from .serializers import BookSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
import string
from rest_framework.pagination import PageNumberPagination
from django.db import transaction


class BookListPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


@api_view(['GET', 'POST'])
def create_books(request):
    if request.method == 'GET':
        paginator = BookListPagination()
        with transaction.atomic():
            books = Book.objects.all()
            result_page = paginator.paginate_queryset(
                books, request, view=None)
            serializer = BookSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        paginator = BookListPagination()

        with transaction.atomic():
            serializer = BookSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            books = serializer.save()
            result_page = paginator.paginate_queryset(
                books, request, view=None)
            return paginator.get_paginated_response(serializer.data)
    return paginator.get_paginated_response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def book_search(request, title):
    books = Book.objects.filter(title__icontains=title)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
