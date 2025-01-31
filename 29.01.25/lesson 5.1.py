# перевод в системы счисления (из 10-чной)
num = int(input())
sys = 7

res =""
while num:
     res += str(num % sys)
     num //= sys

print(res[::-1])