list = [[]]

r = int(input("enter r: "))
c = int(input("enter c: "))

for i in range(r):
    list.append([])
    for j in range(c):
        list[j].append(int(input()))

for i in range(r):
    for j in range(c):
        print(list[i][j], end=" ")
    print("\n")
