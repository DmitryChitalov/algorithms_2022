"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

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


enter_num = 1234567890

print('revers_1: ', timeit(f'revers_1({enter_num})', globals=globals()))
print('revers_2: ', timeit(f'revers_2({enter_num})', globals=globals()))
print('revers_3: ', timeit(f'revers_3({enter_num})', globals=globals()))
print('revers_4: ', timeit(f'revers_4({enter_num})', globals=globals()))

run("revers_1(enter_num)")
run("revers_2(enter_num)")
run("revers_3(enter_num)")
run("revers_4(enter_num)")

"""
revers_1:  2.4002221000846475
revers_2:  1.5896976999938488
revers_3:  0.29657999996561557
revers_4:  0.6081014999654144
Третья функция самая быстрая, т.к. отсутсвует арифмитический подсчет
"""
