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
from collections import defaultdict

# 1a)
a = input('Введите 16-ричное число: ')
b = input('Введите 16-ричное число: ')
my_dict = defaultdict(list)
my_dict[a] = list(a)
my_dict[b] = list(b)
my_dict['sum_hex'] = list(hex(int(''.join(my_dict[a]), 16) + int(''.join(my_dict[b]), 16)).upper())
my_dict['mult_hex'] = list(hex(int(''.join(my_dict[a]), 16) * int(''.join(my_dict[b]), 16)).upper())

print(f'Сумма чисел: {my_dict["sum_hex"][2:]}')
print(f'Произведение чисел: {my_dict["mult_hex"][2:]}')


# # Я не очень понял зачем здесь использовать именно defaultdict,
# вроде все решается намного проще встроенными функциями
#
# 1b)

a = input('Введите 16-ричное число: ')
b = input('Введите 16-ричное число: ')

c = hex(int(a, 16) + int(b, 16))
print(f'Сумма чисел: {list(c.upper())[2:]}')
d = hex(int(a, 16) * int(b, 16))
print(f'произведение чисел: {list(d.upper())[2:]}')


# 2)


class CalcHex:

    def __init__(self, x):
        self.x = int(x, 16)

    def __add__(self, other):
        return list(hex(self.x + other.x))[2:]

    def __mul__(self, other):
        return list(hex(self.x * other.x))[2:]


a = CalcHex(input('Введите 16-ричное число: '))
b = CalcHex(input('Введите 16-ричное число: '))

print(f'Сумма чисел: {a + b}')
print(f'Произведение чисел: {a * b}')
