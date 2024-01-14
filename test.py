list = [1, 4, 3, 6, 2, 9]
for i in range(len(list) - 1):
    max = list[i]
    for j in range(i + 1, len(list) - 1, 1):
        if(list[i] < list[j]):
            max = list[j]
    tmp = max
    max = list[i]
    list[i] = tmp
    
for i in list:
    print(i)