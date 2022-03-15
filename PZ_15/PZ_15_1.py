# Вариант №3
# В квадратной матрице элементы на главной диагонали увеличить в 2 раза

from random import randint
import numpy as np

m, n, y, z = [int(input(i)) for i in ('Количество строк = ', 'Количество столбцов = ', 'От = ', 'До = ')]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матица: ')
for i in matrix:
    print(*i)
h = np.diagonal(matrix)
for x in range(0, len(matrix)):
    matrix[x][x] = h[x] * 2
print("Полученная матрица: ")
for i in matrix:
    print(*i)
