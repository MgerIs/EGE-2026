with open("26_19256.txt") as file:
    N = int(file.readline())
    students = {}
    for i in file:
        ident, num = map(int, i.split())
        if ident in students:
            students[ident].add(num)
        else:
            students[ident] = {num}
ans = []
for ident in students:
    student = sorted(students[ident])
    cnt = 1
    max_cnt = 0
    for i in range(len(student)-1):
        if student[i+1] - student[i] == 1:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 1
        ans.append([max_cnt, ident])

ans.sort(key= lambda x: (x[0], -x[1]), reverse=True)
print(ans[0])

