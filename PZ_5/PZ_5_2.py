#Практическая №5
#Вариант №3
#Описать функцию TrianglePS(параметры), вычисляющую по стороне a равностороннего
#треугольника его периметр P = 3*a и площадь S = a2 √3/4. С помощью этой функции найти
#периметры и площади трех равносторонних треугольников с данными сторонами.

from math import *  # Импорт функций из библиотеки math


# Функция вычисления периметра и площади
def triugolnik(a):
    P = 3 * a
    S = pow(a, 2)
    sqrt(3) / 4
    print(P)
    print(round(S, 2))


t = 3
while t != 0:
    a = int(input('Введите сторону треугольника: '))
    triugolnik(a)
    t -= 1