class Book:
    "represent a book object"

    def __init__(self, title, author, pages, is_completed=False):

        self.title=title
        self.author=author
        self.pages=pages
        self.is_completed =is_completed

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages, {'Completed' if self.is_completed else 'Required'}"

    def mark_completed(self):
        """Mark the book as completed."""
        self.is_completed = True

    def mark_required(self):
        """Mark the book as required."""
        self.is_completed = False

    def is_long(self):
        """Determine if the book is considered long (>= 500 pages)."""
        return self.pages >= 500


