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

# a, b = input('a: '), input('b: ')
#
# print(f'Сумма чисел: {list(str(hex(int(a, 16) + int(b, 16)))[2:].upper())}')
# print(f'Произведение чисел: {list(str(hex(int(a, 16) * int(b, 16)))[2:].upper())}')


class MyClass:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return list(str(hex(int(self.num, 16) + int(other.num, 16)))[2:].upper())

    def __mul__(self, other):
        return list(str(hex(int(self.num, 16) * int(other.num, 16)))[2:].upper())


x = MyClass(input('x: '))
y = MyClass(input('y: '))
print(f'Сумма чисел: {x + y}')
print(f'Произведение чисел: {x * y}')
