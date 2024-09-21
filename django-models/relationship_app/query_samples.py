from .models import *

# Querying the database

# Filter books by author's name (fixed field name and query)
books_by_author = Book.objects.filter(author__name='Gashu')
print(books_by_author)

# Get all books in a specific library
library_name = "Some Library Name"  # Define your library name here
books_in_library = Library.objects.get(name=library_name).books.all()
print(books_in_library)

# List all librarians
librarians = Librarian.objects.all()
print(librarians)
