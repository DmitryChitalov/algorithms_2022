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

fst = list(input('Введите число 1: '))
snd = list(input('Введите число 2: '))

# Решение вариант 1:
numbers_d = defaultdict(list)
numbers_d['fst'] = fst
numbers_d['snd'] = snd
f_num = int((''.join(numbers_d['fst'])), 16)
s_num = int((''.join(numbers_d['snd'])), 16)
print(f'Сумма чисел из примера: {list(hex(f_num + s_num).upper())[2:]}')
print(f'Произведение чисел из примера: {list(hex(f_num * s_num).upper())[2:]}\n')


# Решение вариант 2:
class Number:
    def __init__(self, num_lst):
        self.num_16 = int(''.join(num_lst), 16)

    def __add__(self, other):
        res = self.num_16 + other.num_16
        return list(hex(res).upper()[2:])

    def __mul__(self, other):
        res = self.num_16 * other.num_16
        return list(hex(res).upper()[2:])


f_num = Number(fst)
s_num = Number(snd)

print(f'Сумма чисел из примера: {f_num + s_num}')
print(f'Произведение чисел из примера: {f_num * s_num}')
