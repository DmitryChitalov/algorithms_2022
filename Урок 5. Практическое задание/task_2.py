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
# 1) через collections
from collections import defaultdict

my_dict = defaultdict(list)

my_dict[1] = list(input('Введите первое число: '))
my_dict[2] = list(input('Введите второе число: '))

multiplication = hex(int(''.join(my_dict[1]), 16) *
                     int(''.join(my_dict[2]), 16)).removeprefix('0x')
addition = hex(int(''.join(my_dict[1]), 16) +
               int(''.join(my_dict[2]), 16)).removeprefix('0x')

print(f'Сумма чисел: {addition}\n Произведение: {multiplication}')



#  2) через ООП


class MyDict:
    def __init__(self, num_one, num_two):
        self.num_one = num_one
        self.num_two = num_two

    def __add__(self, other):
        return hex(int(''.join(self.num_one), 16) +
                   int(''.join(other.num_two), 16)).removeprefix('0x')

    def __mul__(self, other):
        return hex(int(''.join(self.num_one), 16) *
                   int(''.join(other.num_two), 16)).removeprefix('0x')


a = list(input('Введите первое число: '))
b = list(input('Введите второе число: '))
addition = MyDict(a, b) + MyDict(a, b)
multiplication = MyDict(a, b) * MyDict(a, b)
print(f'Сумма чисел: {addition}\nПроизведение: {multiplication}')

