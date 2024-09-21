from .models import *

# Querying the database

books_by_author =  Book.objects.filter(Author='Gashu')
print(books_by_author)
books_in_library = Library.objects.get(name = "").books.all()
print(books_in_library)
librarian = Librarian.objects.all()
