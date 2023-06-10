import random


# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

min_1 = int(input('Ведите мин: '))
max_1 = int(input('Введите макс: '))
size = int(input('Введите длину массива: '))
arr = [random.randint(-20, 20) for i in range(size)]
arr_1 = []
for i in range(len(arr)):
    if min_1 <= arr[i] <= max_1:
        arr_1.append(i)
print(arr)
print(arr_1)
