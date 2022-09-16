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
from collections import defaultdict, deque

signs = '0123456789ABCDEF'
table = defaultdict(int)


def str_number(string):
    x = 0
    str_num = deque(string)
    str_num.reverse()
    for i in range(len(str_num)):
        x += table[str_num[i]] * 16 ** i
    return x


def hex_number(numb):
    hex_num = deque()
    while numb > 0:
        y = numb % 16
        for i in table:
            if table[i] == y:
                hex_num.append(i)
        numb //= 16
    hex_num.reverse()
    return list(hex_num)


counter = 0
for key in signs:
    table[key] += counter
    counter += 1

num_1 = str_number(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
num_2 = str_number(input('Введите первое число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел из примера: {hex_number(num_1 + num_2)}')
print(f'Произведение чисел из примера: {hex_number(num_1 * num_2)}')
