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
from random import randint


def reverse(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        reverse(enter_num, revers_num)


def reverse_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def reverse_3(enter_num):
    enter_num = str(enter_num)  # O(1)
    revers_num = enter_num[::-1]  # O(b-a) = O(1)
    return revers_num  # O(1)


def recursive_reverse(enter_num):
    return f'{str(enter_num % 10)}{recursive_reverse(enter_num // 10)}' if enter_num != 0 else ''  # O(len(str))


def reverse_lc(enter_num):
    return str(enter_num)[::-1]


num_100 = randint(10000, 1000000)
# print(num_100, reverse_lc(num_100))
print(timeit("reverse(num_100)", setup='from __main__ import reverse, num_100', number=100000))
print(timeit("reverse_2(num_100)", setup='from __main__ import reverse_2, num_100', number=100000))
print(timeit("reverse_3(num_100)", setup='from __main__ import reverse_3, num_100', number=100000))
print(timeit("recursive_reverse(num_100)", setup='from __main__ import recursive_reverse, num_100', number=100000))
print(timeit("reverse_lc(num_100)", setup='from __main__ import reverse_lc, num_100', number=100000))
'''наибыстрейшая функция lc с наименьшей сложностью'''
