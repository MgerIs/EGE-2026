# Решение задач со списками 2.0
from timeit import timeit
def f1(matrix):
    for i in matrix:
        arr = str(i)
        l1 = arr.replace(",","" )
        l1 = l1.replace("[", "")
        l1 = l1.replace("]", "")
    #print(l1)

def f2(matrix):
    for i in range(len(matrix)):
        for g in range(len(matrix[i])):
            g=g
            #print(matrix[i][g], end= " ")
        #print()

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(timeit("f1(matrix)", globals = globals(), number= 10))
print(timeit("f2(matrix)", globals = globals(), number= 10))
