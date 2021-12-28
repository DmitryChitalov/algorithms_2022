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
Попытайтесь решить это задание в двух вариантах.
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


# 1
def sum_hexadecimal(op_1: str, op_2: str):
    n_1 = list(op_1)
    n_2 = list(op_2)
    numbers = defaultdict(list, operand_1=n_1, operand_2=n_2)
    sum_ = sum([int(''.join(i), 16) for i in numbers.values()])
    print('Sum:', list('%X' % sum_))
    mul_ = reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in numbers.values()])
    print('Product of multipliers:', list('%X' % mul_))
    return numbers.values()


# 2
class Hex:
    def __init__(self, number: str):
        self.number = list(number)

    def __add__(self, other):
        if isinstance(other, Hex):
            return Hex('%X' % (int(''.join(self.number), 16) + int(''.join(other.number), 16)))
        elif isinstance(other, str):
            return Hex('%X' % (int(''.join(self.number), 16) + int(''.join(other), 16)))

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Hex):
            return Hex('%X' % (int(''.join(self.number), 16) * int(''.join(other.number), 16)))
        elif isinstance(other, str):
            return Hex('%X' % (int(''.join(self.number), 16) * int(other, 16)))

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return f'{self.number}'


if __name__ == '__main__':
    print(sum_hexadecimal('A2', 'C4F'))
    print(Hex('A2') + Hex('C4F'))
    print(Hex('C4F') + 'A2')
    print(Hex('A2') * Hex('C4F'))
    print(Hex('C4F') * 'A2')
