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


def reducer_func(el_prev, el):
    return el_prev + el


dct = defaultdict(list)
# dct[1] = list('A2')
# dct[2] = list('C4F')

dct[1] = list(input(f'Введите число 1: '))
dct[2] = list(input(f'Введите число 2: '))

val1 = reduce(reducer_func, dct[1])
val2 = reduce(reducer_func, dct[2])

sm = list(hex(int(val1, 16) + int(val2, 16)).replace('0x', '').upper())
ml = list(hex(int(val1, 16) * int(val2, 16)).replace('0x', '').upper())
print(f'Сумма чисел из примера: {sm}')
print(f'Произведение чисел: {ml}')
