with open("26_20815.txt") as file:
    people, places = map(int,file.readline().split())
    students =[]
    for i in file:
        students.append(list(map(int,i.split())))
students.sort(key=lambda arr: (arr[1]+arr[2]+arr[3]+arr[4],arr[4],-arr[0]), reverse=True)
print(students[people-1])