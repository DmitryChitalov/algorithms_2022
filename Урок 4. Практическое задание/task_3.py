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

enter_num_start = 23456


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


def get_reverse_dig(num, rev_str=' '):
    if num // 10 == 0:
        return str(rev_str) + str(num % 10)
    else:
        return get_reverse_dig(num // 10, (str(rev_str) + str(num % 10)))


print(timeit("revers(enter_num_start)", setup="from __main__ import revers, enter_num_start",
             number=1000))
print(timeit("revers_2(enter_num_start)", setup="from __main__ import revers_2, enter_num_start",
             number=1000))
print(timeit("revers_3(enter_num_start)", setup="from __main__ import revers_3, enter_num_start",
             number=1000))
print(timeit("get_reverse_dig(enter_num_start)", setup="from __main__ import get_reverse_dig, enter_num_start",
             number=1000))

"""


Вывод: самый оптимальный вариант - использование среза последовательности [::-1], т.к. этот вариант 
фактически разворачивает строку за 1 раз, не используя циклы или рекурсии


"""