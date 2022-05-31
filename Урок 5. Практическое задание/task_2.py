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

# Variant 1
defdict = collections.defaultdict(str)
defdict[0] = str(input(f"Введите число 1: "))
defdict[1] = str(input(f"Введите число 2: "))
dict_sum = int(defdict[0], 16) + int(defdict[1], 16)
print(dict_sum)

# Variant 2
dict_sum = functools.reduce(lambda a, b: a * b, (int(i, 16) for i in defdict.values()))
print(dict_sum)
