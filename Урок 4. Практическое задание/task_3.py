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


def revers_4(enter_num, revers_num=''):
    if enter_num > 0:
        revers_num, enter_num = f'{revers_num}{enter_num % 10}', enter_num // 10
        return revers_4(enter_num, revers_num)
    return revers_num

enter_num = 123456789

print(timeit('revers(enter_num)', globals=globals()))
# 4.100596999982372

print(timeit('revers_2(enter_num)', globals=globals()))
# 2.383672000025399

print(timeit('revers_3(enter_num)', globals=globals()))
# 0.46177810011431575

print(timeit('revers_4(enter_num)', globals=globals()))
# 3.7534398999996483

# Вывод: самый быстрый и эффективный способ - срез (reverse_3)