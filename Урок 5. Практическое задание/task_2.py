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

num_dict = defaultdict(tuple)
first_num1 = input('Первое число в HEX: ')
second_num1 = input('Второе число в HEX: ')
num_dict[first_num1] = tuple(first_num1)
num_dict[second_num1] = tuple(second_num1)
print(f'Сумма двух чисел равна: {str(hex(int(first_num1, 16) + int(second_num1, 16))).split("x")[1].upper()}')
print(f'Произведение двух чисел равно: {str(hex(int(first_num1, 16) * int(second_num1, 16))).split("x")[1].upper()}')

"""
__________________________________________________________________________________________________
"""


class HexCalc:
    def __init__(self, value):
        self.value = int(value, 16)

    def __str__(self):
        result = str(hex(self.value)).split('x')[1].upper()
        return f'{result}'

    def __add__(self, other):
        res = self.value + other.value
        return str(hex(res)).split('x')[1].upper()

    def __mul__(self, other):
        res = self.value * other.value
        return str(hex(res)).split('x')[1].upper()


first_num2, second_num2 = HexCalc(input('Первое число в HEX: ')), HexCalc(input('Второе число в HEX: '))
print(f'Сумма двух чисел равна: {first_num2 + second_num2}')
print(f'Произведение двух чисел равно: {first_num2 * second_num2}')
