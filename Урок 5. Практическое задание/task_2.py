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


def hex_():
    dct = defaultdict(list)
    count_ = 1
    while count_ < 3:
        num = input('введите шеснадцатеричное число: ')
        for i in num:
            dct[num + '_' + str(count_)].append(i)
        count_ += 1
    print(dct)
    number = [int(''.join(i), 16) for i in dct.values()]
    add_ = list(hex(sum(number)).upper())[2:]
    mul = list(hex(reduce(lambda x, y: x * y, number)))[2:]
    return f'сумма: {add_}, произведение: {mul}'

print(hex_())


class HexOperation:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return list(hex(int(''.join(self.num_1), 16) + int(''.join(self.num_2), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_1), 16) * int(''.join(self.num_2), 16)))[2:]


hex_add = HexOperation(input('введите первое шеснадцатеричное число: '),
                       input('введите второе шеснадцатеричное число: '))
sum_hex_add = hex_add + hex_add
print(f'сумма {sum_hex_add}')
hex_mul = HexOperation('A2', 'CF4')
sum_hex_mul = hex_mul * hex_mul
print(f'произведение :{sum_hex_mul}')





























