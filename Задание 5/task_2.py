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
from functools import reduce 

def input_hex_arr(n):
    print(f'Введите {n} 16-ричных чисел')
    res = []
    for i in range(n):
        res.append(list(input(f'{i+1}-е число:')))
    return res

def hex_arr_to_int(hex_arr):
    return reduce(lambda res, dig: res*16 + '0123456789abcdef'.find(dig.lower()), hex_arr, 0)

def int_to_hex_arr(i):
    return list(hex(i)[2:].upper())

def sum_hex_arr(v1, v2):
    return list(hex(int(''.join(v1), 16) + int(''.join(v2), 16))[2:].upper())

def mul_hex_arr(v1, v2):
    return list(hex(int(''.join(v1), 16) * int(''.join(v2), 16))[2:].upper())

class list_add_mul(list): # list с перегруженными методами 
    def __add__(self, other_list):
        return list(hex(int(''.join(self), 16) + int(''.join(other_list), 16)).upper()[2:])
    
    def __mul__(self, other_list):
        return list(hex(int(''.join(self), 16) * int(''.join(other_list), 16)).upper()[2:])

hex_arr = input_hex_arr(2)
print('Операции со списками:')
print('Сумма =', sum_hex_arr(hex_arr[0], hex_arr[1]))
print('Сумма =', int_to_hex_arr(hex_arr_to_int(hex_arr[0]) + hex_arr_to_int(hex_arr[1])))
print('Произведение =', mul_hex_arr(hex_arr[0], hex_arr[1]))
print('Произведение =', int_to_hex_arr(hex_arr_to_int(hex_arr[0]) * hex_arr_to_int(hex_arr[1])))

print('Перегрузка методов списка:')
print('Сумма =', list_add_mul(hex_arr[0]) + list_add_mul(hex_arr[1]))
print('Произведение = ', list_add_mul(hex_arr[0]) * list_add_mul(hex_arr[1]))
