#Вариант №3
#Из матрицы сформировать массив из положительных четных элементов, найти их сумму и среднее арифметическое.

from random import randint

m, n, y, z, = [int(input(i)) for i in ('Количество строк = ', 'Количество столбцов = ', 'От = ', 'До = ')]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матица: ')
for i in matrix:
    print(*i)
h = []
for i in matrix:
   for o in i:
       if o > 0 and o % 2 == 0:
           h.append(o)
print(h, '\n' + str(sum(h)), '\n' + str(sum(h) / len(h)))


