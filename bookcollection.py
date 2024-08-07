import json

class BookCollection:
    """Manage a collection of books"""

    def __init__(self):
        """Initialize a BookCollection with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the collection."""
        self.books.append(book)

    def get_number_of_unread_pages(self):

        return sum(book.pages for book in self.books if not books.is_completed)

    def get_number_of_completed_pages(self):
        """Return the total number of completed pages."""
        return sum(book.pages for book in self.books if book.is_completed)

    def load_books(self, filename):
        """Load books from a JSON file."""
        with open(filename, 'r') as file:
            books_data = json.load(file)
            self.books = [Book(**data) for data in books_data]

    def save_books(self, filename):

        with open(filename, "w")as file:
            json.dump({book.__dict__ for book in self.books], file)

     def sort(self, key):
         """Sort the books by the given key and title."""
         self.books.sort(key=lambda book: (getattr(book, key), book.title))

