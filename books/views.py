from books.models import Book
from rest_framework.viewsets import ModelViewSet
from books.serializers import BookSerializer

# Create your views here.

class BooksViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_fields = ('genre',)
