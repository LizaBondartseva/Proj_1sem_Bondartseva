#Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.
#Вариант №3
while True:
    try:
        a = float(input('Введте цену 1 кг конфет: '))
        if a<=0:
            print('Ошибка ввода')
        else:
            break
    except:
        print('Ошибка ввода введите число')

k = int(1)
while k<=10:
    print('Цена', k, 'конфет:', a*k, 'рублей')
    k += 1