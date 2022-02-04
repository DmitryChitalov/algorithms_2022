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

result = defaultdict(list)
a = "A2"
b = "C4F"
a = int(a, 16)
b = int(b, 16)
summa = list(hex(a + b))
mult = list(hex(a * b))
result['suma'] = list(hex(a + b)[2:])
result['mult'] = list(hex(a * b)[2:])
print(result['suma'])
print(result['mult'])
