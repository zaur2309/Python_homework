# # Задача 12:
# # Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# # Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# # Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# # Помогите Кате отгадать задуманные Петей числа.
# # 4 4 -> 2 2
# # 5 6 -> 2 3
# # 9 20 -> 5 4
s = int(input("Введите сумму: "))
p = int(input("Введите произведение: "))
for i in range(1, 1001):
    z = s - i
    if i <= z and i * z == p:
        print(z, i)
