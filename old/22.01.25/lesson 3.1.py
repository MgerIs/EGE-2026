# условный оператор
a = float(input())
if a > 0:
    print("+")
if a < 0:
    print("-")
if a == 0:
    print("0")

var = 19
# If понимает только true и false
# Все значения в условии if конвертируются в bool(лог тип данных)
#if var:
    #print("hello")

# порядок выполнения операций в Python
# 1.()
# 2. **
# 3. *, /, //, %
# 4. +-
# 5. >,<, >=, <=(импликация), ==(эквивалентност/тождество), !=
# 6. not (инверсия)
# 7. and (коньюнкция)
# 8. or (дизьюнкция)




num1 = 12
num2 = -1
num3 = 0
f1 = 10<= num1 <=99
f2 = num2<0
f3 = (num1+num2+num3)%2 == 0






if f1 and f2 and f3:
    print("text1")
if f1 or f2 of f3:
    print("text2")