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
from collections import deque


def my_dex(string):
    dex = 0
    number = deque(string)
    number.reverse()
    for i in range(len(number)):
        dex += table[number[i]] * 16 ** i
    return dex


def my_hex(numb):
    number = deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                number.append(i)
        numb //= 16
    number.reverse()
    return list(number)


signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in signs:
    table[key] += counter
    counter += 1

num_1 = my_dex(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
num_2 = my_dex(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел: {my_hex(num_1 + num_2)}')
print(f'Произведение чисел: {my_hex(num_1 * num_2)}')
