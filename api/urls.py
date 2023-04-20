from django.urls import path
from .views import book_detail, book_search, create_books

urlpatterns = [
    # path('books', book_list, name='book-list'),
    path('books/<int:pk>', book_detail, name='book-detail'),
    path('books/search/<str:title>', book_search, name='book-search'),
    path('books', create_books, name='create-books')
]
