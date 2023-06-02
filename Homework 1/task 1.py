# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
number = input("Введите число: ")
if int(number) < 100 or int(number) > 999 or number.isdigit() == False:
    print("error")
else:
    print(int(number) // 100 + (int(number) // 10) % 10 + int(number) % 10)
