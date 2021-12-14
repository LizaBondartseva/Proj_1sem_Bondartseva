#Практическая работа №7
#Вариант №3
#Дана строка содержащая цифры и строчные латинские буквы. Если буквы в строке упорядочены по алфавиту, то вывести 0;
# в противном случае вывести номер первого символа строки, нарущающего алфавитный порядок.

def f(a):
    b = list(filter(lambda x: not x.isdigit(), sorted(list(a))))
    d = list(filter(lambda x: not x.isdigit(), list(a)))
    res = 0
    for i in range(len(b)):
        if b[i] != d[i]: res = d[i]; break
    return res
print(f('a4bc5d'))
print(f('7ab6dct'))
print(f('abcedf'))