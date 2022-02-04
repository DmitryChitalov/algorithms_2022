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

ddict = defaultdict(list)

ddict[1] = list(input('Введите первое число: '))
ddict[2] = list(input('Введите второе число: '))
print(ddict)

c = hex(int(''.join(str(i) for i in ddict[1]), 16) * int(''.join(str(i) for i in ddict[2]), 16))
d = hex(int(''.join(str(i) for i in ddict[1]), 16) + int(''.join(str(i) for i in ddict[2]), 16))
print(f'Сумма: {list(c[2:].upper())}')
print(f'Произведение: {list(d[2:].upper())}')