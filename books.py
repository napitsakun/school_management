class Book:
    def __init__(self, idd, name, author):
        self.idd = idd
        self.name = name
        self.author = author
        
    def getId(self):
        return self.idd
    
    def getName(self):
        return self.name
    
    def getAuthor(self):
        return self.author

book = []
n = int(input("how many book details? "))

for i in range(n):
    a = input("Enter id of book")
    b = input("Enter name of book: ")
    c = input("Enter author naame of the book: ")
    entry = Book(a, b, c)
    book.append(entry)

disp = map(lambda entry: entry.getId() + " " + entry.getName() + " " + entry.getAuthor(), book)
print(list(disp))