# a = input()
# var_str = ""
# for i in a:
#     if 'z' >= i >= "a":
#         var_str += chr(ord(i)-32)
#     else:
#         var_str += i
# print(var_str)


a = input()
b = a[0]
res = ""
if "A" <= b <= "Z":
    res += b
else:
    res += chr(ord(b) - 32)
for i in range(1, len(a)):
    if "a" <= a[i] <= "z":
        res += a[i]
    else:
        res += chr(ord(a[i])+32)
print(res)






a = input()
b = input()
l = len(b)
print(a[-l:] == b)
