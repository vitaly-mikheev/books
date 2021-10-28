from django.urls import include, path
from rest_framework import routers
from books.views import BooksViewSet

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
