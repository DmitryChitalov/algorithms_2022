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


def check(a, b):
    print(f'сумма(проверка):{str(hex(int(a, 16) + int(b, 16)))[2:].upper()}')
    print(f'произведение(проверка):{str(hex(int(a,16)*int(b,16)))[2:].upper()}')


def conv_int(lst):
    d_d = defaultdict(list)
    for n,i in enumerate(list(lst)):
        print(n, i)
        d_d[len(list(lst))-n-1].append(int(i,16))
    print(d_d)
    r = 0
    for k,v in d_d.items():
        r = r+((16**k)*v[0])
    print(r)
    return r


def conv_hex(num):
    res = []
    while num > 15:
        res.append(hex(num % 16)[2:])
        num = num//16
    res.append(hex(num)[2:])
    res.reverse()
    return res


def method_1(a, b):
    s = conv_hex(conv_int(str(a)) + conv_int(str(b)))
    m = conv_hex(conv_int(str(a)) * conv_int(str(b)))
    print(f'сумма:{s}')
    print(f'произведение:{m}')
    check(a, b)


method_1(input('Введите 1 число'),input('Введите 2 число'))