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

# 1)

from collections import defaultdict

def hex_num():
    hex_1 = input('Первое число: ')
    hex_2 = input('Второе число: ')
    operator = input('Операция + или *: ')
    hex_dict = defaultdict(list)
    hex_dict[int(hex_1, 16)] = list(hex_1)
    hex_dict[int(hex_2, 16)] = list(hex_2)
    return hex_oper(hex_dict, operator)

def hex_oper(hex_dict, operator):
    if operator == '+':
        sum = 0
        for key in hex_dict.keys():
            sum += key
        return list(hex(sum)[2:].upper())
    mult = 1
    for key in hex_dict.keys():
        mult *= key
    return list(hex(mult)[2:].upper())

print(hex_num())

# 2)

class HexClass:
    def __init__(self, num_1):
        self.num_1 = num_1

    def __add__(self, other):
        sum_nums = int(''.join(self.num_1), 16) + int(''.join(other.num_1), 16)
        return list(f'{sum_nums:X}')

    def __mul__(self, other):
        mult_nums = int(''.join(self.num_1), 16) * int(''.join(other.num_1), 16)
        return list(f'{mult_nums:X}')


hex_1 = HexClass('A2')
hex_2 = HexClass('C4F')

print(f'Сумма чисел из примера: {hex_1 + hex_2}\n'
      f'произведение: {hex_1 * hex_2}')