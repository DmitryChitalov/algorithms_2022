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
from functools import reduce


# через collections defaultdict
def sum_hexadecimal(op_1, op_2):
    nums_1 = list(op_1)
    nums_2 = list(op_2)
    numbers = defaultdict(list, operand_1=nums_1, operand_2=nums_2)

    sum_res1 = reduce(lambda x, y: x + y, [int(''.join(i), 16) for i in numbers.values()])

    print("Сумма: ", list('%X' % sum_res1))

    mul_res1 = reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in numbers.values()])
    print("Произведение: ", list('%X' % mul_res1))

    return numbers.values()


sum_hexadecimal('A2', 'C4F')

print('*' * 100)


#  через ООП

class Hexadecimal:
    def __init__(self, number: str):
        self.number = list(number)

    def __add__(self, other):
        return Hexadecimal('%X' % (int(''.join(self.number), 16) + int(''.join(other.number), 16)))

    def __mul__(self, other):
        return Hexadecimal('%X' % (int(''.join(self.number), 16) * int(''.join(other.number), 16)))

    def __str__(self):
        return f'{self.number}'


first_num = input('Введите первое шестнадцатиричное число: ')
second_num = input('Введите второе шестнадцатиричное число: ')

sum_res2 = (Hexadecimal(first_num) + Hexadecimal(second_num))
mul_res2 = (Hexadecimal(first_num) * Hexadecimal(second_num))

print(f'Сумма: {sum_res2}')
print(f'Произведение: {mul_res2}')