"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from random import randint
from timeit import timeit


def revers(enter_num, revers_num=0):
    """
    Самая неоптимальная реализация. Из-за использования рекурсии.
    """ 
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    """
    Приемлимый вариант, но проигривает 3-му из-за арифемтических операций.
    """
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    """
    Самый быстрый вариант, здесь число переводится в строку и переворачивается с помощью среза.
    """

    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num, revers_num=0):
    """
    Более оптимизировання версия варианта 2, упрощена арифметика, убрана лишняя в запись в переменную.
    """
    while enter_num > 0:
        revers_num = (10 * revers_num) + enter_num % 10
        enter_num //= 10
    return revers_num


num = randint(0, 1234578)

print(
    timeit(
        'revers(num)',
        globals=globals(),
        number=10000
    ))

print(
    timeit(
        'revers_2(num)',
        globals=globals(),
        number=10000
    ))

print(
    timeit(
        'revers_3(num)',
        globals=globals(),
        number=10000
    ))

print(
    timeit(
        'revers_4(num)',
        globals=globals(),
        number=10000,
    ))
