#Список размера N.
#Найти номер его первого локального минимума(локальный минимум - это элемент, который меньше любого из своих соседей).
#Вариант №3

N = int(input("Введите длину списка: "))
A = []
for i in range(N):
    A.append(int(input("Введите число " + str(i + 1) + ": ")))

for i in range(len(A) - 1):
    if A[i] <A[i +1]:
        print("Первый локальный минимум под номером " + str(i + 1))
        break
    elif A[len(A)-1] < A[len(A)-2]:
        print("Первый локальный минимум под номером ", len(A))
        break
    elif A[i] < A[i + 1] and A[i] < A[i - 1]:
        print("Первый локальный минимум под номером " + str(i + 1))
        break