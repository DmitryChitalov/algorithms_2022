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
from collections import defaultdict


def culc():
    nums = collections.defaultdict(list)
    for i in range(2):
        number = input(f'Введите {i + 1}-e шестнадцатиричное число: ')
        nums[i + 1] = list(number)

    sum_10 = sum([int(''.join(i), 16) for i in nums.values()])
    # вывод в 16-тиричной форме
    sum_16 = ''
    h = '0123456789ABCDEF'
    while sum_10 > 0:
        sum_16 = h[sum_10 % 16] + sum_16
        sum_10 = sum_10 // 16
    print('Сумма чисел: ', list(sum_16))

    mul_10 = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
    mul_16 = ''
    h = '0123456789ABCDEF'
    while mul_10 > 0:
        mul_16 = h[mul_10 % 16] + mul_16
        mul_10 = mul_10 // 16
    print('Произведение: ', list(mul_16))


culc()
