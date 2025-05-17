# def calculator(*args, k=1):
#
#     summ = 0
#     for i in args:
#         summ += i *k
#     return summ
# ans = calculator(1,2,4, k=2)
# print(ans)


def read_file(file_name):
    with open(file_name) as file:
        N = int(file.readline())
        data = []
        for i in file:
            data.append(list(map(int,i.split())))
    return N,data


def solution():
    N, data = read_file("26_21598.txt")
    time = [0] * 1441
    for i in data:
        for j in range(i[0], i[1] + 1):
            time[j] += 1
    change = []
    for i in range(len(time)-1):
        if time[i] != time[i+1]:
            change.append(i)
    print(change[-2])

solution()








