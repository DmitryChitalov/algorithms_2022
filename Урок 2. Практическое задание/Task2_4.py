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

from functools import reduce


def even_odd_collector(arrays, x):
    """
    :param arrays: Массив вида [0: [нечетные числа], 1: [четные числа]]
    :param x: Число
    :return: Массив вида [0: [нечетные числа], 1: [четные числа]]
    """
    x = int(x)
    arrays[x % 2].append(x)
    return arrays


n = input('Введите число: ')
(odd, even) = reduce(even_odd_collector, n, [[], []])
print('{} нечетных цифр {} и {} четных цифр {}'.format(len(even), even, len(odd), odd))