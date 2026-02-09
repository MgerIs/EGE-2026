from re import finditer
# with open("24-314.txt") as file:
#     data = file.read()
#     lenmax = []
#
#     maxx3 = []
#     number = r"([1-7][0-7]*|0)"
#     must_1 = r"F"
#     pattern = fr"(?<={must_1})({number}[+*])+{number}"
#     matches = [match.group() for match in finditer(pattern, data)]
#     maxlen = len(max(matches, key=len))
#     for i in matches:
#         if len(i) == maxlen:
#             lenmax.append(i)
#     maxx = (max(lenmax))
#     maxx2 = maxx.split("+")
#     cnt = 0
#     for i in maxx2:
#         multiply = 1
#         for j in i.split("*"):
#             multiply *= int(j,8)
#         cnt += multiply
#     print(cnt)

# with open("24_7600 (1).txt") as file:
#     data = file.read()
#     pattern = r"([^QRS]+[QRS])+[^QRS]*[QRS]?"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(len(max(matches, key=len)))
with open("24_7624.txt") as file:
    data = file.read()
    pattern = r"([^XYZ]+[XYZ])+[^XYZ]*[XYZ]?"
    matches = [match.group() for match in finditer(pattern, data)]
    print(len(max(matches, key=len)))
with open("24_8510.txt") as file:
    data = file.read()
    pattern = r"([^NOP]+[NOP])+[^NOP]*[NOP  ]?"
    matches = [match.group() for match in finditer(pattern, data)]
    print(len(max(matches, key=len)))
with open("24_4710.txt") as file:
    data = file.read()
    pattern = r"([CDF][AO])+"
    matches = [match.group() for match in finditer(pattern, data)]
    print(len(max(matches, key=len))//2)















