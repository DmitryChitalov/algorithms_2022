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
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


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

enter_num = 123456789

print(
    timeit(
        "revers_1(enter_num)",
        setup="from __main__ import revers_1, enter_num", number=10000))

print(
    timeit(
        "revers_2(enter_num)",
        setup="from __main__ import revers_2, enter_num", number=10000))

print(
    timeit(
        "revers_3(enter_num)",
        setup="from __main__ import revers_3, enter_num", number=10000))

print(
    timeit(
        "revers_4(enter_num)",
        setup="from __main__ import revers_4, enter_num", number=10000))

run("revers_1(enter_num)")
run("revers_2(enter_num)")
run("revers_3(enter_num)")
run("revers_4(enter_num)")

"""
Самым эффективным  способом оказался СРЕЗ(0.00452039999999998), 
остальные функции отработали практически одинаково:
revers_1 (0.041620199999999996)
revers_2 (0.020560399999999923)
revers_4 (0.03135509999999997)

Эффективность разворота строки через срез достигается отсутствием арифметических вычислений.
"""
