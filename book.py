import json
"""
Module:book.py
This module defines two classes:Book and BookCollection
The Book class represents a single book with attributes like title,author,pages and status
The BookCollection class manages a collection of Book objects, providing methods to add books 
Author:Jayaprakash bijay prakash
Date:4/8/8
"""

class Book:
    """
    A class to represent book
    attributes:title,authir,pages is_completed
    """
    def __init__(self, title, author, pages, status='u'):#intialize the book object with title , author and pages and completion status
        self.title = title
        self.author = author
        self.pages = pages
        self.status = status

    def __str__(self):#return the string representation of the book
        return f"{self.title} by {self.author} ({self.pages} pages) - {'Completed' if self.status == 'C' else 'Unread'}"

    def mark_completed(self):#marks the book as completed
        self.status = 'C'

    def mark_unread(self):#marks the book a unread
        self.status = 'u'

    def is_long(self):#determine if the book is long(500 pages or more.
        return self.pages >= 500

class BookCollection:
    """
    A class to represent the collection of books
    attributes:books:list
    """
    def __init__(self):#intialize the Bookcollection with an empty list of books
        self.books = []

    def add_book(self, book):#Add a single Book object to the collection
        self.books.append(book)

    def get_number_of_unread_pages(self):#get the total number of unread pages in the collection
        return sum(book.pages for book in self.books if book.status == 'u')

    def get_number_of_completed_pages(self):#get the number of completed pages
        return sum(book.pages for book in self.books if book.status == 'C')

    def load_books(self, filename):#load books from JSON file to load books from
        with open(filename, 'r') as file:
            data = json.load(file)
            self.books = [Book(**book) for book in data]

    def save_books(self, filename):#Save the books in the collection to a JSON file
        with open(filename, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file, indent=4)

    def sort_books(self, key):#sort the books in the collection by the specified ket, then by title
        self.books.sort(key=lambda book: (getattr(book, key), book.title))
