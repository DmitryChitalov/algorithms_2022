"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

"""
Замеры выполнения 1000 вызовов каждой из функций:
0.003971000000000002
0.0025944999999999996
0.0005194999999999991
0.0012003999999999973
Оптимальным по времени является третий алгоритм - выполнение реверса через стрез строки.
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
    revers_num = ''.join(reversed(str(enter_num)))
    return revers_num


number = 123456789
print(timeit("revers(number)", setup="from __main__ import revers, number", number=1000))
print(timeit("revers_2(number)", setup="from __main__ import revers_2, number", number=1000))
print(timeit("revers_3(number)", setup="from __main__ import revers_3, number", number=1000))
print(timeit("revers_4(number)", setup="from __main__ import revers_4, number", number=1000))


