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
from math import prod

def hex_sum(dct):
    return list(hex(sum([int(''.join(i), 16) for i in dct.values()]))[2:].upper())

def hex_mult(dct):
    return list(hex(prod([int(''.join(i), 16) for i in dct.values()]))[2:].upper())

class HexNumber:
    
    __slots__ = ('_hex_number')

    def __init__(self, hex_humber: str):
        self._hex_number = list(hex_humber)

    @property
    def hex_number(self):
        return ''.join(self._hex_number)

    def __add__(self, hex_number):
        if isinstance(hex_number, HexNumber):
            return list(hex(sum([int(self.hex_number, 16), int(hex_number.hex_number, 16)]))[2:].upper())

    def __mul__(self, hex_number):
        if isinstance(hex_number, HexNumber):
            return list(hex(prod([int(self.hex_number, 16), int(hex_number.hex_number, 16)]))[2:].upper())




if __name__ == "__main__":

    items = defaultdict(list)
    items['first_item'] = list(input("Введите первое шестнадцатеричное число: "))
    items['second_item'] = list(input("Введите первое шестнадцатеричное число: "))
    print(f"Сумма чисел равна: {hex_sum(items)}")
    print(f"Произведение чисел равно: {hex_mult(items)}")

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    first = HexNumber(list(input("Введите первое шестнадцатеричное число: ")))
    second = HexNumber(list(input("Введите первое шестнадцатеричное число: ")))
    print(f"Сумма чисел равна: {first + second}")
    print(f"Произведение чисел равно: {first * second}")