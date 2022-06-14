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

check = '0123456789ABCDEF'
test = defaultdict(list)


def get_val(array, value):
    for el in value:
        if el in check:
            test[value].append(el)
        else:
            return exit('Wrong value')
    return array


def to_hex(dec):
    hexed = ""
    while dec != 0:
        dec, value = divmod(dec, 16)
        hexed = check[value] + hexed
    return hexed


def reduce_sum(p_el, el):
    return to_hex(int(p_el, 16) + int(el, 16))


def reduce_mul(p_el, el):
    return to_hex(int(p_el, 16) * int(el, 16))


f_val = input('Enter first hexadecimal value: ')
get_val(test, f_val)
symb = input('Enter operand + or * : ')
sec_val = input('Enter second hexadecimal value: ')
get_val(test, sec_val)

if symb == '+':
    result = reduce(reduce_sum, test)
elif symb == '*':
    result = reduce(reduce_mul, test)
else:
    exit('Wrong operand')
get_val(test, result)
print(test[result])


# ООП

class HexValue:
    def __init__(self, val):
        self.__check = '0123456789ABCDEF'
        self.value = self.input_convert(val)
        self.dec_value = int(val, 16)

    def input_convert(self, val):
        convert = []
        for el in val.upper():
            if el not in self.__check:
                return exit('Wrong value')
            convert.append(el)
        return convert

    def to_hex(self, dec):
        hexed = []
        while dec != 0:
            dec, val = divmod(dec, 16)
            hexed.insert(0, self.__check[val])
        return hexed

    def __add__(self, other):
        return self.to_hex(self.dec_value + other.dec_value)

    def __mul__(self, other):
        return self.to_hex(self.dec_value * other.dec_value)


first_val = HexValue(input('Enter first hexadecimal value: '))
operand = input('Enter operand + or * : ')
second_val = HexValue(input('Enter second hexadecimal value: '))
if operand == '+':
    print(first_val + second_val)
elif operand == '*':
    print(first_val * second_val)
else:
    print('Wrong operand')
