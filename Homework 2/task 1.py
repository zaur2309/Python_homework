import random


# # Задача 10: На столе лежат n монеток.
# # Некоторые из них лежат вверх решкой, а некоторые – гербом.
# # Определите минимальное число монеток, которые нужно перевернуть,
# # чтобы все монетки были повернуты вверх одной и той же стороной.
# # Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2
n = int(input("Введите кол-во монет: "))
coin_1 = 1 # орел
coin_2 = 0 # решка
count_n = 0 # счетчик для решки
count_m = 0 # счетчик для орла
print(n, '-> ', end='')
for i in range(n):
    coin = random.randint(0, 1)# сама монета
    print(coin, end=' ')
    if coin == coin_2:
        count_n += 1
    elif coin == coin_1:
        count_m += 1
print()
print(f'кол-во решек - {count_n}, кол-во орлов - {count_m}')
if count_n <= count_m:
    print("минимальное количество монет, которые нужно перевернуть",  count_n)
else:
    print("минимальное количество монет, которые нужно перевернуть",  count_m)
