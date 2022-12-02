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

dict_num = defaultdict(list)

num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')

dict_num[num_1] = list(num_1)
dict_num[num_2] = list(num_2)

print(dict_num)

sum_nums = reduce(lambda a, b: a+b, [int(''.join(i), 16) for i in dict_num.values()])
mult_nums = reduce(lambda a, b: a*b, [int(''.join(i), 16) for i in dict_num.values()])
print(sum_nums, '\n', mult_nums, sep='')

sum_nums_hex = list(f'{sum_nums:X}')
mult_nums_hex = list(f'{mult_nums:X}')

print(f'Сумма введенных вами чисел: {sum_nums_hex}\nПроизведение: {mult_nums_hex}')


class HexClass:
    def __init__(self, num_1):
        self.num_1 = num_1

    def __add__(self, other):
        sum_nums = int(''.join(self.num_1), 16) + int(''.join(other.num_1), 16)
        return list(f'{sum_nums:X}')

    def __mul__(self, other):
        mult_nums = int(''.join(self.num_1), 16) * int(''.join(other.num_1), 16)
        return list(f'{mult_nums:X}')


h1 = HexClass('A2')
h2 = HexClass('C4F')

print(h1 + h2)
print(h1 * h2)
