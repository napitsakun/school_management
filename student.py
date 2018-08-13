'''class Student:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address

n = int(input("Enter number of students"))
student = []

for i in range(n):
    x = input("Enter name: ")
    y = input("Enter address: ")
    stud = Student(x, y)
    student.append(stud)

disp = map(lambda stud: stud.getName() + " " + stud.getAddress(), student)
print(list(disp))
'''

from books import Book

class Student:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address

n = int(input("Enter number of students"))
student = []

for i in range(n):
    x = input("Enter name: ")
    y = input("Enter address: ")
    stud = Student(x, y)
    student.append(stud)

disp = map(lambda stud: stud.getName() + " " + stud.getAddress(), student)
print(list(disp))

book = Book(1, "sad", "me")
print(book.getAuthor())
