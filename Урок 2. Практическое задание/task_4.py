"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

def sum_func(num, s = 0, a = 1):
    if num > 0:
        s += a
        a = a * (-0.5) 
        return sum_func(num - 1, s, a)
    else:
        return f"Сумма элементов - {s}"


print(sum_func(3))
