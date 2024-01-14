def delWithName(persons, deletedList, database):
    collection = database["members"]
    findIndex = -1
    tmpName = input("nhập tên cần xoá: ")
    for i in range(len(persons)):
        if persons[i].name == tmpName:
            findIndex = i


    if findIndex == -1:
        print("không tồn tại đối tượng!")
        return
    
    delete_data = {
        "$pull": {
            "data": {
                "name": tmpName
            }
        }
    }
    
    person_filter = [{"element.name": tmpName}]
    collection.update_one({},delete_data, array_filters=person_filter)
    # thêm đối tượng vào dữ liệu đã xoá
    dataDeleted(deletedList, persons[findIndex])
    del persons[findIndex]
    print("đã xoá thành công!")