# from gettext import dgettext
#
# a = input()
# b = ""
# for i in a:
#     if "A"<=i<="Z":
#         b += chr(ord(i)+ 32)
#     else:
#         b += i
# print(b)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# q = input()
# if '0' in q or '1' in q or '2' in q or '3' in q or '4' in q or '5' in q or '6' in q or '7' in q or '8' in q or '9' in q:
#     print(False)
# else:
#     print(True)
#
#
#
#
#
#
#
#
#
#
#
# d = input()
# c = ""
# for i in d:
#     if '0'<=i<="9":
#         c +=i
#         print(c)
#
#
#
#
#
#
#
#







# a = input()
# b = ""
# chislo = 0
# for i in a:
#     if i != '+':
#         b += i
#     else:
#         chislo += int(b)
#         b = ""
# print(chislo+int(b))



num = input()
num = num.split('+')
num2 = 0
for i in num:
    num2 += int(i)


print(num2)




