# def f(x, P, Q, A):
#     return ((x in A) <= (x in P)) or ((not (x in Q)) <= (not (x in A)))
#
# P = [x for x in range(2, 21, 2)]
# Q = [x for x in range(3, 31, 3)]
# A = set(x for x in range(40))
#
# for x in range(1,100):
#     if not f(x, P, Q, A):
#      A.remove(x)
# print(len(A))

P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

A_max = P.intersection(Q)


print(len(A_max))
