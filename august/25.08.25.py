from re import finditer
# with open("24-337.txt") as file:
#     data = file.read()
#     ans = []
#     ans_2 = []
#     pattern = r"[1-9ABCD][0-9ABCD]+"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)
#     for i in matches:
#         if int(i, 14) % 98 == 0:
#             ans.append(i)
#         else:
#             for l in range(0, len(i)):
#                 for r in range(1, len(i) - l):
#                     i_cut = i[l:-r].lstrip("0")
#                     if i_cut and int(i_cut, 14) % 98 == 0:
#                         ans.append(i_cut)
# print(ans)
# print(len(max(ans, key=len)))

with open("24-314.txt") as file:
    data = file.read()
    number = r"([1-7][0-7]*|0)"
    must_1 = r"F"
    pattern = fr"(?<={must_1})({number}[+*])+{number}"
    matches = [match.group() for match in finditer(pattern, data)]






