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

import collections


class HexNumber:
    def __init__(self, a):
        if type(a) != str:
            raise ValueError('Недопустимый тип: на вход должна быть строка')
        for i in a:
            if i not in '1234567890ABCDEF':
                raise ValueError('Недопустимое значение: невозможно перевести в шестнадцатиричное число')
        self.val = int(a, 16)

    def __add__(self, other):
        return hex(self.val + other.val)[2:].upper()

    def __mul__(self, other):
        return hex(self.val * other.val)[2:].upper()


def from_hex(lst):
    return sum([number[lst[i]] * 16 ** (-i - 1) for i in range(-1, -len(lst) - 1, -1)])


def to_hex(n):
    if n // 16 == 0:
        return number_reverse[n]
    else:
        return to_hex(n // 16) + number_reverse[n % 16]


def hex_sum(a, b):
    return list(to_hex(from_hex(a) + from_hex(b)))


def hex_mult(a, b):
    return list(to_hex(from_hex(a) * from_hex(b)))


a, b = input("Введите первое число"), input("Введите второе число")
x, y = HexNumber(a), HexNumber(b)
print(x + y)
print(x * y)

number = collections.defaultdict(int, zip(list('0123456789ABCDEF'), range(16)))
number_reverse = collections.defaultdict(int, zip(range(16), list('0123456789ABCDEF')))
c = list(a)
d = list(b)
print(hex_sum(c, d))
print(hex_mult(c, d))
