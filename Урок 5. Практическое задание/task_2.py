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

import re
from collections import namedtuple


# Collections ######################################################

def hex_add(hex_nums):
    first = ''.join(hex_nums.first)
    second = ''.join(hex_nums.second)
    return list(hex(int(first, 16) + int(second, 16))[2:].upper())


def hex_mul(hex_nums):
    first = ''.join(hex_nums.first)
    second = ''.join(hex_nums.second)
    return list(hex(int(first, 16) * int(second, 16))[2:].upper())


def calc_collections():
    hex_1 = input('Введите первое шестнадцатеричное число: ')
    hex_2 = input('Введите второе шестнадцатеричное число: ')

    hexes = namedtuple('hex_numbers', 'first second')
    hex_numbers = hexes(list(hex_1), list(hex_2))

    print(f'Сумма чисел: {hex_add(hex_numbers)}')
    print(f'Произведение чисел: {hex_mul(hex_numbers)}')


# OOP ##############################################################

class HexError(Exception):
    def __init__(self):
        self.string = None
        self.message = None

    def __str__(self):
        return f'Ошибка: "{self.string}" -> {self.message}'


class NotHexFormat(HexError):
    def __init__(self, string, message='Неверный формат строки'):
        self.string = string
        self.message = message


class NotHexType(HexError):
    def __init__(self, string, message='Не является типом HexNum'):
        self.string = string
        self.message = message


class HexNum:
    def __init__(self, string):
        self._check_format(string)
        self.digits = tuple(string.upper())

    @staticmethod
    def _check_format(string):
        pattern = r'^[1-9a-fA-F][0-9a-fA-F]*$'
        if not re.fullmatch(pattern, string):
            raise NotHexFormat(string)

    @staticmethod
    def _is_hex(obj):
        if type(obj) != HexNum:
            raise NotHexType(obj)

    def get_string(self):
        return str(''.join(self.digits))

    def __str__(self):
        return str(list(self.digits))

    def __add__(self, other):
        self._is_hex(other)
        first_operand = self.get_string()
        second_operand = other.get_string()
        return HexNum(hex(int(first_operand, 16) + int(second_operand, 16))[2:])

    def __mul__(self, other):
        self._is_hex(other)
        first_operand = self.get_string()
        second_operand = other.get_string()
        return HexNum(hex(int(first_operand, 16) * int(second_operand, 16))[2:])


def calc_oop():
    try:
        hex_1 = HexNum(input('Введите первое шестнадцатеричное число: '))
        hex_2 = HexNum(input('Введите второе шестнадцатеричное число: '))

        print(f'Сумма чисел: {hex_1 + hex_2}')
        print(f'Произведение чисел: {hex_1 + hex_2}')

    except HexError as e:
        print(e)


if __name__ == '__main__':

    calc_collections()
    calc_oop()
