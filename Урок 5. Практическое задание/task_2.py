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


def hexadecimal_multiplication(first, second):
    num_first_list = list(first)
    num_second_list = list(second)
    numbers = defaultdict(list, a=num_first_list, b=num_second_list)
    summa = reduce(lambda j, k: j + k, [int(''.join(i), 16) for i in numbers.values()])
    total_sum = list(f"{summa:X}")
    print(f"Сумма чисел из примера: {total_sum}")
    work_numbers = reduce(lambda l, m: l * m, [int(''.join(i), 16) for i in numbers.values()])
    work = list(f"{work_numbers:X}")
    print(f"произведение - {work}")
    return numbers.values()


num_first = input('Введите первое шестнадцатеричное число: ')
num_second = input('Введите второе шестнадцатеричное число: ')
print('1) через collections')

hexadecimal_multiplication(num_first, num_second)


class Hexadecimals:
    def __init__(self):
        self.number_1 = num_first
        self.number_2 = num_second
        self.number_1_1 = int(self.number_1, 16)
        self.number_2_2 = int(self.number_2, 16)

    def __mul__(self, other):
        return list(f"{self.number_1_1 * other.number_2_2:X}")

    def __add__(self, other):
        return list(f"{self.number_1_1 + other.number_2_2:X}")


number_one = Hexadecimals()
number_two = Hexadecimals()

print('2) через ООП')
print(f'Сумма чисел из примера: {number_one + number_two}')
print(f'произведение - {number_one * number_two}')
