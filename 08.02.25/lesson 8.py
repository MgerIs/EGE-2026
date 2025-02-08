import random
var_list = random.sample(range(1,1000),100)
number = var_list[0]
for i in range(0,len(var_list)):
    if var_list[i] > number:
        number = var_list[i]

maxx_2 = 0
for i in range(len(var_list)):
    if var_list[i] != number and var_list[i]>maxx_2:
        maxx_2 = var_list[i]
print(number, maxx_2)
print(sorted(var_list)[::-1])




maxx = [0,0]
for i in range(len(var_list)):
    if maxx[0] < var_list[i]:
        maxx[1] = maxx[0]
        maxx[0] = var_list[i]
    elif maxx[1]<var_list[i]:
        maxx[1] = var_list[i]
print(maxx)










from random import *
len_n = 10
nums = [randint(1,100)for i in range(100)]
print(nums)
ans = 0
for i in range(len_n -1):
    if nums[i] == nums[i+1]:
        count = 1
        for j in range(i, len_n - 1):
            if nums[j] == nums[j+1]:
                count += 1
            else:
                break
        ans = max(ans, count)
print(ans)