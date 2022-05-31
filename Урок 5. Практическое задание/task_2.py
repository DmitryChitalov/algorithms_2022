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


def hex_calc():
    dct = defaultdict(list)
    for i in range(1, 3):
        num = input(f'Введите {i}-ое число в шестнадцатиричном формате: ')
        dct[num] = list(num)
    hex_sum = hex(sum([int(i, 16) for i in dct]))[2:].upper()
    print(f'Сумма чисел: {list(hex_sum)}')
    hex_add = hex(reduce(lambda x, y: int(x, 16) * int(y, 16), dct))[2:].upper()
    print(f'Произведение чисел: {list(hex_add)}')


hex_calc()
