import json

class Book:
    def __init__(self, title, author, pages, status='u'):
        self.title = title
        self.author = author
        self.pages = pages
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages) - {'Completed' if self.status == 'C' else 'Unread'}"

    def mark_completed(self):
        self.status = 'C'

    def mark_unread(self):
        self.status = 'u'

    def is_long(self):
        return self.pages >= 500

class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_number_of_unread_pages(self):
        return sum(book.pages for book in self.books if book.status == 'u')

    def get_number_of_completed_pages(self):
        return sum(book.pages for book in self.books if book.status == 'C')

    def load_books(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.books = [Book(**book) for book in data]

    def save_books(self, filename):
        with open(filename, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file, indent=4)

    def sort_books(self, key):
        self.books.sort(key=lambda book: (getattr(book, key), book.title))
