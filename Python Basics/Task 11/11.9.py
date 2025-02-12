# Create a class Library that maintains a list of books and allows adding/removing books.
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)
    
    def display_books(self):
        print(self.books)

library = Library()

library.add_book("Book 1")
library.add_book("Book 2")
library.add_book("Book 3")

library.display_books()

library.remove_book("Book 2")

library.display_books()