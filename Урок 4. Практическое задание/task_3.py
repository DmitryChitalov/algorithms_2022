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
from functools import lru_cache

num_10000 = randint(100000000, 10000000000000)


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


def revers_4(num):
    return "".join(reversed(str(num)))


print(f""" Revers
    {timeit(
    'revers(num_10000)',
    setup='from __main__ import revers, num_10000',
    number=100000)}""")

print(f""" Revers_2
    {timeit(
    'revers_2(num_10000)',
    setup='from __main__ import revers_2, num_10000',
    number=100000)}""")

print(f""" Revers_3
    {timeit(
    'revers_3(num_10000)',
    setup='from __main__ import revers_3, num_10000',
    number=100000)}""")

print(f""" Revers_4
    {timeit(
    'revers_4(num_10000)',
    setup='from __main__ import revers_4, num_10000',
    number=100000)}""")

# Вывод
"""
Быстрее всего оказалась функция с reverse_3 так как она просто делает срез-копию строки в обратном порядку 
меньше операций чем в других функциях 


 Revers
    0.5185826000088127
 Revers_2
    0.38380559999495745
 Revers_3
    0.03614849998848513
 Revers_4
    0.07461110000440385

"""
