from transactions import Transaction

# create a class for the borrowers of books from library
students_ID_list = []
students_List = {}
names = []


class Borrower:
    def __init__(self, name, studentID, department):
        self.name = name
        self.studentID = studentID
        self.department = department
        students_ID_list.append(studentID)
        names.append(name)
        students_List[name] = [studentID, department]

    
    def __str__(self) -> str:
        return f'Student: {self.name}, Student ID: {self.studentID} of Department: {self.department}'
    

# Creating instances of Borrower class
student1 = Borrower('Ali', 'awkum123', 'Computer Science')
student2 = Borrower('Ahmad', 'awkum124', 'Software Engineering')
student3 = Borrower('Gul', 'awkum125', 'Political Science')


# function for signup
def registeration():
    print('    Registration    ')
    name = input('Name: ')
    stdID = input("Student ID: ")
    dep = input('Department: ')

    student = Borrower(name, stdID, dep)
    return student



# A function for student log in
def student_login():
    login = False
    print('\n\n            Log In     \n\n')

    name = input('Name: ')
    stud_ID = input('Student ID: ')

   
   # Condition for checking the student instance 
    
    if name in students_List:
        if students_List[name][0] == stud_ID:
            print('Login Successfull!')
            dep = students_List[name][1]
            login = True
            student = Borrower(name, stud_ID, dep)
        else:
            print('Invalid Student ID or name!')
    return student, login
    
