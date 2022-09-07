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
from functools import reduce

MY_DEF_DIC = defaultdict(list)


def add_nums():
    """Для ввода шестнадцатеричного числа и помещения его в словарь MY_DEF_DIC"""
    inp_num = input('Введите число: ')
    MY_DEF_DIC[inp_num] = list(inp_num)
    print(f'Число сохранено : {MY_DEF_DIC[inp_num]}')


def sum_nums(my_dic):
    """Для сложения двух шестнадцатеричных чисел, находящихчя в словаре MY_DEF_DIC"""
    if len(my_dic) == 2:
        sum_two = reduce(
            lambda x, y: hex(int(''.join(my_dic[x]), 16) + int(''.join(my_dic[y]), 16)).upper(), my_dic)
        sum_num = list(sum_two)[2:]
    elif len(my_dic) == 1:
        for key in my_dic.keys():
            sum_num = list(hex(int(key, 16) + int(key, 16)).upper())[2:]
    else:
        sum_num = "Не считаю. Вы ввели больше, чем 2 числа."
    return sum_num


def mul_nums(my_dic):
    """Для умножения двух шестнадцатеричных чисел, находящихчя в словаре MY_DEF_DIC"""
    if len(my_dic) == 2:
        mul_two = reduce(
            lambda x, y: hex(int(''.join(my_dic[x]), 16) * int(''.join(my_dic[y]), 16)).upper(), my_dic)
        mul_num = list(mul_two)[2:]
    elif len(my_dic) == 1:
        for key in my_dic.keys():
            mul_num = list(hex(int(key, 16) ** 2).upper())[2:]
    else:
        mul_num = "Не считаю. Вы ввели больше, чем 2 числа."
    return mul_num


if __name__ == '__main__':
    print("Введите два шестнадцатеричных числа.")
    add_nums()
    add_nums()
    print(f'Сумма чисел: {sum_nums(MY_DEF_DIC)}')
    print(f'Произведение - {mul_nums(MY_DEF_DIC)}')
