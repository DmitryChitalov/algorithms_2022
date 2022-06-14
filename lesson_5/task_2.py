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

nums = defaultdict(list)

nums['first_num'] = list(input('Введите первое число: '))
nums['second_num'] = list(input('Введите второе число: '))

sum_res = sum([int(''.join(v), 16) for v in nums.values()])
mul_res = reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])

print(f'Сумма чисел из примера: ', list('%X' % sum_res))
print(f'произведение - ', list('%X' % mul_res))
