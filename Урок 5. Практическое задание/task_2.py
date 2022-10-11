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

from collections import defaultdict
from functools import reduce


def convert_input_to_array():
    hex_num1 = input('Введите первое число: ')
    hex_num2 = input('Введите первое число: ')
    num_array = defaultdict(list)
    num_array[1] = list(hex_num1)
    num_array[2] = list(hex_num2)
    return num_array


def sum_hex_numbers(num_array):
    # ф-ю сложения решил без reduce реализовать, а ф-ю умножения через reduce
    res = sum([int(''.join(el), 16) for el in num_array.values()])
    res = list(format(res, 'X'))
    # res = list(format(sum([int(''.join(el), 16) for el in num_array.values()]), 'X'))
    # можно еще таким вариантом сложить:
    # res = list(f'{sum([int("".join(i), 16) for i in num_array.values()]):X}')
    return res


def mult_hex_numbers(num_array):
    res = reduce(lambda a, b: a * b, [int(''.join(el), 16) for el in num_array.values()])
    # сделал по разному, чтобы спросить: как правильнее, в return готовый результат выложить как в предыдущей функции
    # или выражение (для сокращения длинной строки)?
    return list(format(res, 'X'))


my_array = convert_input_to_array()
print('Сумма = ', sum_hex_numbers(my_array))
print('Произведение = ', mult_hex_numbers(my_array))
