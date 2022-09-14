from collections import defaultdict


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


def oper_16():
    super_dict = defaultdict(list)
    first = input('Введите первое число: ')
    second = input('Введите второе число: ')
    for i in first:
        super_dict[1].append(i)
    for i in second:
        super_dict[2].append(i)
    numb_1 = ''.join(str(x) for x in super_dict[1])
    numb_2 = ''.join(str(x) for x in super_dict[2])
    sum_numbs = hex(int(numb_1, 16) + int(numb_2, 16))
    mult_numbs = hex(int(numb_1, 16) * int(numb_2, 16))
    for i in sum_numbs[2:]:
        super_dict['sum'].append(i.upper())
    for i in mult_numbs[2:]:
        super_dict['mult'].append(i.upper())
    return f'сумма чисел: {super_dict["sum"]}\n' \
           f'произведение чисел: {super_dict["mult"]}'


print(oper_16())
'''
Введите первое число: A2
Введите второе число: C4F
сумма чисел: ['C', 'F', '1']
произведение чисел: ['7', 'C', '9', 'F', 'E']

Process finished with exit code 0
'''