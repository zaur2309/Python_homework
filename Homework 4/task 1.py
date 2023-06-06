import random


# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


size_1 = int(input('Введите длину первого массива: '))
size_2 = int(input('Введите длину второго массива: '))
array_1 = [random.randint(0, 20) for i in range(size_1)]
array_2 = [random.randint(0, 20) for j in range(size_2)]
print('Первый массив: ', end='')
print(array_1)
print('Второй массив: ', end='')
print(array_2)
lst = []
for i in range(len(array_1)):
    for j in range(len(array_2)):
        if array_1[i] == array_2[j] and array_1[i] not in lst:
            lst.append(array_1[i])

for i in range(len(lst)):
    for j in range(i + 1, len(lst) - 1):
        if lst[i] >= lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print(lst)
