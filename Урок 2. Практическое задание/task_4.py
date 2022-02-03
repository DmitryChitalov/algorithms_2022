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

n = int(input('Введите количество элементов: '))


def fun(h):
    k = h - 1
    if h == 0:
        return []
    return fun(k) + [(-1) ** (k % 2) / (1 << k)]


print(fun(n))
print(sum(fun(n)))
