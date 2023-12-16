# create a transaction class where students can borrow and return book to Library

class Transaction:
    def __init__(self, student):
        self.student = student

    # define a function where students borrow books from library
    def borrow_book(self, book):
        return f'You: {self.student}, borrowed book: {book}'
    
    def return_book(self, book):
        return f'You: {self.student}, returned book: {book}'
    

