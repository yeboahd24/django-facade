from rest_framework.response import Response
from rest_framework import status
from .services import BookService


class BookFacade:
    @staticmethod
    def create_book(request):
        try:
            book_data = BookService.create_book(request.data)
            return Response(book_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_all_books(request):
        try:
            books = BookService.get_all_books()
            return Response(books, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @staticmethod
    def get_book(request, book_id):
        try:
            book = BookService.get_book(book_id)
            if book is None:
                return Response(
                    {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
                )
            return Response(book, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @staticmethod
    def update_book(request, book_id):
        try:
            book = BookService.update_book(book_id, request.data)
            if book is None:
                return Response(
                    {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
                )
            return Response(book, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete_book(request, book_id):
        try:
            if BookService.delete_book(book_id):
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
