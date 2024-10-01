class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book: 'Book'):
        self.books.append(book)

    def get_books(self):
        return f"Libros del autor: {[book.title for book in self.books]}"

#________________________________________________________________


class Book:
    def __init__(self, title: str, pages: int, author: Author):
        self.title = title
        self.pages = pages
        self.author = author
    
    def __str__(self):
        return f"Libro: {self.title}"

#________________________________________________________________


class Library:
    def __init__(self):
        self.books = []


author_1 = Author(name='Gabriel García Marquez')

author_1.add_books(book_1)

book_1 = Book('Cien años de soledad', 473, author_1)

#Llamado de atributos de clase

print(author_1.book_1)
