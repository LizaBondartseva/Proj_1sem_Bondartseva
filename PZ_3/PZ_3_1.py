#Дано целое число A. Проверить истинность высказывания: «Число A является четным».
while True:
    try:
        a = int(input('Введите число:'))
        break
    except ValueError:
        print('Ошибка')
if a % 2 == 0:
    print('Четное')
else:
    print('Нечетное')