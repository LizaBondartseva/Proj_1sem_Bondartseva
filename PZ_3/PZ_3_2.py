#Размер скидки на продукты определен следующим образом: при покупке до 500 р. скидка
#составит 2%; при покупке от 500 р. до 1000 р. скидка составит 3%; при покупке от 1000 р.
#до 1500 р. скидка составит 4%; при покупке от 1500 р. до 2000 р. скидка составит 5%.
#Составить программу определяющую размер скидки в зависимости от потраченной суммы.
while True:
    try:
        a = int(input('Введите стоимость продукта: '))
        if 0 < a < 2000:
            break
        else:
            print('Ошибка')
    except:
        print('Ошибка')

k = int()
if a < 500:
    k = 2
elif a < 1000:
    k = 3
elif a < 1500:
    k = 4
elif a < 2000:
    k = 5
print('Скидка на товар стоимость' , a, 'рублей будет', k,'%.')
