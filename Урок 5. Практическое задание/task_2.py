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

from functools import reduce
from collections import defaultdict


def sum_hex_number(num1: list, num2: list) -> list:
    dd = defaultdict(list, val1=num1, val2=num2)
    return reduce(
        lambda x, y: list(hex(int(''.join(x), 16) + int(''.join(y), 16)).replace('0x', '').upper()),
        dd.values()
    )


def mul_hex_number(num1: list, num2: list) -> list:
    dd = defaultdict(list, val1=num1, val2=num2)
    return reduce(
        lambda x, y: list(hex(int(''.join(x), 16) * int(''.join(y), 16)).replace('0x', '').upper()),
        dd.values()
    )


class HexNumber:
    # dh = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
    #       13: 'D', 14: 'E', 15: 'F'}
    # hd = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
    #       'D': 13, 'E': 14, 'F': 15}
    #
    # def __init__(self, hex_num: list):
    #     for char in hex_num:
    #         if not self.hd.get(char):  # is None
    #             raise TypeError(f"{hex_num} - это не шестнадцатеричное число")
    #     self.hex_num = hex_num
    #
    # def from_dec_to_hex(self, num: int) -> list:
    #     result = []
    #     while num > 16:
    #         result.insert(0, self.dh[num % 16])
    #         num //= 16
    #     result.insert(0, self.dh[num])
    #     return result
    #
    # def from_hex_to_dec(self, num: list) -> int:
    #     result = 0
    #     degree = len(num) - 1
    #     for i, n in enumerate(num):
    #         result += self.hd[n] * 16 ** (degree - i)
    #     return result
    #
    # def __add__(self, other):
    #     return self.from_dec_to_hex(self.from_hex_to_dec(self.hex_num) + self.from_hex_to_dec(other.hex_num))
    #
    # def __mul__(self, other):
    #     return self.from_dec_to_hex(self.from_hex_to_dec(self.hex_num) * self.from_hex_to_dec(other.hex_num))

    def __init__(self, hex_num: list):
        self.hex_num = hex_num

    def __add__(self, other):
        return list(hex(int(''.join(self.hex_num), 16) + int(''.join(other.hex_num), 16)).replace('0x', '').upper())

    def __mul__(self, other):
        return list(hex(int(''.join(self.hex_num), 16) * int(''.join(other.hex_num), 16)).replace('0x', '').upper())


if __name__ == '__main__':
    num1 = list(input('Введите первое шестнадцатеричное число: ').upper())
    num2 = list(input('Введите второе шестнадцатеричное число: ').upper())

    # Вариант 1. Решение через collections
    print('Сумма:', sum_hex_number(num1, num2))
    print('Произведение:', mul_hex_number(num1, num2))

    # Вариант 2. Решение через класс
    # Закомментировано решение через встроенные функции hex(), int(, 16)
    hn1 = HexNumber(num1)
    hn2 = HexNumber(num2)
    print('Сумма:', hn1 + hn2)
    print('Произведение:', hn1 * hn2)
