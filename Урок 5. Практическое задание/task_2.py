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

"""
1
"""
from collections import defaultdict


def hex_numbers(hex_1, hex_2, operation):
    dicthex = defaultdict(list)
    dicthex[int(hex_1, 16)] = list(hex_1)
    dicthex[int(hex_2, 16)] = list(hex_2)
    return oper(dicthex, operation)


def oper(hex_dict, operator):
    if operator == '+':
        summa = 0
        for key in hex_dict.keys():
            summa += key
        return list(hex(summa)[2:].upper())
    multiply = 1
    for key in hex_dict.keys():
        multiply *= key
    return list(hex(multiply)[2:].upper())

hex_1 = input('Первое 16ричное число')
hex_2 = input('Первое 16ричное число')
operation = input("Выберите операцию")
print(hex_numbers(hex_1, hex_2, operation))

"""
2
"""


class HexClass:
    def __init__(self, num):
        self.num = num


    def __add__(self, other):
        summa_nums = int(''.join(self.num), 16) + int(''.join(other.num), 16)
        return list(hex(summa_nums)[2:].upper())


    def __mul__(self, other):
        multiply_nums = int(''.join(self.num), 16) * int(''.join(other.num), 16)
        return list(hex(multiply_nums)[2:].upper())


class_hex_1 = HexClass(hex_1)
class_hex_2 = HexClass(hex_2)

print(class_hex_2 + class_hex_1)
print(class_hex_2 * class_hex_1)