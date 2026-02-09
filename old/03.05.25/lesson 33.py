with open("26_9171.txt") as file:
    m, k, n = map(int, file.readline().split())
    line = []
    requests = []
    for line in range(n):
        otkuda, kuda = map(int,str)
        requests.append((otkuda, kuda))

    passazhirov_doehalo = 0
    waiters = []
    peregonov_polniy_poezd = 0
    mesta_v_poezde = [0] * k
for i in range(1,m):
    for j in range(k):
        if mesta_v_poezde != 0:
            start, end = mesta_v_poezde
            if start == i:
                mesta_v_poezde[j] = 0
    for start, end in requests:
        if start == i:
            requests.append((start, end))
waiters.sort(key=lambda x: x[1], reverse=True)
for start, end in waiters:
    for j in range(k):
        if mesta_v_poezde[j] == 0:
            mesta_v_poezde = (start, end)
            passazhirov_doehalo += 1
            break
polniy_poezd = True
for j in range(k):
    if mesta_v_poezde[j] == 0:
        polniy_poezd = False
        break
    if polniy_poezd:
        peregonov_polniy_poezd += 1
new_requests = []
for start, end in requests:
    sel_v_poezd = False
    for j in range(k):
        if mesta_v_poezde[j] == (start,end):
            sel_v_poezd = True
            break
        if not sel_v_poezd:
            new_requests.append((start,end))
        requests = new_requests
print(passazhirov_doehalo, peregonov_polniy_poezd)


