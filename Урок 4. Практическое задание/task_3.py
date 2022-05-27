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


def revers_4(enter_num):
    return ''.join(list(reversed([i for i in str(enter_num)])))



print(revers_4(123456789))

print(
    timeit(
        'revers(123456789)',
        setup='from __main__ import revers',
        number=10000))
print(
    timeit(
        'revers_2(123456789)',
        setup='from __main__ import revers_2',
        number=10000))
print(
    timeit(
        'revers_3(123456789)',
        setup='from __main__ import revers_3',
        number=10000))

print(
    timeit(
        'revers_4(123456789)',
        setup='from __main__ import revers_4',
        number=10000))
"""
0.030070100000000002
0.018858399999999997
0.003654699999999997
0.010387099999999996

самый быстрый 3ий, так как в остальных случаях много операций, либо используется не эффективный тип данных
"""