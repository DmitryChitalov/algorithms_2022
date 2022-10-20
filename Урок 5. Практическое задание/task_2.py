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

def calc(k):
    nums = collections.defaultdict(list)

    # defaultdict(<class 'list'>,
    # {'1-A2': ['A', '2'], '2-C4F': ['C', '4', 'F']})
    for d in range(k):
        n = input(f"Введите {d+1}-е натуральное шестнадцатиричное число: ")
        nums[f"{d+1}-{n}"] = list(n)
    print(nums)

    # 16-указываем с числами какой системы делаем операции
    sum_res = sum([int(''.join(i), 16) for i in nums.values()])
    print(sum_res)
    # '%X'	Число в шестнадцатеричной системе счисления

    print(f"Сумма {k} чисел равна: ", list('%X' % sum_res))
    # f'{15:x}' -> f
    mul_res = functools.reduce(lambda a, b: a * b,
                               [int(''.join(i), 16) for i in nums.values()])
    print(f"Произведение {k} чисел равно: ", list('%X' % mul_res))


calc(3)
