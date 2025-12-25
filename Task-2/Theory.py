# Порядок выполнения операций в алгебре логики
# 1. Отрицание / Инверсия (¬A, (not A))
# 2. Логическое умножение / Конъюнкция (A∧B, A∙B, A and B)
# 3. Логическое сложение / Дизъюнкция (A∨B, A+B, A or B)
# 4. Следование / Импликация (A→B, A <= B)
# 5. Тождество / Эквивалентность (A≡B, A == B)

# Исключающее или / XOR (A ⊕ B, A ^ B)
# Порядок выполнения операций в Python
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. in, not in
# 6. ==, !=, >, >=, <, <=
# 7. ^
# 8. not
# 9. and
# 10. or

# Решение через лесенку
# print('a b c d')
# for a in 0,1:
#     for b in 0, 1:
#         for c in 0, 1:
#             for d in 0, 1:
#                 f = (not a and not b) or (b == c) or d
#                 # Все строки истинны
#                 if f:
#                     print(a, b, c, d)
#                 # Все строки ложны
#                 if not f:
#                     print(a, b, c, d)
#                 # Строки вперемешку
#                 print(a, b, c, d)


# second way

#args
def f1(a,b,c):
    return a+b+c
test = [1,2,3]
print(f1(*test))


# kwargs
def f2(a,b):
    return a / b
test2 = {"a":5, "b":2}
print(f2(**test2))

from itertools import *
def f(x,y,z,w):
    return (x or y) and not(y==z) and not w
for i in product((0,1), repeat=4):
    table = [
        (1,i[0],1,i[1]),
        (0,1,i[2],0),
        (i[3],1,1,0)
    ]
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p,t))) for t in table] == [1,1,1]:
                print(*p,sep="")