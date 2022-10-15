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


def calc():
    nums = collections.defaultdict(list)
    for i in range(2):
        n = input(f'Введите {i+1}-e шестнадцатиричное число: ')
        nums[f'{i+1}-{n}'] = list(n)

    calc_sum = sum([int(''.join(x), 16) for x in nums.values()])
    print(f'Сумма = ', list('%X' % calc_sum))

    calc_mul = functools.reduce(lambda a, b: a * b,
                                [int(''.join(x), 16) for x in nums.values()])
    print(f'Произведение = ', list('%X' % calc_mul))


if __name__ == '__main__':
    calc()