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


def revers_nums(enter_num):
    return str(enter_num % 10)[::-1]


nums = randint(10000, 1000000)
# print(num_100, reverse_lc(num_100))
print(timeit("revers(nums)", setup='from __main__ import revers, nums', globals=globals()))
print(timeit("revers_2(nums)", setup='from __main__ import revers_2, nums', globals=globals()))
print(timeit("revers_3(nums)", setup='from __main__ import revers_3, nums', globals=globals()))
print(timeit("revers_nums(nums)", setup='from __main__ import revers_nums, nums', globals=globals()))

# 1.677488771 - рекурсия самая медленная
# 1.0657876149999999 - цикл выполняется быстрее рекурсии
# 0.388942718 - срез выполняется быстрее циела и рекурсии
# 0.35413986899999994 - а в моем случае код выполняется чуть быстрее среза из-за отсутствия переменных
