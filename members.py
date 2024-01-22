import os;

class Member:
    def __init__(self, name, age, GPA):
        self.name = name
        self.age = age
        self.GPA = GPA
    def show(self):
        print(f"name: {self.name} | age: {self.age} | GPA: {self.GPA}")


default = "\033[0m"
red = "\033[1;31m"
yellow = "\033[1;33m"
green = "\033[1;32m"

#làm sạch terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


#nhap thong tin thanh vien
def insert(members):
    name = input("enter name: ")
    while True:
        try:
            age = int(input("enter age: "))
            break
        except ValueError:
            print("ban da nhap sai, hay nhap la so!")

    while True:
        try:
            GPA = float(input("enter GPA: "))
            break
        except ValueError:
            print("ban da nhap sai, hay nhap la so!")
    members.append(Member(name, age, GPA))
    print(f"{green}Thêm thành công!")



#xoa thanh vien 
def deleteWithName(members):
        name = input("name you want to delete: ")
        index = -1
        for i in range(len(members)):
            if(members[i].name == name):
                index = i
        if(index != -1):
            del members[index]
            print("delete succesful!")
        else:
            print("not find!")

def change(members):
    name = input("ten ban muon thay doi: ")
    index = -1
    for i in range(len(members)):
        if(members[i].name == name):
                index = i
        
    if(index != -1):
        isChanging = True
        while(isChanging):
            nameChange = input("nhập trường muốn thay đổi: ") #=> muốn đổi gì thì nhập đó
            
            #truy cập vào đối tượng theo một trường không tồn tại
            try:
                getattr(members[index], nameChange) #get attribute
                if(nameChange == "age"):
                    valueChange = int(input("nhập tuổi mới: "));
                elif(valueChange == "GPA"):
                    valueChange = float(input("nhập GPA mới: "))
                else:
                    valueChange = input("nhập tên mới: ")
                    
                setattr(members[index], nameChange, valueChange)
                
                print("thay doi thanh cong!")
            except Exception as error:
                print(f"lỗi: {error}")
                
            
            
            #lập vô tận để hỏi người dùng muốn đổi tiếp hay không
            #nếu chọn 1 -> đổi tiếp. thì quay lại vòng tuần hoàn trên với biến isChanging = True (tiếp tục việc thay đổi)
            #nếu chọn 0 -> ngừng đổi. thì cho isChanging = False ( ngừng vòng tuần hoàn -> thoát việc thay đổi)
            while(True):
                try:              
                    choice = int(input("có muốn thay đổi tiếp không (1/0):"))
                    if(choice == 0):
                        isChanging = False
                        break
                    elif(choice == 1):
                        break
                    else:
                        print("lựa chọn phải là 0 hoặc 1: ")
                except ValueError:
                    print("lựa chọn phải là số nguyên!")
                    
            
    else:
            print("khong tim thay ten muon thay doi!")




#sap xep
def sort(members):
    if not members:
        print("Danh sach trong, khong the sap xep!")
    else:    
        isRunning = True
        while(isRunning):
            try: #thử làm cái việc dưới này
                option = int(input("bạn muốn sắp xếp tăng/giảm (1/0): "))
                if(option == 0 or option == 1):
                    isRunning = False
                    if(option == 1):
                    
                        for i in range(len(members) - 1):
                            for j in range(0, len(members) - (i+1), 1):
                                if(members[j].GPA > members[j + 1].GPA):
                                    tmp = members[j]
                                    members[j]= members[j + 1]
                                    members[j + 1] = tmp
                    else:
                        for i in range(len(members) - 1):
                            for j in range(0, len(members) - (i+1), 1):
                                if(members[j].GPA < members[j + 1].GPA):
                                    tmp = members[j]
                                    members[j] = members[j + 1]
                                    members[j + 1] = tmp
                else:
                    print("lựa chọn không hợp lệ, vui lòng chọn lại")
            except ValueError: #nếu mà cái việc trên kia ko đúng yêu cầu (valueError: lỗi giá trị) thì thực thi câu lệnh
                print("giá trị ko hợp lệ, vui lòng nhập số nguyên")


#hien thi do dai mang
def showLength(members):
    print(f"length: {len(members)}") 
   
   
#hien thi thong tin thanh vien
def display(members):

    if not members:
        print("Danh sach trong!")
    else:
        for member in members:
            member.show()

#
def menu():
    print(default)
    print("------------- MENU -------------") 
    print("1. Them thanh vien")  
    print("2. Xoa thanh vien")
    print("3. Sap xep thanh vien")
    print("4. Hien thi thong tin thanh vien")
    print("5. Thay doi thong tin thanh vien")
    print("0. Thoat")
    try:
        luaChon = int(input("Hay nhap lua chon: "))
        return luaChon
    except ValueError:
        print("ban da nhap sai, vui long nhap lua chon la so nguyen!")
        return -1
    
   

#noi dung chinh       
members = []

while True:
    choice = menu()
    if (choice == 1):
        clear_terminal()
        print("Lua chon: Them thanh vien")
        insert(members)
    elif (choice == 2):
        clear_terminal()
        print("Lua chon: Xoa thanh vien")
        deleteWithName(members)
    elif (choice == 3):
        clear_terminal()
        print("Lua chon: Sap xep thanh vien")
        sort(members)
    elif (choice == 4):
        clear_terminal()
        print("Lua chon: Hien thi thong tin thanh vien")
        display(members)
    elif (choice == 5):
        clear_terminal()
        print("Lua chon: thay doi thong tin thanh vien")
        change(members)
    elif (choice == 0):
        print("Lua chon: Thoat")
        break
    else:
        print("Lua chon khong hop le, vui long chon lai!")