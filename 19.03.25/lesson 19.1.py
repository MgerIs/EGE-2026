column = int(input("введите колво столбцов"))
line = int(input("введите колво строк"))
matrix = []
for i in range(line):
    l1 = list(map(int,input(f'введите {column} чисел:').split()))
    matrix.append(l1)
for r in range(len(matrix)):
    for g in range(len(matrix)):
        print(matrix[r][g], end= " ")
    print()





