from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from .models import Book
from .serializers import BookSerializer, CreateBookSerializer, UpdateBookSerializer


class BookService:
    @staticmethod
    @transaction.atomic
    def create_book(data):
        serializer = CreateBookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return BookSerializer(book).data

    @staticmethod
    def get_all_books():
        books = Book.objects.all()
        return BookSerializer(books, many=True).data

    @staticmethod
    def get_book(book_id):
        try:
            book = Book.objects.get(id=book_id)
            return BookSerializer(book).data
        except ObjectDoesNotExist:
            return None

    @staticmethod
    @transaction.atomic
    def update_book(book_id, data):
        try:
            book = Book.objects.get(id=book_id)
            serializer = UpdateBookSerializer(book, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            updated_book = serializer.save()
            return BookSerializer(updated_book).data
        except ObjectDoesNotExist:
            return None

    @staticmethod
    @transaction.atomic
    def delete_book(book_id):
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return True
        except ObjectDoesNotExist:
            return False
