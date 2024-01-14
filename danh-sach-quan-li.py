# nạp thư viện hệ thống
import os
# nạp thư viện thời gian
from datetime import datetime
# thư viện gửi mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# đọc JSON
import json
import bson
import pymongo



# lớp đối tượng sao lưu
class Deleted:
    def __init__(self, data, time):
        self.data = data
        self.time = time

    def displayData(self):
        print(f"name: {self.data.name} | age: {self.data.age} | email: {self.data.email}")
        print(f"Thời gian xoá: {self.time.day}/{self.time.month}/{self.time.year} | Lúc: {self.time.hour}h{self.time.minute}p")
        print("------------------------------------")

# lớp đối tượng chỉ thời gian
class Date:
    def __init__(self, date):
        self.day = date.day
        self.month = date.month
        self.year = date.year
        self.hour = date.hour
        self.minute = date.minute

# lớp đối tượng chỉ người
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = None
    
    def print(self):
        print(f"name: {self.name} | age: {self.age} | gender: {self.gender} | email: {self.email}")


# làm sạch terminal
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# in ra menu lựa chọn
def menu():
    print("------MENU------")
    print("1. Thêm người vào danh sách")
    print("2. In danh sách")
    print("3. Khôi phục dữ liệu theo tên")
    print("4. chức năng khác")
    print("0. Thoát chương trình!")
    try:
        choice = int(input("Nhập lựa chọn: "))
        return choice
    except ValueError:
        print("dữ liệu phải là kiểu số nguyên!")
        return -1

# menu level 2
def menu2():
    print("------OPTIONS------")
    print("1. Chỉnh sửa thông tin")
    print("2. xoá đối tượng theo tên")
    print("3. sắp xếp theo tuổi")
    print("4. xem lịch sử xoá")
    print("5. gửi mail cho một đối tượng")
    print("6. chuyển dữ liệu thành JSON")
    print("0. trở lại menu")

    try:
        choice = int(input("nhập lựa chọn: "))
        return choice
    except ValueError:
        print("lựa chọn phải là số nguyên")
        return -1
   
# thêm người mới
def insertPerson(persons, database):
    name = input("nhập tên: ")
    try:
        age = int(input("nhập tuổi: "))
        while(True):
            gender = input("nhập giới tính: ")
            if gender == "Nam" or gender == "Nữ" or gender == "nam" or gender == "nữ":
                break
            else:
                print("giới tính phải là Nam/Nữ!")


        persons.append(Person(name, age, gender))
        
        if len(persons) == 1:
            dataSave = {
                "name": "DANH SÁCH THÀNH VIÊN",
                "length": len(persons),
                "data": [
                    {
                        "name": name,
                        "age": age,
                        "gender": gender,
                        "email": persons[len(persons) - 1].email
                    }
                    ],
            }
        else:
            dataSave = {
                "name": name,
                "age": age,
                "gender": gender,
                "email": persons[len(persons) - 1].email
                
            }
            
            
               
        DBSave(dataSave, database, persons)
        print("đã thêm thành công!")
    except ValueError:
        print("tuổi phải là số nguyên!")


# in ra danh sách
def printPerson(persons):
    if not persons:
        print("danh sách trống!")
    else:
        for person in persons:
            person.print()

# thay đổi thông tin
def changeInfo(persons, database):
    collection = database["persons"]
    findIndex = -1
    tmpName = input("nhập tên người cần thay đổi: ")
    for i in range(len(persons)):
        if persons[i].name == tmpName:
            findIndex = i

    print("ĐỐI TƯỢNG ĐƯỢC TÌM THẤY: ")
    persons[findIndex].print()
    isRunning = True
    while(isRunning):
        changeName = input("nhập trường muốn thay đổi: ")
        try:
            getattr(persons[findIndex], changeName)
            if changeName == "age":
                changeValue = int(input(f"{changeName} mới: "))
            else:   
                changeValue = input(f"{changeName} mới: ")
            update_data = {
                "$set": {
                    f"data.$.{changeName}": changeValue
                }
            }
            collection.update_one({"data.$.name": tmpName}, update_data)
            setattr(persons[findIndex], changeName, changeValue)
            print("đã thay đổi thông tin thành công")
        except Exception as error:
            print(f"lỗi: {error}")
    
        
        while(isRunning):
            try:
                result = int(input("có muốn thay đổi tiếp(1/0): "))
                if result == 0:
                    isRunning = False
                elif result == 1:
                    break
                else:
                    print("yêu cầu phải là 0 hoặc 1!")
            except ValueError:
                print("lỗi: lựa chọn phải là số nguyên!")
        

# xoá đối tượng theo tên
def delWithName(persons, deletedList):
    findIndex = -1
    tmpName = input("nhập tên cần xoá: ")
    for i in range(len(persons)):
        if persons[i].name == tmpName:
            findIndex = i


    if findIndex == -1:
        print("không tồn tại đối tượng!")
        return
    
    # thêm đối tượng vào dữ liệu đã xoá
    dataDeleted(deletedList, persons[findIndex])
    del persons[findIndex]
    print("đã xoá thành công!")

# sắp xếp danh sách
def sortPersons(persons):
    length = len(persons)
    if length == 0:
        print("danh sách trống!")
        return
    

    isRunning = True
    while(isRunning):
        sortChoice = int(input("bạn muốn sắp xếp theo tăng/giảm (1/0): "))
        if sortChoice != 0 and sortChoice != 1:
            print("lựa chọn phải là 0 hoặc 1!")
        else:
            isRunning = False

    if sortChoice == 1:
        # sắp xếp theo kiểu tăng dần
        for i in range(length - 1, -1, -1):
            for j in range(i):
                if persons[j].age > persons[j + 1].age:
                    tmp = persons[j]
                    persons[j] = persons[j + 1]
                    persons[j + 1] = tmp
    else:
        # sắp xếp theo kiểu giảm dần
        for i in range(length - 1, -1, -1):
            for j in range(i):
                if persons[j].age < persons[j + 1].age:
                    tmp = persons[j]
                    persons[j] = persons[j + 1]
                    persons[j + 1] = tmp


    print("sắp xếp xong!")

# dữ liệu được sao lưu
def dataDeleted(deletedList, data):
    currentDate = datetime.now()
    deletedList.append(Deleted(data, Date(currentDate)))

# hiện thị thông tin đã xoá
def showDataDeleted(deletedList):
    if not deletedList:
        print("chưa có dữ liệu nào được xoá!")
        return
    for data in deletedList:
        data.displayData()

# khôi phục dữ liệu theo tên
def backup(persons, deletedList):
    if not deletedList:
        print("chưa có dữ liệu nào được xoá!")
        return
    

    tmpName = input("nhập tên người cần khôi phục lại: ")
    findIndex = -1
    for i in range(len(deletedList)):
        if deletedList[i].data.name == tmpName:
            findIndex = i
            break


    if findIndex == -1:
        print("không tìm thấy đối tượng cần tìm!")
        return
    
    # khôi phục đối tượng lại danh sách và xoá đối tượng khỏi list xoá
    persons.append(deletedList[findIndex].data)
    del deletedList[findIndex]
    print("khôi phục thành công!")

# setup cấu trúc gửi mail
def customMail(toMail, subject, body):
    try:
        # khởi tạo email sender/ADMIN
        adminMail = "hieurury007@gmail.com"
        adminPass = "mawy mskw qgeq dbbj"

        # Tạo đối tượng bằng MIMEMultipart
        msg = MIMEMultipart()
        msg["From"] = adminMail
        msg["To"] = toMail
        msg["Subject"] = subject

        # Thêm nội dung email
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(adminMail, adminPass)

            # Gửi email
            server.sendmail(adminMail, toMail, msg.as_string())
            print("gửi thành công!")
    except Exception as error:
        print(f"error: {error}")


# hàm gửi mail
def sendEmail(persons):
    # danh sách trống
    if not persons:
        print("danh sách trống, không có đối tượng để gửi mail!")
        return
    
    # tìm vị trí người gửi trong danh sách
    tmpName = input("tên người cần gửi: ")
    findIndex = -1
    for i in range(len(persons)):
        if persons[i].name == tmpName:
            findIndex = i

    # kiểm tra xem đối tượng cần gửi đã tồn tại chưa
    if findIndex == -1:
        print("không tìm thấy đối tượng!")
        return
    
    # kiểm tra xem đối tượng cần gửi có email chưa
    if persons[findIndex].email == None:
        print("đối tượng chưa có email")
        return

    subject = input("nhập tiêu đề: ")
    body = input("nhập nội dung cần gửi: ")
    customMail(persons[findIndex].email, subject, body)

# chuyển dữ liệu thành json
def toJSON(persons):
    dataConvert = []

    # lấy thông tin người chơi gán cho object
    for person in persons:
        dataConvert.append(
            {
                "name": person.name,
                "age": person.age,
                "gender": person.gender,
                "email": person.email
            }
        )

    # cấu trúc lại dữ liệu file json
    dataToSave = {
        "name": "DANH SÁCH CÁC THÀNH VIÊN",
        "length": len(dataConvert),
        "data": dataConvert,
    }

    fileName = input("nhập tên file muốn lưu: ")

    # mở file/tạo file mới và lưu vào
    with open(fileName, "w", encoding="utf-8") as json_file:
        json.dump(dataToSave, json_file, ensure_ascii=False, indent=4)
    print("dữ liệu đã được lưu thành công!")


def DBSave(dataSave, database, persons):
    collection = database["members"]
    result = collection.find_one({"name": "DANH SÁCH THÀNH VIÊN"})
    if len(persons) == 1:
        collection.insert_one(dataSave)
        
    else:
        update_query = {
            "$set": {
                "length": len(persons)  
            },
            "$push": {
                "data": dataSave
            }
        }
        collection.update_one(result, update_query)
        
def DBRender(persons, database):
    collection = database["members"] 
    result = collection.find_one({"name": "DANH SÁCH THÀNH VIÊN"})
    DBPersons = result["data"]
    for person in DBPersons:
        persons.append(Person(person["name"], person["age"], person["gender"]))
        persons[len(persons) - 1].email = person["email"]
    
    
    
# ========================= CẤU TRÚC CHÍNH =====================

try:
    DBconnect = pymongo.MongoClient("mongodb://localhost:27017/")
    database = DBconnect["hieururyStudent"]
    # collection = database["persons"]
    print("kết nối database thành công!")
except Exception as error:
    print(f"lỗi: {error}")
    
#khai báo các mảng và điều kiện 
deletedList = []
persons = []
isRunning = True


try:
    DBRender(persons, database)

except:
    print("chưa có dữ liệu")
    
    
while isRunning:
    choice = menu()
    if choice == 1:
        clearTerminal()
        insertPerson(persons, database)
    elif choice == 2:
        clearTerminal()
        printPerson(persons)
    elif choice == 3:
        clearTerminal()
        backup(persons, deletedList)

    # menu cấp 2 
    elif choice == 4:
        choice = menu2()
        if choice == 1:
            clearTerminal()
            changeInfo(persons, database)
        elif choice == 2:
            clearTerminal()
            delWithName(persons, deletedList)
        elif choice == 3:
            clearTerminal()
            sortPersons(persons)
        elif choice == 4:
            clearTerminal()
            showDataDeleted(deletedList)
        elif choice == 5:
            clearTerminal()
            sendEmail(persons)
        elif choice == 6:
            clearTerminal()
            toJSON(persons)
        elif choice == 0:
            isRunning = True
        else:
            print("lựa chọn không hợp lệ")


    elif choice == 0:
        print("đã chọn thoát")
        isRunning = False
    else:
        print("lựa chọn không hợp lệ")
            
