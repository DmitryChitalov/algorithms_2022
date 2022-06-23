from collections import defaultdict
from functools import reduce

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


# функциональная реализация для defaultdict
def hex_num():
    """Запрос числа от пользователя"""
    num = input('Введите шестнадцптиричное число: ')
    return list(num.upper())


def hex_sum(data):
    """Сложение"""
    return list(
        hex(reduce(
            lambda x, y: x + y, [int(''.join(i), 16) for i in data.values()]
                    )
            ).upper()
    )[2:]


def hex_multi(data):
    """Умножение"""
    return list(
        hex(reduce(
            lambda x, y: x * y, [int(''.join(i), 16) for i in data.values()]
                    )
            ).upper()
        )[2:]


# Решение через класс
class HexNumber:
    def __init__(self, num):
        self.num = int(num, 16)

    def __mul__(self, other):
        if isinstance(other, HexNumber):
            return list(hex(self.num * other.num).upper()[2:])

    def __add__(self, other):
        if isinstance(other, HexNumber):
            return list(hex(self.num + other.num).upper()[2:])


if __name__ == '__main__':
    def_data = defaultdict(list)
    def_data['1'] = hex_num()
    def_data['2'] = hex_num()
    print(def_data)
    print(hex_sum(def_data))
    print(hex_multi(def_data))

    num_1 = HexNumber('a2')
    num_2 = HexNumber('c4f')

    print(num_1 + num_2)
    print(num_1 * num_2)
