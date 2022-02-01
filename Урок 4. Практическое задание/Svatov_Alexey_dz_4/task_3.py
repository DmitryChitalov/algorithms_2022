"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""

from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


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
    return ''.join(reversed(str(enter_num)))


num = 123456789

print(f'revers_time = {timeit("revers(num)", setup="from __main__ import revers, num", number=100000)}')
print(f'revers_2_time = {timeit("revers_2(num)", setup="from __main__ import revers_2, num", number=100000)}')
print(f'revers_3_time = {timeit("revers_3(num)", setup="from __main__ import revers_3, num", number=100000)}')
print(f'revers_4_time = {timeit("revers_4(num)", setup="from __main__ import revers_4, num", number=100000)}')
