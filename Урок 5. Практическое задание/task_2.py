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

lst = defaultdict()
first_number = input('Введите шестнадцатиричное число: ')
second_number = input('Введите шестнадцатиричное число: ')

lst['first number'] = list(first_number.upper())
lst['second number'] = list(second_number.upper())
lst['sum_lst'] = list(hex(int(first_number, 16) + int(second_number, 16))[2:].upper())
lst['multiplication_lst'] = list(hex(int(first_number, 16) * int(second_number, 16))[2:].upper())
print(lst)