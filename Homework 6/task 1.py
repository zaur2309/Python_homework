# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

arr = []
a_1 = int(input('Введите первый элемент массива: '))
d = int(input('Введите разность: '))
n = int(input('Введите кол-во элементов: '))
for i in range(1, n + 1):
    arr.append(a_1 + (i - 1) * d)
print(arr)