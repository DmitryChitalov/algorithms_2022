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

def recursive_series_of_numbers(n: int, num: float = 1.0) -> float:
    """
    :param n: elements number to sum
    :param num: series start number (float or int), default = 1.0.
    :return: return sum of numbers in series
    """
    return num if n <= 1 else num + recursive_series_of_numbers(n-1, num=num / -2)


print(recursive_series_of_numbers(1))
print(recursive_series_of_numbers(2))
print(recursive_series_of_numbers(3))
print(recursive_series_of_numbers(4))