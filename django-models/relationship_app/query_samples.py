from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Gashu"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}: {books_by_author}")

# List all books in a specific library
library_name = "Some Library Name"  # Replace with actual library name
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {books_in_library}")

# Retrieve the librarian for a specific library
librarian = Librarian.objects.get(library=library)
print(f"Librarian of {library_name}: {librarian}")
