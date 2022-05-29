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


def calc():
    num = defaultdict(list)
    for i in range(2):
        el = input(f'Введите {i + 1} число: ')
        num[i + 1] = list(el)
    sum_num = hex(sum(int(''.join(i), 16) for i in num.values()))
    mulply_num = hex(int(''.join(num.get(1))) * int(''.join(num.get(2))))
    print(f'Сумма чисел из примера: {list(sum_num[2:])},\n'
          f'произведение - {list(mulply_num)[2:]}.')


calc()
