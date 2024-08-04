import json

class BookCollection:
    """Manage a collection of books"""

    def __init__(self):
        """Initialize a BookCollection with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the collection."""
        self.books.append(book)
