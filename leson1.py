# tạo một danh sách quản lí thành viên
# yêu cầu: tên, tuổi, gpa.
# chức năng thêm thành viên vào danh sách
# xoá thành viên khỏi danh sách
# sắp xếp danh sách theo 1 trong 2 thứ tự tăng dần hoặc giảm dần (quyết định bằng 0 hoặc 1)
# in danh sách


#khởi tạo kiểu dữ liệu Member
class Member:
    def __init__( self, name, age, GPA):
        self.name = name
        self.age = age
        self.GPA = GPA
    
    def show(self):
        print(f"name: {self.name} | age: {self.age} | GPA: {self.GPA}")
    
 
 
#thêm thành viên
def insert(members):
    name = input("enter name: ")
    age = int(input("enter age: "))
    GPA = float(input("enter GPA: "))
    
    members.append(Member(name, age, GPA))
 
 
 
 
def deleteWithName(members):
    # kêu ngta nhập tên muốn xoá -> lặp trong danh sách -> nếu có người đó -> lấy index
    # từ index đã lấy được -> xoá
    
    isRunning = True
    while(isRunning):
        name = input("name: ")
        index = -1
    # index chạy từ 0 cho đến độ dài của mảng - 1
    
        for i in range(len(members) - 1):
            if(members[i].name == name):
                index = i
                
        #đặt index mặc định = -1
        #lập qua từng phần tử trong mảng -> nếu tìm thấy -> index = i, ko tìm thấy index VẪN NHƯ CŨ
                
        if(index != -1 ):
            del members[index]
            print("đã xoá thành công!")
            isRunning = False
        else:
            print("không tìm thấy, vui lòng nhập lại!")
            


def sort(members):
    isRunning = True
    while(isRunning):
        try: #thử làm cái việc dưới này
            option = int(input("bạn muốn sắp xếp tăng/giảm (1/0): "))
            if(option == 0 or option == 1):
                isRunning = False
                if(option == 1):
                    # 1 2 5 3
                    # 0 1 2 3    01  12  23 34
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



#hiện độ dài của mảng
def showLength(members):
    print(f"length: {len(members)}") 
   
   
#hiện thị thông tin các thành viên
def display(members):
    for member in members:
        member.show()
        
        
members = []
insert(members)
insert(members)
sort(members)
display(members)
