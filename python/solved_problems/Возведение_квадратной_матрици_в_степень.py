#  Формат ввода матрицы
# 5- матрица квадратная
# 1 2 1 1 2
# 3 3 3 3 3
# 1 2 1 1 2
# 3 3 3 3 3
# 1 2 1 1 2
# 3 - степень
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix_2 = [[0] * n for i in range(n)]
f = int(input())
for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_2[i][j] += matrix[i][k] * matrix[k][j]
                
def res(n, matrix, matrix_2):
    matrix_3 = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_3[i][j] += matrix[i][k] * matrix_2[k][j]
    matrix_2 = matrix_3
    return matrix_3, matrix_2 

if f > 2:
    for _ in range(f-2):
        matrix_3, matrix_2 = res(n, matrix, matrix_2)
    for i in matrix_3:
        print(*i)     
else:
    for i in matrix_2:
        print(*i)