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


def calculation16():
    numbers = defaultdict(list)
    for i in range(2):
        number = input("Введите первое шестнадцатеричное число: ")
        numbers[number] = list(number)
    sum_numbers = 0
    mult_numbers = 1
    for i in numbers.values():
        sum_numbers += int(''.join(i), 16)
        mult_numbers *= int(''.join(i), 16)
    sum_numbers = list(hex(sum_numbers).split('x')[-1])
    mult_numbers = list(hex(mult_numbers).split('x')[-1])
    return f"Сумма чисел: {sum_numbers}, произведение чисел: {mult_numbers}"


print(calculation16())

