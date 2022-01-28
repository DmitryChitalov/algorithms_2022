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

# ========== 1 ==============
# Так и не понял где можно применить defaultdict(list) и reduce
from collections import deque
from itertools import zip_longest



def get_hex_num(mes):
    while True:
        try:
            num = input(mes).strip()
            int(num, 16)
            return num
        except ValueError:
            print('Wrong value')

hex_num1 = get_hex_num('Enter first hex number: ')
hex_num1_list = [i for i in hex_num1]
hex_num2 = get_hex_num('Enter second hex number: ')
hex_num2_list = [i for i in hex_num2]

class ResultSet:
    addition_dict_hex = dict()
    for n1 in range(16):
        for n2 in range(16):
            addition_dict_hex[(f'{n1:X}', f'{n2:X}')] = f'{n1+n2:X}'

    multiplication_dict_hex = dict()
    for n1 in range(16):
        for n2 in range(16):
            multiplication_dict_hex[(f'{n1:X}', f'{n2:X}')] = f'{n1*n2:X}'

class Operation:
    @staticmethod
    def hex_sum_2_digits(hex_digit1, hex_digit2):
        hex_sum = ResultSet.addition_dict_hex[(hex_digit1, hex_digit2)]
        return ('0', hex_sum) if len(hex_sum) == 1 else (hex_sum[0], hex_sum[1])
        
    @staticmethod
    def hex_sum_2_numbers(hex_num1_list, hex_num2_list):
        hex_sum_result = deque()
        next_digit = '0'
        for hex_n1, hex_n2 in zip_longest(hex_num1_list[::-1], hex_num2_list[::-1], fillvalue='0'):
            next_digit_from_transef, current_digit_transef = Operation.hex_sum_2_digits(hex_n1, next_digit)
            next_digit, current_digit = Operation.hex_sum_2_digits(current_digit_transef, hex_n2)
            _, next_digit = Operation.hex_sum_2_digits(next_digit, next_digit_from_transef)
            hex_sum_result.appendleft(current_digit)

        hex_sum_result.appendleft(next_digit)
        result = list(hex_sum_result)
        return result

    @staticmethod
    def hex_mul_2_digits(hex_digit1, hex_digit2):
        hex_mul = ResultSet.multiplication_dict_hex[(hex_digit1, hex_digit2)]
        return ('0', hex_mul) if len(hex_mul) == 1 else (hex_mul[0], hex_mul[1])
    @staticmethod
    def hex_mul_2_numbers(hex_num1_list, hex_num2_list):
        result = None
        for hex_n1 in hex_num1_list[::-1]:
            hex_mul_result = deque()
            next_digit_from_transef = '0'
            for hex_n2 in hex_num2_list[::-1]:
                next_digit, current_digit = Operation.hex_mul_2_digits(hex_n1, hex_n2)
                next_digit_from_transef, current_digit = Operation.hex_sum_2_digits(current_digit, next_digit_from_transef)
                next_digit_from_transef = next_digit
                hex_mul_result.appendleft(current_digit)
            hex_mul_result.appendleft(next_digit_from_transef)

            if not result:
                result = list(hex_mul_result)
            else:
                result = Operation.hex_sum_2_numbers(result, list(hex_mul_result) + ['0'])
        return result

print(f'1---sum={Operation.hex_sum_2_numbers(hex_num1_list, hex_num2_list)}')
print(f'1---mul={Operation.hex_mul_2_numbers(hex_num1_list, hex_num2_list)}')


# ========== 2 ==============
class HexNumber:
    def __init__(self, hex_num1):
        self.hex_num1_list = [i for i in hex_num1]

    def __getitem__(self, item):
        return self.hex_num1_list[item]

    def __add__(self, other):
        result_list = Operation.hex_sum_2_numbers(self.hex_num1_list, other)
        return HexNumber(''.join(result_list))

    def __mul__(self, other):
        result_list = Operation.hex_mul_2_numbers(self.hex_num1_list, other)
        return HexNumber(''.join(result_list))

    def __str__(self):
        return f'{self.hex_num1_list}'


hex_num1 = HexNumber(hex_num1)
hex_num2 = HexNumber(hex_num2)

print(f'2---sum={hex_num1 + hex_num2}')
print(f'2---mul={hex_num1 * hex_num2}')





