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


def calc(nums):

    sum_result = sum([int(''.join(i), 16) for i in nums.values()])
    mul_result = reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
    print(f'Сумма чисел равна: {list("%X" % sum_result)}')
    print(f'Произведение чисел равно: {list("%X" % mul_result)}')



num1 = input(f'Введите первое шестнадцатиричное число:')
nums[f'1-{num1}'] = list(num1)
num2 = input(f'Введите второе шестнадцатиричное число:')
nums[f'2-{num2}'] = list(num2)
print(nums)
calc(nums)