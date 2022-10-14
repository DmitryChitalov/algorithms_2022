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


def hexadecimal_number():
    hex_dict, hex_sum, hex_mul = defaultdict(list), 0, 1
    hex_1 = input('Введите первое число: ')
    hex_2 = input('Введите второе число: ')
    hex_dict[int(hex_1, 16)] = list(hex_1)
    hex_dict[int(hex_2, 16)] = list(hex_2)
    for hex_num in hex_dict:
        hex_sum += hex_num
    for hex_num in hex_dict:
        hex_mul *= hex_num

    print(f'Сумма чисел {list(hex_1)} и {list(hex_2)} равна {list(hex(hex_sum))[2:]}\n'
          f'Произведение чисел {list(hex_1)} и {list(hex_2)} равна {list(hex(hex_mul))[2:]}')


if __name__ == "__main__":
    hexadecimal_number()
