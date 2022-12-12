"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import timeit
from random import randint
import sys
import math


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    revers_num = 0
    for _ in range(0, len(str(enter_num))):
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_5(enter_num):
    revers_num = 0
    for _ in range(0, int(math.log10(enter_num)) + 1):
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_6(enter_num):
    revers_num = []
    for i in range(0, int(math.log10(enter_num)) + 1):
        revers_num.append(str(enter_num % 10))
        enter_num //= 10
    return ''.join(revers_num)


sys.setrecursionlimit(10000)
number = randint(1, 500) ** randint(1, 500)
print(f'Сгенерировано число ~{number / (10 ** (len(str(number)) - 1)):.2f}E+{len(str(number)) - 1}')
print(f'{timeit(stmt="revers(number)", setup="from __main__ import revers", number=1000, globals=globals()):.7f}'
      f' сек: revers')
print(f'{timeit(stmt="revers_2(number)", setup="from __main__ import revers_2", number=1000, globals=globals()):.7f}'
      f' сек: revers_2')
print(f'{timeit(stmt="revers_3(number)", setup="from __main__ import revers_3", number=1000, globals=globals()):.7f}'
      f' сек: revers_3: САМОЕ БЫСТРОЕ РЕШЕНИЕ потому что:\n'
      f'                         а) работа со строками (наверно) оптимизирована на более низком уровне\n'
      f'                         б) отсутствуют математические операции и преобразования форматов')
print(f'{timeit(stmt="revers_4(number)", setup="from __main__ import revers_4", number=1000, globals=globals()):.7f}'
      f' сек: revers_4: решение через for,'
      f' количество итераций определяется через преобразование числа в строку и функцию len()')
print(f'{timeit(stmt="revers_5(number)", setup="from __main__ import revers_5", number=1000, globals=globals()):.7f}'
      f' сек: revers_5: решение через for, количество итераций определяется через log10 входного числа')
print(f'{timeit(stmt="revers_6(number)", setup="from __main__ import revers_6", number=1000, globals=globals()):.7f}'
      f' сек: revers_6: решение через массив, преобразование массива в строку с помощью метода join')
