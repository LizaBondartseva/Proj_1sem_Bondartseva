#Дано целое число N (N>0). С помощью операций деления нацело и взятия остатка от деления
#определить, имеется ли в записи числа N цифра «2». Если имеется, то вывести TRUE, если
#нет — вывести FALSE.
#Вариант №3
while True:
    try:
        a = int(input())
        if a<0:
            print('Ошибка ввода')
        else:
            break
    except:
        print('Ошибка ввода')

while a//10!=0:
    if a//10 == 2:
        print(True)
        break
    else:
        a = a//10
else:
    print(False)

