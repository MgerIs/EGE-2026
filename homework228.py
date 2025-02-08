age = int(input())
if age < 0 or age > 3000:
    print('эээ дон слушай мене суда унимателно нормальное число введи ежже')
if age % 4 == 0 and age % 100 != 0:
    print("я тебе афигено сделаю")
elif age % 400 == 0 and age % 100 == 0:
    print("")
else:
    print("говно переделывай")








import random
var_list = random.sample(range(1,1000), 100)
number = var_list[0]
for i in range(0,len(var_list)):
    if var_list[i] > number:
        number = var_list[i]
while number + 1 in var_list:
    print(number)
counter = number - 1
while counter  not in var_list:
    counter -= 1
print(number, counter, var_list)





























