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
Попытайтесь решить это задание в двух вариантах.
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""

# __________________________________________________________1___________________________________________________________

from collections import defaultdict
from functools import reduce


def input_num():
    ddict_num = defaultdict(list)
    raw_num = input('Введите шестнадцатиричное число: ')
    dec_num = int(raw_num, 16)
    for el in raw_num:
        ddict_num[dec_num].append(el)
    return ddict_num


def sum_hex(first_num, second_num):
    ddict_result = defaultdict(list)
    dec_sum_result = first_num.popitem()[0] + second_num.popitem()[0]
    hex_sum_result = hex(dec_sum_result)[2:]
    for el in hex_sum_result:
        ddict_result[dec_sum_result].append(el)
    return f'Сумма чисел из примера: {ddict_result[dec_sum_result]}'


first = input_num()
second = input_num()
print(sum_hex(first, second))
