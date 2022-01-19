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
from collections import deque


class HexNum:
    def __init__(self, value):
        need_num = {'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

        if set(value.lower()) <= need_num:
            self.value = list(value.lower())
        else:
            self.value = None

    def __add__(self, other):
        return list(str(
            hex(int('0x' + ''.join(map(str, self.value)), 16) + int('0x' + ''.join(map(str, other.value)), 16))))[2:]

    def __mul__(self, other):
        return list(str(
            hex(int('0x' + ''.join(map(str, self.value)), 16) * int('0x' + ''.join(map(str, other.value)), 16))))[2:]


number1 = HexNum('A2')
number2 = HexNum('C4f')

print(number1 + number2)
print(number1 * number2)


def plus16(pl1, pl2, adding):
    result = deque(str(hex(int('0x' + pl1, 16) + int('0x' + pl2, 16) + adding)))
    result.popleft()
    result.popleft()
    return result


def x16(pl1, pl2):
    result = deque(str(hex(int('0x' + pl1, 16) * int('0x' + pl2, 16))))
    result.popleft()
    result.popleft()
    return result


# def sum16(num1, num2):
#     summand1 = deque(num1)
#     summand2 = deque(num2)
#     if len(summand1) > len(summand2):
#         for i in range(0, len(summand1) - len(summand2)):
#             summand2.appendleft('0')
#     else:
#         for i in range(0, len(summand2) - len(summand1)):
#             summand1.appendleft('0')
#     summand1.reverse()
#     summand2.reverse()
#     summ_all = deque()
#     inter_summ = []
#     for i in range(0, len(summand1)):
#         if len(inter_summ) > 1:
#             inter_summ = plus16(summand1[i], summand2[i], int(inter_summ[0]))
#         else:
#             inter_summ = plus16(summand1[i], summand2[i], 0)
#         summ_all.appendleft(inter_summ[-1])
#     if len(inter_summ) > 1:
#         summ_all.appendleft(inter_summ[0])
#
#     return summ_all


print(plus16('a2', 'c4f', 0))
print(x16('a2', 'c4f'))

