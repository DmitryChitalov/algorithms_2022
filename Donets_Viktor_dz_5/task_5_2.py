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


# Вариант 1
num_1 = input('Введите число в шестнадцатиричном формате: ').upper()
num_2 = input('Введите второе число в шестнадцатиричном формате: ').upper()
sum_num_1 = reduce(lambda x, y: x + y, [int(num_1, 16), int(num_2, 16)])
product_num_1 = reduce(lambda x, y: x * y, [int(num_1, 16), int(num_2, 16)])
print(f'Сумма чисел: {sum_num_1:X}')
print(f'Произведение чисел: {product_num_1:X}')

# Вариант 2
n = int(input('Введите количество чисел участвующих в операции:'))
table = defaultdict(int)
for i in range(n):
    table[i] = int(
        (input('Введите число в шестнадцатиричном формате: ').upper()), 16)

sum_num_2 = reduce(lambda x, y: x + y, table.values())
product_num_2 = reduce(lambda x, y: x * y, table.values())
print(f'Сумма чисел: {sum_num_2:X}')
print(f'Произведение чисел: {product_num_2:X}')


# Вариант 3
class Hex:
    def __init__(self, x):
        self.x = int(x, 16)


    def __add__(self, other):
        self.sum_num = self.x + other.x
        self.sum_num = f'{self.sum_num: X}'
        return self.sum_num

    def __mul__(self, other):
        self.product_num = self.x * other.x
        self.product_num = f'{self.product_num: X}'
        return self.product_num


num_1 = Hex(input('Введите число в шестнадцатиричном формате: ').upper())
num_2 = Hex(
    input('Введите второе число в шестнадцатиричном формате: ').upper())

print(f'Сумма чисел: {num_1 + num_2}')
print(f'Произведение чисел: {num_1 * num_2}')
