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
"""

from collections import defaultdict

try:
    numbers = defaultdict(list)
    first_number = input('Введите первое число: ')
    second_number = input('Введите второе число: ')
    numbers['first_number'], numbers['second_number'] = list(first_number), list(second_number)
    numbers['add'] = list(hex(int(''.join(numbers['first_number']), 16)+int(''.join(numbers['second_number']), 16))[2:].upper())
    numbers['mul'] = list(hex(int(''.join(numbers['first_number']), 16)*int(''.join(numbers['second_number']), 16))[2:].upper())
    print(f"Сумма введённых чисел: {numbers['add']}")
    print(f"Произведение введённых чисел: {numbers['mul']}")
except ValueError:
    print('Вы ввели число не в 16-тиричном представлении.')
