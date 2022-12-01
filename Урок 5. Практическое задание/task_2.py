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
import numpy


def calc_num():
    tmp = defaultdict(list)
    n = 0
    while n != 2:
        n += 1
        num = input(f'Введите {n}-е шестнадцатеричное число: ')
        tmp[num] = list(num)
    sum_num = sum([int(''.join(i), 16) for i in tmp.values()])
    mul_num = numpy.prod([int(''.join(i), 16) for i in tmp.values()])
    result_sum = list('%X' % sum_num)
    result_mul = list('%X' % mul_num)
    return f'Сумма чисел: {result_sum}\nПроизведение: {result_mul}'


# print(calc_num())


class OtherNumb:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return list(hex(int(''.join(self.num_1), 16) + int(''.join(other.num_2), 16)).upper())[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_1), 16) * int(''.join(other.num_2), 16)).upper())[2:]

numb_1 = input('Введите 1-е шестнадцатеричное число: ')
numb_2 = input('Введите 2-е шестнадцатеричное число: ')

result_sum = OtherNumb(numb_1, numb_2) + OtherNumb(numb_1, numb_2)
result_mul = OtherNumb(numb_1, numb_2) * OtherNumb(numb_1, numb_2)

print(f'Сумма чисел: {result_sum}\nПроизведение: {result_mul}')

