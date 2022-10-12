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
from collections import deque


def read_hex_digit(n = ""):
    correct_list = False
    while not correct_list:
        inp_string = input(f'please enter hex digit {n} : ')
        list1 = list(inp_string)
        # print (list1)
        for i in list1:
            if i not in ['1', '2', '3', '4', '5', '6', '7', '8',
                         '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']:
                print(' not correct input, please repeat ')
                correct_list = False
                break
            else:
                correct_list = True
        if correct_list:
            return list1


def hex_to_int(i):
    return int(i, 16)

def int_to_hex(i):
    return str(f'{i:X}')

def sum_hex(a, b):
    a = deque(a)
    b = deque(b)
    if len(b) > len(a):
        a, b = b, a

    result_list = []
    transfer = 0
    for i in range(len(a)):
        if b:
            res1 = hex_to_int(a.pop()) + hex_to_int(b.pop()) + transfer
        else:
            res1 = res1 = hex_to_int(a.pop()) + transfer
        transfer = 0
        if res1 > 15:
            res1 -= 16
            transfer = 1
        res1 = int_to_hex(res1)
        result_list.append(str(res1))
    if transfer:
        result_list.append('1')
    return result_list[::-1]


def mult_hex(a, b):
    a = deque(a)
    b = deque(b)
    len_a = len(a)
    len_b = len(b)
    int_result = 0
    for i, a_i in enumerate(a, start=1):
        for j,  b_j in enumerate(b, start=1):
            # a_i_oct = hex_to_int(a_i) * 16 ** (len_a - i)
            # b_j_oct = hex_to_int(b_j) * 16 ** (len_b - j)
            # print(f'a_i = {a_i} , oct = {a_i_oct} , b_j = {b_j} , oct = {b_j_oct}')
            int_result += hex_to_int(a_i) * 16 ** (len_a - i) * hex_to_int(b_j) * 16 ** (len_b - j)
            # print(int_result)
    hex_result = int_to_hex(int_result)
    return list(hex_result)

print(f'\n  --- SUMM and MULT of hex values --- ')
x = deque(read_hex_digit(1))
y = deque(read_hex_digit(2))

print(f' x = {x}')
print(f' y = {y}')
print('\n --- Result --- ')
print(f' Hex summ of {list(x)} and {list(y)} equals to {sum_hex(x,y)}')
print(f' Hex mult of {list(x)} and {list(y)} equals to {mult_hex(x,y)}')


# Script listing:
#
#   --- SUMM and MULT of hex values ---
# please enter hex digit 1 : A2
# please enter hex digit 2 : C4F
#  x = deque(['A', '2'])
#  y = deque(['C', '4', 'F'])
#
#  --- Result ---
#  Hex summ of ['A', '2'] and ['C', '4', 'F'] equals to ['C', 'F', '1']
#  Hex mult of ['A', '2'] and ['C', '4', 'F'] equals to ['7', 'C', '9', 'F', 'E']
#
# Process finished with exit code 0