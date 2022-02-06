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

from collections import deque, defaultdict

numbers = defaultdict(list)
number_1 = "A2"
number_2 = "C4F"


def full_dict():
    sum_of_nums = hex(int(number_1, 16) + int(number_2, 16))[2:].upper()
    multiplication_of_nums = hex(int(number_1, 16) * int(number_2, 16))[2:].upper()
    sum = list(deque(sum_of_nums))
    multiplication = list(deque(multiplication_of_nums))
    return f'Сумма чисел из примера: {sum}, произведение - {multiplication}'


print(full_dict())

