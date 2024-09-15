from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# BookListView handles listing all books and creating new books.
# Only authenticated users can create new books, while anyone can read the list of books.

# BookDetailView handles retrieving, updating, and deleting a specific book by ID.
# Only authenticated users can update or delete, while anyone can read the book details.
