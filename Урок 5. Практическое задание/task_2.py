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


# решение через ООП
class HexadecClass:
    def __init__(self, val: str):
        self.val = val

    def __add__(self, other):
        return str(hex(int(self.val, 16) + int(other.val, 16)))[2::].upper()

    def __mul__(self, other):
        return str(hex(int(self.val, 16) * int(other.val, 16)))[2::].upper()


a = HexadecClass('A2')  # a = HexadecClass(input('Введите первое число: '))
b = HexadecClass('C4F')  # b = HexadecClass(input('Введите второе число: '))
# print(a + b)
# print(a * b)


# решение через collections

hex_nums = defaultdict(str)
for i in range(2):
    hex_nums[f'{i}'] = int(input(f'Введите {i + 1}-е число: '), 16)

print(hex_nums)
print(hex(reduce(lambda a, b: a + b, hex_nums.values())))
print(hex(reduce(lambda a, b: a * b, hex_nums.values())))
