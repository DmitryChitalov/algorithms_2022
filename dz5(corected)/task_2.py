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
# 1) через collections
from functools import reduce
from collections import defaultdict


def sum_16():
    num_1 = input('Введите первое число: ')
    num_2 = input('Введите второе число: ')
    operation = input('Выберете операцию "+" или "*": ')
    num_dict_1 = defaultdict(int)

    def split(s):
        return [char for char in s]

    num_dict_1[num_1] = int(num_1, 16)
    num_dict_1[num_2] = int(num_2, 16)
    if operation == "+":
        sum_num_1 = reduce(lambda x, y: x + y, num_dict_1.values())
        return split(hex(sum_num_1)[2:])
    elif operation == "*":
        multiply = reduce(lambda x, y: x * y, num_dict_1.values())
        return split(hex(multiply)[2:])


print(sum_16())


# 2) через ООП
def func_sum():
    class SumMy:
        def __init__(self, num_1, num_2):
            self.num_1 = int(num_1, 16)
            self.num_2 = int(num_2, 16)

        def __add__(self):
            res = (hex(self.num_1 + self.num_2))[2:]
            return [char for char in res]

        def __mul__(self):
            res = (hex(self.num_1 * self.num_2))[2:]
            return [char for char in res]

    operation = input('Введите желаемую операцию "+" или "*": ')
    num_3 = input('Введите первое число: ')
    num_4 = input('Введите второе число: ')
    a = SumMy(num_3, num_4)
    if operation == '+':
        return a.__add__()
    else:
        return a.__mul__()


print(func_sum())
