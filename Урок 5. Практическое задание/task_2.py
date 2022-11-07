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

# 1) Решение collections
from collections import defaultdict
from functools import reduce

hex_line = '0123456789ABCDEF'
test = defaultdict(list)


def collect(array, val):
    for el in val:
        if el in hex_line:
            test[val].append(el)
        else:
            return exit('Введено не верное значение')
    return array


def to_hex(dec):
    result = ''
    while dec != 0:
        dec, val = divmod(dec, 16)
        result = hex_line[val] + result
    return result


def reduce_sum(p_el, el):
    return to_hex(int(p_el, 16) + int(el, 16))


def reduce_mul(p_el, el):
    return to_hex(int(p_el, 16) * int(el, 16))


val1 = input('Введите первое 16-ое число: ').upper()
collect(test, val1)
sign = input('Введите математический знак (* или +): ')
val2 = input('Введите второе 16-ое число: ').upper()
collect(test, val2)

if sign == '+':
    result = reduce(reduce_sum, test)
elif sign == '*':
    result = reduce(reduce_mul, test)
else:
    exit('Был введен некорректный математический знак!')
collect(test, result)
print(test[result])


# 2) Решение через ООП`
class HexValue:
    def __init__(self, in_val):
        self.__hex_line = '0123456789ABCDEF'
        self.value = self.__input_convert(in_val)
        self.dec_value = int(in_val, 16)

    def __add__(self, other):
        return self.__to_hex(self.dec_value + other.dec_value)

    def __mul__(self, other):
        return self.__to_hex(self.dec_value * other.dec_value)

    # На случай если ООП надо было без int( ,16)
    # def __to_dec(self):
    #     result = 0
    #     n = len(self.value) - 1
    #     for el in self.value:
    #         if el in self.hex_list:
    #             val = self.hex_list.index(el) + 10
    #         else:
    #             val = int(el)
    #         for _ in range(n):
    #             val *= 16
    #         n -= 1
    #         result += val
    #     return result

    def __to_hex(self, dec):
        result = []
        while dec != 0:
            dec, val = divmod(dec, 16)
            result.insert(0, self.__hex_line[val])
        return result

    def __input_convert(self, in_val):
        result = []
        for el in in_val.upper():
            if el not in self.__hex_line:
                return exit('Введено не верное значение')
            result.append(el)
        return result


val1 = HexValue(input('Введите первое 16-ое число: '))
sign = input('Введите математический знак (* или +): ')
val2 = HexValue(input('Введите второе 16-ое число: '))
if sign == '+':
    print(val1 + val2)
elif sign == '*':
    print(val1 * val2)
else:
    print('Был введен некорректный математический знак!')
