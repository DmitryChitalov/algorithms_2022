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
# 1 вариант решение через collections
from collections import UserString


in_1 = 'A2'  # input('введите 1-ое 16-и ричное число например A2 ')
in_2 = 'C4F'  # input('введите 2-ое 16-и ричное число например C4F ')
in_1 = in_1.upper()
in_2 = in_2.upper()


z = [str(x) for x in range(1, 10)]+['A', 'B', 'C', 'D', 'E', 'F']
convert_di = {x:num for num, x in enumerate(z, start=1)}
unconvert_di = {v:k for k, v in convert_di.items()}


def converter(num):
    res = 0
    for en, item in enumerate(num[::-1]):
        res += convert_di[item]*(16**en)
    return res


def unconverter(num):
    res2 = UserString('')
    while num > 16:
        res = num % 16
        num = num // 16
        
        if res < 16:
            res2 += unconvert_di[res]
        if num < 16:
            res2 += unconvert_di[num]
    res2 = res2[::-1]
    return res2


res = unconverter(converter(in_1) + converter(in_2))
print(f'сумма чисел {res}')

res = unconverter(converter(in_1) * converter(in_2))
print(f'произведение чисел {res}')


# 2 вариант решение через ООП

class Digit():
    def __init__(self, hex_num, convert=True):
        self.convert_di = {x:num for num, x in enumerate(z, start=1)}
        self.unconvert_di = {v:k for k, v in convert_di.items()}
        if convert:
            self.decimal_num = self.converter(hex_num.upper())
        else:
            self.decimal_num = hex_num

    def converter(self, num):
        res = 0
        for en, item in enumerate(num[::-1]):
            res += self.convert_di[item]*(16**en)
        return res

    def unconverter(self, num):
        res2 = ''
        while num > 16:
            res = num % 16
            num = num // 16
            
            if res < 16:
                res2 += self.unconvert_di[res]
            if num < 16:
                res2 += self.unconvert_di[num]
        res2 = res2[::-1]
        return res2

    def __mul__(self, cls):
        return Digit((self.decimal_num * cls.decimal_num), False)

    def __add__(self, cls):
        return Digit((self.decimal_num + cls.decimal_num), False)

    def __sub__(self, cls):
        return Digit((self.decimal_num - cls.decimal_num), False)

    def __truediv__(self, cls):
        return Digit(int(self.decimal_num / cls.decimal_num), False)

    def __str__(self) -> str:
        '''return hex digit'''
        return str(self.unconverter(self.decimal_num))
        
hex_1 = Digit('ca2')
hex_2 = Digit('4f')
hex_summ = hex_1 + hex_2
hex_multiply = hex_1 * hex_2
hex_div = hex_1 - hex_2
print(f'сумма {hex_summ}')
print(f'произведение {hex_multiply}')
print(f'разность {hex_div}')
print(f'остаток от деления {hex_multiply}')