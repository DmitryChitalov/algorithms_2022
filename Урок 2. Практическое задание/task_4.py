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
from sys import getrecursionlimit, setrecursionlimit


def recursive_number_series_sum(count, sum_=1.0):  # Решение через рекурсию.
    if count <= 1:
        return sum_
    sum_ += recursive_number_series_sum(count - 1, -sum_ / 2)
    return sum_


def lh_number_series_sum(num):  # ДЛЯ ПРОВЕРКИ !!! Решение через цикл
    return sum([1 / (2 ** n) * (1, -1)[n % 2 or 0] for n in range(num)])


print(f'{       lh_number_series_sum(3)=}')
print(f'{recursive_number_series_sum(3)=}')
print(f'{       lh_number_series_sum(20)=}')
print(f'{recursive_number_series_sum(20)=}')
# c num = 999 ошибка: RecursionError: maximum recursion depth exceeded in comparison
print(f'{getrecursionlimit()=}')
setrecursionlimit(2002)
print(f'{getrecursionlimit()=}')
print(f'{       lh_number_series_sum(2000)=}')
print(f'{recursive_number_series_sum(2000)=}')


