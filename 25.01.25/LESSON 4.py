#работа с модулями и слэш библиотеками и пакетами


#импорт всех функций из модуля
import random

num_1 = random.randint(1,10)

#импорт всех функций через псевдоним
import random as rnd
num_2 = rnd.randint(1,10)


#импорт одной функции из модуля. К модулю по имени обращаться не надо
from random import randint
num3 = randint(1,30)


# импорт всех функций из модуля. к модулю по имени обращаться не надо
from random import *
num4 = randint(1,21)




from string import ascii_uppercase

print(ascii_uppercase)
print(chr(0x2764))
print(ord("a"))


