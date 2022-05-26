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

from collections import deque
from itertools import zip_longest

DEC_TO_HEX = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def hex_add(n1: list, n2: list) -> list:
    # Сложение столбиком.
    # С помощью zip_longest формируется кортеж, состоящий из пар, которые будут складываться
    # если какой-то список короче, то недостающие элемены заполняются нулями
    tup_to_sum = tuple(zip_longest(reversed(n1), reversed(n2), fillvalue='0'))
    remainder = False
    res = deque()  # В дек будем складывать ответ, дополняя дек слева

    for itm in tup_to_sum:
        # По заданию разрешается пользоваться int(, 16). Поэтому использую этот метод, для преобразования в десятичную
        # систему. Хотя можно было бы сдалать словарь обратный словарю DEC_TO_HEX
        d = sum(map(lambda x: int(x, 16), itm)) + remainder
        if d >= 16:
            remainder = True
            d -= 16
        else:
            remainder = False
        res.appendleft(DEC_TO_HEX[d])
    if remainder:
        res.appendleft(DEC_TO_HEX[remainder])
    return list(res)


def hex_mul(n1: list, n2: list) -> list:
    deque1 = deque(n1)
    deque2 = deque(n2)

    # дополняем нулями слева дек, который короче
    if len(deque1) > len(deque2):
        deque2.extendleft(['0' * (len(deque1) - len(deque2))])
    elif len(deque2) > len(deque1):
        deque1.extendleft(['0' * (len(deque2) - len(deque1))])

    result = '0'
    # Суть в том, что мы проходим по "цифрам" второго числа складывая первое число n раз функцией сложения. Где n -
    # десятичное представление этих "цифр". Подобно умножению в столбик
    for i in range(len(deque2) - 1, -1, -1):
        pre_result = '0'
        for n in range(int(deque2[i], 16)):
            pre_result = hex_add(list(pre_result), list(deque1))
        pre_result += '0' * (len(deque1) - i - 1)
        result = hex_add(result, pre_result)
    return list(result)


num1 = input('Введите первое число:') or 'A2'
num2 = input('Введите второе число:') or 'C4F'

print(hex_add(list(num1), list(num2)))
print(hex_mul(list(num1), list(num2)))
