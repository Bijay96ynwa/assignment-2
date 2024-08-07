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

        def list_books(book_collection):
            """List all books in the collection."""
            for book in book_collection.books:
                print(book)

        def add_book(book_collection):
            """Add a new book to the collection."""
            title = input("Title: ")
            author = input("Author: ")
            while True:
                try:
                    pages = int(input("Pages: "))
                    if pages <= 0:
                        print("The book must have some pages!")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number")

            new_book = Book(title, author, pages)
            book_collection.add_book(new_book)
            print(f"Book '{title}' added.")

        def mark_book(book_collection):
            """Mark a book as completed."""
            list_books(book_collection)
            title = input("Enter the title of the book to mark as completed: ")
            for book in book_collection.books:
                if book.title.lower() == title.lower():
                    book.mark_completed()
                    print(f"Book '{title}' marked as completed.")
                    return
            print(f"Book '{title}' not found.")

        if __name__ == '__main__':
            main()












