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

# Вариант 1
from collections import defaultdict


def input_hex(n : int):
    num_list = []
    while True:
        num = input(f'Введите {n}-е число в шестнадцатиричном формате: ').upper()
        zn = True
        for i in num:
            if i not in zn_hex:
                zn = False
                break
            else:
                num_list.append(i)
        if zn: break
    return num_list

zn_hex = '0123456789ABCDEF'
hex_dict = defaultdict(list)

hex_dict[1] = input_hex(1)
hex_dict[2] = input_hex(2)
hex_dict[3] = list(str(hex(int(''.join(hex_dict[1]), 16) + int(''.join(hex_dict[2]), 16)))[2:].upper())
hex_dict[4] = list(str(hex(int(''.join(hex_dict[1]), 16) * int(''.join(hex_dict[2]), 16)))[2:].upper())

print('Сумма чисел из примера: ', hex_dict[3])
print('Произведение чисел из примера: ', hex_dict[4])


# Вариант 2
class HexCalc():
    def __init__(self):
        self.number = 0

    def enter_number(self, n : int):
        zn_hex = '0123456789ABCDEF'
        num = ''
        while True:
            en = input(f'Введите {n}-е число в шестнадцатиричном формате: ').upper()
            zn = True
            for i in en:
                if i not in zn_hex:
                    zn = False
                    break
                else:
                    num += i
            if zn: break
        self.number = int(num, 16)

    def getHex(self):
        return hex(self.number)

    def setHex(self, new_number_hex):
        self.number = int(new_number_hex, 16)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number

    @staticmethod
    def hex2list(hex_number):
        return list(str(hex(hex_number))[2:].upper())


h1 = HexCalc()
h1.enter_number(1)
h2 = HexCalc()
h2.enter_number(2)

print('1-е число:', HexCalc.hex2list(h1.number))
print('2-е число:', HexCalc.hex2list(h2.number))
print('1-e + 2-e =', HexCalc.hex2list(h1 + h2))
print('1-e * 2-e =', HexCalc.hex2list(h1 * h2))