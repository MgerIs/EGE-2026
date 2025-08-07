# num = input()
# num1 = num.split()
# cnt = 0
# nums2 = 0
# cnt2 = 0
# nums3 = 0
# for i in num1:
#     cnt += int(i)
# print(cnt)
# for i in num1:
#     nums2 = list(map(int, num1))
#     cnt = nums2[0] + nums2[1] + nums2[2]
# print(cnt)
nums = input()
print(*(map(lambda x:int(x)**2 ,nums.split())))