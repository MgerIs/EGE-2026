# Системы счисления

# Двоичная система
N = 25
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'
print(bin(N)[2:])
# f'' - форматируемая строка, которая позволяет вставлять в себя переменные
print(f'{N:b}')

# Восьмеричная система
print(oct(N)[2:])
print(f'{N:o}')

# Шестнадцатеричная система
print(hex(N)[2:])
print(f'{N:x}')

# Перевод в любую систему (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]


# Перевод в любую систему (2 <= sys <= 36)
from string import printable as alph

def convert2(num, sys):
    res = ''
    while num != 0:
        res += alph[num % sys]
        num //= sys
    return res[::-1]


# Перевод в 10 систему
num_bin = '101'
num_tri = '121'
num_hex = 'fa8'

print(int(num_bin, 2))
print(int(num_tri, 3))
print(int(num_hex, 16))

# Сумма цифр числа
# двоичное число
R_1 = '101'
sum_1 = R_1.count('1')

# число в любой системе до 10 включительно
R_2 = '198'
sum_2 = sum(map(int,R_2))

# число в любой системе до 10 включительно
R_3 = 'AF7'
sum_3 = sum(map(lambda x: int(x,36), R_3))