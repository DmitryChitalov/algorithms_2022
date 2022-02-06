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
from functools import reduce


def hex_sum(num1, num2):
    return list(hex(int(num1, 16) + int(num2, 16))[2:])


def hex_mul(num1, num2):
    return list(hex(int(num1, 16) * int(num2, 16))[2:])


nums = defaultdict(list)

n = input('Введите первое число: ')
nums[n].append(list(n))
n = input('Введите второе число: ')
nums[n].append(list(n))

print(f'Сумма: {reduce(hex_sum, nums)}')
print(f'Произведение: {reduce(hex_mul, nums)}')


class HexNumber(str):
    def __add__(self, other):
        return list(hex(int(self, 16) + int(other, 16))[2:])

    def __mul__(self, other):
        return list(hex(int(self, 16) * int(other, 16))[2:])


hex1 = HexNumber(nums.popitem()[0])
hex2 = HexNumber(nums.popitem()[0])
print(hex1 + hex2)
print(hex1 * hex2)
