from books import *
from borrowers import *
from transactions import *
# from main import transaction1

borrowed_books = {}

# Main loop for book Borrowing
def main_borrow():
    while True:
        print('Here is list of books to select:')
        j = 1
        # for loop for printing the books
        for i in list_books:
            print(f'{j} ). ',i)
            print()
            j += 1
        # Exit and main library option
        print('m ).  Return to Library')
        print('0 ).  Exit')

        usr = input('>>> ')
        if usr == '1':
            print(transaction1.borrow_book(book1))
            borrowed_books[book1.book_ID] =  book1.book_title
        elif usr == '2':
            print(transaction1.borrow_book(book2))
            borrowed_books[book2.book_ID] = book2.book_title
        elif usr == '3':
            print(transaction1.borrow_book(book3))
            borrowed_books[book3.book_ID] =  book3.book_title
        elif usr.lower() == 'm':
            lib()
            break
        elif usr == '0':
            print('Good bye')
            break
        else:
            print('Invalid Input!')

# function for returning the Books

def main_return():
    print('     ** Here is The Books You Borrowed select the Book you want to return. **')
    # loop for printing borrowed books
    while True:
        for i in borrowed_books:
            print(f'{i}     {borrowed_books[i]}\n')
        print('0.    Exit')
    
        usr = input('>>>  ')
        if usr == '1':
            borrowed_books.__delitem__(1)
            print(transaction1.return_book(book1))
        elif usr == '2':
            borrowed_books.__delitem__(2)
            print(transaction1.return_book(book2))

        elif usr == '3':
            borrowed_books.__delitem__(3)
            print(transaction1.return_book(book3))

        elif usr == '0':
            break
        else: 
            print('Invalid input!')



# A function that display the book borrowed and return option
def lib():
    print('*******....*** Welcome to Library ***....*******')
    print('''
           Please select from the list:
          1.     Borrow
          2.     Return
          ''')
    std = input('>>> ')
    if std == '1':
        main_borrow()
    elif std == '2':
        main_return()
    
    else:
        print('Ivalid input! Please try again.')



print('    Welcome to Library\n\n')
print('''
              1.  Login
              2.  Registration
          ''')
usr = input('>>> ')
if usr == '1':
    # Calling the login Functio
    try:
        trans,a = student_login()
        transaction1 = Transaction(trans)
        print(a)
        if a == True:
            lib()
    except Exception as e:
        print(e)

elif usr == '2':
    registeration()
    print('Congratulations! You have registered.\n\n')
    trans, a = student_login()
    transaction1 = Transaction(trans)
    if a == True:
        lib()
        