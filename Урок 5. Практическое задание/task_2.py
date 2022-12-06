"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""

import collections
import functools


def calc():
    numbers = collections.defaultdict(list)

    for i in range(2):
        hexadecimal_number = input(f"Введите {i + 1}-е натуральное шестнадцатиричное число: ")
        numbers[f"{i + 1}-{hexadecimal_number}"] = list(hexadecimal_number)
    print(numbers)

    sum_of_numbers = sum([int(''.join(i), 16) for i in numbers.values()])
    print(sum_of_numbers)

    print("Сумма: ", list('%X' % sum_of_numbers))
    multiplication_of_numbers = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in numbers.values()])
    print("Произведение: ", list('%X' % multiplication_of_numbers))


calc()
