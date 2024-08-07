from book import Book
from bookcollection import BookCollection

def main():
    """Run he console program to manage books"""
    book_collection= BookCollection()
    book_collection.load_books("books.json")

    while True:
        print_menu()
        choice = input("Enter your choice: ").upper()
        if choice == 'Q':
            book_collection.save_books('books.json')
            print("Books saved. Goodbye!")
            break
        elif choice == 'L':
            list_books(book_collection)
        elif choice == 'A':
            add_book(book_collection)
        elif choice == 'M':
            mark_book(book_collection)
        else:
            print("Invalid choice")

        def print_menu():
            """print the menu options """
            print("\nMenu:")
            print("\nMenu:")
            print("L - List all books")
            print("A - Add a new book")
            print("M - Mark a book as completed")
            print("Q - Quit")









