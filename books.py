# create a class for books
list_books = []
class Book:
    def __init__(self, book_title, author, book_ID):
        self.book_title = book_title
        self.author = author
        self.book_ID = book_ID
    
    def __str__(self) -> str:
        return f'Book Name: {self.book_title}, Author: {self.author}'

# creating instances of book class
book1 = Book('An introduction to Computer Science', 'Gul Khan', 1)
book2 = Book('An Introduction to Programming in C++', 'John Dalton', 2)
book3 = Book('An Introduction to Programming in Python', 'Dawid Malan', 3)
list_books.append(book1)
list_books.append(book2)
list_books.append(book3)

