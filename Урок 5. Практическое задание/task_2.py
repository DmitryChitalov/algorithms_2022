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


class CalcHaxNum:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return list(hex(int(''.join(self.num_1), 16) + int(''.join(other.num_2), 16))[2:])

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_1), 16) * int(''.join(other.num_2), 16))[2:])


def culc_num_16():
    """
    Сумирует и умножает два шестнадцатиричных числа
    :return: сумма и произведение чисел
    """
    num_dict = defaultdict(list)
    for i in range(2):
        num_16 = input(f'Введите {i + 1} шестнадцатиричное число: ')
        num_dict[num_16] = list(num_16)
    print(num_dict)
    sum_num = 0
    prod_num = 1
    for val in num_dict.values():
        try:
            sum_num += int(''.join(val), 16)
            prod_num *= int(''.join(val), 16)
        except ValueError:
            return print('Ошибка в воде цифр')
    sum_num_16 = list(hex(sum_num)[2:])
    prod_num_16 = list(hex(prod_num)[2:])
    print(f'Сумма чисел равна: {sum_num_16}')
    print(f'Произведение чисел равна: {prod_num_16}')
    return sum_num_16, prod_num_16


def culc_num_16_oop():
    """
    Сумирует и умножает два шестнадцатиричных числа
    :return: сумма и произведение чисел
    """
    num_dict = defaultdict(list)
    for i in range(2):
        num_16 = input(f'Введите {i + 1} шестнадцатиричное число: ')
        num_dict[i + 1] = list(num_16)
    print(num_dict)
    sum_num_16 = CalcHaxNum(num_dict[1], num_dict[2]) + CalcHaxNum(num_dict[1], num_dict[2])
    prod_num_16 = CalcHaxNum(num_dict[1], num_dict[2]) * CalcHaxNum(num_dict[1], num_dict[2])
    print(f'Сумма чисел равна: {sum_num_16}')
    print(f'Произведение чисел равна: {prod_num_16}')
    return sum_num_16, prod_num_16


if __name__ == '__main__':
    culc_num_16()
    culc_num_16_oop()
