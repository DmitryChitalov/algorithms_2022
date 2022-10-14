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


def calc():
    nums = defaultdict(list)

    for d in range(2):
        n = input(f"Введите {d + 1}-е натуральное шестнадцатиричное число: ")
        nums[f"{d + 1} - {n}"] = list(n)
    print(nums)

    sum_nums = sum([int("".join(i), 16) for i in nums.values()])
    print(sum_nums)

    print("Сумма: ", list("%X" % sum_nums))

    mul_res = reduce(lambda a, b: a * b, [int("".join(i), 16) for i in nums.values()])
    print("Произведение: ", list("%X" % mul_res))


calc()
