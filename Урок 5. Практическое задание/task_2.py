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


#  1)
def hexadecimal_interface():
    hex_one = input('Введите первое число: ')
    hex_two = input('Введите второе число: ')
    operator = input('Введите операцию: ')
    hex_dict = defaultdict(list)
    hex_dict[int(hex_one, 16)] = list(hex_one)
    hex_dict[int(hex_two, 16)] = list(hex_two)
    return hexadecimal_operations(hex_dict, operator)


def hexadecimal_operations(hex_dict, operator):
    if operator == '+':
        addition = 0
        for key in hex_dict.keys():
            addition += key
        return list(hex(addition)[2:].upper())
    multiplication = 1
    for key in hex_dict.keys():
        multiplication *= key
    return list(hex(multiplication)[2:].upper())


#  print(hexadecimal_interface())

#  2)
class Hexadecimal:
    def __init__(self, hex_num_str):
        self.hex_number = hex_num_str

    def __add__(self, other):
        return list(hex(int(self.hex_number, 16) + int(other.hex_number, 16))[2:].upper())

    def __mul__(self, other):
        return list(hex(int(self.hex_number, 16) * int(other.hex_number, 16))[2:].upper())


def hexadecimal_oop_interface():
    hex_one = Hexadecimal(input('Введите первое число: '))
    hex_two = Hexadecimal(input('Введите второе число: '))
    operator = input('Введите операцию: ')
    if operator == '+':
        return hex_one + hex_two
    return hex_one * hex_two


print(hexadecimal_oop_interface())
