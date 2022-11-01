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

operand_1 = input("Введите первое число в шестнадцатеричном формате: ").upper()
operand_2 = input("Введите второе число в шестнадцатеричном формате: ").upper()


def func_1(op_1, op_2):

    d = defaultdict(list)
    d[f"{op_1}"] = list(op_1)
    d[f"{op_2}"] = list(op_2)

    return list('%X' % sum([int(''.join(i), 16) for i in d.values()]))


def func_2(op_1,op_2):
    mult = 1
    d = defaultdict(list)
    d[f"{op_1}"] = list(op_1)
    d[f"{op_2}"] = list(op_2)

    for i in d.values():
        mult *= int(''.join(i), 16)

    return list('%X' % mult)


print("Сумма чисел: ", func_1(operand_1, operand_2))
print("Произведение чисел: ", func_2(operand_1, operand_2))



