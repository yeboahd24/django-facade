from rest_framework.views import APIView
from .facades import BookFacade


class BookListView(APIView):
    def post(self, request):
        return BookFacade.create_book(request)

    def get(self, request):
        return BookFacade.get_all_books(request)


class BookDetailView(APIView):
    def get(self, request, book_id):
        return BookFacade.get_book(request, book_id)

    def put(self, request, book_id):
        return BookFacade.update_book(request, book_id)

    def delete(self, request, book_id):
        return BookFacade.delete_book(request, book_id)
