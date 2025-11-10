from re import finditer
# with open(f'Regexp contest/regexp-practice-7.txt', encoding="utf-8") as file:
#     data = file.read()
#     pattern = r'[0-9a-zA-Z-_]+@[0-9a-zA-Z-_]+\.[a-z]+'
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)
# with open("24-334.txt") as file:
#     data = file.readline()
#     pattern = r"([1-9AB][0-9AB]*[0246A])|([0-9AB])"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(len(max(matches, key=len)))
with open("24-347.txt") as file:
    data = file.readline()
    pattern = r"[1-7][0-7]*"
    matches = [match.group() for match in finditer(pattern, data)]
    ans = []
    ans2 = []
    for i in matches:
        if int(i, 8) % 13 == 0:
            ans.append(i)
        else:
            for l in range(0, len(i)):
                for r in range(1, len(i) - l):
                    i_slice = i[l:-r]
                    if int(i_slice, 8) % 13 == 0:
                        ans2.append(i_slice)
                        break
max_len = []
minn = []
max_len1 = len(max(ans, key=int))
for i in ans2:
    if len(i) == max_len1:
        max_len.append(i)
for i in max_len:
    i1 = int(i)
    minn.append(i)
minn2=min(minn)
print(minn2)
for i in ans:
    if len()














