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
from collections import defaultdict


def hex_sum():
    return list(hex(int(''.join(my_dict[1]), 16) + int(''.join(my_dict[2]), 16)).upper())[2:]


def hex_mul():
    return list(hex(int(''.join(my_dict[1]), 16) * int(''.join(my_dict[2]), 16)).upper())[2:]


my_dict = defaultdict(list)
my_dict[1] = list(input('--> '))
my_dict[2] = list(input('--> '))
print(f'Сумма чисел: {hex_sum()}, \n'
      f'Произведение чисел: {hex_mul()}')