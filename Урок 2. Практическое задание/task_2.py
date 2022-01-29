"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
from functools import reduce


def even_odd_nums(number: int) -> tuple:
    """
    Recursive function returns tuple with odd and even numbers
    :param number: int
    :return: tuple (odd, even)
    """
    if number // 10 == 0:
        return number % 10 % 2,
    else:
        recursive_num = even_odd_nums(number // 10)[0]
        return  number % 10 % 2 + recursive_num, len(str(number)) - recursive_num - number % 10 % 2


def even_odd_nums_ternary(number: int) -> tuple:
    """
    Version 2 of recursion function
    This f() is less readable
    :param number: int
    :return: tuple (odd, even)
    """
    return number % 10 % 2 if number // 10 == 0 else \
           number % 10 % 2 + even_odd_nums(number // 10)[0], \
           len(str(number)) - even_odd_nums(number // 10)[0] - number % 10 % 2

print(even_odd_nums(123))
print(even_odd_nums(34560))
print(even_odd_nums_ternary(123))
print(even_odd_nums_ternary(34560))


