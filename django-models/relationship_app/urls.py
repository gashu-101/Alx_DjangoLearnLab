# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('libraries/<str:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
