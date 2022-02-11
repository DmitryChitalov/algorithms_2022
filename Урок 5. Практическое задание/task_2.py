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

first_num = input('Введите первое число: ')
second_num = input('Введите второе число: ')

num_1 = list(first_num)
num_2 = list(second_num)

lst['Первое число'] = num_1
lst['Второе число'] = num_2
result_sum = (hex(int(first_num, 16) + int(second_num, 16))[2:]).upper()
result_mult = (hex(int(first_num, 16) * int(second_num, 16))[2:]).upper()
lst['Сумма чисел'] = list(result_sum)
lst['Произведение'] = list(result_mult)

print(lst)