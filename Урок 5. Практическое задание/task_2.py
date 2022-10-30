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
import functools


hex_numbers = collections.defaultdict(list)

for i in range(2):
    hex_numbers[i] = list(input(f"Введите число {i + 1}: "))

sum_10 = sum([int(''.join(i), 16) for i in hex_numbers.values()])
mult_10 = functools.reduce(lambda n1, n2: n1 * n2, [int(''.join(i), 16) for i in hex_numbers.values()])
print(f'Сумма: {list(str(hex(sum_10)).lstrip("0x").rstrip("L").upper())}\n'
      f'Произведение: {list(str(hex(mult_10)).lstrip("0x").rstrip("L").upper())}')


class MyHex:
    def __init__(self, in_list: list):
        self.value = int(''.join(in_list), 16)

    def __add__(self, other):
        return list(str(hex(self.value + other.value)).lstrip("0x").rstrip("L").upper())

    def __mul__(self, other):
        return list(str(hex(self.value * other.value)).lstrip("0x").rstrip("L").upper())


print(f'Сумма: {MyHex(hex_numbers[0]) + MyHex(hex_numbers[1])}\n'
      f'Произведение: {MyHex(hex_numbers[0]) * MyHex(hex_numbers[1])}')
