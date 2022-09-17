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


hex_nums = defaultdict(list)
for i in range(2):
    hex_num = input('Введите шестнадцатиричное число: ')
    hex_nums[hex_num] = list(hex_num)
hex_sum = hex(sum([int(i, 16) for i in hex_nums.keys()]))
res_sum = list(str(hex_sum)[2:].upper())
int_prod = 1
for i in hex_nums.keys():
    int_prod *= int(i, 16)
hex_prod = hex(int_prod)
res_prod = list(str(hex_prod)[2:].upper())
print('Сумма чисел: ', res_sum)
print('Произведение: ', res_prod)


# 2)
class HexNum:

    def __init__(self, a_str):
        self.arr = list(a_str.upper())
        self.int = int(''.join(self.arr), 16)

    def __str__(self):
        return str(self.arr)

    def __add__(self, other):
        hex_sum = hex(self.int + other.int)
        str_sum = str(hex_sum)[2:]
        return HexNum(str_sum)

    def __mul__(self, other):
        hex_sum = hex(self.int * other.int)
        str_sum = str(hex_sum)[2:]
        return HexNum(str_sum)


hex_1 = HexNum(input('Введите первое шестнадцатиричное число: '))
hex_2 = HexNum(input('Введите второе шестнадцатиричное число: '))
print('Сумма чисел: ', hex_1 + hex_2)
print('Произведение: ', hex_1 * hex_2)
