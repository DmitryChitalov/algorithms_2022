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

import functools
from collections import deque, defaultdict


def calc():
    signs = '0123456789ABCDEF'
    hex2dec = {}
    dec2hex = {}
    n = 0
    for el in signs:
        hex2dec[el] = n
        dec2hex[n] = el
        n += 1

    def num_dec(string):
        dec = 0
        num = deque(string)
        for i in range(len(num)):
            dec += hex2dec[num.pop()] * 16 ** i
        return dec

    def num_hex(res):
        n_hex = deque()
        while res > 0:
            s = res % 16
            n_hex.appendleft(dec2hex[s])
            res //= 16
        return list(n_hex)

    num_1 = num_dec(input('Введите первое число в шестнадцатиричной системе исчисления: ').upper())
    num_2 = num_dec(input('Введите второе число в шестнадцатиричной системе исчисления: ').upper())

    print(f'Сумма чисел равна {num_hex(num_1 + num_2)}')
    print(f'Произведение чисел равно {num_hex(num_1 * num_2)}')


calc()


def calc_2():
    numbers = collections.defaultdict(list)

    for i in range(2):
        n = input(f'Введите {i + 1} число в шестнадцатиричной системе исчисления: ')
        numbers[f'{i+1} - {n}'] = list(n)

    summa = sum([int(''.join(i), 16) for i in numbers.values()])
    print('Сумма чисел равна ', list('%X' % summa))

    mult = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in numbers.values()])
    print('Произведение чисел равно ', list('%X' % mult))


calc_2()


def calc_3():
    class HexOperation:

        def __init__(self, n1, n2):
            self.n1 = n1
            self.n2 = n2

        def __add__(self, other):
            return list(hex(int(''.join(self.n1), 16) + int(''.join(other.n2), 16)).upper())[2:]

        def __mul__(self, other):
            return list(hex(int(''.join(self.n1), 16) * int(''.join(other.n2), 16)).upper())[2:]

    hex_n1 = list(input('Введите первое число в шестнадцатиричной системе исчисления: '))
    hex_n2 = list(input('Введите второе число в шестнадцатиричной системе исчисления: '))

    summa = HexOperation(hex_n1, hex_n2) + HexOperation(hex_n1, hex_n2)
    mult =  HexOperation(hex_n1, hex_n2) * HexOperation(hex_n1, hex_n2)

    print(f'Сумма чисел равна {summa}')
    print(f'Произведение чисел равно {mult}')


calc_3()
