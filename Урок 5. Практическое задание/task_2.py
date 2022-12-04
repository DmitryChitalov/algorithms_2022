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


"""
1) Через collections
"""
from collections import defaultdict
from functools import reduce


print('1) Через collections')
def hex_sum_mult():
    nums = defaultdict(list)
    for i in range(2):
        numb_16 = input(f'Введите {i+1}-е натуральное число: ')
        nums[numb_16] = list(numb_16)
        print(f'{i+1}-е число: {nums[numb_16]}')
    print()

    nums_int_list = [int(''.join(i), 16) for i in nums.values()]

    sum_res = sum(nums_int_list)
    print('Сумма:', list('%X' % sum_res))

    mul_res = reduce(lambda x, y: x * y, nums_int_list)
    print('Произведение:', list('%X' % mul_res))


hex_sum_mult()
print()

"""
2) Через ООП
"""
class HexAddMult:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number
        self.__first_number = int(''.join(self.first_number), 16)
        self.__second_number = int(''.join(self.second_number), 16)

    def __add__(self, other):
        return list(hex(self.__first_number + other.__second_number).upper())[2:]

    def __mul__(self, other):
        return list(hex(self.__first_number * other.__second_number).upper())[2:]


print('2) Через ООП')

first_hex_number = list(input('Введите первое число: '))
print(f'1-е число: {first_hex_number}')
second_hex_number = list(input('Введите второе число: '))
print(f'2-е число: {second_hex_number}')
print()

res_sum = HexAddMult(first_hex_number, second_hex_number) + HexAddMult(first_hex_number, second_hex_number)
res_mul = HexAddMult(first_hex_number, second_hex_number) * HexAddMult(first_hex_number, second_hex_number)

print(f'Сумма чисел = {list(res_sum)}')
print(f'Произведение чисел = {list(res_mul)}')