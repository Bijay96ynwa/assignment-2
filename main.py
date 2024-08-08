from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from book import Book, BookCollection
import json

class BookApp(App):
    def build(self):
        self.title = "Book Manager"
        self.book_collection = BookCollection()
        self.book_collection.load_books('books.json')

        self.main_layout = BoxLayout(orientation='horizontal')
        self.left_layout = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        self.right_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 1))

        self.spinner = Spinner(
            text='Sort by Author',
            values=('author', 'title'),
            size_hint=(1, 0.1)
        )
        self.spinner.bind(text=self.sort_books)
        self.left_layout.add_widget(self.spinner)

        self.title_input = TextInput(hint_text='Title', size_hint=(1, 0.1))
        self.author_input = TextInput(hint_text='Author', size_hint=(1, 0.1))
        self.pages_input = TextInput(hint_text='Number of pages', size_hint=(1, 0.1))
        self.add_button = Button(text='Add Book', size_hint=(1, 0.1))
        self.add_button.bind(on_press=self.add_book)

        self.left_layout.add_widget(self.title_input)
        self.left_layout.add_widget(self.author_input)
        self.left_layout.add_widget(self.pages_input)
        self.left_layout.add_widget(self.add_button)

        self.status_label = Label(text='Number of pages to read:', size_hint=(1, 0.1))
        self.right_layout.add_widget(self.status_label)

        self.main_layout.add_widget(self.left_layout)
        self.main_layout.add_widget(self.right_layout)
        self.update_books_display()

        return self.main_layout

    def sort_books(self, spinner, text):
        self.book_collection.sort_books(text)
        self.update_books_display()

    def update_books_display(self):
        self.right_layout.clear_widgets()
        self.right_layout.add_widget(self.status_label)
        self.book_buttons = []
        for i, book in enumerate(self.book_collection.books):
            button = Button(text=str(book), size_hint=(1, None), height=40)
            button.bind(on_press=self.toggle_book_status)
            self.right_layout.add_widget(button)
            self.book_buttons.append(button)

        unread_pages = self.book_collection.get_number_of_unread_pages()
        unread_count = sum(1 for book in self.book_collection.books if book.status == 'u')
        self.status_label.text = f"You still need to read {unread_pages} pages in {unread_count} books."

    def toggle_book_status(self, instance):
        index = self.book_buttons.index(instance)
        book = self.book_collection.books[index]
        if book.status == 'u':
            book.mark_completed()
            instance.text = str(book)
        else:
            book.mark_unread()
            instance.text = str(book)
        self.update_books_display()

    def add_book(self, instance):
        title = self.title_input.text
        author = self.author_input.text
        try:
            pages = int(self.pages_input.text)
            if pages <= 0:
                self.show_error("The book must have some pages!")
                return
        except ValueError:
            self.show_error("Please enter a valid number")
            return

        if not title or not author:
            self.show_error("Please complete all fields.")
            return

        book = Book(title, author, pages)
        self.book_collection.add_book(book)
        self.update_books_display()
        self.title_input.text = ''
        self.author_input.text = ''
        self.pages_input.text = ''

    def show_error(self, message):
        popup = Popup(title='Error',
                      content=Label(text=message),
                      size_hint=(0.6, 0.4))
        popup.open()

    def on_stop(self):
        self.book_collection.save_books('books.json')
        print(f"{len(self.book_collection.books)} books saved to books.json")

if __name__ == '__main__':
    BookApp().run()
