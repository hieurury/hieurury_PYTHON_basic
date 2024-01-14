import pymongo


class Book:
    def __init__(self, name, author, typeBook):
        self.name = name
        self.author = author
        self.typeBook = typeBook
        
    def displayBook(self):
        print(f"Name book: {self.name} | Author: {self.author} | type book: {self.typeBook}")
        

def menu():
    print("-----MENU-----")
    print("1. add new book")
    print("2. show list book")
    print("3. exit")
    try:
        choice = int(input("enter your choice: "))
        return choice
    except ValueError:
        print("type input is number!")
        return -1

def insert(library, database):
    collection = database["comics"]
    name = input("enter name book: ")
    author = input("enter name author: ")
    typeBook = input("enter name typeBook: ")
    try:
        dataSave = {
            "name": 
        }
        library.append(Book(name, author, typeBook))
        print("successful!")
    except Exception as error:
        print(f"error: {error}")


def printBook(library):
    for book in library:
        book.displayBook()
  
  
try:
    DBconnect = pymongo.MongoClient("mongodb://localhost:27017/")
    database = DBconnect["library"]
    print("connected")
except Exception as error:
    print(f"lỗi: {error}") 
    
         
comics = []
isRunning = True

while isRunning:
    number = menu()
    if number == 1:
        insert(comics)
    elif number == 2:
        printBook(comics)
    elif number == 3:
        print("exited")
        isRunning = False
    else:
        print("pls choice number in menu")
