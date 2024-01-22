
# nạp thư viện thời gian
from datetime import datetime


class Date:
    def __init__(self, date):
        self.day = date.day
        self.month = date.month
        self.year = date.year
        self.hour = date.hour
        self.minute = date.minute
        self.second = date.second
class User :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayU(self):
        print(f"name: {self.name} | age: {self.age}")    



class DataBackup:
    def __init__(self, data, time):
        self.data = data # databackup -> data(User) -> name, age 
        self.time = time
        
    def displayU(self):
        print(f"name: {self.data.name} | age: {self.data.age}")
        print(f"xoa luc: {self.time.day}/{self.time.month}/{self.time.year} - {self.time.hour}.{self.time.minute}.{self.time.second}")

def delWithName():
    name = input("name: ")
    
    index = -1
    for i in range(len(users)):
        if(users[i].name == name):
            index = i
            
    if(index != -1):
        time = datetime.now()
        bins.append(DataBackup(users[index], time))
        del users[index]
    else:
        print("ko tim thay!")


      
def backup():
    name = input("name: ")
    
    index = -1
    for i in range(len(bins)):
        if(bins[i].data.name == name):
            index = i
            
    if(index != -1):
        users.append(bins[index].data)
        del bins[index]
    else:
        print("ko tim thay!")
  
def display(lists, cmt):
    print(cmt)
    for value in lists:
        value.displayU()
        
time = datetime.now()   


        
users = []
bins = []


users.append(User("huynh", 19))
users.append(User("hieu", 19))
display(users, "in danh sách")
display(bins, "in thùng rác")


delWithName()
print("---------------")
display(users, "in danh sách sau xoá")
display(bins, "in thùng rác sau xoá")
backup()
print("---------------")
display(users, "in danh sách sau khoi phuc")
display(bins, "in thùng rác sau khoi phuc")
