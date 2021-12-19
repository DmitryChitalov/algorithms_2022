"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""


def sum_number(num=1.0, count=None):
    if count is None:
        count = input("Введите число: \n")
        if not count.isdigit():
            print("Вы ввели не число!")
            return sum_number()
        count = int(count)
    if count <= 0:
        return 0
    res = num / -2
    count -= 1
    return num + sum_number(res, count)

print(sum_number())
