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
"""
1) Через collections
"""
from collections import defaultdict
from functools import reduce


print('1) Через collections')
def hex_sum_mult():
    nums = defaultdict(list)
    for i in range(2):
        numb_16 = input(f'Введите {i+1}-е натуральное число: ')
        nums[numb_16] = list(numb_16)
        print(f'{i+1}-е число: {nums[numb_16]}')
    print()

    nums_int_list = [int(''.join(i), 16) for i in nums.values()]

    sum_res = sum(nums_int_list)
    print('Сумма:', list('%X' % sum_res))

    mul_res = reduce(lambda x, y: x * y, nums_int_list)
    print('Произведение:', list('%X' % mul_res))