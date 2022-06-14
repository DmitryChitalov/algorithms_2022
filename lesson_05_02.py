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


def hex_num():
    numbers = defaultdict(int)
    numbers['operand_1'] = list(input('Operand 1: '))
    numbers['operand_2'] = list(input('Operand 2: '))
    numbers['num_mul'] = list(hex(int("".join(numbers['operand_1']), 16) * int("".join(numbers['operand_2']), 16)))[2:]
    numbers['num_sum'] = list(hex(int("".join(numbers['operand_1']), 16) + int("".join(numbers['operand_2']), 16)))[2:]
    print(f"Сумма {numbers['operand_1']} и {numbers['operand_2']} равна: {numbers['num_sum']}")
    print(f"Произведение {numbers['operand_1']} и {numbers['operand_2']} равно: {numbers['num_mul']}")


hex_num()
"""
Operand 1: 2FC
Operand 2: 2AB
Сумма ['2', 'F', 'C'] и ['2', 'A', 'B'] равна: ['5', 'a', '7']
Произведение ['2', 'F', 'C'] и ['2', 'A', 'B'] равно: ['7', 'f', '6', '5', '4']
"""


class HexNumbers:

    def __init__(self, operand):
        self.operand = list(operand)

    def __add__(self, other):
        return list(hex(int("".join(self.operand), 16) + int("".join(other.operand), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int("".join(self.operand), 16) * int("".join(other.operand), 16)))[2:]


a = HexNumbers('2FC')
b = HexNumbers('2AB')
print(a + b)
print(a * b)
