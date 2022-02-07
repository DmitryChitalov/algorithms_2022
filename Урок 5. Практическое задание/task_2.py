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
from functools import reduce


def mul_add_hexadecimal(f_num, s_num):
    first_num_lst = list(f_num)
    second_num_lst = list(s_num)
    entered_numbers = defaultdict(list, operand1=first_num_lst, operand2=second_num_lst)

    sum_numbers = reduce(lambda x, y: x + y, [int(''.join(i), 16) for i in entered_numbers.values()])
    total_sum_lst = list(f"{sum_numbers:X}")
    print(f"Сумма чисел: {total_sum_lst}")

    mul_numbers = reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in entered_numbers.values()])
    multiplication = list(f"{mul_numbers:X}")
    print(f"Произведение чисел:  {multiplication}")

    return entered_numbers.values()


first_num = input('Введите первое шестнадцатиричное число: ')
second_num = input('Введите второе шестнадцатиричное число: ')
mul_add_hexadecimal(first_num, second_num)


class Hexadecimal:
    def __init__(self):
        self.n_1 = first_num
        self.n_2 = second_num
        self.num_1 = int(self.n_1, 16)
        self.num_2 = int(self.n_2, 16)

    def __mul__(self, other):
        return list(f"{self.num_1 * other.num_2:X}")

    def __add__(self, other):
        return list(f"{self.num_1 + other.num_2:X}")



num_1 = Hexadecimal()
num_2 = Hexadecimal()

print(f'Сумма чисел: {num_1 + num_2}')
print(f'Произведение чисел: {num_1 * num_2}')
