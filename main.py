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
