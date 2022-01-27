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


def calc():

    nums = defaultdict(list)

    for i in range(2):
        number = input('Введите число в шестнадцатеричной системе счисления: ')
        nums[f'{number}'] = list(number)
    print(nums)

    sum_of_numbers = sum([int(''.join(i), 16) for i in nums.values()])
    print(f'Сумма этих чисел равна: {str(hex(sum_of_numbers))[2:]}')

    mul_of_numbers = int(''.join(nums.popitem()[1]), 16) * int(''.join(nums.popitem()[1]), 16)
    print(f'Произведение этих чисел равно: {str(hex(mul_of_numbers))[2:]}')


calc()
