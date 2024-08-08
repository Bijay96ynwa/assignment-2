"""
Module: a1_classes.py

This module defines a console-based application for managing a collection of books.
It uses the Book and BookCollection classes to load, display, add, and update book
information. The user can interact with the application through a simple text-based menu.

Author: JAYA PRAKASH BIJAYPRAKASH
Date:7/08/24
"""
from book import Book, BookCollection

FILE_NAME = 'books.json'

def main():#the main function that runs the book manager application
    print("Books to Read 2.0 by JAYA PRAKASH BIJAYPRAKSH")
    book_collection = BookCollection()
    book_collection.load_books(FILE_NAME)

    while True:
        print("Menu:\nD - Display books\nA - Add a new book\nC - Complete a book\nQ - Quit")
        choice = input(">>> ").strip().upper()
        if choice == 'D':
            display_books(book_collection)
        elif choice == 'A':
            add_book(book_collection)
        elif choice == 'C':
            complete_book(book_collection)
        elif choice == 'Q':
            book_collection.save_books(FILE_NAME)
            print(f"{len(book_collection.books)} books saved to {FILE_NAME}")
            print("So many books, so little time. Frank Zappa")
            break
        else:
            print("Invalid menu choice")

def display_books(collection):#display the list of books in the collection
    print()
    collection.sort_books('author')
    for i, book in enumerate(collection.books):
        status = '*' if book.status == 'u' else ''
        print(f"{status}{i + 1}. {book}")
    unread_pages = collection.get_number_of_unread_pages()
    unread_count = sum(1 for book in collection.books if book.status == 'u')
    if unread_count > 0:
        print(f"You still need to read {unread_pages} pages in {unread_count} books.")
    else:
        print("No books left to read. Why not add a new book?")
    print()

def add_book(collection):#add a new book to the collection
    print()
    title = get_non_empty_input('Title: ')
    author = get_non_empty_input('Author: ')
    pages = get_positive_integer('Number of pages: ')
    book = Book(title, author, pages)
    collection.add_book(book)
    print(f"{title} by {author} {pages} pages added.")
    print()

def complete_book(collection):#marks as a book completed in the collection
    print()
    unread_books = [book for book in collection.books if book.status == 'u']
    if not unread_books:
        print("No unread books - well done!")
        return
    display_books(collection)
    book_number = get_valid_book_number("Enter the number of a book to mark as completed", len(collection.books))
    if collection.books[book_number - 1].status == 'C':
        print("That book is already completed.")
    else:
        collection.books[book_number - 1].mark_completed()
        print(f"{collection.books[book_number - 1].title} by {collection.books[book_number - 1].author} completed!")
    print()

def get_non_empty_input(prompt):
    #prompt the user for non-empty input
    while True:
        response = input(prompt).strip()
        if response:
            return response
        print("Input cannot be blank")

def get_positive_integer(prompt):#prompt the user for a positive integer
    while True:
        try:
            response = int(input(prompt))
            if response > 0:
                return response
            print("Number must be > 0")
        except ValueError:
            print("Invalid input - please enter a valid number")

def get_valid_book_number(prompt, max_number):#prompt the user for a valid book number
    while True:
        try:
            response = int(input(prompt))
            if 1 <= response <= max_number:
                return response
            print("Invalid book number")
        except ValueError:
            print("Invalid input - please enter a valid number")

if __name__ == '__main__':
    main()
