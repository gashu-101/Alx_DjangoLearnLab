from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Library, Book


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'list_books.html', {'books': books})  # Render template with books



# Class-based view to display details of a specific library
class LibraryDetailView(View):
    def get(self, request, library_name):
        library = get_object_or_404(Library, name=library_name)  # Retrieve the library
        books = library.books.all()  # Get all books in the library
        return render(request, 'library_detail.html', {'library': library, 'books': books})
