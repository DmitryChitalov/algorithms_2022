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
from functools import reduce

def numbers():
    numbers = defaultdict(list)
    for i in range(1, 3):
        number = input(f"Введите {i}-е шестнадцатеричное число: ")
        numbers[number] = list(number)
    return numbers

def_number = numbers()
print("Числа сохранены как: ", end=' ')
print(*def_number.values())
my_sum = sum([int(''.join(i), 16) for i in def_number.values()])
print("Сумма: ", list(format(my_sum, 'X')))
my_mult = reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in def_number.values()])
print("Произведение: ", list(format(my_mult, 'X')))