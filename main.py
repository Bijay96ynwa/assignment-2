from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from book import Book
from bookcollection import BookCollection


class BookApp(App):
     """Kivy App for managing books"""

     status_text= StringProperty()
     book_collection=BookCollection()

     def build(self):

         self.title="Book Collection"
         self.root =Builder.load_file("app.kv")
         self.book_collection.load_books("books.json")
         self.create_book_buttons()
         return self.root

     def create_book_buttons(self):
         """create buttons for each bok in the collection"""
         self.root.ids.books_box.clear_widgets()
         for book in self.book_collection.books:
             button = Button(text=str(book))
             button.bind(on_release=self.press_entry)
             button.background_color = (0, 1, 0, 1) if book.is_completed else (1, 0, 0, 1)
             self.root.ids.books_box.add_widget(button)
         self.update_status()

     def press_entry(self, instance):
         """Handle pressing a book button."""
         title = instance.text.split(" by ")[0]
         for book in self.book_collection.books:
             if book.title == title:
                 if book.is_completed:
                     book.mark_required()
                 else:
                     book.mark_completed()
                 instance.background_color = (0, 1, 0, 1) if book.is_completed else (1, 0, 0, 1)
                 self.update_status()
                 break

     def handle_add(self):
         """Handle adding a new book."""
         title = self.root.ids.input_title.text
         author = self.root.ids.input_author.text
         pages = self.root.ids.input_pages.text

         if not title or not author or not pages:
             self.status_text = "Please complete all fields."
             return

         try:
             pages = int(pages)
             if pages <= 0:
                 self.status_text = "The book must have some pages!"
                 return
         except ValueError:
             self.status_text = "Please enter a valid number."
             return

         new_book = Book(title, author, pages)
         self.book_collection.add_book(new_book)
         self.root.ids.input_title.text = ""
         self.root.ids.input_author.text = ""
         self.root.ids.input_pages.text = ""
         self.create_book_buttons()
         self.status_text = f"Book '{title}' added."

     def update_status(self):
         """Update the status labels."""
         unread_pages = self.book_collection.get_number_of_unread_pages()
         self.root.ids.status_label.text = f"Pages to read: {unread_pages}"

     def on_stop(self):
         """Save books when the app is closed."""
         self.book_collection.save_books('books.json')


if __name__ == '__main__':
    BookApp().run()

