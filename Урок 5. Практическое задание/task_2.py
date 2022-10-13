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
import copy
from collections import defaultdict
from functools import reduce


class HexResult:
    def __init__(self, my_str):
        self.my_str = list(my_str)

    def __add__(self, other):
        my_list = defaultdict(list)
        my_list[1] = copy.copy(self.my_str)
        my_list[2] = copy.copy(other.my_str)
        sum_m = sum([int(''.join(el), 16) for el in my_list.values()])
        sum_m = list(format(sum_m, 'X'))
        return sum_m

    def __mul__(self, other):
        my_list = defaultdict(list)
        my_list[1] = copy.copy(self.my_str)
        my_list[2] = copy.copy(other.my_str)
        sum_m = reduce(lambda a, b: a * b, [int(''.join(el), 16) for el in my_list.values()])
        return list(format(sum_m, 'X'))


a = HexResult('A2')
b = HexResult('C4F')

print(f'Сумма чисел равна: {a+b}')
print(f'произведение - {a*b}')


