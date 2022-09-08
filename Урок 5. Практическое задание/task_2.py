from collections import defaultdict
from functools import reduce
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

# Решение с defaultdict.
numbers = defaultdict(list)
def lst_numbers():
    for i in range(2):
        str_number = input(f"Введите шестнадцатеричное число: ")
        numbers[str_number] = list(str_number)
    return numbers

# print(lst_numbers())


def get_sum():
    summ = sum([int(''.join(i), 16) for i in numbers.values()])
    return f"Сумма чисел равна: , {list(format(summ, 'X'))}"
# print(get_sum())

def get_mul():
    mul = reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in numbers.values()])
    return f"Произведение чисел равно: , {list(format(mul, 'X'))}"
# print(get_mul())

# Решение с ООП.
class Number:
    def __init__(self, number):
        self.lst = list(number)

    def get_number(self):
        return self.lst

    def __add__(self, other):
        summ = list(format(int(''.join(self.lst), 16) + int(''.join(other.lst), 16),'X'))
        return f'Сумма чисел равна {summ}'

    def __mul__(self, other):
        mul = list(format(int(''.join(self.lst), 16) * int(''.join(other.lst), 16),'X'))
        return f'Произведение чисел равно: {mul}'

    def __str__(self):
        return f'Cохраненное число: {self.lst} '

str_number_1 = input("Введите первое шестнадцатеричное число: ")
str_number_2 = input("Введите второе шестнадцатеричное число: ")
num_1 = Number(str_number_1)
num_2 = Number(str_number_2)
print(num_1)
print(num_2)
print(num_1 + num_2)
print(num_1 * num_2)