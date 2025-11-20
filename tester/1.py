# ans = []
# def convert(num, sys):
#      res = ''
#      while num != 0:
#          res += str(num % sys)
#          num //= sys
#      return res[::-1]
# #
# for N in range(1,100000):
#     R = convert(N,3)
#     if sum(map(int,R))%3==0:
#         R = R + "212"
#     else:
#         R = R + convert(sum(map(int,R))*2,3)
#     R=int(R,3)
#     if R>490:
#         ans.append(R)
# print(min(ans))

# from string import printable as alph
# def convert2(num, sys):
#     res = ''
#     while num != 0:
#         res += alph[num % sys]
#         num //= sys
#     return res[::-1]
# x=283**382+9**15+2**3
# print(abs(convert2(x,14).count("b")-convert2(x,14).count("c")))


